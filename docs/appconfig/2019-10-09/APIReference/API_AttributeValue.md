---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_AttributeValue.html
---

# AttributeValue
<a name="API_AttributeValue"></a>

A value for a feature flag attribute. Only one of the members can be set.

## Contents
<a name="API_AttributeValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** BooleanValue **   <a name="appconfig-Type-AttributeValue-BooleanValue"></a>
A Boolean value for the attribute.
Type: Boolean
Required: No

 ** NumberArray **   <a name="appconfig-Type-AttributeValue-NumberArray"></a>
An array of numeric values for the attribute.
Type: Array of doubles
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: No

 ** NumberValue **   <a name="appconfig-Type-AttributeValue-NumberValue"></a>
A numeric value for the attribute.
Type: Double
Required: No

 ** StringArray **   <a name="appconfig-Type-AttributeValue-StringArray"></a>
An array of string values for the attribute.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** StringValue **   <a name="appconfig-Type-AttributeValue-StringValue"></a>
A string value for the attribute.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_AttributeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/AttributeValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/AttributeValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/AttributeValue)
