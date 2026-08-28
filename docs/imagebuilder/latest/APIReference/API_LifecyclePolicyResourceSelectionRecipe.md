---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecyclePolicyResourceSelectionRecipe.html
---

# LifecyclePolicyResourceSelectionRecipe
<a name="API_LifecyclePolicyResourceSelectionRecipe"></a>

Specifies an Image Builder recipe that the lifecycle policy uses for resource selection.

## Contents
<a name="API_LifecyclePolicyResourceSelectionRecipe_Contents"></a>

 ** name **   <a name="imagebuilder-Type-LifecyclePolicyResourceSelectionRecipe-name"></a>
The name of an Image Builder recipe that the lifecycle policy uses for resource selection.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: Yes

 ** semanticVersion **   <a name="imagebuilder-Type-LifecyclePolicyResourceSelectionRecipe-semanticVersion"></a>
The version of the Image Builder recipe specified by the `name` field.
Type: String
Pattern: `^(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
Required: Yes

## See Also
<a name="API_LifecyclePolicyResourceSelectionRecipe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/LifecyclePolicyResourceSelectionRecipe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/LifecyclePolicyResourceSelectionRecipe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/LifecyclePolicyResourceSelectionRecipe)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
