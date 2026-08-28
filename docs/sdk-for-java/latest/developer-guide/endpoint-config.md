---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/endpoint-config.html
---

# Configuring client endpoints in the AWS SDK for Java 2.x
<a name="endpoint-config"></a>

The SDK for Java 2.x provides multiple ways to configure service endpoints. An endpoint is the URL that the SDK uses to make API calls to AWS services. By default, the SDK automatically determines the appropriate endpoint for each service based on the AWS Region you've configured. However, there are scenarios where you might need to customize or override these endpoints:
+ Working with local or third-party service implementations (such as LocalStack)
+ Connecting to AWS services through a proxy or VPC endpoint
+ Testing against beta or pre-release service endpoints

## Endpoint configuration options
<a name="endpoint-configuration-options"></a>

 The AWS SDK for Java 2.x provides several ways to configure endpoints:
+ In-code configuration by using the service client builder
+ External configuration with environment variables
+ External configuration with JVM system properties
+ External configuration with shared AWS config file

## In-code endpoint configuration
<a name="in-code-endpoint-configuration"></a>

### Using `endpointOverride`
<a name="endpoint-override"></a>

 The most direct way to configure an endpoint is by using the `endpointOverride` method on the service client builder. This method accepts a `URI` object representing the custom endpoint URL.

**Example Setting a custom endpoint for an Amazon S3 client**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import java.net.URI;

S3Client s3 = S3Client.builder()
        .region(Region.US_WEST_2)
        .endpointOverride(URI.create("https://my-custom-s3-endpoint.example.com"))
        .build();
```

When using `endpointOverride`, you must still specify a region for the client, even though the endpoint is being explicitly set. The region is used for signing requests.

### Endpoint discovery
<a name="endpoint-discovery"></a>

Some AWS services support endpoint discovery, where the SDK can automatically discover the optimal endpoint to use. You can enable or disable this feature using the `endpointDiscoveryEnabled` method on the service client builder.

**Example Enabling endpoint discovery for a DynamoDB client**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;

DynamoDbClient dynamoDb = DynamoDbClient.builder()
        .region(Region.US_WEST_2)
        .endpointDiscoveryEnabled(true)
        .build();
```

## Request-level endpoint configuration
<a name="request-level-endpoint-configuration"></a>

In some cases, you might need to override the endpoint for a specific request while using the same client for other requests with the default endpoint. The AWS SDK for Java 2.x supports this through request overrides.

**Example Overriding the endpoint for a specific request**

```
import software.amazon.awssdk.core.SdkRequest;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.http.SdkHttpRequest;

S3Client s3 = S3Client.builder()
        .region(Region.US_WEST_2)
        .build();

// Create a request
GetObjectRequest getObjectRequest = GetObjectRequest.builder()
        .bucket("amzn-s3-demo-bucket")
        .key("my-key")
        .overrideConfiguration(c -> c.putHeader("Host", "custom-endpoint.example.com"))
        .build();

// Execute the request with the custom endpoint
s3.getObject(getObjectRequest);
```

Note that request-level endpoint overrides are limited and may not work for all services or scenarios. For most cases, it's recommended to use client-level endpoint configuration.

## External endpoint configuration
<a name="external-endpoint-configuration"></a>

### Using environment variables
<a name="environment-variables-for-endpoints"></a>

You can configure endpoints using environment variables. The SDK supports service-specific endpoint configuration through environment variables in the format `AWS_ENDPOINT_URL_[SERVICE]`, where `[SERVICE]` is the uppercase service identifier.

**Example Setting an S3 endpoint using environment variables**

```
# For Linux/macOS
export AWS_ENDPOINT_URL_S3=https://my-custom-s3-endpoint.example.com

# For Windows
set AWS_ENDPOINT_URL_S3=https://my-custom-s3-endpoint.example.com
```

 You can also set a global endpoint URL prefix or suffix using the following environment variables:
+ `AWS_ENDPOINT_URL` - Sets a global endpoint for all services
+ `AWS_ENDPOINT_URL_PREFIX` - Adds a prefix to all service endpoints
+ `AWS_ENDPOINT_URL_SUFFIX` - Adds a suffix to all service endpoints

### Using JVM system properties
<a name="jvm-system-properties-for-endpoints"></a>

 You can also configure endpoints using JVM system properties. The format is similar to environment variables but uses a different naming convention.

**Example Setting an S3 endpoint using JVM system properties**

```
java -Daws.endpointUrl.s3=https://my-custom-s3-endpoint.example.com -jar your-application.jar
```

 Global endpoint configuration is also available through system properties:
+ `aws.endpointUrl` - Sets a global endpoint for all services
+ `aws.endpointUrl.prefix` - Adds a prefix to all service endpoints
+ `aws.endpointUrl.suffix` - Adds a suffix to all service endpoints

### Using the shared AWS config file
<a name="aws-config-file-for-endpoints"></a>

 The AWS SDK for Java 2.x also supports endpoint configuration through the shared AWS config file, typically located at `~/.aws/config` (Linux/macOS) or `%USERPROFILE%\.aws\config` (Windows). See the [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/feature-ss-endpoints.html#ss-endpoints-config) for information and examples.

## Configuration precedence
<a name="endpoint-configuration-precedence"></a>

 When multiple endpoint configurations are present, the SDK follows this order of precedence (from highest to lowest):

1. Request-level overrides (when applicable)

1. Client-level configuration via `endpointOverride`

1. Environment variables

1. JVM system properties

1. Shared AWS config file

1. Default endpoints based on the configured AWS Region

## Service-specific endpoint configuration
<a name="service-specific-endpoint-configuration"></a>

 Some AWS services have additional endpoint configuration options specific to that service. Here are a few examples:

### Amazon S3 Endpoint Configuration
<a name="s3-endpoint-configuration"></a>

 Amazon S3 supports several endpoint configurations through the `S3Configuration` class:
+ `dualstackEnabled` - Enables IPv6 support
+ `accelerateModeEnabled` - Enables S3 Transfer Acceleration
+ `pathStyleAccessEnabled` - Uses path-style access instead of virtual-hosted style
+ `useArnRegionEnabled` - Uses the region from an ARN for cross-region requests
+ `fipsModeEnabled` - Routes requests to FIPS-compliant endpoints

**Example Configuring S3-specific endpoint options**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.S3Configuration;

S3Client s3 = S3Client.builder()
        .region(Region.US_WEST_2)
        .serviceConfiguration(S3Configuration.builder()
                .accelerateModeEnabled(true)
                .dualstackEnabled(true)
                .pathStyleAccessEnabled(false)
                .fipsModeEnabled(true)
                .build())
        .build();
```

### DynamoDB endpoint configuration
<a name="dynamodb-endpoint-configuration"></a>

 For DynamoDB, you might want to use endpoint discovery or connect to [DynamoDB local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html) for testing:

**Example Connecting to DynamoDB local**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import java.net.URI;

DynamoDbClient dynamoDb = DynamoDbClient.builder()
        .endpointOverride(URI.create("http://localhost:8000"))
        // The region is meaningless for DynamoDB local but required for the client builder.
        .region(Region.US_WEST_2)
        .build();
```

DynamoDB also supports the use of [account-based endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-account-endpoints.html), which you can configure in code or using external settings. The following example shows how to disable the use of account-based endpoints in code when you create the client (the default settings is *preferred*):

```
DynamoDbClient dynamoDbClient = DynamoDbClient.builder()
    .region(Region.US_EAST_1)
    .accountIdEndpointMode(AccountIdEndpointMode.DISABLED)
    .build();
```

## Best practices
<a name="endpoint-configuration-best-practices"></a>

 When configuring endpoints in the AWS SDK for Java 2.x, consider these best practices:
+  *Use external configuration for environment-specific endpoints*—Use environment variables, system properties, or the AWS config file for endpoints that vary between environments (development, testing, production).
+  *Use in-code configuration for application-specific endpoints*— Use the client builder's `endpointOverride` method for endpoints that are specific to your application's design.
+  *Always specify a region*—Even when overriding endpoints, always specify a region as it's used for request signing.
+  *Be cautious with global endpoint overrides*—Using global endpoint overrides can affect all services, which might not be what you intend.
+  *Consider security implications*—When using custom endpoints, ensure they have appropriate security measures, especially for production workloads.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
