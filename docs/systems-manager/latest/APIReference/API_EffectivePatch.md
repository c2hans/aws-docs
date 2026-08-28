---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_EffectivePatch.html
---

# EffectivePatch
<a name="API_EffectivePatch"></a>

The `EffectivePatch` structure defines metadata about a patch along with the approval state of the patch in a particular patch baseline. The approval state includes information about whether the patch is currently approved, due to be approved by a rule, explicitly approved, or explicitly rejected and the date the patch was or will be approved.

## Contents
<a name="API_EffectivePatch_Contents"></a>

 ** Patch **   <a name="systemsmanager-Type-EffectivePatch-Patch"></a>
Provides metadata for a patch, including information such as the KB ID, severity, classification and a URL for where more information can be obtained about the patch.
Type: [Patch](API_Patch.md) object
Required: No

 ** PatchStatus **   <a name="systemsmanager-Type-EffectivePatch-PatchStatus"></a>
The status of the patch in a patch baseline. This includes information about whether the patch is currently approved, due to be approved by a rule, explicitly approved, or explicitly rejected and the date the patch was or will be approved.
Type: [PatchStatus](API_PatchStatus.md) object
Required: No

## See Also
<a name="API_EffectivePatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/EffectivePatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/EffectivePatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/EffectivePatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
