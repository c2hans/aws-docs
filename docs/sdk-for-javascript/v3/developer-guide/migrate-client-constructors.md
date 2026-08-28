---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrate-client-constructors.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Client constructors
<a name="migrate-client-constructors"></a>

 This list is indexed by [v2 config parameters](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html).
+  [`computeChecksums`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#computeChecksums-property)
  +  **v2**: Whether to compute MD5 checksums for payload bodies when the service accepts it (currently supported in S3 only).
  +  **v3**: applicable commands of S3 (PutObject, PutBucketCors, etc.) will automatically compute the MD5 checksums for of the request payload. You can also specify a different checksum algorithm in the commands' `ChecksumAlgorithm` parameter to use a different checksum algorithm. You can find more information in the [S3 feature announcement](https://aws.amazon.com/blogs/aws/new-additional-checksum-algorithms-for-amazon-s3/).
+  [`convertResponseTypes`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#convertResponseTypes-property)
  +  **v2**: Whether types are converted when parsing response data.
  +  **v3**: **Deprecated**. This option is considered not type-safe because it doesn't convert the types like time stamp or base64 binaries from the JSON response.
+  [`correctClockSkew`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#correctClockSkew-property)
  +  **v2**: Whether to apply a clock skew correction and retry requests that fail because of an skewed client clock.
  +  **v3**: **Deprecated**. SDK *always* applies a clock skew correction.
+  [`systemClockOffset`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#systemClockOffset-property)
  +  **v2**: An offset value in milliseconds to apply to all signing times.
  +  **v3**: No change.
+  [`credentials`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#credentials-property)
  +  **v2**: The AWS credentials to sign requests with.
  +  **v3**: No change. It can also be an async function that returns credentials. If the function returns an `expiration (Date)`, the function will be called again when the expiration datetime nears. See [v3 API reference for `AwsAuthInputConfig` credentials](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-middleware-signing/Interface/AwsAuthInputConfig/).
+  [`endpointCacheSize`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#endpointCacheSize-property)
  +  **v2**: The size of the global cache storing endpoints from endpoint discovery operations.
  +  **v3**: No change.
+  [`endpointDiscoveryEnabled`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#endpointDiscoveryEnabled-property)
  +  **v2**: Whether to call operations with endpoints given by service dynamically.
  +  **v3**: No change.
+  [`hostPrefixEnabled`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#hostPrefixEnabled-property)
  +  **v2**: Whether to marshal request parameters to the prefix of hostname.
  +  **v3**: **Deprecated**. SDK *always* injects the hostname prefix when necessary.
+  [`httpOptions`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#httpOptions-property)

   A set of options to pass to the low-level HTTP request. These options are aggregated differently in v3. You can configure them by supplying a new `requestHandler`. Here's the example of setting http options in Node.js runtime. You can find more in [v3 API reference for NodeHttpHandler](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-smithy-node-http-handler/).

   All v3 requests use HTTPS by default. You only need to provide custom httpsAgent.

  ```
  const { Agent } = require("https");
  const { Agent: HttpAgent } = require("http");
  const { NodeHttpHandler } = require("@smithy/node-http-handler");
  const dynamodbClient = new DynamoDBClient({
      requestHandler: new NodeHttpHandler({
          httpsAgent: new Agent({
              /*params*/
          }),
          connectionTimeout: /*number in milliseconds*/,
          socketTimeout: /*number in milliseconds*/
      }),
  });
  ```

   If you are passing custom endpoint which uses http, then you need to provide httpAgent.

  ```
  const { Agent } = require("http");
  const { NodeHttpHandler } = require("@smithy/node-http-handler");

  const dynamodbClient = new DynamoDBClient({
      requestHandler: new NodeHttpHandler({
          httpAgent: new Agent({
              /*params*/
          }),
      }),
      endpoint: "http://example.com",
  });
  ```

   If the client is running in browsers, a different set of options is available. You can find more in [v3 API reference for FetchHttpHandler](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-smithy-fetch-http-handler/).

  ```
  const { FetchHttpHandler } = require("@smithy/fetch-http-handler");
  const dynamodbClient = new DynamoDBClient({
      requestHandler: new FetchHttpHandler({
          requestTimeout: /* number in milliseconds */
      }),
  });
  ```

   Each option of `httpOptions` is specified below:
  +  `proxy`
    +  **v2**: The URL to proxy requests through.
    +  **v3**: You can set up a proxy with an agent following [Configuring proxies for Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/node-configuring-proxies.html).
  +  `agent`
    +  **v2**: The Agent object to perform HTTP requests with. Used for connection pooling.
    +  **v3**: You can configure `httpAgent` or `httpsAgent` as shown in the examples above.
  +  `connectTimeout`
    +  **v2**: Sets the socket to timeout after failing to establish a connection with the server after `connectTimeout` milliseconds.
    +  **v3**: `connectionTimeout` is available [in `NodeHttpHandler` options](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-smithy-node-http-handler/).
  +  `timeout`
    +  **v2**: The number of milliseconds a request can take before automatically being terminated.
    +  **v3**: `socketTimeout` is available [in `NodeHttpHandler` options](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-smithy-node-http-handler/).
  +  `xhrAsync`
    +  **v2**: Whether the SDK will send asynchronous HTTP requests.
    +  **v3**: **Deprecated**. Requests are *always* asynchronous.
  +  `xhrWithCredentials`
    +  **v2**: Sets the "withCredentials" property of an XMLHttpRequest object.
    +  **v3**: Not available. SDK inherits [the default fetch configurations](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).
+  [`logger`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#logger-property)
  +  **v2**: An object that responds to `.write()` (like a stream) or `.log()` (like the console object) in order to log information about requests.
  +  **v3**: No change. More granular logs are available in v3.
+  [`maxRedirects`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#maxRedirects-property)
  +  **v2**: The maximum amount of redirects to follow for a service request.
  +  **v3**: **Deprecated**. SDK *does not* follow redirects to avoid unintentional cross-region requests.
+  [`maxRetries`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#maxRetries-property)
  +  **v2**: The maximum amount of retries to perform for a service request.
  +  **v3**: Changed to `maxAttempts`. See more in [v3 API reference for RetryInputConfig](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-smithy-middleware-retry/Interface/RetryInputConfig/). Note that `maxAttempts` should be `maxRetries + 1`.
+  [`paramValidation`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#paramValidation-property)
  +  **v2**: Whether input parameters should be validated against the operation description before sending the request.
  +  **v3**: **Deprecated**. SDK *does not* do validation on client-side at runtime.
+  [`region`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#region-property)
  +  **v2**: The region to send service requests to.
  +  **v3**: No change. It can also be an async function that returns a region string.
+  [`retryDelayOptions`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#retryDelayOptions-property)
  +  **v2**: A set of options to configure the retry delay on retryable errors.
  +  **v3**: **Deprecated**. SDK supports more flexible retry strategy with `retryStrategy` client constructor option. See more [in v3 API reference](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-smithy-util-retry/).
+  [`s3BucketEndpoint`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#s3BucketEndpoint-property)
  +  **v2**: Whether the provided endpoint addresses an individual bucket (false if it addresses the root API endpoint).
  +  **v3**: Changed to `bucketEndpoint`. See more in [v3 API reference for bucketEndpoint](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-middleware-bucket-endpoint/Interface/BucketEndpointInputConfig/). Note that when set to `true`, you specify the request endpoint in the `Bucket` request parameter, the original endpoint will be overwritten. Whereas in v2, the request endpoint in client constructor overwrites the `Bucket` request parameter.
+  [`s3DisableBodySigning`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#s3DisableBodySigning-property)
  +  **v2**: Whether to disable S3 body signing when using signature version v4.
  +  **v3**: Renamed to `applyChecksum`.
+  [`s3ForcePathStyle`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#s3ForcePathStyle-property)
  +  **v2**: Whether to force path style URLs for S3 objects.
  +  **v3**: Renamed to `forcePathStyle`.
+  [`s3UseArnRegion`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#s3UseArnRegion-property)
  +  **v2**: Whether to override the request region with the region inferred from requested resource's ARN.
  +  **v3**: Renamed to `useArnRegion`.
+  [`s3UsEast1RegionalEndpoint`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#s3UsEast1RegionalEndpoint-property)
  +  **v2**: When region is set to 'us-east-1', whether to send s3 request to global endpoints or 'us-east-1' regional endpoints.
  +  **v3**: **Deprecated**. S3 client will always use regional endpoint if region is set to `us-east-1`. You can set the region to `aws-global` to send requests to S3 global endpoint.
+  [`signatureCache`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#signatureCache-property)
  +  **v2**: Whether the signature to sign requests with (overriding the API configuration) is cached.
  +  **v3**: **Deprecated**. SDK *always* caches the hashed signing keys.
+  [`signatureVersion`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#signatureVersion-property)
  +  **v2**: The signature version to sign requests with (overriding the API configuration).
  +  **v3**: **Deprecated**. Signature V2 supported in v2 SDK has been deprecated by AWS. v3 *only* supports signature v4.
+  [`sslEnabled`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#sslEnabled-property)
  +  **v2**: Whether SSL is enabled for requests.
  +  **v3**: Renamed to `tls`.
+  [`stsRegionalEndpoints`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#stsRegionalEndpoints-property)
  +  **v2**: Whether to send sts request to global endpoints or regional endpoints.
  +  **v3**: **Deprecated**. STS client will *always* use regional endpoints if set to a specific region. You can set the region to `aws-global` to send request to STS global endpoint.
+  [`useAccelerateEndpoint`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#useAccelerateEndpoint-property)
  +  **v2**: Whether to use the Accelerate endpoint with the S3 service.
  +  **v3**: No change.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for JavaScript. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-javascript` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
