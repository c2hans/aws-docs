---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelPackageContainerDefinition.html
---

# ModelPackageContainerDefinition
<a name="API_ModelPackageContainerDefinition"></a>

Describes the Docker container for the model package.

## Contents
<a name="API_ModelPackageContainerDefinition_Contents"></a>

 ** AdditionalModelDataSources **   <a name="sagemaker-Type-ModelPackageContainerDefinition-AdditionalModelDataSources"></a>
Data sources that are available to your model in addition to the one that you specify for `ModelDataSource` when you use the `CreateModelPackage` action.
Type: Array of [AdditionalModelDataSource](API_AdditionalModelDataSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** AdditionalS3DataSource **   <a name="sagemaker-Type-ModelPackageContainerDefinition-AdditionalS3DataSource"></a>
The additional data source that is used during inference in the Docker container for your model package.
Type: [AdditionalS3DataSource](API_AdditionalS3DataSource.md) object
Required: No

 ** BaseModel **   <a name="sagemaker-Type-ModelPackageContainerDefinition-BaseModel"></a>
 Identifies the foundation model that was used as the starting point for model customization.
Type: [BaseModel](API_BaseModel.md) object
Required: No

 ** ContainerHostname **   <a name="sagemaker-Type-ModelPackageContainerDefinition-ContainerHostname"></a>
The DNS host name for the Docker container.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** Environment **   <a name="sagemaker-Type-ModelPackageContainerDefinition-Environment"></a>
The environment variables to set in the Docker container. Each key and value in the `Environment` string to string map can have length of up to 1024. We support up to 16 entries in the map.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Value Pattern: `[\S\s]*`
Required: No

 ** Framework **   <a name="sagemaker-Type-ModelPackageContainerDefinition-Framework"></a>
The machine learning framework of the model package container image.
Type: String
Required: No

 ** FrameworkVersion **   <a name="sagemaker-Type-ModelPackageContainerDefinition-FrameworkVersion"></a>
The framework version of the Model Package Container Image.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 10.
Pattern: `[0-9]\.[A-Za-z0-9.-]+`
Required: No

 ** Image **   <a name="sagemaker-Type-ModelPackageContainerDefinition-Image"></a>
The Amazon Elastic Container Registry (Amazon ECR) path where inference code is stored.
If you are using your own custom algorithm instead of an algorithm provided by SageMaker, the inference code must meet SageMaker requirements. SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\S]+`
Required: No

 ** ImageDigest **   <a name="sagemaker-Type-ModelPackageContainerDefinition-ImageDigest"></a>
An MD5 hash of the training algorithm that identifies the Docker image used for training.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 72.
Pattern: `[Ss][Hh][Aa]256:[0-9a-fA-F]{64}`
Required: No

 ** IsCheckpoint **   <a name="sagemaker-Type-ModelPackageContainerDefinition-IsCheckpoint"></a>
 Specifies whether the model data is a training checkpoint.
Type: Boolean
Required: No

 ** ModelDataETag **   <a name="sagemaker-Type-ModelPackageContainerDefinition-ModelDataETag"></a>
The ETag associated with Model Data URL.
Type: String
Required: No

 ** ModelDataSource **   <a name="sagemaker-Type-ModelPackageContainerDefinition-ModelDataSource"></a>
Specifies the location of ML model data to deploy during endpoint creation.
Type: [ModelDataSource](API_ModelDataSource.md) object
Required: No

 ** ModelDataUrl **   <a name="sagemaker-Type-ModelPackageContainerDefinition-ModelDataUrl"></a>
The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single `gzip` compressed tar archive (`.tar.gz` suffix).
The model artifacts must be in an S3 bucket that is in the same region as the model package.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

 ** ModelInput **   <a name="sagemaker-Type-ModelPackageContainerDefinition-ModelInput"></a>
A structure with Model Input details.
Type: [ModelInput](API_ModelInput.md) object
Required: No

 ** NearestModelName **   <a name="sagemaker-Type-ModelPackageContainerDefinition-NearestModelName"></a>
The name of a pre-trained machine learning benchmarked by Amazon SageMaker Inference Recommender model that matches your model. You can find a list of benchmarked models by calling `ListModelMetadata`.
Type: String
Required: No

 ** ProductId **   <a name="sagemaker-Type-ModelPackageContainerDefinition-ProductId"></a>
The AWS Marketplace product ID of the model package.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

## See Also
<a name="API_ModelPackageContainerDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelPackageContainerDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelPackageContainerDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelPackageContainerDefinition)
