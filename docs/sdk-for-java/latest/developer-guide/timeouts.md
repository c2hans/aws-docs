---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/timeouts.html
---

# Configure timeouts in AWS SDK for Java 2.x
<a name="timeouts"></a>

The AWS SDK for Java 2.x provides multiple layers of timeout configuration to help you build resilient applications. The SDK offers different types of timeouts that work together to optimize your application's performance and reliability.

There are two main categories of timeouts in the SDK:
+ **Service Client Timeouts** - High-level timeouts that control API operations
+ **HTTP Client Timeouts** - Low-level timeouts that control network communication

## Service client timeouts
<a name="service-client-timeouts"></a>

Service client timeouts operate at the API level and control the overall behavior of service operations, including retries and multiple attempts.

### API call timeout
<a name="api-call-timeout"></a>

The API call timeout sets the maximum amount of time for an entire API operation, including all retry attempts. This timeout provides a hard limit on how long your application waits for a complete operation to finish.

```
S3Client s3Client = S3Client.builder()
    .overrideConfiguration(ClientOverrideConfiguration.builder()
        .apiCallTimeout(Duration.ofMinutes(2))  // Total time for entire operation, such as when you call the getObject method.
        .build())
    .build();
```

Key characteristics:
+ Includes all retry attempts.
+ Includes time spent waiting between retries.
+ Provides absolute maximum wait time.
+ Prevents operations from running indefinitely.

### API call attempt timeout
<a name="api-call-attempt-timeout"></a>

The API call attempt timeout sets the maximum time for a single attempt of an API operation. If this timeout is exceeded, the SDK retries the operation (if retries are configured) rather than failing the entire call.

```
S3Client s3Client = S3Client.builder()
    .overrideConfiguration(ClientOverrideConfiguration.builder()
        .apiCallAttemptTimeout(Duration.ofSeconds(30))  // Time for single attempt.
        .build())
    .build();
```

Key characteristics:
+ Applies to individual attempts only.
+ Enables fast failure and retry for slow requests.
+ Must be shorter than API call timeout.
+ Helps identify and recover from transient issues.

### Configure service client timeouts
<a name="service-timeout-configuration"></a>

You can configure service client timeouts globally for all operations or per-request:

**Global Configuration:**

```
S3Client s3Client = S3Client.builder()
    .overrideConfiguration(b -> b
        .apiCallTimeout(Duration.ofSeconds(105L))
        .apiCallAttemptTimeout(Duration.ofSeconds(25L)))
    .build();
// When you use the s3Client for an API operation, the SDK uses the configured timeout values.
```

**Per-Request Configuration:**

```
S3Client basicS3Client = S3Client.create();

// The following configuration uses the same settings as shown before, but these settings
// apply to only the `putObject` call. When you use `basicS3Client` in another API call without
// supplying the override configuration, there are no API timeout limits. No timeout limits is the default for the SDK.
AwsRequestOverrideConfiguration overrideConfiguration = AwsRequestOverrideConfiguration.builder()
    .apiCallTimeout(Duration.ofSeconds(105L))
    .apiCallAttemptTimeout(Duration.ofSeconds(25L))
    .build();

basicS3Client.putObject(b -> b
        .bucket("amzn-s3-demo-bucket")
        .key("example-key")
        .overrideConfiguration(overrideConfiguration),
    RequestBody.fromString("test"));
```

### Best practices for API timeouts
<a name="timeout-best-practice"></a>

The SDK for Java 2.x doesn't set API call timeouts or individual API call attempt timeouts by default. Set timeouts for both individual attempts and the entire request. This helps your application fail fast when transient issues cause request attempts to take longer or when fatal network issues occur.

## HTTP client timeouts
<a name="http-client-timeouts"></a>

HTTP client timeouts operate at the network level and control various aspects of HTTP communication. These timeouts vary depending on which HTTP client implementation you use.

### Connection timeout
<a name="connection-timeout"></a>

The connection timeout controls how long to wait when establishing a new connection to the AWS service endpoint.

```
// Available with all HTTP clients.
ApacheHttpClient.builder()
    .connectionTimeout(Duration.ofSeconds(5L))
    .build();
```

Purpose:
+ Prevents hanging on network connectivity issues.
+ Fails fast when services are unreachable.
+ Essential for applications that need responsive error handling.

### Socket timeout (Apache and URLConnection clients)
<a name="socket-timeout"></a>

The socket timeout controls how long to wait for data on an established connection.

```
ApacheHttpClient.builder()
    .socketTimeout(Duration.ofSeconds(30L))  // Time to wait for response data.
    .build();
```

### Read and write timeouts (Netty client)
<a name="read-write-timeouts"></a>

The Netty client provides separate timeouts for read and write operations:

```
NettyNioAsyncHttpClient.builder()
    .readTimeout(Duration.ofSeconds(30L))   // Reading response data.
    .writeTimeout(Duration.ofSeconds(30L))  // Writing request data.
    .build();
```

### TLS negotiation timeout (Netty client)
<a name="tls-negotiation-timeout"></a>

Controls the time allowed for TLS/SSL handshake:

```
NettyNioAsyncHttpClient.builder()
    .tlsNegotiationTimeout(Duration.ofSeconds(3L))
    .build();
```

### Connection pool timeouts
<a name="connection-pool-timeouts"></a>

Some HTTP clients provide timeouts for connection pool operations:

```
ApacheHttpClient.builder()
    .connectionAcquisitionTimeout(Duration.ofSeconds(10L))  // Wait for pool connection.
    .connectionTimeToLive(Duration.ofMinutes(5L))           // Maximum connection age.
    .connectionMaxIdleTime(Duration.ofSeconds(60L))         // Maximum idle time.
    .build()
```

The [Configure HTTP clients](http-configuration.md) contains more information on HTTP clients in the AWS SDK for Java 2.x

## Timeout interactions and hierarchy
<a name="timeout-interactions"></a>

Understanding how different timeouts interact is crucial for proper configuration:

### Timeout hierarchy
<a name="timeout-hierarchy"></a>

```
API Call Timeout (2 minutes)
├── Retry Attempt 1
│   ├── API Call Attempt Timeout (45 seconds)
│   └── HTTP Client Timeouts
│       ├── Connection Timeout (5 seconds)
│       ├── TLS Negotiation Timeout (3 seconds)
│       └── Read/Write Timeout (30 seconds)
├── Retry Attempt 2
│   └── [Same structure as Attempt 1]
└── Retry Attempt 3
    └── [Same structure as Attempt 1]
```

### Configuration rules
<a name="configuration-rules"></a>

API call timeout ≥ API call attempt timeout

```
// Correct configuration.
.apiCallTimeout(Duration.ofMinutes(2))         // 120 seconds.
.apiCallAttemptTimeout(Duration.ofSeconds(30)) // 30 seconds.
```

API call attempt timeout ≥ HTTP client timeouts

```
// HTTP client timeouts must be less than attempt timeout.
.apiCallAttemptTimeout(Duration.ofSeconds(30L))   // 30 seconds.
// HTTP client configuration.
.connectionTimeout(Duration.ofSeconds(5L))        // 5 seconds.
.readTimeout(Duration.ofSeconds(25L))             // 25 seconds (< 30).
```

Account for multiple attempts

```
// If you have 3 retry attempts, each taking up to 30 seconds
// API call timeout must be at least 90 seconds plus overhead.
.apiCallTimeout(Duration.ofMinutes(2L))          // 120 seconds.
.apiCallAttemptTimeout(Duration.ofSeconds(30))   // 30 seconds per attempt.
```

## Use smart configuration defaults
<a name="smart-configuration-defaults"></a>

The SDK provides smart defaults that automatically configure appropriate timeout values:

```
// Enable smart defaults.
S3Client client = S3Client.builder()
    .defaultsMode(DefaultsMode.AUTO)  // Automatically choose appropriate defaults.
    .build();

// Available modes:
// - STANDARD: Balanced defaults
// - IN_REGION: Optimized for same-region calls
// - CROSS_REGION: Optimized for cross-region calls
// - MOBILE: Optimized for mobile applications
// - AUTO: Automatically detect and choose appropriate mode
// - LEGACY: Provides settings that were used before smart defaults existed.
```

Smart defaults automatically configure:
+ Connection timeout values.
+ TLS negotiation timeout values.
+ Other client settings.

## Summary
<a name="timeout-summary"></a>

Effective timeout configuration in AWS SDK for Java 2.x requires understanding the interaction between service client timeouts and HTTP client timeouts:

1. **Service client timeouts** control high-level API behavior.

1. **HTTP client timeouts** control low-level network behavior.

1. **Proper hierarchy** ensures timeouts work together effectively.

1. **Smart defaults** provide good starting points for most applications.

Configure timeouts appropriately for your use case to build applications that are both resilient to network issues and responsive to users.
