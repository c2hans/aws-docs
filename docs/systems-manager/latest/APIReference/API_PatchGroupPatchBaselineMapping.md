---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchGroupPatchBaselineMapping.html
---

# PatchGroupPatchBaselineMapping
<a name="API_PatchGroupPatchBaselineMapping"></a>

The mapping between a patch group and the patch baseline the patch group is registered with.

## Contents
<a name="API_PatchGroupPatchBaselineMapping_Contents"></a>

 ** BaselineIdentity **   <a name="systemsmanager-Type-PatchGroupPatchBaselineMapping-BaselineIdentity"></a>
The patch baseline the patch group is registered with.
Type: [PatchBaselineIdentity](API_PatchBaselineIdentity.md) object
Required: No

 ** PatchGroup **   <a name="systemsmanager-Type-PatchGroupPatchBaselineMapping-PatchGroup"></a>
The name of the patch group registered with the patch baseline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_PatchGroupPatchBaselineMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/PatchGroupPatchBaselineMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/PatchGroupPatchBaselineMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/PatchGroupPatchBaselineMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
