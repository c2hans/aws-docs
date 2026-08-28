---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-dynamodb.html
---

# Work with DynamoDB
<a name="examples-dynamodb"></a>

[DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. This section shows you how to work with DynamoDB using the AWS SDK for Java 2.x.

## Choose your DynamoDB client
<a name="ddb-clients-overview"></a>

The SDK provides two main approaches for working with DynamoDB:

Low-level client (`DynamoDbClient`)
Provides direct access to DynamoDB operations with full control over requests and responses. Use this client when you need fine-grained control or work with dynamic schemas.

Enhanced client (`DynamoDbEnhancedClient`)
Offers object-oriented programming with automatic mapping between Java objects and DynamoDB items. Also provides document-oriented capabilities for working with JSON-like data that doesn't follow a fixed schema. Use this client when working with well-defined data models or document-type data.

## Configure DynamoDB clients
<a name="ddb-configuration-setup"></a>

Before working with DynamoDB, configure your client for optimal performance and reliability.

### Understand DynamoDB retry behavior
<a name="ddb-retry-behavior"></a>

DynamoDB clients use a default maximum retry count of 8, which is higher than other AWS service clients. This higher retry count helps handle DynamoDB's distributed nature and temporary capacity limitations. For more information about retry strategies, see [Configure retry behavior in the AWS SDK for Java 2.x](retry-strategy.md).

### Optimize performance with account-based endpoints
<a name="ddb-account-based-endpoints-v2"></a>

DynamoDB offers [AWS account-based endpoints](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.SDKOverview.html#Programming.SDKs.endpoints) that improve performance by using your AWS account ID to streamline request routing.

To use this feature, you need version 2.28.4 or greater of the AWS SDK for Java 2.x. You can find the latest version in the [Maven central repository](https://central.sonatype.com/artifact/software.amazon.awssdk/bom/versions). Supported SDK versions automatically use the new endpoints.

To opt out of account-based routing, choose one of these options:
+ Configure a DynamoDB service client with `AccountIdEndpointMode` set to `DISABLED`.
+ Set an environment variable.
+ Set a JVM system property.
+ Update the shared AWS config file setting.

The following example shows how to disable account-based routing by configuring a DynamoDB service client:

```
DynamoDbClient.builder()
                 .accountIdEndpointMode(AccountIdEndpointMode.DISABLED)
                 .build();
```

For more information about the other configuration options, see [Account-based endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-account-endpoints.html) in the AWS SDKs and Tools Reference Guide.

## What's covered in this topic
<a name="ddb-topics-overview"></a>

The following sections show you how to work with DynamoDB:
+ [Work with tables in DynamoDB](examples-dynamodb-tables.md) - Create, describe, update, and delete tables
+ [Work with items in DynamoDB](examples-dynamodb-items.md) - Add, retrieve, and update individual items
+ [Map Java objects to DynamoDB items with the AWS SDK for Java 2.x](dynamodb-enhanced-client.md) - Use object mapping and document-oriented data with the Enhanced Client

For additional DynamoDB code examples, see [DynamoDB code examples](java_dynamodb_code_examples.md) in the AWS Code Examples Library.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
