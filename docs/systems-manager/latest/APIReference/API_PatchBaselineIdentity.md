---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchBaselineIdentity.html
---

# PatchBaselineIdentity
<a name="API_PatchBaselineIdentity"></a>

Defines the basic information about a patch baseline.

## Contents
<a name="API_PatchBaselineIdentity_Contents"></a>

 ** BaselineDescription **   <a name="systemsmanager-Type-PatchBaselineIdentity-BaselineDescription"></a>
The description of the patch baseline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** BaselineId **   <a name="systemsmanager-Type-PatchBaselineIdentity-BaselineId"></a>
The ID of the patch baseline.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-:/]{20,128}$`
Required: No

 ** BaselineName **   <a name="systemsmanager-Type-PatchBaselineIdentity-BaselineName"></a>
The name of the patch baseline.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** DefaultBaseline **   <a name="systemsmanager-Type-PatchBaselineIdentity-DefaultBaseline"></a>
Indicates whether this is the default baseline. AWS Systems Manager supports creating multiple default patch baselines. For example, you can create a default patch baseline for each operating system.
Type: Boolean
Required: No

 ** OperatingSystem **   <a name="systemsmanager-Type-PatchBaselineIdentity-OperatingSystem"></a>
Defines the operating system the patch baseline applies to. The default value is `WINDOWS`.
Type: String
Valid Values: `WINDOWS | AMAZON_LINUX | AMAZON_LINUX_2 | AMAZON_LINUX_2022 | UBUNTU | REDHAT_ENTERPRISE_LINUX | SUSE | CENTOS | ORACLE_LINUX | DEBIAN | MACOS | RASPBIAN | ROCKY_LINUX | ALMA_LINUX | AMAZON_LINUX_2023`
Required: No

## See Also
<a name="API_PatchBaselineIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/PatchBaselineIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/PatchBaselineIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/PatchBaselineIdentity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
