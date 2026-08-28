---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpgradeHistory.html
---

# UpgradeHistory
<a name="API_UpgradeHistory"></a>

History of the last 10 upgrades and upgrade eligibility checks for an Amazon OpenSearch Service domain.

## Contents
<a name="API_UpgradeHistory_Contents"></a>

 ** StartTimestamp **   <a name="opensearchservice-Type-UpgradeHistory-StartTimestamp"></a>
UTC timestamp at which the upgrade API call was made, in the format `yyyy-MM-ddTHH:mm:ssZ`.
Type: Timestamp
Required: No

 ** StepsList **   <a name="opensearchservice-Type-UpgradeHistory-StepsList"></a>
A list of each step performed as part of a specific upgrade or upgrade eligibility check.
Type: Array of [UpgradeStepItem](API_UpgradeStepItem.md) objects
Required: No

 ** UpgradeName **   <a name="opensearchservice-Type-UpgradeHistory-UpgradeName"></a>
A string that describes the upgrade.
Type: String
Required: No

 ** UpgradeStatus **   <a name="opensearchservice-Type-UpgradeHistory-UpgradeStatus"></a>
 The current status of the upgrade. The status can take one of the following values:
+ In Progress
+ Succeeded
+ Succeeded with Issues
+ Failed
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | SUCCEEDED_WITH_ISSUES | FAILED`
Required: No

## See Also
<a name="API_UpgradeHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/UpgradeHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/UpgradeHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/UpgradeHistory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
