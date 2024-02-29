"""
WASI filesystem is a filesystem API primarily intended to let users run WASI
programs that access their files on their existing filesystems, without
significant overhead.

It is intended to be roughly portable between Unix-family platforms and
Windows, though it does not hide many of the major differences.

Paths are passed as interface-type `string`s, meaning they must consist of
a sequence of Unicode Scalar Values (USVs). Some filesystems may contain
paths which are not accessible by this API.

The directory separator in WASI is always the forward-slash (`/`).

All paths in WASI are relative paths, and are interpreted relative to a
`descriptor` referring to a base directory. If a `path` argument to any WASI
function starts with `/`, or if any step of resolving a `path`, including
`..` and symbolic link steps, reaches a directory outside of the base
directory, or reaches a symlink to an absolute or rooted path in the
underlying filesystem, the function fails with `error-code::not-permitted`.

For more information about WASI path resolution and sandboxing, see
[WASI filesystem path resolution].

[WASI filesystem path resolution]: https://github.com/WebAssembly/wasi-filesystem/blob/main/path-resolution.md
"""
from typing import TypeVar, Generic, Union, Optional, Union, Protocol, Tuple, List, Any, Self
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some
from ..imports import streams
from ..imports import poll
from ..imports import wall_clock
from ..imports import error


@dataclass
class MethodGet:
    pass


@dataclass
class MethodHead:
    pass


@dataclass
class MethodPost:
    pass


@dataclass
class MethodPut:
    pass


@dataclass
class MethodDelete:
    pass


@dataclass
class MethodConnect:
    pass


@dataclass
class MethodOptions:
    pass


@dataclass
class MethodTrace:
    pass


@dataclass
class MethodPatch:
    pass


@dataclass
class MethodOther:
    value: str


Method = Union[MethodGet, MethodHead, MethodPost, MethodPut, MethodDelete, MethodConnect, MethodOptions, MethodTrace, MethodPatch, MethodOther]
"""
This type corresponds to HTTP standard Methods.
"""



@dataclass
class SchemeHttp:
    pass


@dataclass
class SchemeHttps:
    pass


@dataclass
class SchemeOther:
    value: str


Scheme = Union[SchemeHttp, SchemeHttps, SchemeOther]
"""
This type corresponds to HTTP standard Related Schemes.
"""


@dataclass
class DnsErrorPayload:
    """
    Defines the case payload type for `DNS-error` above:
    """
    rcode: Optional[str]
    info_code: Optional[int]

@dataclass
class TlsAlertReceivedPayload:
    """
    Defines the case payload type for `TLS-alert-received` above:
    """
    alert_id: Optional[int]
    alert_message: Optional[str]

@dataclass
class FieldSizePayload:
    """
    Defines the case payload type for `HTTP-response-{header,trailer}-size` above:
    """
    field_name: Optional[str]
    field_size: Optional[int]


@dataclass
class ErrorCodeDnsTimeout:
    pass


@dataclass
class ErrorCodeDnsError:
    value: DnsErrorPayload


@dataclass
class ErrorCodeDestinationNotFound:
    pass


@dataclass
class ErrorCodeDestinationUnavailable:
    pass


@dataclass
class ErrorCodeDestinationIpProhibited:
    pass


@dataclass
class ErrorCodeDestinationIpUnroutable:
    pass


@dataclass
class ErrorCodeConnectionRefused:
    pass


@dataclass
class ErrorCodeConnectionTerminated:
    pass


@dataclass
class ErrorCodeConnectionTimeout:
    pass


@dataclass
class ErrorCodeConnectionReadTimeout:
    pass


@dataclass
class ErrorCodeConnectionWriteTimeout:
    pass


@dataclass
class ErrorCodeConnectionLimitReached:
    pass


@dataclass
class ErrorCodeTlsProtocolError:
    pass


@dataclass
class ErrorCodeTlsCertificateError:
    pass


@dataclass
class ErrorCodeTlsAlertReceived:
    value: TlsAlertReceivedPayload


@dataclass
class ErrorCodeHttpRequestDenied:
    pass


@dataclass
class ErrorCodeHttpRequestLengthRequired:
    pass


@dataclass
class ErrorCodeHttpRequestBodySize:
    value: Optional[int]


@dataclass
class ErrorCodeHttpRequestMethodInvalid:
    pass


@dataclass
class ErrorCodeHttpRequestUriInvalid:
    pass


@dataclass
class ErrorCodeHttpRequestUriTooLong:
    pass


@dataclass
class ErrorCodeHttpRequestHeaderSectionSize:
    value: Optional[int]


@dataclass
class ErrorCodeHttpRequestHeaderSize:
    value: Optional[FieldSizePayload]


@dataclass
class ErrorCodeHttpRequestTrailerSectionSize:
    value: Optional[int]


@dataclass
class ErrorCodeHttpRequestTrailerSize:
    value: FieldSizePayload


@dataclass
class ErrorCodeHttpResponseIncomplete:
    pass


@dataclass
class ErrorCodeHttpResponseHeaderSectionSize:
    value: Optional[int]


@dataclass
class ErrorCodeHttpResponseHeaderSize:
    value: FieldSizePayload


@dataclass
class ErrorCodeHttpResponseBodySize:
    value: Optional[int]


@dataclass
class ErrorCodeHttpResponseTrailerSectionSize:
    value: Optional[int]


@dataclass
class ErrorCodeHttpResponseTrailerSize:
    value: FieldSizePayload


@dataclass
class ErrorCodeHttpResponseTransferCoding:
    value: Optional[str]


@dataclass
class ErrorCodeHttpResponseContentCoding:
    value: Optional[str]


@dataclass
class ErrorCodeHttpResponseTimeout:
    pass


@dataclass
class ErrorCodeHttpUpgradeFailed:
    pass


@dataclass
class ErrorCodeHttpProtocolError:
    pass


@dataclass
class ErrorCodeLoopDetected:
    pass


@dataclass
class ErrorCodeConfigurationError:
    pass


@dataclass
class ErrorCodeInternalError:
    value: Optional[str]


ErrorCode = Union[ErrorCodeDnsTimeout, ErrorCodeDnsError, ErrorCodeDestinationNotFound, ErrorCodeDestinationUnavailable, ErrorCodeDestinationIpProhibited, ErrorCodeDestinationIpUnroutable, ErrorCodeConnectionRefused, ErrorCodeConnectionTerminated, ErrorCodeConnectionTimeout, ErrorCodeConnectionReadTimeout, ErrorCodeConnectionWriteTimeout, ErrorCodeConnectionLimitReached, ErrorCodeTlsProtocolError, ErrorCodeTlsCertificateError, ErrorCodeTlsAlertReceived, ErrorCodeHttpRequestDenied, ErrorCodeHttpRequestLengthRequired, ErrorCodeHttpRequestBodySize, ErrorCodeHttpRequestMethodInvalid, ErrorCodeHttpRequestUriInvalid, ErrorCodeHttpRequestUriTooLong, ErrorCodeHttpRequestHeaderSectionSize, ErrorCodeHttpRequestHeaderSize, ErrorCodeHttpRequestTrailerSectionSize, ErrorCodeHttpRequestTrailerSize, ErrorCodeHttpResponseIncomplete, ErrorCodeHttpResponseHeaderSectionSize, ErrorCodeHttpResponseHeaderSize, ErrorCodeHttpResponseBodySize, ErrorCodeHttpResponseTrailerSectionSize, ErrorCodeHttpResponseTrailerSize, ErrorCodeHttpResponseTransferCoding, ErrorCodeHttpResponseContentCoding, ErrorCodeHttpResponseTimeout, ErrorCodeHttpUpgradeFailed, ErrorCodeHttpProtocolError, ErrorCodeLoopDetected, ErrorCodeConfigurationError, ErrorCodeInternalError]
"""
These cases are inspired by the IANA HTTP Proxy Error Types:
https://www.iana.org/assignments/http-proxy-status/http-proxy-status.xhtml#table-http-proxy-error-types
"""



@dataclass
class HeaderErrorInvalidSyntax:
    pass


@dataclass
class HeaderErrorForbidden:
    pass


@dataclass
class HeaderErrorImmutable:
    pass


HeaderError = Union[HeaderErrorInvalidSyntax, HeaderErrorForbidden, HeaderErrorImmutable]
"""
This type enumerates the different kinds of errors that may occur when
setting or appending to a `fields` resource.
"""


class Fields:
    """
    This following block defines the `fields` resource which corresponds to
    HTTP standard Fields. Fields are a common representation used for both
    Headers and Trailers.
    
    A `fields` may be mutable or immutable. A `fields` created using the
    constructor, `from-list`, or `clone` will be mutable, but a `fields`
    resource given by other means (including, but not limited to,
    `incoming-request.headers`, `outgoing-request.headers`) might be be
    immutable. In an immutable fields, the `set`, `append`, and `delete`
    operations will fail with `header-error.immutable`.
    """
    
    def __init__(self):
        """
        Construct an empty HTTP Fields.
        
        The resulting `fields` is mutable.
        """
        raise NotImplementedError

    @classmethod
    def from_list(cls, entries: List[Tuple[str, bytes]]) -> Self:
        """
        Construct an HTTP Fields.
        
        The resulting `fields` is mutable.
        
        The list represents each key-value pair in the Fields. Keys
        which have multiple values are represented by multiple entries in this
        list with the same key.
        
        The tuple is a pair of the field key, represented as a string, and
        Value, represented as a list of bytes. In a valid Fields, all keys
        and values are valid UTF-8 strings. However, values are not always
        well-formed, so they are represented as a raw list of bytes.
        
        An error result will be returned if any header or value was
        syntactically invalid, or if a header was forbidden.
        
        Raises: `consumer.types.Err(consumer.imports.types.HeaderError)`
        """
        raise NotImplementedError

    def get(self, name: str) -> List[bytes]:
        """
        Get all of the values corresponding to a key. If the key is not present
        in this `fields`, an empty list is returned. However, if the key is
        present but empty, this is represented by a list with one or more
        empty field-values present.
        """
        raise NotImplementedError

    def has(self, name: str) -> int:
        """
        Returns `true` when the key is present in this `fields`. If the key is
        syntactically invalid, `false` is returned.
        """
        raise NotImplementedError

    def set(self, name: str, value: List[bytes]) -> None:
        """
        Set all of the values for a key. Clears any existing values for that
        key, if they have been set.
        
        Fails with `header-error.immutable` if the `fields` are immutable.
        
        Raises: `consumer.types.Err(consumer.imports.types.HeaderError)`
        """
        raise NotImplementedError

    def delete(self, name: str) -> None:
        """
        Delete all values for a key. Does nothing if no values for the key
        exist.
        
        Fails with `header-error.immutable` if the `fields` are immutable.
        
        Raises: `consumer.types.Err(consumer.imports.types.HeaderError)`
        """
        raise NotImplementedError

    def append(self, name: str, value: bytes) -> None:
        """
        Append a value for a key. Does not change or delete any existing
        values for that key.
        
        Fails with `header-error.immutable` if the `fields` are immutable.
        
        Raises: `consumer.types.Err(consumer.imports.types.HeaderError)`
        """
        raise NotImplementedError

    def entries(self) -> List[Tuple[str, bytes]]:
        """
        Retrieve the full set of keys and values in the Fields. Like the
        constructor, the list represents each key-value pair.
        
        The outer list represents each key-value pair in the Fields. Keys
        which have multiple values are represented by multiple entries in this
        list with the same key.
        """
        raise NotImplementedError

    def clone(self) -> Self:
        """
        Make a deep copy of the Fields. Equivelant in behavior to calling the
        `fields` constructor on the return value of `entries`. The resulting
        `fields` is mutable.
        """
        raise NotImplementedError

    def __enter__(self):
        """Returns self"""
        return self
                                                                    
    def __exit__(self, *args):
        """
        Release this resource.
        """
        raise NotImplementedError


class FutureTrailers:
    """
    Represents a future which may eventaully return trailers, or an error.
    
    In the case that the incoming HTTP Request or Response did not have any
    trailers, this future will resolve to the empty set of trailers once the
    complete Request or Response body has been received.
    """
    
    def subscribe(self) -> poll.Pollable:
        """
        Returns a pollable which becomes ready when either the trailers have
        been received, or an error has occured. When this pollable is ready,
        the `get` method will return `some`.
        """
        raise NotImplementedError

    def get(self) -> Optional[Result[Result[Optional[Fields], ErrorCode], None]]:
        """
        Returns the contents of the trailers, or an error which occured,
        once the future is ready.
        
        The outer `option` represents future readiness. Users can wait on this
        `option` to become `some` using the `subscribe` method.
        
        The outer `result` is used to retrieve the trailers or error at most
        once. It will be success on the first call in which the outer option
        is `some`, and error on subsequent calls.
        
        The inner `result` represents that either the HTTP Request or Response
        body, as well as any trailers, were received successfully, or that an
        error occured receiving them. The optional `trailers` indicates whether
        or not trailers were present in the body.
        
        When some `trailers` are returned by this method, the `trailers`
        resource is immutable, and a child. Use of the `set`, `append`, or
        `delete` methods will return an error, and the resource must be
        dropped before the parent `future-trailers` is dropped.
        """
        raise NotImplementedError

    def __enter__(self):
        """Returns self"""
        return self
                                                                    
    def __exit__(self, *args):
        """
        Release this resource.
        """
        raise NotImplementedError


class IncomingBody:
    """
    Represents an incoming HTTP Request or Response's Body.
    
    A body has both its contents - a stream of bytes - and a (possibly
    empty) set of trailers, indicating that the full contents of the
    body have been received. This resource represents the contents as
    an `input-stream` and the delivery of trailers as a `future-trailers`,
    and ensures that the user of this interface may only be consuming either
    the body contents or waiting on trailers at any given time.
    """
    
    def stream(self) -> streams.InputStream:
        """
        Returns the contents of the body, as a stream of bytes.
        
        Returns success on first call: the stream representing the contents
        can be retrieved at most once. Subsequent calls will return error.
        
        The returned `input-stream` resource is a child: it must be dropped
        before the parent `incoming-body` is dropped, or consumed by
        `incoming-body.finish`.
        
        This invariant ensures that the implementation can determine whether
        the user is consuming the contents of the body, waiting on the
        `future-trailers` to be ready, or neither. This allows for network
        backpressure is to be applied when the user is consuming the body,
        and for that backpressure to not inhibit delivery of the trailers if
        the user does not read the entire body.
        
        Raises: `consumer.types.Err(None)`
        """
        raise NotImplementedError

    @classmethod
    def finish(cls, this: Self) -> FutureTrailers:
        """
        Takes ownership of `incoming-body`, and returns a `future-trailers`.
        This function will trap if the `input-stream` child is still alive.
        """
        raise NotImplementedError

    def __enter__(self):
        """Returns self"""
        return self
                                                                    
    def __exit__(self, *args):
        """
        Release this resource.
        """
        raise NotImplementedError


class IncomingRequest:
    """
    Represents an incoming HTTP Request.
    """
    
    def method(self) -> Method:
        """
        Returns the method of the incoming request.
        """
        raise NotImplementedError

    def path_with_query(self) -> Optional[str]:
        """
        Returns the path with query parameters from the request, as a string.
        """
        raise NotImplementedError

    def scheme(self) -> Optional[Scheme]:
        """
        Returns the protocol scheme from the request.
        """
        raise NotImplementedError

    def authority(self) -> Optional[str]:
        """
        Returns the authority from the request, if it was present.
        """
        raise NotImplementedError

    def headers(self) -> Fields:
        """
        Get the `headers` associated with the request.
        
        The returned `headers` resource is immutable: `set`, `append`, and
        `delete` operations will fail with `header-error.immutable`.
        
        The `headers` returned are a child resource: it must be dropped before
        the parent `incoming-request` is dropped. Dropping this
        `incoming-request` before all children are dropped will trap.
        """
        raise NotImplementedError

    def consume(self) -> IncomingBody:
        """
        Gives the `incoming-body` associated with this request. Will only
        return success at most once, and subsequent calls will return error.
        
        Raises: `consumer.types.Err(None)`
        """
        raise NotImplementedError

    def __enter__(self):
        """Returns self"""
        return self
                                                                    
    def __exit__(self, *args):
        """
        Release this resource.
        """
        raise NotImplementedError


class OutgoingBody:
    """
    Represents an outgoing HTTP Request or Response's Body.
    
    A body has both its contents - a stream of bytes - and a (possibly
    empty) set of trailers, inducating the full contents of the body
    have been sent. This resource represents the contents as an
    `output-stream` child resource, and the completion of the body (with
    optional trailers) with a static function that consumes the
    `outgoing-body` resource, and ensures that the user of this interface
    may not write to the body contents after the body has been finished.
    
    If the user code drops this resource, as opposed to calling the static
    method `finish`, the implementation should treat the body as incomplete,
    and that an error has occured. The implementation should propogate this
    error to the HTTP protocol by whatever means it has available,
    including: corrupting the body on the wire, aborting the associated
    Request, or sending a late status code for the Response.
    """
    
    def write(self) -> streams.OutputStream:
        """
        Returns a stream for writing the body contents.
        
        The returned `output-stream` is a child resource: it must be dropped
        before the parent `outgoing-body` resource is dropped (or finished),
        otherwise the `outgoing-body` drop or `finish` will trap.
        
        Returns success on the first call: the `output-stream` resource for
        this `outgoing-body` may be retrieved at most once. Subsequent calls
        will return error.
        
        Raises: `consumer.types.Err(None)`
        """
        raise NotImplementedError

    @classmethod
    def finish(cls, this: Self, trailers: Optional[Fields]) -> None:
        """
        Finalize an outgoing body, optionally providing trailers. This must be
        called to signal that the response is complete. If the `outgoing-body`
        is dropped without calling `outgoing-body.finalize`, the implementation
        should treat the body as corrupted.
        
        Fails if the body's `outgoing-request` or `outgoing-response` was
        constructed with a Content-Length header, and the contents written
        to the body (via `write`) does not match the value given in the
        Content-Length.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def __enter__(self):
        """Returns self"""
        return self
                                                                    
    def __exit__(self, *args):
        """
        Release this resource.
        """
        raise NotImplementedError


class OutgoingRequest:
    """
    Represents an outgoing HTTP Request.
    """
    
    def __init__(self, headers: Fields):
        """
        Construct a new `outgoing-request` with a default `method` of `GET`, and
        `none` values for `path-with-query`, `scheme`, and `authority`.
        
        * `headers` is the HTTP Headers for the Request.
        
        It is possible to construct, or manipulate with the accessor functions
        below, an `outgoing-request` with an invalid combination of `scheme`
        and `authority`, or `headers` which are not permitted to be sent.
        It is the obligation of the `outgoing-handler.handle` implementation
        to reject invalid constructions of `outgoing-request`.
        """
        raise NotImplementedError

    def body(self) -> OutgoingBody:
        """
        Returns the resource corresponding to the outgoing Body for this
        Request.
        
        Returns success on the first call: the `outgoing-body` resource for
        this `outgoing-request` can be retrieved at most once. Subsequent
        calls will return error.
        
        Raises: `consumer.types.Err(None)`
        """
        raise NotImplementedError

    def method(self) -> Method:
        """
        Get the Method for the Request.
        """
        raise NotImplementedError

    def set_method(self, method: Method) -> None:
        """
        Set the Method for the Request. Fails if the string present in a
        `method.other` argument is not a syntactically valid method.
        
        Raises: `consumer.types.Err(None)`
        """
        raise NotImplementedError

    def path_with_query(self) -> Optional[str]:
        """
        Get the combination of the HTTP Path and Query for the Request.
        When `none`, this represents an empty Path and empty Query.
        """
        raise NotImplementedError

    def set_path_with_query(self, path_with_query: Optional[str]) -> None:
        """
        Set the combination of the HTTP Path and Query for the Request.
        When `none`, this represents an empty Path and empty Query. Fails is the
        string given is not a syntactically valid path and query uri component.
        
        Raises: `consumer.types.Err(None)`
        """
        raise NotImplementedError

    def scheme(self) -> Optional[Scheme]:
        """
        Get the HTTP Related Scheme for the Request. When `none`, the
        implementation may choose an appropriate default scheme.
        """
        raise NotImplementedError

    def set_scheme(self, scheme: Optional[Scheme]) -> None:
        """
        Set the HTTP Related Scheme for the Request. When `none`, the
        implementation may choose an appropriate default scheme. Fails if the
        string given is not a syntactically valid uri scheme.
        
        Raises: `consumer.types.Err(None)`
        """
        raise NotImplementedError

    def authority(self) -> Optional[str]:
        """
        Get the HTTP Authority for the Request. A value of `none` may be used
        with Related Schemes which do not require an Authority. The HTTP and
        HTTPS schemes always require an authority.
        """
        raise NotImplementedError

    def set_authority(self, authority: Optional[str]) -> None:
        """
        Set the HTTP Authority for the Request. A value of `none` may be used
        with Related Schemes which do not require an Authority. The HTTP and
        HTTPS schemes always require an authority. Fails if the string given is
        not a syntactically valid uri authority.
        
        Raises: `consumer.types.Err(None)`
        """
        raise NotImplementedError

    def headers(self) -> Fields:
        """
        Get the headers associated with the Request.
        
        The returned `headers` resource is immutable: `set`, `append`, and
        `delete` operations will fail with `header-error.immutable`.
        
        This headers resource is a child: it must be dropped before the parent
        `outgoing-request` is dropped, or its ownership is transfered to
        another component by e.g. `outgoing-handler.handle`.
        """
        raise NotImplementedError

    def __enter__(self):
        """Returns self"""
        return self
                                                                    
    def __exit__(self, *args):
        """
        Release this resource.
        """
        raise NotImplementedError


class RequestOptions:
    """
    Parameters for making an HTTP Request. Each of these parameters is
    currently an optional timeout applicable to the transport layer of the
    HTTP protocol.
    
    These timeouts are separate from any the user may use to bound a
    blocking call to `wasi:io/poll.poll`.
    """
    
    def __init__(self):
        """
        Construct a default `request-options` value.
        """
        raise NotImplementedError

    def connect_timeout(self) -> Optional[int]:
        """
        The timeout for the initial connect to the HTTP Server.
        """
        raise NotImplementedError

    def set_connect_timeout(self, duration: Optional[int]) -> None:
        """
        Set the timeout for the initial connect to the HTTP Server. An error
        return value indicates that this timeout is not supported.
        
        Raises: `consumer.types.Err(None)`
        """
        raise NotImplementedError

    def first_byte_timeout(self) -> Optional[int]:
        """
        The timeout for receiving the first byte of the Response body.
        """
        raise NotImplementedError

    def set_first_byte_timeout(self, duration: Optional[int]) -> None:
        """
        Set the timeout for receiving the first byte of the Response body. An
        error return value indicates that this timeout is not supported.
        
        Raises: `consumer.types.Err(None)`
        """
        raise NotImplementedError

    def between_bytes_timeout(self) -> Optional[int]:
        """
        The timeout for receiving subsequent chunks of bytes in the Response
        body stream.
        """
        raise NotImplementedError

    def set_between_bytes_timeout(self, duration: Optional[int]) -> None:
        """
        Set the timeout for receiving subsequent chunks of bytes in the Response
        body stream. An error return value indicates that this timeout is not
        supported.
        
        Raises: `consumer.types.Err(None)`
        """
        raise NotImplementedError

    def __enter__(self):
        """Returns self"""
        return self
                                                                    
    def __exit__(self, *args):
        """
        Release this resource.
        """
        raise NotImplementedError


class OutgoingResponse:
    """
    Represents an outgoing HTTP Response.
    """
    
    def __init__(self, headers: Fields):
        """
        Construct an `outgoing-response`, with a default `status-code` of `200`.
        If a different `status-code` is needed, it must be set via the
        `set-status-code` method.
        
        * `headers` is the HTTP Headers for the Response.
        """
        raise NotImplementedError

    def status_code(self) -> int:
        """
        Get the HTTP Status Code for the Response.
        """
        raise NotImplementedError

    def set_status_code(self, status_code: int) -> None:
        """
        Set the HTTP Status Code for the Response. Fails if the status-code
        given is not a valid http status code.
        
        Raises: `consumer.types.Err(None)`
        """
        raise NotImplementedError

    def headers(self) -> Fields:
        """
        Get the headers associated with the Request.
        
        The returned `headers` resource is immutable: `set`, `append`, and
        `delete` operations will fail with `header-error.immutable`.
        
        This headers resource is a child: it must be dropped before the parent
        `outgoing-request` is dropped, or its ownership is transfered to
        another component by e.g. `outgoing-handler.handle`.
        """
        raise NotImplementedError

    def body(self) -> OutgoingBody:
        """
        Returns the resource corresponding to the outgoing Body for this Response.
        
        Returns success on the first call: the `outgoing-body` resource for
        this `outgoing-response` can be retrieved at most once. Subsequent
        calls will return error.
        
        Raises: `consumer.types.Err(None)`
        """
        raise NotImplementedError

    def __enter__(self):
        """Returns self"""
        return self
                                                                    
    def __exit__(self, *args):
        """
        Release this resource.
        """
        raise NotImplementedError


class ResponseOutparam:
    """
    Represents the ability to send an HTTP Response.
    
    This resource is used by the `wasi:http/incoming-handler` interface to
    allow a Response to be sent corresponding to the Request provided as the
    other argument to `incoming-handler.handle`.
    """
    
    @classmethod
    def set(cls, param: Self, response: Result[OutgoingResponse, ErrorCode]) -> None:
        """
        Set the value of the `response-outparam` to either send a response,
        or indicate an error.
        
        This method consumes the `response-outparam` to ensure that it is
        called at most once. If it is never called, the implementation
        will respond with an error.
        
        The user may provide an `error` to `response` to allow the
        implementation determine how to respond with an HTTP error response.
        """
        raise NotImplementedError

    def __enter__(self):
        """Returns self"""
        return self
                                                                    
    def __exit__(self, *args):
        """
        Release this resource.
        """
        raise NotImplementedError


class IncomingResponse:
    """
    Represents an incoming HTTP Response.
    """
    
    def status(self) -> int:
        """
        Returns the status code from the incoming response.
        """
        raise NotImplementedError

    def headers(self) -> Fields:
        """
        Returns the headers from the incoming response.
        
        The returned `headers` resource is immutable: `set`, `append`, and
        `delete` operations will fail with `header-error.immutable`.
        
        This headers resource is a child: it must be dropped before the parent
        `incoming-response` is dropped.
        """
        raise NotImplementedError

    def consume(self) -> IncomingBody:
        """
        Returns the incoming body. May be called at most once. Returns error
        if called additional times.
        
        Raises: `consumer.types.Err(None)`
        """
        raise NotImplementedError

    def __enter__(self):
        """Returns self"""
        return self
                                                                    
    def __exit__(self, *args):
        """
        Release this resource.
        """
        raise NotImplementedError


class FutureIncomingResponse:
    """
    Represents a future which may eventaully return an incoming HTTP
    Response, or an error.
    
    This resource is returned by the `wasi:http/outgoing-handler` interface to
    provide the HTTP Response corresponding to the sent Request.
    """
    
    def subscribe(self) -> poll.Pollable:
        """
        Returns a pollable which becomes ready when either the Response has
        been received, or an error has occured. When this pollable is ready,
        the `get` method will return `some`.
        """
        raise NotImplementedError

    def get(self) -> Optional[Result[Result[IncomingResponse, ErrorCode], None]]:
        """
        Returns the incoming HTTP Response, or an error, once one is ready.
        
        The outer `option` represents future readiness. Users can wait on this
        `option` to become `some` using the `subscribe` method.
        
        The outer `result` is used to retrieve the response or error at most
        once. It will be success on the first call in which the outer option
        is `some`, and error on subsequent calls.
        
        The inner `result` represents that either the incoming HTTP Response
        status and headers have recieved successfully, or that an error
        occured. Errors may also occur while consuming the response body,
        but those will be reported by the `incoming-body` and its
        `output-stream` child.
        """
        raise NotImplementedError

    def __enter__(self):
        """Returns self"""
        return self
                                                                    
    def __exit__(self, *args):
        """
        Release this resource.
        """
        raise NotImplementedError


class DescriptorType(Enum):
    """
    The type of a filesystem object referenced by a descriptor.
    
    Note: This was called `filetype` in earlier versions of WASI.
    """
    UNKNOWN = 0
    BLOCK_DEVICE = 1
    CHARACTER_DEVICE = 2
    DIRECTORY = 3
    FIFO = 4
    SYMBOLIC_LINK = 5
    REGULAR_FILE = 6
    SOCKET = 7

class DescriptorFlags(Flag):
    """
    Descriptor flags.
    
    Note: This was called `fdflags` in earlier versions of WASI.
    """
    READ = auto()
    WRITE = auto()
    FILE_INTEGRITY_SYNC = auto()
    DATA_INTEGRITY_SYNC = auto()
    REQUESTED_WRITE_SYNC = auto()
    MUTATE_DIRECTORY = auto()

class PathFlags(Flag):
    """
    Flags determining the method of how paths are resolved.
    """
    SYMLINK_FOLLOW = auto()

class OpenFlags(Flag):
    """
    Open flags used by `open-at`.
    """
    CREATE = auto()
    DIRECTORY = auto()
    EXCLUSIVE = auto()
    TRUNCATE = auto()

@dataclass
class DescriptorStat:
    """
    File attributes.
    
    Note: This was called `filestat` in earlier versions of WASI.
    """
    type: DescriptorType
    link_count: int
    size: int
    data_access_timestamp: Optional[wall_clock.Datetime]
    data_modification_timestamp: Optional[wall_clock.Datetime]
    status_change_timestamp: Optional[wall_clock.Datetime]


@dataclass
class NewTimestampNoChange:
    pass


@dataclass
class NewTimestampNow:
    pass


@dataclass
class NewTimestampTimestamp:
    value: wall_clock.Datetime


NewTimestamp = Union[NewTimestampNoChange, NewTimestampNow, NewTimestampTimestamp]
"""
When setting a timestamp, this gives the value to set it to.
"""


@dataclass
class DirectoryEntry:
    """
    A directory entry.
    """
    type: DescriptorType
    name: str

class ErrorCode(Enum):
    """
    Error codes returned by functions, similar to `errno` in POSIX.
    Not all of these error codes are returned by the functions provided by this
    API; some are used in higher-level library layers, and others are provided
    merely for alignment with POSIX.
    """
    ACCESS = 0
    WOULD_BLOCK = 1
    ALREADY = 2
    BAD_DESCRIPTOR = 3
    BUSY = 4
    DEADLOCK = 5
    QUOTA = 6
    EXIST = 7
    FILE_TOO_LARGE = 8
    ILLEGAL_BYTE_SEQUENCE = 9
    IN_PROGRESS = 10
    INTERRUPTED = 11
    INVALID = 12
    IO = 13
    IS_DIRECTORY = 14
    LOOP = 15
    TOO_MANY_LINKS = 16
    MESSAGE_SIZE = 17
    NAME_TOO_LONG = 18
    NO_DEVICE = 19
    NO_ENTRY = 20
    NO_LOCK = 21
    INSUFFICIENT_MEMORY = 22
    INSUFFICIENT_SPACE = 23
    NOT_DIRECTORY = 24
    NOT_EMPTY = 25
    NOT_RECOVERABLE = 26
    UNSUPPORTED = 27
    NO_TTY = 28
    NO_SUCH_DEVICE = 29
    OVERFLOW = 30
    NOT_PERMITTED = 31
    PIPE = 32
    READ_ONLY = 33
    INVALID_SEEK = 34
    TEXT_FILE_BUSY = 35
    CROSS_DEVICE = 36

class Advice(Enum):
    """
    File or memory access pattern advisory information.
    """
    NORMAL = 0
    SEQUENTIAL = 1
    RANDOM = 2
    WILL_NEED = 3
    DONT_NEED = 4
    NO_REUSE = 5

@dataclass
class MetadataHashValue:
    """
    A 128-bit hash value, split into parts because wasm doesn't have a
    128-bit integer type.
    """
    lower: int
    upper: int

class DirectoryEntryStream:
    """
    A stream of directory entries.
    """
    
    def read_directory_entry(self) -> Optional[DirectoryEntry]:
        """
        Read a single directory entry from a `directory-entry-stream`.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def __enter__(self):
        """Returns self"""
        return self
                                                                    
    def __exit__(self, *args):
        """
        Release this resource.
        """
        raise NotImplementedError


class Descriptor:
    """
    A descriptor is a reference to a filesystem object, which may be a file,
    directory, named pipe, special file, or other object on which filesystem
    calls may be made.
    """
    
    def read_via_stream(self, offset: int) -> streams.InputStream:
        """
        Return a stream for reading from a file, if available.
        
        May fail with an error-code describing why the file cannot be read.
        
        Multiple read, write, and append streams may be active on the same open
        file and they do not interfere with each other.
        
        Note: This allows using `read-stream`, which is similar to `read` in POSIX.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def write_via_stream(self, offset: int) -> streams.OutputStream:
        """
        Return a stream for writing to a file, if available.
        
        May fail with an error-code describing why the file cannot be written.
        
        Note: This allows using `write-stream`, which is similar to `write` in
        POSIX.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def append_via_stream(self) -> streams.OutputStream:
        """
        Return a stream for appending to a file, if available.
        
        May fail with an error-code describing why the file cannot be appended.
        
        Note: This allows using `write-stream`, which is similar to `write` with
        `O_APPEND` in in POSIX.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def advise(self, offset: int, length: int, advice: Advice) -> None:
        """
        Provide file advisory information on a descriptor.
        
        This is similar to `posix_fadvise` in POSIX.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def sync_data(self) -> None:
        """
        Synchronize the data of a file to disk.
        
        This function succeeds with no effect if the file descriptor is not
        opened for writing.
        
        Note: This is similar to `fdatasync` in POSIX.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def get_flags(self) -> DescriptorFlags:
        """
        Get flags associated with a descriptor.
        
        Note: This returns similar flags to `fcntl(fd, F_GETFL)` in POSIX.
        
        Note: This returns the value that was the `fs_flags` value returned
        from `fdstat_get` in earlier versions of WASI.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def get_type(self) -> DescriptorType:
        """
        Get the dynamic type of a descriptor.
        
        Note: This returns the same value as the `type` field of the `fd-stat`
        returned by `stat`, `stat-at` and similar.
        
        Note: This returns similar flags to the `st_mode & S_IFMT` value provided
        by `fstat` in POSIX.
        
        Note: This returns the value that was the `fs_filetype` value returned
        from `fdstat_get` in earlier versions of WASI.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def set_size(self, size: int) -> None:
        """
        Adjust the size of an open file. If this increases the file's size, the
        extra bytes are filled with zeros.
        
        Note: This was called `fd_filestat_set_size` in earlier versions of WASI.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def set_times(self, data_access_timestamp: NewTimestamp, data_modification_timestamp: NewTimestamp) -> None:
        """
        Adjust the timestamps of an open file or directory.
        
        Note: This is similar to `futimens` in POSIX.
        
        Note: This was called `fd_filestat_set_times` in earlier versions of WASI.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def read(self, length: int, offset: int) -> Tuple[bytes, int]:
        """
        Read from a descriptor, without using and updating the descriptor's offset.
        
        This function returns a list of bytes containing the data that was
        read, along with a bool which, when true, indicates that the end of the
        file was reached. The returned list will contain up to `length` bytes; it
        may return fewer than requested, if the end of the file is reached or
        if the I/O operation is interrupted.
        
        In the future, this may change to return a `stream<u8, error-code>`.
        
        Note: This is similar to `pread` in POSIX.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def write(self, buffer: bytes, offset: int) -> int:
        """
        Write to a descriptor, without using and updating the descriptor's offset.
        
        It is valid to write past the end of a file; the file is extended to the
        extent of the write, with bytes between the previous end and the start of
        the write set to zero.
        
        In the future, this may change to take a `stream<u8, error-code>`.
        
        Note: This is similar to `pwrite` in POSIX.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def read_directory(self) -> DirectoryEntryStream:
        """
        Read directory entries from a directory.
        
        On filesystems where directories contain entries referring to themselves
        and their parents, often named `.` and `..` respectively, these entries
        are omitted.
        
        This always returns a new stream which starts at the beginning of the
        directory. Multiple streams may be active on the same directory, and they
        do not interfere with each other.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def sync(self) -> None:
        """
        Synchronize the data and metadata of a file to disk.
        
        This function succeeds with no effect if the file descriptor is not
        opened for writing.
        
        Note: This is similar to `fsync` in POSIX.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def create_directory_at(self, path: str) -> None:
        """
        Create a directory.
        
        Note: This is similar to `mkdirat` in POSIX.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def stat(self) -> DescriptorStat:
        """
        Return the attributes of an open file or directory.
        
        Note: This is similar to `fstat` in POSIX, except that it does not return
        device and inode information. For testing whether two descriptors refer to
        the same underlying filesystem object, use `is-same-object`. To obtain
        additional data that can be used do determine whether a file has been
        modified, use `metadata-hash`.
        
        Note: This was called `fd_filestat_get` in earlier versions of WASI.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def stat_at(self, path_flags: PathFlags, path: str) -> DescriptorStat:
        """
        Return the attributes of a file or directory.
        
        Note: This is similar to `fstatat` in POSIX, except that it does not
        return device and inode information. See the `stat` description for a
        discussion of alternatives.
        
        Note: This was called `path_filestat_get` in earlier versions of WASI.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def set_times_at(self, path_flags: PathFlags, path: str, data_access_timestamp: NewTimestamp, data_modification_timestamp: NewTimestamp) -> None:
        """
        Adjust the timestamps of a file or directory.
        
        Note: This is similar to `utimensat` in POSIX.
        
        Note: This was called `path_filestat_set_times` in earlier versions of
        WASI.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def link_at(self, old_path_flags: PathFlags, old_path: str, new_descriptor: Self, new_path: str) -> None:
        """
        Create a hard link.
        
        Note: This is similar to `linkat` in POSIX.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def open_at(self, path_flags: PathFlags, path: str, open_flags: OpenFlags, flags: DescriptorFlags) -> Self:
        """
        Open a file or directory.
        
        The returned descriptor is not guaranteed to be the lowest-numbered
        descriptor not currently open/ it is randomized to prevent applications
        from depending on making assumptions about indexes, since this is
        error-prone in multi-threaded contexts. The returned descriptor is
        guaranteed to be less than 2**31.
        
        If `flags` contains `descriptor-flags::mutate-directory`, and the base
        descriptor doesn't have `descriptor-flags::mutate-directory` set,
        `open-at` fails with `error-code::read-only`.
        
        If `flags` contains `write` or `mutate-directory`, or `open-flags`
        contains `truncate` or `create`, and the base descriptor doesn't have
        `descriptor-flags::mutate-directory` set, `open-at` fails with
        `error-code::read-only`.
        
        Note: This is similar to `openat` in POSIX.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def readlink_at(self, path: str) -> str:
        """
        Read the contents of a symbolic link.
        
        If the contents contain an absolute or rooted path in the underlying
        filesystem, this function fails with `error-code::not-permitted`.
        
        Note: This is similar to `readlinkat` in POSIX.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def remove_directory_at(self, path: str) -> None:
        """
        Remove a directory.
        
        Return `error-code::not-empty` if the directory is not empty.
        
        Note: This is similar to `unlinkat(fd, path, AT_REMOVEDIR)` in POSIX.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def rename_at(self, old_path: str, new_descriptor: Self, new_path: str) -> None:
        """
        Rename a filesystem object.
        
        Note: This is similar to `renameat` in POSIX.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def symlink_at(self, old_path: str, new_path: str) -> None:
        """
        Create a symbolic link (also known as a "symlink").
        
        If `old-path` starts with `/`, the function fails with
        `error-code::not-permitted`.
        
        Note: This is similar to `symlinkat` in POSIX.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def unlink_file_at(self, path: str) -> None:
        """
        Unlink a filesystem object that is not a directory.
        
        Return `error-code::is-directory` if the path refers to a directory.
        Note: This is similar to `unlinkat(fd, path, 0)` in POSIX.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def is_same_object(self, other: Self) -> int:
        """
        Test whether two descriptors refer to the same filesystem object.
        
        In POSIX, this corresponds to testing whether the two descriptors have the
        same device (`st_dev`) and inode (`st_ino` or `d_ino`) numbers.
        wasi-filesystem does not expose device and inode numbers, so this function
        may be used instead.
        """
        raise NotImplementedError

    def metadata_hash(self) -> MetadataHashValue:
        """
        Return a hash of the metadata associated with a filesystem object referred
        to by a descriptor.
        
        This returns a hash of the last-modification timestamp and file size, and
        may also include the inode number, device number, birth timestamp, and
        other metadata fields that may change when the file is modified or
        replaced. It may also include a secret value chosen by the
        implementation and not otherwise exposed.
        
        Implementations are encourated to provide the following properties:
        
        - If the file is not modified or replaced, the computed hash value should
        usually not change.
        - If the object is modified or replaced, the computed hash value should
        usually change.
        - The inputs to the hash should not be easily computable from the
        computed hash.
        
        However, none of these is required.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def metadata_hash_at(self, path_flags: PathFlags, path: str) -> MetadataHashValue:
        """
        Return a hash of the metadata associated with a filesystem object referred
        to by a directory descriptor and a relative path.
        
        This performs the same hash computation as `metadata-hash`.
        
        Raises: `consumer.types.Err(consumer.imports.types.ErrorCode)`
        """
        raise NotImplementedError

    def __enter__(self):
        """Returns self"""
        return self
                                                                    
    def __exit__(self, *args):
        """
        Release this resource.
        """
        raise NotImplementedError



def http_error_code(err: error.Error) -> Optional[ErrorCode]:
    """
    Attempts to extract a http-related `error` from the wasi:io `error`
    provided.
    
    Stream operations which return
    `wasi:io/stream/stream-error::last-operation-failed` have a payload of
    type `wasi:io/error/error` with more information about the operation
    that failed. This payload can be passed through to this function to see
    if there's http-related information about the error to return.
    
    Note that this function is fallible because not all io-errors are
    http-related errors.
    """
    raise NotImplementedError

def filesystem_error_code(err: error.Error) -> Optional[ErrorCode]:
    """
    Attempts to extract a filesystem-related `error-code` from the stream
    `error` provided.
    
    Stream operations which return `stream-error::last-operation-failed`
    have a payload with more information about the operation that failed.
    This payload can be passed through to this function to see if there's
    filesystem-related information about the error to return.
    
    Note that this function is fallible because not all stream-related
    errors are filesystem-related errors.
    """
    raise NotImplementedError

