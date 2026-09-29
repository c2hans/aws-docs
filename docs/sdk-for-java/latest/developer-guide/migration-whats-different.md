---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-whats-different.html
---

# What's different between the AWS SDK for Java 1.x and 2.x
<a name="migration-whats-different"></a>

This section describes the main changes to be aware of when converting an application from using the AWS SDK for Java version 1.x to version 2.x.

## Package name change
<a name="mig-diff-package-name-change"></a>

A noticeable change from the SDK for Java 1.x to the SDK for Java 2.x is the package name change. Package names begin with `software.amazon.awssdk` in SDK 2.x, whereas the SDK 1.x uses `com.amazonaws`.

These same names differentiate Maven artifacts from SDK 1.x to SDK 2.x. Maven artifacts for the SDK 2.x use the `software.amazon.awssdk` groupId, whereas the SDK 1.x uses the `com.amazonaws` groupId.

There are a few times when your code requires a `com.amazonaws` dependency for a project that otherwise uses only SDK 2.x artifacts. One example of this is when you work with server-side AWS Lambda. This was shown in the [Set up an Apache Maven project](setup-project-maven.md#modules-dependencies) section earlier in this guide.

**Note**
Several package names in the SDK 1.x contain `v2`. The use of `v2` in this case usually means that code in the package is targeted to work with version 2 of the service.
Since the full package name begins with `com.amazonaws`, these are SDK 1.x components. Examples of these package names in the SDK 1.x are:
`com.amazonaws.services.dynamodbv2`
`com.amazonaws.retry.v2`
`com.amazonaws.services.apigatewayv2`
`com.amazonaws.services.simpleemailv2`

## Adding version 2.x to your project
<a name="adding-v2"></a>

Maven is the recommended way to manage dependencies when using the AWS SDK for Java 2.x. To add version 2.x components to your project, update your `pom.xml` file with a dependency on the SDK.

**Example**

```
<dependencyManagement>
    <dependencies>
        <dependency>
          <groupId>software.amazon.awssdk</groupId>
          <artifactId>bom</artifactId>
          <version>2.27.21</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<dependencies>
    <dependency>
      <groupId>software.amazon.awssdk</groupId>
      <artifactId>dynamodb</artifactId>
    </dependency>
</dependencies>
```

You can also [use version 1.x and 2.x side-by-side](migration-side-by-side.md) as you migrate your project to version 2.x.

## Immutable POJOs
<a name="immutable-classes"></a>

Clients and operation request and response objects are now immutable and cannot be changed after creation. To reuse a request or response variable, you must build a new object to assign to it.

**Example of updating a request object in 1.x**

```
DescribeAlarmsRequest request = new DescribeAlarmsRequest();
DescribeAlarmsResult response = cw.describeAlarms(request);

request.setNextToken(response.getNextToken());
```

**Example of updating a request object in 2.x**

```
DescribeAlarmsRequest request = DescribeAlarmsRequest.builder().build();
DescribeAlarmsResponse response = cw.describeAlarms(request);

request = DescribeAlarmsRequest.builder()
        .nextToken(response.nextToken())
        .build();
```

## Setter and getter methods
<a name="setter-getter-methods"></a>

In the AWS SDK for Java 2.x, setter method names don’t include the `set` or `with` prefix. For example, `*.withEndpoint()` is now `*.endpoint()`.

Getter method names do not use the `get` prefix.

**Example of using setter methods in 1.x**

```
AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard()
        		.withRegion("us-east-1")
        		.build();
```

**Example of using setter methods in 2.x**

```
DynamoDbClient client = DynamoDbClient.builder()
        		.region(Region.US_EAST_1)
        		.build();
```

**Example of using getter methods in 1.x**

```
String token = request.getNextToken();
```

**Example of using getter methods in 2.x**

```
String token = request.nextToken();
```

## Model class names
<a name="model-classname-changes"></a>

Model class names that represent service responses end with `Response` in v2 instead of `Result` that v1 uses.

**Example of class names that represent a response in v1**

```
CreateApiKeyResult
AllocateAddressResult
```

**Example of class names that represent a response in v2**

```
CreateApiKeyResponse
AllocateAddressResponse
```

## Migration status of libraries and utilities
<a name="migration-libraries-utilities"></a>

### SDK for Java libraries and utilities
<a name="migration-java-sdk-libs-utils"></a>

The following table lists the migration status of libraries and utilities for the SDK for Java.

| Version 1.12.x name | Version 2.x name | Since version in 2.x |
| --- | --- | --- |
| DynamoDBMapper | [DynamoDbEnhancedClient](dynamodb-enhanced-client.md) | 2.12.0 |
| Waiters | [Waiters](waiters.md) | 2.15.0 |
| CloudFrontUrlSigner, CloudFrontCookieSigner | [CloudFrontUtilities](https://aws.amazon.com/blogs/developer/amazon-cloudfront-signed-urls-and-cookies-are-now-supported-in-aws-sdk-for-java-2-x/) | 2.18.33 |
| TransferManager | [S3TransferManager](transfer-manager.md) | 2.19.0 |
| EC2 Metadata client |  [EC2 Metadata client](examples-ec2-IMDS.md)  | 2.19.29 |
| S3 URI parser |  [S3 URI parser](https://aws.amazon.com/blogs/devops/s3-uri-parsing-is-now-available-in-aws-sdk-for-java-2-x/)  | 2.20.41 |
| IAM Policy Builder | [IAM Policy Builder](feature-iam-policy-builder.md) | 2.20.126 |
| S3 Event Notifications | [S3 Event Notifications](examples-s3-event-notifications.md#s3-event-notification-read) | 2.25.11  |
| Amazon SQS Client-side Buffering | [Automatic Request Batching API for Amazon SQS](sqs-auto-batch.md) | 2.28.0 |
| Progress Listeners | Progress Listeners | [not yet released](https://github.com/aws/aws-sdk-java-v2/issues/25) |

### Related libraries
<a name="migration-other-sdks"></a>

The following table lists libraries that are released separately but work with the SDK for Java 2.x.

| Name used with version 2.x of the SDK for Java | Since version |
| --- | --- |
|  [Amazon S3 Encryption Client](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/what-is-s3-encryption-client.html)  |  3.0.01  |
| [AWS Database Encryption SDK for DynamoDB](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-java.html) | 3.0.02 |

#### 1Amazon S3 Encryption Client
<a name="migration-s3-encryption-sdk"></a>

The encryption client for Amazon S3 is available by using the following Maven dependency.

```
<dependency>
    <groupId>software.amazon.encryption.s3</groupId>
    <artifactId>amazon-s3-encryption-client-java</artifactId>
    <version>{{3.x}}</version>
</dependency>
```

#### 2AWS Database Encryption SDK for DynamoDB
<a name="migration-ddb-encryption-sdk"></a>

The AWS Database Encryption SDK for DynamoDB is available for V2 by using the following Maven dependency.

```
<dependency>
    <groupId>software.amazon.cryptography</groupId>
    <artifactId>aws-database-encryption-sdk-dynamodb</artifactId>
    <version>{{3.x}}</version>
</dependency>
```

Information on the encryption library for DynamoDB that works with v1 of the Java SDK is available in the [AWS Database Encryption SDK Developer Guide](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/java.html) (named *Amazon DynamoDB Encryption Client for Java*) and in [GitHub](https://github.com/aws/aws-dynamodb-encryption-java).

For more information on the DynamoDB encryption library that is compatible with V2 of the Java SDK, see the [AWS Database Encryption SDK Developer Guide](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-java.html) and the [GitHub source](https://github.com/aws/aws-database-encryption-sdk-dynamodb).

Migration information about the encryption library is available in the [AWS Database Encryption SDK Developer Guide](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-java-migrate.html).

### Migration details for libraries and utilities
<a name="migrate-libs-utils-details"></a>
+ [Transfer Manager](migration-s3-transfer-manager.md)
+ [EC2 metadata utility](migration-imds.md)
+ [CloudFront presigning](migration-cloudfront-presigning.md)
+ [S3 URI parsing](migration-s3-uri-parser.md)
+ [DynamoDB mapping/document APIs](migration-ddb-mapper.md)
+ [IAM Policy Builder](migration-iam-policy-builder.md)
+ [S3 Event Notifications](migration-s3-event-notification.md)
+ [SDK metric publishing](migration-metrics.md)
