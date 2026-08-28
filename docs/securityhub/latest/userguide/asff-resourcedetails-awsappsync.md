---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/asff-resourcedetails-awsappsync.html
---

# AwsAppSync resources in ASFF
<a name="asff-resourcedetails-awsappsync"></a>

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsAppSync` resources.

AWS Security Hub CSPM normalizes findings from various sources into ASFF. For background information about ASFF, see [AWS Security Finding Format (ASFF)](securityhub-findings-format.md).

## AwsAppSyncGraphQLApi
<a name="asff-resourcedetails-awsappsyncgraphqlapi"></a>

`AwsAppSyncGraphQLApi` provides information about an AWS AppSync GraphQL API, which is a top-level construct for your application.

The following example shows the ASFF for the `AwsAppSyncGraphQLApi` object. To view descriptions of `AwsAppSyncGraphQLApi` attributes, see [AwsAppSyncGraphQLApi](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAppSyncGraphQLApiDetails.html) in the *AWS Security Hub API Reference*.

**Example**

```
"AwsAppSyncGraphQLApi": {
    "AdditionalAuthenticationProviders": [
    {
    	"AuthenticationType": "AWS_LAMBDA",
    	"LambdaAuthorizerConfig": {
    		"AuthorizerResultTtlInSeconds": 300,
    		"AuthorizerUri": "arn:aws:lambda:us-east-1:123456789012:function:mylambdafunc"
    	}
    },
    {
    	"AuthenticationType": "AWS_IAM"
    }
    ],
    "ApiId": "021345abcdef6789",
    "Arn": "arn:aws:appsync:eu-central-1:123456789012:apis/021345abcdef6789",
    "AuthenticationType": "API_KEY",
    "Id": "021345abcdef6789",
    "LogConfig": {
    	"CloudWatchLogsRoleArn": "arn:aws:iam::123456789012:role/service-role/appsync-graphqlapi-logs-eu-central-1",
    	"ExcludeVerboseContent": true,
    	"FieldLogLevel": "ALL"
    },
    "Name": "My AppSync App",
    "XrayEnabled": true,
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
