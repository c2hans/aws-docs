---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_Dataset.html
---

# Dataset
<a name="API_Dataset"></a>

Defines where the training dataset is located, what type of data it contains, and how to access the data.

## Contents
<a name="API_Dataset_Contents"></a>

 ** inputConfig **   <a name="API-Type-Dataset-inputConfig"></a>
A DatasetInputConfig object that defines the data source and schema mapping.
Type: [DatasetInputConfig](API_DatasetInputConfig.md) object
Required: Yes

 ** type **   <a name="API-Type-Dataset-type"></a>
What type of information is found in the dataset.
Type: String
Valid Values: `INTERACTIONS`
Required: Yes

## See Also
<a name="API_Dataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/Dataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/Dataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/Dataset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
