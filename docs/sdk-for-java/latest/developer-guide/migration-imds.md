---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-imds.html
---

# Changes in the EC2 metadata utility from version 1 to version 2
<a name="migration-imds"></a>

This topic details the changes in the SDK for Java Amazon Elastic Compute Cloud (EC2) metadata utility from version 1 (v1) to version 2 (v2).

## High-level changes
<a name="migration-imds-high-level-changes"></a>

****

| Change | v1 | v2 |
| --- | --- | --- |
|  <br />Maven dependencies |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>com.amazonaws</groupId><br />            <artifactId>aws-java-sdk-bom</artifactId><br />            <version>{{1.12.5871}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>com.amazonaws</groupId><br />        <artifactId>aws-java-sdk-core</artifactId><br />    </dependency><br /></dependencies></pre>  |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>software.amazon.awssdk</groupId><br />            <artifactId>bom</artifactId><br />            <version>{{2.27.212}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>software.amazon.awssdk</groupId><br />        <artifactId>imds</artifactId><br />    </dependency><br />    <dependency><br />        <groupId>software.amazon.awssdk</groupId><br />        <artifactId>apache-client3</artifactId><br />    </dependency><br /></dependencies></pre>  |
| Package name |  com.amazonaws.util  |  software.amazon.awssdk.imds  |
| Instantiation approach | Use static utility methods; no instantiation:<pre>String localHostName = <br />           EC2MetadataUtils.getLocalHostName();</pre> | Use a static factory method:<pre>Ec2MetadataClient client = Ec2MetadataClient.create();</pre><br />Or use a builder approach:<pre>Ec2MetadataClient client = Ec2MetadataClient.builder()<br />    .endpointMode(EndpointMode.IPV6)<br />    .build();</pre> |
| Types of clients | Synchronous only utility methods: EC2MetadataUtils | Synchronous: `Ec2MetadataClient`<br />Asynchronous: `Ec2MetadataAsyncClient` |

1 [Latest version](https://central.sonatype.com/artifact/com.amazonaws/aws-java-sdk-bom). 2 [Latest version](https://central.sonatype.com/artifact/software.amazon.awssdk/bom).

3Notice the declaration of the `apache-client` module for v2. V2 of the EC2 metadata utility requires an implementation of the `SdkHttpClient` interface for the synchronous metadata client, or the `SdkAsyncHttpClient` interface for the asynchronous metadata client. The [Configure HTTP clients in the AWS SDK for Java 2.x](http-configuration.md) section shows the list of HTTP clients that you can use.

### Requesting metadata
<a name="migration-imds-fetching-changes"></a>

In v1, you use static methods that accept no parameters to request metadata for an EC2 resource. In contrast, you need to specify the path to the EC2 resource as a parameter in v2. The following table shows the different approaches.

****

| v1 | v2 |
| --- | --- |
|  <pre>String userMetaData = EC2MetadataUtils.getUserData();</pre>  |  <pre>Ec2MetadataClient client = Ec2MetadataClient.create();<br />Ec2MetadataResponse response = <br />                client.get("/latest/user-data");<br />String userMetaData = <br />                response.asString();</pre>  |

Refer to the [instance metadata categories](https://docs.aws.amazon.com//AWSEC2/latest/UserGuide/instancedata-data-categories.html) to find the path you need to supply to request a piece of metadata.

**Note**
When you use an instance metadata client in v2, you should aim to use the same client for all request to retrieve metadata.

## Behavior changes
<a name="migration-imds-behavior-changes"></a>

### JSON data
<a name="migration-imds-behavior-json"></a>

On EC2, the locally running Instance Metadata Service (IMDS) returns some metadata as JSON formatted strings. One such example is the dynamic metadata of an [instance identity document](https://docs.aws.amazon.com//AWSEC2/latest/UserGuide/instance-identity-documents.html).

The v1 API contains separate methods for each piece of instance identity metadata, whereas the v2 API directly returns the JSON string. To work with the JSON string, you can use the [Document API ](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/document/package-summary.html) to parse the response and navigate the JSON structure.

The following table compares how you retrieve metadata of an instance identity document in v1 and v2.

****

| Use case | v1 | v2 |
| --- | --- | --- |
| Retrieve the Region |  <pre>InstanceInfo instanceInfo = <br />        EC2MetadataUtils.getInstanceInfo();<br />String region = instanceInfo.getRegion();</pre>  |  <pre>Ec2MetadataResponse response = <br />    client.get("/latest/dynamic/instance-identity/document");<br />Document instanceInfo = response.asDocument();<br />String region = instanceInfo.asMap().get("region").asString();</pre>  |
| Retrieve the instance id |  <pre>InstanceInfo instanceInfo = <br />        EC2MetadataUtils.getInstanceInfo();<br />String instanceId = instanceInfo.instanceId;</pre>  |  <pre>Ec2MetadataResponse response = <br />    client.get("/latest/dynamic/instance-identity/document");<br />Document instanceInfo = response.asDocument();<br />String instanceId = instanceInfo.asMap().get("instanceId").asString();</pre>  |
| Retrieve the instance type |  <pre>InstanceInfo instanceInfo = <br />        EC2MetadataUtils.getInstanceInfo();<br />String instanceType = instanceInfo.instanceType();</pre>  |  <pre>Ec2MetadataResponse response = <br />    client.get("/latest/dynamic/instance-identity/document");<br />Document instanceInfo = response.asDocument();<br />String instanceType = instanceInfo.asMap().get("instanceType").asString();</pre>  |

### Endpoint resolution differences
<a name="migration-imds-behavior-endpoint-res"></a>

The following table shows the locations that the SDK checks to resolve the endpoint to IMDS. The locations are listed in descending priority.

****

| v1 | v2 |
| --- | --- |
| System property: com.amazonaws.sdk.ec2MetadataServiceEndpointOverride | Client builder configuration method: endpoint(...) |
| Environment variable: AWS\_EC2\_METADATA\_SERVICE\_ENDPOINT | System property: aws.ec2MetadataServiceEndpoint |
| Default Value: http://169.254.169.254 | Config file: \~.aws/config with the ec2\_metadata\_service\_endpoint setting |
|  | Value associated with resolved endpoint-mode  |
|  | Default value: http://169.254.169.254 |

### Endpoint resolution in v2
<a name="migration-imds-behavior-endpoint-res2"></a>

When you explicitly set an endpoint by using the builder, that endpoint value takes priority over all other settings. When the following code executes, the `aws.ec2MetadataServiceEndpoint` system property and config file `ec2_metadata_service_endpoint` setting are ignored if they exist.

```
Ec2MetadataClient client = Ec2MetadataClient
  .builder()
  .endpoint(URI.create("{{endpoint.to.use}}"))
  .build();
```

#### Endpoint-mode
<a name="migration-imds-behavior-endpoint-mode"></a>

With v2, you can specify an endpoint-mode to configure the metadata client to use the default endpoint values for IPv4 or IPv6. Endpoint-mode is not available for v1. The default value used for IPv4 is `http://169.254.169.254` and `http://[fd00:ec2::254]` for IPv6.

The following table shows the different ways that you can set the endpoint mode in order of descending priority.

****

|  |  | Possible values |
| --- | --- | --- |
| Client builder configuration method: endpointMode(...) |  <pre>Ec2MetadataClient client = Ec2MetadataClient<br />  .builder()<br />  .endpointMode(EndpointMode.IPV4)<br />  .build();</pre>  | EndpointMode.IPV4, EndpointMode.IPV6 |
| System property | aws.ec2MetadataServiceEndpointMode | IPv4, IPv6 (case does not matter) |
| Config file: \~.aws/config | ec2\_metadata\_service\_endpoint setting | IPv4, IPv6 (case does not matter) |
| Not specified in the previous ways | IPv4 is used |  |

#### How the SDK resolves `endpoint` or `endpoint-mode` in v2
<a name="migration-imds-behavior-endpoint-res2-which"></a>

1. The SDK uses the value that you set in code on the client builder and ignores any external settings. Because the SDK throws an exception if both `endpoint` and `endpointMode` are called on the client builder, the SDK uses the endpoint value from whichever method you use.

1. If you do not set a value in code, the SDK looks to external configuration—first for system properties and then for a setting in the config file.

   1. The SDK first checks for an endpoint value. If a value is found, it is used.

   1. If the SDK still hasn't found a value, the SDK looks for endpoint mode settings.

1. Finally, if the SDK finds no external settings and you have not configured the metadata client in code, the SDK uses the IPv4 value of `http://169.254.169.254`.

### IMDSv2
<a name="migration-imds-behavior-imdsv2"></a>

Amazon EC2 defines two approaches to access instance metadata:
+ Instance Metadata Service Version 1 (IMDSv1) – Request/response approach
+ Instance Metadata Service Version 2 (IMDSv2) – Session-oriented approach

The following table compares how the Java SDKs work with IMDS.

****

| v1 | v2 |
| --- | --- |
| IMDSv2 is used by default | Always uses IMDSv2 |
| Attempts to fetch a session token for each request and falls back to IMDSv1 if it fails to fetch a session token | Keeps a session token in an internal cache that is reused for multiple requests |

The SDK for Java 2.x supports only IMDSv2 and does not fall back to IMDSv1.

## Configuration differences
<a name="migration-imds-config-diffs"></a>

The following table lists the differing configuration options.

****

| Configuration | v1 | v2 |
| --- | --- | --- |
| Retries | Configuration not available | Configurable through builder method retryPolicy(...) |
| HTTP | Connection timeout configurable through the AWS\_METADATA\_SERVICE\_TIMEOUT environment variable. The default is 1 second. | Configuration available by passing an HTTP client to the builder method httpClient(...). The default connection timeout for HTTP clients is 2 seconds. |

### Example v2 HTTP configuration
<a name="migration-imds-http-conf-v2-ex"></a>

The following example shows how you can configure the metadata client. This example configures the connection timeout and uses the Apache HTTP client.

```
SdkHttpClient httpClient = ApacheHttpClient.builder()
    .connectionTimeout(Duration.ofSeconds(1))
    .build();

Ec2MetadataClient imdsClient = Ec2MetadataClient.builder()
    .httpClient(httpClient)
    .build();
```
