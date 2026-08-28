---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataLakeDataset.html
---

# DataLakeDataset
<a name="API_DataLakeDataset"></a>

The data lake dataset details.

## Contents
<a name="API_DataLakeDataset_Contents"></a>

 ** arn **   <a name="supplychain-Type-DataLakeDataset-arn"></a>
The arn of the dataset.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1011.
Pattern: `arn:aws:scn(?::([a-z0-9-]+):([0-9]+):instance)?/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})[-_./A-Za-z0-9]*`
Required: Yes

 ** createdTime **   <a name="supplychain-Type-DataLakeDataset-createdTime"></a>
The creation time of the dataset.
Type: Timestamp
Required: Yes

 ** instanceId **   <a name="supplychain-Type-DataLakeDataset-instanceId"></a>
The AWS Supply Chain instance identifier.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** lastModifiedTime **   <a name="supplychain-Type-DataLakeDataset-lastModifiedTime"></a>
The last modified time of the dataset.
Type: Timestamp
Required: Yes

 ** name **   <a name="supplychain-Type-DataLakeDataset-name"></a>
The name of the dataset. For **asc** namespace, the name must be one of the supported data entities under [https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 75.
Pattern: `[a-z0-9_]+`
Required: Yes

 ** namespace **   <a name="supplychain-Type-DataLakeDataset-namespace"></a>
The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:
+  **asc** - For information on the AWS Supply Chain supported datasets see [https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html).
+  **default** - For datasets with custom user-defined schemas.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-z0-9_]+`
Required: Yes

 ** schema **   <a name="supplychain-Type-DataLakeDataset-schema"></a>
The schema of the dataset.
Type: [DataLakeDatasetSchema](API_DataLakeDatasetSchema.md) object
Required: Yes

 ** description **   <a name="supplychain-Type-DataLakeDataset-description"></a>
The description of the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** partitionSpec **   <a name="supplychain-Type-DataLakeDataset-partitionSpec"></a>
The partition specification for a dataset.
Type: [DataLakeDatasetPartitionSpec](API_DataLakeDatasetPartitionSpec.md) object
Required: No

## See Also
<a name="API_DataLakeDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataLakeDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataLakeDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataLakeDataset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Supply Chain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-supply-chain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
