---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/ddb-account-based-endpoints-v3.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Use AWS account-based endpoints with DynamoDB
<a name="ddb-account-based-endpoints-v3"></a>

DynamoDB offers [AWS account-based endpoints](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.SDKOverview.html#Programming.SDKs.endpoints) that can improve performance by using your AWS account ID to streamline request routing.

To take advantage of this feature, you need to use version 3.656.0 or greater of AWS SDK for JavaScript version 3. This account-based endpoints feature is enabled by default in this new version.

If you want to opt out of the account-based routing, you have the following options:
+ Configure a DynamoDB service client with the `accountIdEndpointMode` parameter set to `disabled`.
+ Set the environment variable `AWS_ACCOUNT_ID_ENDPOINT_MODE` to `disabled`.
+ Update the shared AWS config file setting `account_id_endpoint_mode` to `disabled`.

The following snippet is an example of how to disable account-based routing by configuring a DynamoDB service client:

```
const ddbClient = new DynamoDBClient({
  region: "us-west-2",
  accountIdEndpointMode: "disabled" // Disable account ID in the endpoint
});
```

The AWS SDKs and Tools Reference Guide provides more information on the [other configuration options](https://docs.aws.amazon.com/sdkref/latest/guide/feature-account-endpoints.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for JavaScript. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-javascript` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
