---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_MetricDefinition.html
---

# MetricDefinition
<a name="API_MetricDefinition"></a>

Information about the model metric that is reported for a trained model.

## Contents
<a name="API_MetricDefinition_Contents"></a>

 ** name **   <a name="API-Type-MetricDefinition-name"></a>
The name of the model metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: Yes

 ** regex **   <a name="API-Type-MetricDefinition-regex"></a>
The regular expression statement that defines how the model metric is reported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `.+`
Required: Yes

## See Also
<a name="API_MetricDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/MetricDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/MetricDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/MetricDefinition)
