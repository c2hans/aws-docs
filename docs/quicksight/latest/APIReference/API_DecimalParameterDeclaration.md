---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DecimalParameterDeclaration.html
---

# DecimalParameterDeclaration
<a name="API_DecimalParameterDeclaration"></a>

A parameter declaration for the `Decimal` data type.

## Contents
<a name="API_DecimalParameterDeclaration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="QS-Type-DecimalParameterDeclaration-Name"></a>
The name of the parameter that is being declared.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9]+$`
Required: Yes

 ** ParameterValueType **   <a name="QS-Type-DecimalParameterDeclaration-ParameterValueType"></a>
The value type determines whether the parameter is a single-value or multi-value parameter.
Type: String
Valid Values: `MULTI_VALUED | SINGLE_VALUED`
Required: Yes

 ** DefaultValues **   <a name="QS-Type-DecimalParameterDeclaration-DefaultValues"></a>
The default values of a parameter. If the parameter is a single-value parameter, a maximum of one default value can be provided.
Type: [DecimalDefaultValues](API_DecimalDefaultValues.md) object
Required: No

 ** MappedDataSetParameters **   <a name="QS-Type-DecimalParameterDeclaration-MappedDataSetParameters"></a>
A list of dataset parameters that are mapped to an analysis parameter.
Type: Array of [MappedDataSetParameter](API_MappedDataSetParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 150 items.
Required: No

 ** ValueWhenUnset **   <a name="QS-Type-DecimalParameterDeclaration-ValueWhenUnset"></a>
The configuration that defines the default value of a `Decimal` parameter when a value has not been set.
Type: [DecimalValueWhenUnsetConfiguration](API_DecimalValueWhenUnsetConfiguration.md) object
Required: No

## See Also
<a name="API_DecimalParameterDeclaration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DecimalParameterDeclaration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DecimalParameterDeclaration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DecimalParameterDeclaration)
