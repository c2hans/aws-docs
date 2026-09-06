---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/client-config.html
---

# Configuring AWS SDK for C\+\+ service clients in code
<a name="client-config"></a>

When configuration is handled directly in code, the configuration scope is limited to the application that uses that code. Within that application, there are options for the global configuration of all service clients, the configuration to all clients of a certain AWS service type, or the configuration to a specific service client instance.

The AWS SDK for C\+\+ includes AWS service client classes that provide functionality for interacting with the AWS services that you use in your application. In the SDK for C\+\+, you can change the default client configuration, which is helpful when you want to do things like:
+ Connect to the Internet through proxy
+ Change HTTP transport settings, such as connection timeout and request retries
+ Specify TCP socket buffer size hints

`ClientConfiguration` is a structure in the SDK for C\+\+ that you can instantiate and utilize in your code. The following snippet illustrates using this class to access Amazon S3 through a proxy.

```
Aws::Client::ClientConfiguration clientConfig;
clientConfig.proxyHost = "localhost";
clientConfig.proxyPort = 1234;
clientConfig.proxyScheme = Aws::Http::Scheme::HTTPS;
Aws::S3::S3Client(clientConfig);
```

## Configuration variable declarations
<a name="config-vars-declarations"></a>

 The `ClientConfiguration` struct declares the following member variables:

```
Aws::String accountId;
Aws::String accountIdEndpointMode = "preferred";
bool allowSystemProxy = false;
Aws::String appId;
Aws::String caPath;
Aws::String caFile;

struct {
  RequestChecksumCalculation requestChecksumCalculation = RequestChecksumCalculation::WHEN_SUPPORTED;
  ResponseChecksumValidation responseChecksumValidation = ResponseChecksumValidation::WHEN_SUPPORTED;
} checksumConfig;

ProviderFactories configFactories = ProviderFactories::defaultFactories;
long connectTimeoutMs = 1000;

struct CredentialProviderConfiguration {
    Aws::String profile;
    Aws::String region;
    struct {
        long metadataServiceNumAttempts = 1;
        long metadataServiceTimeout = 1;
        std::shared_ptr<RetryStrategy> imdsRetryStrategy;
        bool disableImdsV1;
        bool disableImds;
    } imdsConfig;
    struct STSCredentialsCredentialProviderConfiguration {
        Aws::String roleArn;
        Aws::String sessionName;
        Aws::String tokenFilePath;
        std::chrono::milliseconds retrieveCredentialsFutureTimeout = std::chrono::seconds(10);
    } stsCredentialsProviderConfig;
} credentialProviderConfig;

bool disableExpectHeader = false;
bool disableIMDS = false;
bool disableImdsV1 = false;
bool enableClockSkewAdjustment = true;
Aws::Crt::Optional<bool> enableEndpointDiscovery;
bool enableHostPrefixInjection = true;
bool enableHttpClientTrace = false;
bool enableTcpKeepAlive = true;
Aws::String endpointOverride;
std::shared_ptr<Aws::Utils::Threading::Executor> executor = nullptr;
FollowRedirectsPolicy followRedirects;
Aws::Http::TransferLibType httpLibOverride;
Aws::Http::TransferLibPerformanceMode httpLibPerfMode = Http::TransferLibPerformanceMode::LOW_LATENCY;
long httpRequestTimeoutMs = 0;
unsigned long lowSpeedLimit = 1;
unsigned maxConnections = 25;
Aws::Utils::Array<Aws::String> nonProxyHosts;
Aws::String profileName;
Aws::String proxyCaFile;
Aws::String proxyCaPath;
Aws::Http::Scheme proxyScheme;
Aws::String proxyHost;
unsigned proxyPort = 0;
Aws::String proxyUserName;
Aws::String proxyPassword;
Aws::String proxySSLCertPath;
Aws::String proxySSLCertType;
Aws::String proxySSLKeyPath;
Aws::String proxySSLKeyType;
Aws::String proxySSLKeyPassword;
std::shared_ptr<Aws::Utils::RateLimits::RateLimiterInterface> readRateLimiter = nullptr;
Aws::String region;
Aws::Client::RequestCompressionConfig requestCompressionConfig;
long requestTimeoutMs = 0;
std::shared_ptr<RetryStrategy> retryStrategy = nullptr;
Aws::Http::Scheme scheme;
unsigned long tcpKeepAliveIntervalMs = 30000;
std::shared_ptr<smithy::components::tracing::TelemetryProvider> telemetryProvider;
Aws::String userAgent;
bool useDualStack = false;
bool useFIPS = false;
bool verifySSL = true;
Aws::Http::Version version = Http::Version::HTTP_VERSION_2TLS;

struct WinHTTPOptions {
  bool useAnonymousAuth = false;
} winHTTPOptions;

std::shared_ptr<Aws::Utils::RateLimits::RateLimiterInterface> writeRateLimiter = nullptr;

static Aws::String LoadConfigFromEnvOrProfile(const Aws::String& envKey, const Aws::String& profile,
                                              const Aws::String& profileProperty, const Aws::Vector<Aws::String>& allowedValues,
                                              const Aws::String& defaultValue);
```

## Configuration variable descriptions
<a name="configuration-variables"></a>

The following list describes the `ClientConfiguration` member variables that you can use to customize client behavior.

**accountId**
Specifies the AWS account ID for account-based endpoint routing. Use the format 111122223333. Account-based endpoint routing improves request performance for some services.

**accountIdEndpointMode**
Controls account-based endpoint routing behavior. Valid values are "required", "disabled", or "preferred". The default value is "preferred". Set to "disabled" to turn off account-based endpoint routing when necessary.

**allowSystemProxy**
Controls whether the HTTP client discovers system proxy settings. The default setting is false. Set to true to enable automatic proxy discovery.

**appId**
Specifies an optional application-specific identifier. When set, this value is appended to the `User-Agent` header in the format `App/{appId}`. You can set this value using the `AWS_SDK_UA_APP_ID` environment variable or the `sdk_ua_app_id` shared config profile attribute.

**caPath, caFile**
Instructs the HTTP client where to find your SSL certificate trust store. An example trust store might be a directory prepared with the OpenSSL `c_rehash` utility. These variables should not need to be set unless your environment uses symlinks. These variables have no effect on Windows and macOS systems.

**checksumConfig**
Contains checksum calculation and validation settings. Includes `requestChecksumCalculation` and `responseChecksumValidation` with default value WHEN\_SUPPORTED.

**configFactories**
Specifies factory methods for initializing client utility classes such as `Executor` and `RetryStrategy`. Uses default factories unless overridden.

**requestTimeoutMs and connectTimeoutMs**
Specifies the amount of time in milliseconds to wait before timing out an HTTP request. For example, consider increasing these times when transferring large files.

**credentialProviderConfig**
Contains configuration settings for credential providers. Use this structure to customize how the SDK obtains AWS credentials.

**disableExpectHeader**
Applicable only for CURL HTTP clients. By default, CURL adds an "Expect: 100-Continue" header in an HTTP request to avoid sending the HTTP payload in situations where the server responds with an error immediately after receiving the header. This behavior can save a round-trip and is useful in situations where the payload is small and network latency is relevant. The variable's default setting is false. If set to true, CURL is instructed to send both the HTTP request header and body payload together.

**disableIMDS**
Controls whether Instance Metadata Service (IMDS) calls are disabled. The default setting is false. Set to true to disable IMDS calls when running outside of EC2 instances.

**disableImdsV1**
Controls whether IMDSv1 calls are disabled while allowing IMDSv2. The default setting is false. Set to true to disable only IMDSv1 calls for enhanced security.

**enableClockSkewAdjustment**
Controls whether clock skew is adjusted after each HTTP attempt. The default setting is false.

**enableEndpointDiscovery**
Controls whether endpoint discovery is used. By default, regional or overridden endpoints are used. To enable endpoint discovery, set the variable to true.

**enableHostPrefixInjection**
Controls whether the HTTP host adds a "data-" prefix to DiscoverInstances requests. By default, this behavior is enabled. To disable it, set the variable to false.

**enableHttpClientTrace**
Controls whether HTTP client tracing is enabled for debugging purposes. The default setting is false. Set to true to enable detailed HTTP request and response logging.

**enableTcpKeepAlive**
Controls whether to send TCP keep-alive packets. The default setting is true. Use in conjunction with the `tcpKeepAliveIntervalMs` variable. This variable is not applicable for WinINet and the IXMLHTTPRequest2 client.

**endpointOverride**
Specifies an overriding HTTP endpoint with which to communicate with a service.

**executor**
References the implementation of the asynchronous Executor handler. The default behavior is to create and detach a thread for each async call. To change this behavior, implement a subclass of the `Executor` class and assign an instance to this variable.

**followRedirects**
Controls the behavior when handling HTTP 300 redirect codes.

**httpLibOverride**
Specifies the HTTP implementation returned by the default HTTP factory. The default HTTP client for Windows is WinHTTP. The default HTTP client for all other platforms is CURL.

**httpLibPerfMode**
Specifies the HTTP library performance mode. The default setting is LOW\_LATENCY. You can adjust this setting to optimize for different performance characteristics.

**httpRequestTimeoutMs**
Specifies the HTTP request timeout in milliseconds. The default value is 0 (no timeout). Consider increasing this value when transferring large files.

**lowSpeedLimit**
Specifies the minimum allowed transfer speed in bytes per second. If the transfer speed falls below the specified speed, the transfer operation is aborted. The default setting is 1 byte/second. This variable is applicable only for CURL clients.

**maxConnections**
Specifies the maximum number of HTTP connections to a single server. The default value is 25. No maximum allowed value exists other than what your bandwidth can reasonably support.

**nonProxyHosts**
Specifies an array of hostnames that should bypass proxy settings. Use this setting to exclude specific hosts from proxy configuration.

**profileName**
Specifies the AWS profile name to use for configuration. The SDK loads settings from the specified profile in the AWS configuration file.

**proxyCaFile**
Specifies the path to the certificate authority file for proxy connections when it differs from the default.

**proxyCaPath**
Specifies the path to the certificate authority trust store for proxy connections when it differs from the default.

**proxyScheme, proxyHost, proxyPort, proxyUserName, and proxyPassword**
Used to set up and configure a proxy for all communications with AWS. Examples of when this functionality might be useful include debugging in conjunction with the Burp suite, or using a proxy to connect to the Internet.

**proxySSLCertPath**
Specifies the path to the SSL certificate file for proxy connections that require client certificates.

**proxySSLCertType**
Specifies the SSL certificate type for proxy connections. Common types include PEM and DER.

**proxySSLKeyPassword**
Specifies the password for the SSL private key used in proxy connections when the key is password-protected.

**proxySSLKeyPath**
Specifies the path to the SSL private key file for proxy connections that require client certificates.

**proxySSLKeyType**
Specifies the SSL private key type for proxy connections. Common types include PEM and DER.

**writeRateLimiter and readRateLimiter**
References to the implementations of read and write rate limiters which are used to throttle the bandwidth used by the transport layer. By default, the read and write rates are not throttled. To introduce throttling, implement a subclass of the `RateLimiterInterface` and assign an instance to these variables.

**region**
Specifies the AWS Region to use, such as *us-east-1*. By default, the Region used is the default Region configured in the applicable AWS credentials.

**requestCompressionConfig**
Contains configuration settings for request compression. Use this structure to control when and how requests are compressed before transmission.

**retryStrategy**
References the implementation of the retry strategy. The default strategy implements an exponential backoff policy. To perform a different strategy, implement a subclass of the `RetryStrategy` class and assign an instance to this variable.

**scheme**
Specifies the URI addressing scheme, either HTTP or HTTPS. The default scheme is HTTPS.

**tcpKeepAliveIntervalMs**
Specifies the time interval in milliseconds at which to send a keep-alive packet over a TCP connection. The default interval is 30 seconds. The minimum setting is 15 seconds. This variable is not applicable for WinINet and the IXMLHTTPRequest2 client.

**telemetryProvider**
References the telemetry provider implementation for collecting metrics and tracing data. Configure this setting to enable observability features.

**userAgent**
For internal use only. Do not change the setting of this variable.

**useDualStack**
Controls whether to use dual stack IPv4 and IPv6 endpoints. Note that not all AWS services support IPv6 in all Regions.

**useFIPS**
Controls whether to use Federal Information Processing Standards (FIPS) 140-2 validated cryptographic modules. The default setting is false. Set to true when FIPS compliance is required.

**verifySSL**
Controls whether to verify SSL certificates. By default SSL certificates are verified. To disable verification, set the variable to false.

**version**
Specifies the HTTP version to use for requests. The default setting is HTTP\_VERSION\_2TLS (HTTP/2 over TLS).

**winHTTPOptions**
Contains Windows-specific HTTP configuration options. Includes useAnonymousAuth with default setting false.
