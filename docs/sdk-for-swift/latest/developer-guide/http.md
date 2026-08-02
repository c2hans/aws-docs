---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/http.html
---

# Configuring HTTP-level settings within the AWS SDK for Swift
<a name="http"></a>

## Configuring HTTP timeouts
<a name="configuring-http-timeouts"></a>

The AWS SDK for Swift supports two types of timeout on HTTP clients. These are configured by setting the corresponding properties on the service client's `httpClientConfiguration` structure to the number of seconds to allow before timing out:
+ **`connectTimeout`** specifies how much time to allow before an attempt to open an HTTP connection times out.
+ **`socketTimeout`** specifies how long to wait for a socket to respond to a request before timing out.

```
        do {
            let config = try await S3Client.S3ClientConfiguration(
                region: region,
                httpClientConfiguration: HttpClientConfiguration(
                    connectTimeout: 2,
                    socketTimeout: 5
                )
            )
            let s3Client = S3Client(config: config)
            _ = try await s3Client.listBuckets(input: ListBucketsInput())
            print("*** Success!")
        } catch CommonRunTimeError.crtError(let crtError) {
            print("*** An error occurred accessing the bucket list: \(crtError.message)")
        } catch {
            print("*** Unexpected error occurred requesting the bucket list.")
        }
```

This example creates an Amazon S3 client that times out HTTP connection attempts after 2 seconds, while allowing up to 5 seconds for sockets to time out.

## Customizing HTTP headers
<a name="configuring-http-headers"></a>

You can add default headers to your HTTP requests by setting the service client's `httpConfiguration.defaultHeaders` property to a `Headers` structure header which is initialized with a dictionary that maps header names to their values.

**Important**
Setting default headers that interfere with headers the AWS service expects may result in unpredictable results.

This example creates an Amazon S3 client whose HTTP configuration adds two custom headers to HTTP requests sent by the client:

```
import ClientRuntime
import AWSS3
import SmithyHTTPAPI
import AwsCommonRuntimeKit

        let config = try await S3Client.S3ClientConfiguration(
            region: region,
            httpClientConfiguration: HttpClientConfiguration(
                defaultHeaders: Headers(
                    [
                        "X-My-Custom-Header": "CustomHeaderValue",
                        "X-Another-Custom-Header": "AnotherCustomValue"
                    ]
                )
            )
        )
        let s3Client = S3Client(config: config)
```

## HTTP/1 vs. HTTP/2
<a name="configuring-http-version"></a>

HTTP version 1.1 is adequate for most tasks when using AWS services, and is used automatically for these. However, there are times when HTTP version 2 is required. While some AWS SDKs require you to specifically customize the service client to use HTTP/2, the SDK for Swift detects when a function uses event streaming and automatically uses HTTP/2 for these actions. Your code doesn't need to do anything to handle this.

## Using a custom HTTP client
<a name="configuring-http-client"></a>

To use a custom HTTP client, create a client class which conforms to the `[HTTPClient](https://sdk.amazonaws.com/swift/api/smithyhttpapi/latest/documentation/smithyhttpapi/httpclient)` class in the `SmithyHTTPAPI` module. This protocol requires a single function: [https://sdk.amazonaws.com/swift/api/smithyhttpapi/latest/documentation/smithyhttpapi/httpclient/send(request:)](https://sdk.amazonaws.com/swift/api/smithyhttpapi/latest/documentation/smithyhttpapi/httpclient/send(request:)), which returns a `[HTTPResponse](https://sdk.amazonaws.com/swift/api/smithyhttpapi/latest/documentation/smithyhttpapi/httpresponse)` object. You can then specify your custom HTTP client by setting the client configuration's `[httpClientEngine](https://sdk.amazonaws.com/swift/api/clientruntime/latest/documentation/clientruntime/defaultsdkruntimeconfiguration/httpclientengine)` property to an instance of your custom HTTP client class.
