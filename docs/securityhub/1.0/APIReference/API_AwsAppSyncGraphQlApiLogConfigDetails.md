---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAppSyncGraphQlApiLogConfigDetails.html
---

# AwsAppSyncGraphQlApiLogConfigDetails
<a name="API_AwsAppSyncGraphQlApiLogConfigDetails"></a>

 Specifies the logging configuration when writing GraphQL operations and tracing to Amazon CloudWatch for an AWS AppSync GraphQL API.

## Contents
<a name="API_AwsAppSyncGraphQlApiLogConfigDetails_Contents"></a>

 ** CloudWatchLogsRoleArn **   <a name="securityhub-Type-AwsAppSyncGraphQlApiLogConfigDetails-CloudWatchLogsRoleArn"></a>
 The Amazon Resource Name (ARN) of the service role that AWS AppSync assumes to publish to CloudWatch Logs in your account.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ExcludeVerboseContent **   <a name="securityhub-Type-AwsAppSyncGraphQlApiLogConfigDetails-ExcludeVerboseContent"></a>
 Set to `TRUE` to exclude sections that contain information such as headers, context, and evaluated mapping templates, regardless of logging level.
Type: Boolean
Required: No

 ** FieldLogLevel **   <a name="securityhub-Type-AwsAppSyncGraphQlApiLogConfigDetails-FieldLogLevel"></a>
 The field logging level.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsAppSyncGraphQlApiLogConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAppSyncGraphQlApiLogConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAppSyncGraphQlApiLogConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAppSyncGraphQlApiLogConfigDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
