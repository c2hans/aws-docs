---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_TrainedModelExportsMaxSize.html
---

# TrainedModelExportsMaxSize
<a name="API_TrainedModelExportsMaxSize"></a>

The maximum size of the trained model metrics that can be exported. If the trained model metrics dataset is larger than this value, it will not be exported.

## Contents
<a name="API_TrainedModelExportsMaxSize_Contents"></a>

 ** unit **   <a name="API-Type-TrainedModelExportsMaxSize-unit"></a>
The unit of measurement for the data size.
Type: String
Valid Values: `GB`
Required: Yes

 ** value **   <a name="API-Type-TrainedModelExportsMaxSize-value"></a>
The maximum size of the dataset to export.
Type: Double
Valid Range: Minimum value of 0.01. Maximum value of 50.0.
Required: Yes

## See Also
<a name="API_TrainedModelExportsMaxSize_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/TrainedModelExportsMaxSize)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/TrainedModelExportsMaxSize)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/TrainedModelExportsMaxSize)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
