---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DateTimeParameterDeclaration.html
---

# DateTimeParameterDeclaration
<a name="API_DateTimeParameterDeclaration"></a>

A parameter declaration for the `DateTime` data type.

## Contents
<a name="API_DateTimeParameterDeclaration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="QS-Type-DateTimeParameterDeclaration-Name"></a>
The name of the parameter that is being declared.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9]+$`
Required: Yes

 ** DefaultValues **   <a name="QS-Type-DateTimeParameterDeclaration-DefaultValues"></a>
The default values of a parameter. If the parameter is a single-value parameter, a maximum of one default value can be provided.
Type: [DateTimeDefaultValues](API_DateTimeDefaultValues.md) object
Required: No

 ** MappedDataSetParameters **   <a name="QS-Type-DateTimeParameterDeclaration-MappedDataSetParameters"></a>
A list of dataset parameters that are mapped to an analysis parameter.
Type: Array of [MappedDataSetParameter](API_MappedDataSetParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 150 items.
Required: No

 ** TimeGranularity **   <a name="QS-Type-DateTimeParameterDeclaration-TimeGranularity"></a>
The level of time precision that is used to aggregate `DateTime` values.
Type: String
Valid Values: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
Required: No

 ** ValueWhenUnset **   <a name="QS-Type-DateTimeParameterDeclaration-ValueWhenUnset"></a>
The configuration that defines the default value of a `DateTime` parameter when a value has not been set.
Type: [DateTimeValueWhenUnsetConfiguration](API_DateTimeValueWhenUnsetConfiguration.md) object
Required: No

## See Also
<a name="API_DateTimeParameterDeclaration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DateTimeParameterDeclaration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DateTimeParameterDeclaration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DateTimeParameterDeclaration)
