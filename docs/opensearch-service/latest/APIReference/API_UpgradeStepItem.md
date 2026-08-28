---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpgradeStepItem.html
---

# UpgradeStepItem
<a name="API_UpgradeStepItem"></a>

Represents a single step of an upgrade or upgrade eligibility check workflow.

## Contents
<a name="API_UpgradeStepItem_Contents"></a>

 ** Issues **   <a name="opensearchservice-Type-UpgradeStepItem-Issues"></a>
A list of strings containing detailed information about the errors encountered in a particular step.
Type: Array of strings
Required: No

 ** ProgressPercent **   <a name="opensearchservice-Type-UpgradeStepItem-ProgressPercent"></a>
The floating point value representing the progress percentage of a particular step.
Type: Double
Required: No

 ** UpgradeStep **   <a name="opensearchservice-Type-UpgradeStepItem-UpgradeStep"></a>
 One of three steps that an upgrade or upgrade eligibility check goes through:
+ PreUpgradeCheck
+ Snapshot
+ Upgrade
Type: String
Valid Values: `PRE_UPGRADE_CHECK | SNAPSHOT | UPGRADE`
Required: No

 ** UpgradeStepStatus **   <a name="opensearchservice-Type-UpgradeStepItem-UpgradeStepStatus"></a>
 The current status of the upgrade. The status can take one of the following values:
+ In Progress
+ Succeeded
+ Succeeded with Issues
+ Failed
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | SUCCEEDED_WITH_ISSUES | FAILED`
Required: No

## See Also
<a name="API_UpgradeStepItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/UpgradeStepItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/UpgradeStepItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/UpgradeStepItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
