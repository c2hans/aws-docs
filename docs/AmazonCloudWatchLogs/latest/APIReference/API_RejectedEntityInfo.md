---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_RejectedEntityInfo.html
---

# RejectedEntityInfo
<a name="API_RejectedEntityInfo"></a>

If an entity is rejected when a `PutLogEvents` request was made, this includes details about the reason for the rejection.

## Contents
<a name="API_RejectedEntityInfo_Contents"></a>

 ** errorType **   <a name="CWL-Type-RejectedEntityInfo-errorType"></a>
The type of error that caused the rejection of the entity when calling `PutLogEvents`.
Type: String
Valid Values: `InvalidEntity | InvalidTypeValue | InvalidKeyAttributes | InvalidAttributes | EntitySizeTooLarge | UnsupportedLogGroupType | MissingRequiredFields`
Required: Yes

## See Also
<a name="API_RejectedEntityInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/RejectedEntityInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/RejectedEntityInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/RejectedEntityInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
