---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_AttributeGroupDetails.html
---

# AttributeGroupDetails
<a name="API_app-registry_AttributeGroupDetails"></a>

 The details related to a specific AttributeGroup.

## Contents
<a name="API_app-registry_AttributeGroupDetails_Contents"></a>

 ** arn **   <a name="servicecatalog-Type-app-registry_AttributeGroupDetails-arn"></a>
The Amazon resource name (ARN) that specifies the attribute group.
Type: String
Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/attribute-groups/[-.\w]+`
Required: No

 ** createdBy **   <a name="servicecatalog-Type-app-registry_AttributeGroupDetails-createdBy"></a>
The service principal that created the attribute group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?!-)([a-z0-9-]+\.)+(aws\.internal|amazonaws\.com(\.cn)?)$`
Required: No

 ** id **   <a name="servicecatalog-Type-app-registry_AttributeGroupDetails-id"></a>
The unique identifier of the attribute group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-.\w]+`
Required: No

 ** name **   <a name="servicecatalog-Type-app-registry_AttributeGroupDetails-name"></a>
 This field is no longer supported. We recommend you don't use the field when using `ListAttributeGroupsForApplication`.
 The name of the attribute group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-.\w]+`
Required: No

## See Also
<a name="API_app-registry_AttributeGroupDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/AttributeGroupDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/AttributeGroupDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/AttributeGroupDetails)
