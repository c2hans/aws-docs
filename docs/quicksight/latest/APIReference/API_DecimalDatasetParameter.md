---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DecimalDatasetParameter.html
---

# DecimalDatasetParameter
<a name="API_DecimalDatasetParameter"></a>

A decimal parameter for a dataset.

## Contents
<a name="API_DecimalDatasetParameter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Id **   <a name="QS-Type-DecimalDatasetParameter-Id"></a>
An identifier for the decimal parameter created in the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** Name **   <a name="QS-Type-DecimalDatasetParameter-Name"></a>
The name of the decimal parameter that is created in the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9]+$`
Required: Yes

 ** ValueType **   <a name="QS-Type-DecimalDatasetParameter-ValueType"></a>
The value type of the dataset parameter. Valid values are `single value` or `multi value`.
Type: String
Valid Values: `MULTI_VALUED | SINGLE_VALUED`
Required: Yes

 ** DefaultValues **   <a name="QS-Type-DecimalDatasetParameter-DefaultValues"></a>
A list of default values for a given decimal parameter. This structure only accepts static values.
Type: [DecimalDatasetParameterDefaultValues](API_DecimalDatasetParameterDefaultValues.md) object
Required: No

## See Also
<a name="API_DecimalDatasetParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DecimalDatasetParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DecimalDatasetParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DecimalDatasetParameter)
