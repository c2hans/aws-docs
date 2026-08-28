---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_LogPublishingOption.html
---

# LogPublishingOption
<a name="API_LogPublishingOption"></a>

Specifies whether the Amazon OpenSearch Service domain publishes the OpenSearch application and slow logs to Amazon CloudWatch. For more information, see [Monitoring OpenSearch logs with Amazon CloudWatch Logs](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createdomain-configure-slow-logs.html).

**Note**
After you enable log publishing, you still have to enable the collection of slow logs using the OpenSearch REST API.

## Contents
<a name="API_LogPublishingOption_Contents"></a>

 ** CloudWatchLogsLogGroupArn **   <a name="opensearchservice-Type-LogPublishingOption-CloudWatchLogsLogGroupArn"></a>
The Amazon Resource Name (ARN) of the CloudWatch Logs group to publish logs to.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** Enabled **   <a name="opensearchservice-Type-LogPublishingOption-Enabled"></a>
Whether the log should be published.
Type: Boolean
Required: No

## See Also
<a name="API_LogPublishingOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/LogPublishingOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/LogPublishingOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/LogPublishingOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
