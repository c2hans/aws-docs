---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_ChangesetSummary.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# ChangesetSummary
<a name="API_ChangesetSummary"></a>

A Changeset is unit of data in a Dataset.

## Contents
<a name="API_ChangesetSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** activeFromTimestamp **   <a name="finspace-Type-ChangesetSummary-activeFromTimestamp"></a>
Beginning time from which the Changeset is active. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Long
Required: No

 ** activeUntilTimestamp **   <a name="finspace-Type-ChangesetSummary-activeUntilTimestamp"></a>
Time until which the Changeset is active. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Long
Required: No

 ** changesetArn **   <a name="finspace-Type-ChangesetSummary-changesetArn"></a>
The ARN identifier of the Changeset.
Type: String
Required: No

 ** changesetId **   <a name="finspace-Type-ChangesetSummary-changesetId"></a>
The unique identifier for a Changeset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: No

 ** changeType **   <a name="finspace-Type-ChangesetSummary-changeType"></a>
Type that indicates how a Changeset is applied to a Dataset.
+  `REPLACE` – Changeset is considered as a replacement to all prior loaded Changesets.
+  `APPEND` – Changeset is considered as an addition to the end of all prior loaded Changesets.
+  `MODIFY` – Changeset is considered as a replacement to a specific prior ingested Changeset.
Type: String
Valid Values: `REPLACE | APPEND | MODIFY`
Required: No

 ** createTime **   <a name="finspace-Type-ChangesetSummary-createTime"></a>
The timestamp at which the Changeset was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Long
Required: No

 ** datasetId **   <a name="finspace-Type-ChangesetSummary-datasetId"></a>
The unique identifier for the FinSpace Dataset in which the Changeset is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: No

 ** errorInfo **   <a name="finspace-Type-ChangesetSummary-errorInfo"></a>
The structure with error messages.
Type: [ChangesetErrorInfo](API_ChangesetErrorInfo.md) object
Required: No

 ** formatParams **   <a name="finspace-Type-ChangesetSummary-formatParams"></a>
Options that define the structure of the source file(s).
Type: String to string map
Key Length Constraints: Maximum length of 128.
Key Pattern: `[\s\S]*\S[\s\S]*`
Value Length Constraints: Maximum length of 1000.
Value Pattern: `[\s\S]*\S[\s\S]*`
Required: No

 ** sourceParams **   <a name="finspace-Type-ChangesetSummary-sourceParams"></a>
Options that define the location of the data being ingested.
Type: String to string map
Key Length Constraints: Maximum length of 128.
Key Pattern: `[\s\S]*\S[\s\S]*`
Value Length Constraints: Maximum length of 1000.
Value Pattern: `[\s\S]*\S[\s\S]*`
Required: No

 ** status **   <a name="finspace-Type-ChangesetSummary-status"></a>
Status of the Changeset ingestion.
+  `PENDING` – Changeset is pending creation.
+  `FAILED` – Changeset creation has failed.
+  `SUCCESS` – Changeset creation has succeeded.
+  `RUNNING` – Changeset creation is running.
+  `STOP_REQUESTED` – User requested Changeset creation to stop.
Type: String
Valid Values: `PENDING | FAILED | SUCCESS | RUNNING | STOP_REQUESTED`
Required: No

 ** updatedByChangesetId **   <a name="finspace-Type-ChangesetSummary-updatedByChangesetId"></a>
The unique identifier of the updated Changeset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: No

 ** updatesChangesetId **   <a name="finspace-Type-ChangesetSummary-updatesChangesetId"></a>
The unique identifier of the Changeset that is updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: No

## See Also
<a name="API_ChangesetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/ChangesetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/ChangesetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/ChangesetSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
