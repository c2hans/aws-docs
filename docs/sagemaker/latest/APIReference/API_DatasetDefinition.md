---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DatasetDefinition.html
---

# DatasetDefinition
<a name="API_DatasetDefinition"></a>

Configuration for Dataset Definition inputs. The Dataset Definition input must specify exactly one of either `AthenaDatasetDefinition` or `RedshiftDatasetDefinition` types.

## Contents
<a name="API_DatasetDefinition_Contents"></a>

 ** AthenaDatasetDefinition **   <a name="sagemaker-Type-DatasetDefinition-AthenaDatasetDefinition"></a>
Configuration for Athena Dataset Definition input.
Type: [AthenaDatasetDefinition](API_AthenaDatasetDefinition.md) object
Required: No

 ** DataDistributionType **   <a name="sagemaker-Type-DatasetDefinition-DataDistributionType"></a>
Whether the generated dataset is `FullyReplicated` or `ShardedByS3Key` (default).
Type: String
Valid Values: `FullyReplicated | ShardedByS3Key`
Required: No

 ** InputMode **   <a name="sagemaker-Type-DatasetDefinition-InputMode"></a>
Whether to use `File` or `Pipe` input mode. In `File` (default) mode, Amazon SageMaker copies the data from the input source onto the local Amazon Elastic Block Store (Amazon EBS) volumes before starting your training algorithm. This is the most commonly used input mode. In `Pipe` mode, Amazon SageMaker streams input data from the source directly to your algorithm without using the EBS volume.
Type: String
Valid Values: `Pipe | File`
Required: No

 ** LocalPath **   <a name="sagemaker-Type-DatasetDefinition-LocalPath"></a>
The local path where you want Amazon SageMaker to download the Dataset Definition inputs to run a processing job. `LocalPath` is an absolute path to the input data. This is a required parameter when `AppManaged` is `False` (default).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** RedshiftDatasetDefinition **   <a name="sagemaker-Type-DatasetDefinition-RedshiftDatasetDefinition"></a>
Configuration for Redshift Dataset Definition input.
Type: [RedshiftDatasetDefinition](API_RedshiftDatasetDefinition.md) object
Required: No

## See Also
<a name="API_DatasetDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DatasetDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DatasetDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DatasetDefinition)
