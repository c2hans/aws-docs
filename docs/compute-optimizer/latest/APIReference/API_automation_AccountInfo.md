---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_AccountInfo.html
---

# AccountInfo
<a name="API_automation_AccountInfo"></a>

 Contains information about an AWS account's enrollment and association status with Compute Optimizer Automation.

## Contents
<a name="API_automation_AccountInfo_Contents"></a>

 ** accountId **   <a name="computeoptimizer-Type-automation_AccountInfo-accountId"></a>
 The ID of the AWS account.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** lastUpdatedTimestamp **   <a name="computeoptimizer-Type-automation_AccountInfo-lastUpdatedTimestamp"></a>
The timestamp when the account's Automation enrollment status was last updated.
Type: Timestamp
Required: Yes

 ** organizationRuleMode **   <a name="computeoptimizer-Type-automation_AccountInfo-organizationRuleMode"></a>
Specifies whether the management account can create Automation rules that implement optimization actions for this account.
Type: String
Valid Values: `AnyAllowed | NoneAllowed`
Required: Yes

 ** status **   <a name="computeoptimizer-Type-automation_AccountInfo-status"></a>
 The enrollment status of the account: Active, Inactive, Pending, or Failed.
Type: String
Valid Values: `Active | Inactive | Pending | Failed`
Required: Yes

 ** statusReason **   <a name="computeoptimizer-Type-automation_AccountInfo-statusReason"></a>
The reason for the current Automation enrollment status.
Type: String
Required: No

## See Also
<a name="API_automation_AccountInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/AccountInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/AccountInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/AccountInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
