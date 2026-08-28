---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchRule.html
---

# PatchRule
<a name="API_PatchRule"></a>

Defines an approval rule for a patch baseline.

## Contents
<a name="API_PatchRule_Contents"></a>

 ** PatchFilterGroup **   <a name="systemsmanager-Type-PatchRule-PatchFilterGroup"></a>
The patch filter group that defines the criteria for the rule.
Type: [PatchFilterGroup](API_PatchFilterGroup.md) object
Required: Yes

 ** ApproveAfterDays **   <a name="systemsmanager-Type-PatchRule-ApproveAfterDays"></a>
The number of days after the release date of each patch matched by the rule that the patch is marked as approved in the patch baseline. For example, a value of `7` means that patches are approved seven days after they are released.
Patch Manager evaluates patch release dates using Coordinated Universal Time (UTC). If a patch is released at `2025-11-09T18:00:00Z` and `ApproveAfterDays` is set to `7`, the patch will be approved after `2025-11-16T18:00:00Z`.
This parameter is marked as `Required: No`, but your request must include a value for either `ApproveAfterDays` or `ApproveUntilDate`.
Not supported for Debian Server or Ubuntu Server.
Use caution when setting this value for Windows Server patch baselines. Because patch updates that are replaced by later updates are removed, setting too broad a value for this parameter can result in crucial patches not being installed. For more information, see the **Windows Server** tab in the topic [How security patches are selected](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-selecting-patches.html) in the * AWS Systems Manager User Guide*.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 360.
Required: No

 ** ApproveUntilDate **   <a name="systemsmanager-Type-PatchRule-ApproveUntilDate"></a>
The cutoff date for auto approval of released patches. Any patches released on or before this date are installed automatically.
Enter dates in the format `YYYY-MM-DD`. For example, `2025-11-16`.
Patch Manager evaluates patch release dates using Coordinated Universal Time (UTC). If you enter the date `2025-11-16`, patches released between `2025-11-16T00:00:00Z` and `2025-11-16T23:59:59Z` will be included in the approval.
This parameter is marked as `Required: No`, but your request must include a value for either `ApproveUntilDate` or `ApproveAfterDays`.
Not supported for Debian Server or Ubuntu Server.
Use caution when setting this value for Windows Server patch baselines. Because patch updates that are replaced by later updates are removed, setting too broad a value for this parameter can result in crucial patches not being installed. For more information, see the **Windows Server** tab in the topic [How security patches are selected](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-selecting-patches.html) in the * AWS Systems Manager User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Required: No

 ** ComplianceLevel **   <a name="systemsmanager-Type-PatchRule-ComplianceLevel"></a>
A compliance severity level for all approved patches in a patch baseline.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | INFORMATIONAL | UNSPECIFIED`
Required: No

 ** EnableNonSecurity **   <a name="systemsmanager-Type-PatchRule-EnableNonSecurity"></a>
For managed nodes identified by the approval rule filters, enables a patch baseline to apply non-security updates available in the specified repository. The default value is `false`. Applies to Linux managed nodes only.
Type: Boolean
Required: No

## See Also
<a name="API_PatchRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/PatchRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/PatchRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/PatchRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
