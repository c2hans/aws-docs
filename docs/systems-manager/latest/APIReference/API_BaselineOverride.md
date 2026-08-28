---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_BaselineOverride.html
---

# BaselineOverride
<a name="API_BaselineOverride"></a>

Defines the basic information about a patch baseline override.

## Contents
<a name="API_BaselineOverride_Contents"></a>

 ** ApprovalRules **   <a name="systemsmanager-Type-BaselineOverride-ApprovalRules"></a>
A set of rules defining the approval rules for a patch baseline.
Type: [PatchRuleGroup](API_PatchRuleGroup.md) object
Required: No

 ** ApprovedPatches **   <a name="systemsmanager-Type-BaselineOverride-ApprovedPatches"></a>
A list of explicitly approved patches for the baseline.
For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html) in the * AWS Systems Manager User Guide*.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** ApprovedPatchesComplianceLevel **   <a name="systemsmanager-Type-BaselineOverride-ApprovedPatchesComplianceLevel"></a>
Defines the compliance level for approved patches. When an approved patch is reported as missing, this value describes the severity of the compliance violation.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | INFORMATIONAL | UNSPECIFIED`
Required: No

 ** ApprovedPatchesEnableNonSecurity **   <a name="systemsmanager-Type-BaselineOverride-ApprovedPatchesEnableNonSecurity"></a>
Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is `false`. Applies to Linux managed nodes only.
Type: Boolean
Required: No

 ** AvailableSecurityUpdatesComplianceStatus **   <a name="systemsmanager-Type-BaselineOverride-AvailableSecurityUpdatesComplianceStatus"></a>
Indicates whether managed nodes for which there are available security-related patches that have not been approved by the baseline are being defined as `COMPLIANT` or `NON_COMPLIANT`. This option is specified when the `CreatePatchBaseline` or `UpdatePatchBaseline` commands are run.
Applies to Windows Server managed nodes only.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT`
Required: No

 ** GlobalFilters **   <a name="systemsmanager-Type-BaselineOverride-GlobalFilters"></a>
A set of patch filters, typically used for approval rules.
Type: [PatchFilterGroup](API_PatchFilterGroup.md) object
Required: No

 ** OperatingSystem **   <a name="systemsmanager-Type-BaselineOverride-OperatingSystem"></a>
The operating system rule used by the patch baseline override.
Type: String
Valid Values: `WINDOWS | AMAZON_LINUX | AMAZON_LINUX_2 | AMAZON_LINUX_2022 | UBUNTU | REDHAT_ENTERPRISE_LINUX | SUSE | CENTOS | ORACLE_LINUX | DEBIAN | MACOS | RASPBIAN | ROCKY_LINUX | ALMA_LINUX | AMAZON_LINUX_2023`
Required: No

 ** RejectedPatches **   <a name="systemsmanager-Type-BaselineOverride-RejectedPatches"></a>
A list of explicitly rejected patches for the baseline.
For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html) in the * AWS Systems Manager User Guide*.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** RejectedPatchesAction **   <a name="systemsmanager-Type-BaselineOverride-RejectedPatchesAction"></a>
The action for Patch Manager to take on patches included in the `RejectedPackages` list. A patch can be allowed only if it is a dependency of another package, or blocked entirely along with packages that include it as a dependency.
Type: String
Valid Values: `ALLOW_AS_DEPENDENCY | BLOCK`
Required: No

 ** Sources **   <a name="systemsmanager-Type-BaselineOverride-Sources"></a>
Information about the patches to use to update the managed nodes, including target operating systems and source repositories. Applies to Linux managed nodes only.
Type: Array of [PatchSource](API_PatchSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

## See Also
<a name="API_BaselineOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/BaselineOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/BaselineOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/BaselineOverride)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
