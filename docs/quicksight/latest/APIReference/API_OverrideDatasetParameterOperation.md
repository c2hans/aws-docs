---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_OverrideDatasetParameterOperation.html
---

# OverrideDatasetParameterOperation
<a name="API_OverrideDatasetParameterOperation"></a>

A transform operation that overrides the dataset parameter values that are defined in another dataset.

## Contents
<a name="API_OverrideDatasetParameterOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ParameterName **   <a name="QS-Type-OverrideDatasetParameterOperation-ParameterName"></a>
The name of the parameter to be overridden with different values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9]+$`
Required: Yes

 ** NewDefaultValues **   <a name="QS-Type-OverrideDatasetParameterOperation-NewDefaultValues"></a>
The new default values for the parameter.
Type: [NewDefaultValues](API_NewDefaultValues.md) object
Required: No

 ** NewParameterName **   <a name="QS-Type-OverrideDatasetParameterOperation-NewParameterName"></a>
The new name for the parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9]+$`
Required: No

## See Also
<a name="API_OverrideDatasetParameterOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/OverrideDatasetParameterOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/OverrideDatasetParameterOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/OverrideDatasetParameterOperation)
