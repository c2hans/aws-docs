---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ComponentTypeSummary.html
---

# ComponentTypeSummary
<a name="API_ComponentTypeSummary"></a>

An object that contains information about a component type.

## Contents
<a name="API_ComponentTypeSummary_Contents"></a>

 ** arn **   <a name="tm-Type-ComponentTypeSummary-arn"></a>
The ARN of the component type.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`
Required: Yes

 ** componentTypeId **   <a name="tm-Type-ComponentTypeSummary-componentTypeId"></a>
The ID of the component type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\.\-0-9:]+`
Required: Yes

 ** creationDateTime **   <a name="tm-Type-ComponentTypeSummary-creationDateTime"></a>
The date and time when the component type was created.
Type: Timestamp
Required: Yes

 ** updateDateTime **   <a name="tm-Type-ComponentTypeSummary-updateDateTime"></a>
The date and time when the component type was last updated.
Type: Timestamp
Required: Yes

 ** componentTypeName **   <a name="tm-Type-ComponentTypeSummary-componentTypeName"></a>
The component type name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*[^\u0000-\u001F\u007F]*.*`
Required: No

 ** description **   <a name="tm-Type-ComponentTypeSummary-description"></a>
The description of the component type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** status **   <a name="tm-Type-ComponentTypeSummary-status"></a>
The current status of the component type.
Type: [Status](API_Status.md) object
Required: No

## See Also
<a name="API_ComponentTypeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ComponentTypeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ComponentTypeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ComponentTypeSummary)
