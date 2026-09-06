---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_AttributeValue.html
---

# AttributeValue
<a name="API_AttributeValue"></a>

Values for use in player attribute key-value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array, or data map. Each `AttributeValue` object can use only one of the available properties.

## Contents
<a name="API_AttributeValue_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** N **   <a name="gameliftservers-Type-AttributeValue-N"></a>
For number values, expressed as double.
Type: Double
Required: No

 ** S **   <a name="gameliftservers-Type-AttributeValue-S"></a>
For single string values. Maximum string length is 100 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** SDM **   <a name="gameliftservers-Type-AttributeValue-SDM"></a>
For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters.
Type: String to double map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** SL **   <a name="gameliftservers-Type-AttributeValue-SL"></a>
For a list of up to 100 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_AttributeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/AttributeValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/AttributeValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/AttributeValue)
