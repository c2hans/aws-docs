---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/http-configuration.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# HTTP configuration

Most applications don't need to change the HTTP client. You might change it to use an HTTP client that supports bidirectional streaming or to provide your own implementation. This page includes the following topics:
+ [Provided HTTP clients](#http-clients) describes the HTTP clients that the SDK provides and their capabilities.
+ [Override the HTTP client](#http-override-client) explains how to replace the HTTP client and implement a custom HTTP client.

Each service client sends requests through a *transport*, the component that sends a request over the network and returns the response. AWS services use HTTP, so the transport of a service client is an *HTTP client*. Synchronous service clients need an HTTP client that implements the `HTTPClient` interface. Asynchronous service clients need one that implements the `AsyncHTTPClient` interface. Both interfaces are defined in the [smithy-http package on PyPI](https://pypi.org/project/smithy-http/). Because the two client types need different HTTP clients, this page shows both.

## Provided HTTP clients
<a name="http-clients"></a>

The SDK provides the following HTTP clients in the smithy-http package. Each service client type uses its default HTTP client unless you set a different one.

| HTTP client | Service client type | HTTP versions | Description |
| --- | --- | --- | --- |
| Urllib3HTTPClient in smithy\_http.urllib3 | Synchronous (default) | HTTP/1.1 | Built on the [urllib3 library](https://urllib3.readthedocs.io/). |
| AIOHTTPClient in smithy\_http.aio.aiohttp | Asynchronous (default) | HTTP/1.1 | Built on the [aiohttp library](https://docs.aiohttp.org/). It doesn't support bidirectional event streams. |
| AWSCRTHTTPClient in smithy\_http.aio.crt | Asynchronous | HTTP/1.1 and HTTP/2 | Built on the [AWS Common Runtime (CRT)](https://docs.aws.amazon.com/sdkref/latest/guide/common-runtime.html). It's the only provided HTTP client that supports bidirectional event streams. |

A standard installation of a service client package includes `Urllib3HTTPClient` and `AIOHTTPClient`. Only `AWSCRTHTTPClient` needs the client's `awscrt` extra. Synchronous service clients can't use `AWSCRTHTTPClient`.

## Override the HTTP client
<a name="http-override-client"></a>

To use a different HTTP client, create an HTTP client and pass it as the `transport` field when you resolve the configuration. The following example sets the default HTTP client of each client type explicitly.

------
#### [ Synchronous client ]

 **Imports**

```python
from aws_sdk_bedrock_runtime import BedrockRuntimeClient, BedrockRuntimeConfig
from smithy_http.urllib3 import Urllib3HTTPClient
```

 **Code**

```python
def create_client() -> BedrockRuntimeClient:
    config = BedrockRuntimeConfig.resolve(
        region="us-east-1",
        transport=Urllib3HTTPClient(),
    )
    return BedrockRuntimeClient(config=config)
```

------
#### [ Asynchronous client ]

 **Imports**

```python
from aws_sdk_bedrock_runtime import AsyncBedrockRuntimeClient, AsyncBedrockRuntimeConfig
from smithy_http.aio.aiohttp import AIOHTTPClient
```

 **Code**

```python
async def create_client() -> AsyncBedrockRuntimeClient:
    config = await AsyncBedrockRuntimeConfig.resolve(
        region="us-east-1",
        transport=AIOHTTPClient(),
    )
    return AsyncBedrockRuntimeClient(config=config)
```

------

When you close a service client, it also closes its HTTP client. Create a separate HTTP client for each service client.

### Use the AWS CRT client for bidirectional streaming
<a name="http-crt-streaming"></a>

Some operations use bidirectional (duplex) event streams. These operations exist only on asynchronous service clients. The default `AIOHTTPClient` doesn't support them. To use these operations, install the client's `awscrt` extra and set `AWSCRTHTTPClient` as the transport.

The `awscrt` extra installs a compatible version of the [awscrt library from PyPI](https://pypi.org/project/awscrt/). Install it as part of the client package:

```bash
python -m pip install "aws-sdk-bedrock-runtime[awscrt]"
```

 **Imports**

```python
from aws_sdk_bedrock_runtime import AsyncBedrockRuntimeClient, AsyncBedrockRuntimeConfig
from smithy_http.aio.crt import AWSCRTHTTPClient
```

 **Code**

```python
async def create_client() -> AsyncBedrockRuntimeClient:
    config = await AsyncBedrockRuntimeConfig.resolve(
        region="us-east-1",
        transport=AWSCRTHTTPClient(),
    )
    return AsyncBedrockRuntimeClient(config=config)
```

The CRT client negotiates HTTP/2 for event-stream operations, so you don't need to change its settings. You can also use `AWSCRTHTTPClient` for operations that don't use bidirectional streaming.

### Provide a custom HTTP client
<a name="http-custom-client"></a>

To control how the service client sends requests, implement the HTTP client interface for your client type and pass an instance as the `transport`. Most applications don't need a custom HTTP client.

A custom HTTP client has a `send` method that accepts an `HTTPRequest` and returns an `HTTPResponse`. To build the response, you can use the `HTTPResponse` class and the `tuples_to_fields` function from `smithy_http`. The class must also set the `TIMEOUT_EXCEPTIONS` attribute to the exception types that your HTTP client raises when a request times out. The SDK converts these exceptions to `ClientTimeoutError` and retries the request.

If your HTTP client holds network resources, such as sessions or connection pools, add a `close` method that releases them. The service client calls this method when you close the service client or exit its `with` or `async with` block.

------
#### [ Synchronous client ]

Implement `smithy_http.interfaces.HTTPClient` with synchronous `send` and `close` methods.

 **Imports**

```python
from smithy_http.interfaces import (
    HTTPClient,
    HTTPClientConfiguration,
    HTTPRequest,
    HTTPRequestConfiguration,
    HTTPResponse,
)
```

 **Code**

```python
class CustomHTTPClient(HTTPClient):
    # Exception types that your underlying HTTP client raises on timeouts.
    TIMEOUT_EXCEPTIONS = (TimeoutError,)

    def __init__(
        self, *, client_config: HTTPClientConfiguration | None = None
    ) -> None:
        self._client_config = client_config
        # Initialize your underlying HTTP client here.

    def send(
        self,
        request: HTTPRequest,
        *,
        request_config: HTTPRequestConfiguration | None = None,
    ) -> HTTPResponse:
        # Send the request with your HTTP client and return an HTTPResponse.
        ...

    def close(self) -> None:
        # Release resources held by your underlying HTTP client.
        ...
```

------
#### [ Asynchronous client ]

Implement `smithy_http.aio.interfaces.AsyncHTTPClient` with asynchronous `send` and `close` methods.

 **Imports**

```python
from smithy_http.aio.interfaces import AsyncHTTPClient
from smithy_http.interfaces import (
    HTTPClientConfiguration,
    HTTPRequest,
    HTTPRequestConfiguration,
    HTTPResponse,
)
```

 **Code**

```python
class CustomAsyncHTTPClient(AsyncHTTPClient):
    # Exception types that your underlying HTTP client raises on timeouts.
    TIMEOUT_EXCEPTIONS = (TimeoutError,)

    def __init__(
        self, *, client_config: HTTPClientConfiguration | None = None
    ) -> None:
        self._client_config = client_config
        # Initialize your underlying HTTP client here.

    async def send(
        self,
        request: HTTPRequest,
        *,
        request_config: HTTPRequestConfiguration | None = None,
    ) -> HTTPResponse:
        # Send the request with your HTTP client and return an HTTPResponse.
        ...

    async def close(self) -> None:
        # Release resources held by your underlying HTTP client.
        ...
```

------

Pass an instance of your HTTP client as the `transport` in the same way as a provided HTTP client.
