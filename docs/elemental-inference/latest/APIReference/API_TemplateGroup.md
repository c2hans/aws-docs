---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_TemplateGroup.html
---

# TemplateGroup
<a name="API_TemplateGroup"></a>

A named set of graphics-compositing templates used by the crop feature, specified in the templateGroups array of a CroppingConfig.

## Contents
<a name="API_TemplateGroup_Contents"></a>

 ** name **   <a name="elementalinference-Type-TemplateGroup-name"></a>
A name for the template group.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`
Required: Yes

 ** templateUris **   <a name="elementalinference-Type-TemplateGroup-templateUris"></a>
An array of Amazon S3 URIs that point to the graphics-compositing templates for this group. You can specify 1 or 2 URIs. Each URI must be in the form `s3://bucket-name/key`. Elemental Inference reads these templates using the IAM role that you specify in accessRoleArn.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Length Constraints: Minimum length of 10. Maximum length of 255.
Pattern: `s3://[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]/.+`
Required: Yes

## See Also
<a name="API_TemplateGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/TemplateGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/TemplateGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/TemplateGroup)
