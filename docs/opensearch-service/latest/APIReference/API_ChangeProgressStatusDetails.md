---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ChangeProgressStatusDetails.html
---

# ChangeProgressStatusDetails
<a name="API_ChangeProgressStatusDetails"></a>

The progress details of a specific domain configuration change.

## Contents
<a name="API_ChangeProgressStatusDetails_Contents"></a>

 ** ChangeId **   <a name="opensearchservice-Type-ChangeProgressStatusDetails-ChangeId"></a>
The unique change identifier associated with a specific domain configuration change.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `\p{XDigit}{8}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{12}`
Required: No

 ** ChangeProgressStages **   <a name="opensearchservice-Type-ChangeProgressStatusDetails-ChangeProgressStages"></a>
The specific stages that the domain is going through to perform the configuration change.
Type: Array of [ChangeProgressStage](API_ChangeProgressStage.md) objects
Required: No

 ** CompletedProperties **   <a name="opensearchservice-Type-ChangeProgressStatusDetails-CompletedProperties"></a>
The list of properties in the domain configuration change that have completed.
Type: Array of strings
Required: No

 ** ConfigChangeStatus **   <a name="opensearchservice-Type-ChangeProgressStatusDetails-ConfigChangeStatus"></a>
The current status of the configuration change.
Type: String
Valid Values: `Pending | Initializing | Validating | ValidationFailed | ApplyingChanges | Completed | PendingUserInput | Cancelled`
Required: No

 ** InitiatedBy **   <a name="opensearchservice-Type-ChangeProgressStatusDetails-InitiatedBy"></a>
The IAM principal who initiated the configuration change.
Type: String
Valid Values: `CUSTOMER | SERVICE`
Required: No

 ** LastUpdatedTime **   <a name="opensearchservice-Type-ChangeProgressStatusDetails-LastUpdatedTime"></a>
The last time that the status of the configuration change was updated.
Type: Timestamp
Required: No

 ** PendingProperties **   <a name="opensearchservice-Type-ChangeProgressStatusDetails-PendingProperties"></a>
The list of properties in the domain configuration change that are still pending.
Type: Array of strings
Required: No

 ** StartTime **   <a name="opensearchservice-Type-ChangeProgressStatusDetails-StartTime"></a>
The time at which the configuration change is made on the domain.
Type: Timestamp
Required: No

 ** Status **   <a name="opensearchservice-Type-ChangeProgressStatusDetails-Status"></a>
The overall status of the domain configuration change.
Type: String
Valid Values: `PENDING | PROCESSING | COMPLETED | FAILED`
Required: No

 ** TotalNumberOfStages **   <a name="opensearchservice-Type-ChangeProgressStatusDetails-TotalNumberOfStages"></a>
The total number of stages required for the configuration change.
Type: Integer
Required: No

## See Also
<a name="API_ChangeProgressStatusDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ChangeProgressStatusDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ChangeProgressStatusDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ChangeProgressStatusDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
