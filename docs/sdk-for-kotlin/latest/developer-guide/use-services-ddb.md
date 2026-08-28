---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/use-services-ddb.html
---

# Work with DynamoDB using the AWS SDK for Kotlin
<a name="use-services-ddb"></a>

## Use AWS account-based endpoints
<a name="use-services-ddb-account-based-endpoints"></a>

DynamoDB offers [AWS account-based endpoints](/amazondynamodb/latest/developerguide/Programming.SDKOverview.html#Programming.SDKs.endpoints) that can improve performance by using your AWS account ID to streamline request routing.

To take advantage of this feature, you need to use version 1.3.37 or greater of the AWS SDK for Kotlin. You can find the latest version of the SDK listed in the [Maven central repository](https://central.sonatype.com/artifact/aws.sdk.kotlin/dynamodb/versions). After a supported version of SDK is active, it automatically uses the new endpoints.

If you want to opt out of the account-based routing, you have four options:
+ Configure a DynamoDB service client with the `AccountIdEndpointMode` set to `DISABLED`.
+ Set an environment variable.
+ Set a JVM system property.
+ Update the shared AWS config file setting.

The following snippet is an example of how to disable account-based routing by configuring a DynamoDB service client:

```
DynamoDbClient.fromEnvironment {
    accountIdEndpointMode = AccountIdEndpointMode.DISABLED // The default value is PREFERRED.
}
```

The AWS SDKs and Tools Reference Guide provides more information on the last [three configuration options](/sdkref/latest/guide/feature-account-endpoints.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
