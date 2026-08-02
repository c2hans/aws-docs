---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ValidationStrategy.html
---

# ValidationStrategy
<a name="API_ValidationStrategy"></a>

The option to relax the validation that is required to create and update analyses, dashboards, and templates with definition objects. When you set this value to `LENIENT`, validation is skipped for specific errors.

## Contents
<a name="API_ValidationStrategy_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Mode **   <a name="QS-Type-ValidationStrategy-Mode"></a>
The mode of validation for the asset to be created or updated. When you set this value to `STRICT`, strict validation for every error is enforced. When you set this value to `LENIENT`, validation is skipped for specific UI errors.
Type: String
Valid Values: `STRICT | LENIENT`
Required: Yes

## See Also
<a name="API_ValidationStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ValidationStrategy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ValidationStrategy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ValidationStrategy)
