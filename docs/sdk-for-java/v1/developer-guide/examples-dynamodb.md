---
source_url: https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-dynamodb.html
---

The AWS SDK for Java 1.x reached end-of-support on December 31, 2025. We recommend that you migrate to the [AWS SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html) to continue receiving new features, availability improvements, and security updates.

# DynamoDB Examples Using the AWS SDK for Java
<a name="examples-dynamodb"></a>

This section provides examples of programming [DynamoDB](https://aws.amazon.com/dynamodb/) using the [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/).

**Note**
The examples include only the code needed to demonstrate each technique. The [complete example code is available on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/java). From there, you can download a single source file or clone the repository locally to get all the examples to build and run.

**Topics**
+ [Use AWS account-based endpoints](#account-based-endpoint-routing)
+ [Working with Tables in DynamoDB](examples-dynamodb-tables.md)
+ [Working with Items in DynamoDB](examples-dynamodb-items.md)

## Use AWS account-based endpoints
<a name="account-based-endpoint-routing"></a>

DynamoDB offers [AWS account-based endpoints](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.SDKOverview.html#Programming.SDKs.endpoints) that can improve performance by using your AWS account ID to streamline request routing.

To take advantage of this feature, you need to use version 1.12.771 or greater of version 1 of AWS SDK for Java. You can find the latest version of the SDK listed in the [Maven central repository](https://central.sonatype.com/artifact/com.amazonaws/aws-java-sdk-bom). After a supported version of SDK is active, it automatically uses the new endpoints.

If you want to opt out of the account-based routing, you have four options:
+ Configure a DynamoDB service client with the `AccountIdEndpointMode` set to `DISABLED`.
+ Set an environment variable.
+ Set a JVM system property.
+ Update the shared AWS config file setting.

The following snippet is an example of how to disable account-based routing by configuring a DynamoDB service client:

```
ClientConfiguration config = new ClientConfiguration()
    .withAccountIdEndpointMode(AccountIdEndpointMode.DISABLED);
AWSCredentialsProvider credentialsProvider = new EnvironmentVariableCredentialsProvider();

AmazonDynamoDB dynamodb = AmazonDynamoDBClientBuilder.standard()
    .withClientConfiguration(config)
    .withCredentials(credentialsProvider)
    .withRegion(Regions.US_WEST_2)
    .build();
```

The AWS SDKs and Tools Reference Guide provides more information on the last [three configuration options](https://docs.aws.amazon.com/sdkref/latest/guide/feature-account-endpoints.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
