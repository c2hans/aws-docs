---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ChangeProgressDetails.html
---

# ChangeProgressDetails
<a name="API_ChangeProgressDetails"></a>

Container for information about a configuration change happening on a domain.

## Contents
<a name="API_ChangeProgressDetails_Contents"></a>

 ** ChangeId **   <a name="opensearchservice-Type-ChangeProgressDetails-ChangeId"></a>
The ID of the configuration change.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `\p{XDigit}{8}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{12}`
Required: No

 ** ConfigChangeStatus **   <a name="opensearchservice-Type-ChangeProgressDetails-ConfigChangeStatus"></a>
The current status of the configuration change.
Type: String
Valid Values: `Pending | Initializing | Validating | ValidationFailed | ApplyingChanges | Completed | PendingUserInput | Cancelled`
Required: No

 ** InitiatedBy **   <a name="opensearchservice-Type-ChangeProgressDetails-InitiatedBy"></a>
The IAM principal who initiated the configuration change.
Type: String
Valid Values: `CUSTOMER | SERVICE`
Required: No

 ** LastUpdatedTime **   <a name="opensearchservice-Type-ChangeProgressDetails-LastUpdatedTime"></a>
The last time that the configuration change was updated.
Type: Timestamp
Required: No

 ** Message **   <a name="opensearchservice-Type-ChangeProgressDetails-Message"></a>
A message corresponding to the status of the configuration change.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** StartTime **   <a name="opensearchservice-Type-ChangeProgressDetails-StartTime"></a>
The time that the configuration change was initiated, in Universal Coordinated Time (UTC).
Type: Timestamp
Required: No

## See Also
<a name="API_ChangeProgressDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ChangeProgressDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ChangeProgressDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ChangeProgressDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
