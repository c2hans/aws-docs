---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_DataValue.html
---

# DataValue
<a name="API_DataValue"></a>

An object that specifies a value for a property.

## Contents
<a name="API_DataValue_Contents"></a>

 ** booleanValue **   <a name="tm-Type-DataValue-booleanValue"></a>
A Boolean value.
Type: Boolean
Required: No

 ** doubleValue **   <a name="tm-Type-DataValue-doubleValue"></a>
A double value.
Type: Double
Required: No

 ** expression **   <a name="tm-Type-DataValue-expression"></a>
An expression that produces the value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 316.
Pattern: `(^\$\{Parameters\.[a-zA-z]+([a-zA-z_0-9]*)}$)`
Required: No

 ** integerValue **   <a name="tm-Type-DataValue-integerValue"></a>
An integer value.
Type: Integer
Required: No

 ** listValue **   <a name="tm-Type-DataValue-listValue"></a>
A list of multiple values.
Type: Array of [DataValue](#API_DataValue) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** longValue **   <a name="tm-Type-DataValue-longValue"></a>
A long value.
Type: Long
Required: No

 ** mapValue **   <a name="tm-Type-DataValue-mapValue"></a>
An object that maps strings to multiple `DataValue` objects.
Type: String to [DataValue](#API_DataValue) object map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `.*`
Required: No

 ** relationshipValue **   <a name="tm-Type-DataValue-relationshipValue"></a>
A value that relates a component to another component.
Type: [RelationshipValue](API_RelationshipValue.md) object
Required: No

 ** stringValue **   <a name="tm-Type-DataValue-stringValue"></a>
A string value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: No

## See Also
<a name="API_DataValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/DataValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/DataValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/DataValue)
