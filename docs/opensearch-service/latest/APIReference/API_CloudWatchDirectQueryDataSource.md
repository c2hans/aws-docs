---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CloudWatchDirectQueryDataSource.html
---

# CloudWatchDirectQueryDataSource
<a name="API_CloudWatchDirectQueryDataSource"></a>

 Configuration details for a CloudWatch Logs data source that can be used for direct queries.

## Contents
<a name="API_CloudWatchDirectQueryDataSource_Contents"></a>

 ** RoleArn **   <a name="opensearchservice-Type-CloudWatchDirectQueryDataSource-RoleArn"></a>
 The unique identifier of the IAM role that grants OpenSearch Service permission to access the specified data source.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 200.
Pattern: `^arn:aws[a-zA-Z-]*:iam::\d{12}:role(\/service-role)?\/[A-Za-z0-9+=,.@\-_]{1,64}$`
Required: Yes

## See Also
<a name="API_CloudWatchDirectQueryDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/CloudWatchDirectQueryDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/CloudWatchDirectQueryDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/CloudWatchDirectQueryDataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
