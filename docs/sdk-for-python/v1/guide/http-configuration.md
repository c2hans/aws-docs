---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/http-configuration.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# HTTP configuration
<a name="http-configuration"></a>

Each service client sends every request through a *transport*, the component that sends the request and returns the response. A transport is protocol-agnostic, which lets the SDK support different wire protocols through a common interface. Because the SDK communicates with AWS over HTTP, a service client's transport is an *HTTP client*: an implementation of the `HTTPClient` protocol. See [smithy-http on PyPI](https://pypi.org/project/smithy-http/) for the runtime library that defines this protocol.

Most applications don't need to change the transport. You might override it to use a different HTTP client, such as one that supports bidirectional streaming, or to provide your own implementation. This page includes the following topics:
+ [Provided HTTP clients](#http-clients) covers the HTTP client implementations that the SDK provides and their capabilities.
+ [Override the HTTP client](#http-override-client) explains how to override the HTTP client, including how to implement a custom client.

## Provided HTTP clients
<a name="http-clients"></a>

The SDK provides two HTTP client implementations, both defined in smithy-http:

`AIOHTTPClient`
Built on the aiohttp library. This is the default transport for every service client and it's the only HTTP client installed by default. It communicates over HTTP/1.1 only. For more information, see the [aiohttp website](https://docs.aiohttp.org/).

`AWSCRTHTTPClient`
Built on the [AWS Common Runtime (CRT)](https://docs.aws.amazon.com/sdkref/latest/guide/common-runtime.html). It communicates over both HTTP/1.1 and HTTP/2, and it's currently the only transport that supports bidirectional (duplex) event streaming.

Each provided client accepts a configuration object for connection settings. The available settings are limited in the current release. Additional settings are planned for future releases.

## Override the HTTP client
<a name="http-override-client"></a>

To use a transport other than the default, construct it and pass it as the `transport` field when you resolve the configuration.

### Use the AWS CRT client for bidirectional streaming
<a name="http-crt-streaming"></a>

Some operations use bidirectional (duplex) event streams. The default aiohttp transport doesn't support duplex streaming. To use these operations, install the client's `awscrt` extra and set `AWSCRTHTTPClient` as the transport.

The `awscrt` extra pulls in a compatible version of the [awscrt library from PyPI](https://pypi.org/project/awscrt/). Install it as part of the client package:

```
python -m pip install "aws-sdk-bedrock-runtime[awscrt]"
```

 **Imports**

```
from aws_sdk_bedrock_runtime.client import AsyncBedrockRuntimeClient
from aws_sdk_bedrock_runtime.config import AsyncBedrockRuntimeConfig
from smithy_http.aio.crt import AWSCRTHTTPClient
```

 **Code**

```
async def create_client() -> AsyncBedrockRuntimeClient:
    config = await AsyncBedrockRuntimeConfig.resolve(
        region="us-east-1",
        transport=AWSCRTHTTPClient(),
    )
    return AsyncBedrockRuntimeClient(config=config)
```

You can use `AWSCRTHTTPClient` for a client even when you don't need bidirectional streaming; the `awscrt` extra is required in either case.

### Provide a custom HTTP client
<a name="http-custom-client"></a>

For full control over how requests are sent, implement the `HTTPClient` protocol and pass an instance as the `transport`. This is an advanced option; the built-in clients are sufficient for most applications. A custom client implements a `send` method that accepts an `HTTPRequest` and returns an `HTTPResponse`.

If your custom HTTP client holds network resources, such as sessions or connection pools, implement an asynchronous `close` method to release them. The generated service client's `close` method calls the transport's `close` method when present. This happens when you invoke `close` directly or exit the client's asynchronous context.

 **Imports**

```
from smithy_http.aio.interfaces import HTTPClient, HTTPRequest, HTTPResponse
from smithy_http.interfaces import (
    HTTPClientConfiguration,
    HTTPRequestConfiguration,
)
```

 **Code**

```
class CustomHTTPClient(HTTPClient):
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

Pass an instance of your client as the `transport` in the same way as a provided client.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Python. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-python` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
