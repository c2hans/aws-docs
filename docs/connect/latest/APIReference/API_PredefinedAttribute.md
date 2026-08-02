---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_PredefinedAttribute.html
---

# PredefinedAttribute
<a name="API_PredefinedAttribute"></a>

Information about a predefined attribute.

## Contents
<a name="API_PredefinedAttribute_Contents"></a>

 ** AttributeConfiguration **   <a name="connect-Type-PredefinedAttribute-AttributeConfiguration"></a>
Custom metadata that is associated to predefined attributes to control behavior in upstream services, such as controlling how a predefined attribute should be displayed in the Connect Customer admin website.
Type: [PredefinedAttributeConfiguration](API_PredefinedAttributeConfiguration.md) object
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-PredefinedAttribute-LastModifiedRegion"></a>
Last modified region.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-PredefinedAttribute-LastModifiedTime"></a>
Last modified time.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-PredefinedAttribute-Name"></a>
The name of the predefined attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Purposes **   <a name="connect-Type-PredefinedAttribute-Purposes"></a>
Values that enable you to categorize your predefined attributes. You can use them in custom UI elements across the Connect Customer admin website.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Values **   <a name="connect-Type-PredefinedAttribute-Values"></a>
The values of the predefined attribute.
Type: [PredefinedAttributeValues](API_PredefinedAttributeValues.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_PredefinedAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/PredefinedAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/PredefinedAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/PredefinedAttribute)
