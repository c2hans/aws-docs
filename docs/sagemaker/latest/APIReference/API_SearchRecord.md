---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SearchRecord.html
---

# SearchRecord
<a name="API_SearchRecord"></a>

A single resource returned as part of the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API response.

## Contents
<a name="API_SearchRecord_Contents"></a>

 ** Endpoint **   <a name="sagemaker-Type-SearchRecord-Endpoint"></a>
A hosted endpoint for real-time inference.
Type: [Endpoint](API_Endpoint.md) object
Required: No

 ** Experiment **   <a name="sagemaker-Type-SearchRecord-Experiment"></a>
The properties of an experiment.
Type: [Experiment](API_Experiment.md) object
Required: No

 ** FeatureGroup **   <a name="sagemaker-Type-SearchRecord-FeatureGroup"></a>
Amazon SageMaker Feature Store stores features in a collection called Feature Group. A Feature Group can be visualized as a table which has rows, with a unique identifier for each row where each column in the table is a feature. In principle, a Feature Group is composed of features and values per features.
Type: [FeatureGroup](API_FeatureGroup.md) object
Required: No

 ** FeatureMetadata **   <a name="sagemaker-Type-SearchRecord-FeatureMetadata"></a>
The feature metadata used to search through the features.
Type: [FeatureMetadata](API_FeatureMetadata.md) object
Required: No

 ** HyperParameterTuningJob **   <a name="sagemaker-Type-SearchRecord-HyperParameterTuningJob"></a>
The properties of a hyperparameter tuning job.
Type: [HyperParameterTuningJobSearchEntity](API_HyperParameterTuningJobSearchEntity.md) object
Required: No

 ** Job **   <a name="sagemaker-Type-SearchRecord-Job"></a>
The properties of a job.
Type: [Job](API_Job.md) object
Required: No

 ** Model **   <a name="sagemaker-Type-SearchRecord-Model"></a>
A model displayed in the Amazon SageMaker Model Dashboard.
Type: [ModelDashboardModel](API_ModelDashboardModel.md) object
Required: No

 ** ModelCard **   <a name="sagemaker-Type-SearchRecord-ModelCard"></a>
An Amazon SageMaker Model Card that documents details about a machine learning model.
Type: [ModelCard](API_ModelCard.md) object
Required: No

 ** ModelPackage **   <a name="sagemaker-Type-SearchRecord-ModelPackage"></a>
A container for your trained model that can be deployed for SageMaker inference. This can include inference code, artifacts, and metadata. The model package type can be one of the following.
+ Versioned model: A part of a model package group in Model Registry.
+ Unversioned model: Not part of a model package group and used in AWS Marketplace.
For more information, see [`CreateModelPackage`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelPackage.html).
Type: [ModelPackage](API_ModelPackage.md) object
Required: No

 ** ModelPackageGroup **   <a name="sagemaker-Type-SearchRecord-ModelPackageGroup"></a>
A group of versioned models in the Model Registry.
Type: [ModelPackageGroup](API_ModelPackageGroup.md) object
Required: No

 ** Pipeline **   <a name="sagemaker-Type-SearchRecord-Pipeline"></a>
A SageMaker Model Building Pipeline instance.
Type: [Pipeline](API_Pipeline.md) object
Required: No

 ** PipelineExecution **   <a name="sagemaker-Type-SearchRecord-PipelineExecution"></a>
An execution of a pipeline.
Type: [PipelineExecution](API_PipelineExecution.md) object
Required: No

 ** PipelineVersion **   <a name="sagemaker-Type-SearchRecord-PipelineVersion"></a>
The version of the pipeline.
Type: [PipelineVersion](API_PipelineVersion.md) object
Required: No

 ** Project **   <a name="sagemaker-Type-SearchRecord-Project"></a>
The properties of a project.
Type: [Project](API_Project.md) object
Required: No

 ** TrainingJob **   <a name="sagemaker-Type-SearchRecord-TrainingJob"></a>
The properties of a training job.
Type: [TrainingJob](API_TrainingJob.md) object
Required: No

 ** Trial **   <a name="sagemaker-Type-SearchRecord-Trial"></a>
The properties of a trial.
Type: [Trial](API_Trial.md) object
Required: No

 ** TrialComponent **   <a name="sagemaker-Type-SearchRecord-TrialComponent"></a>
The properties of a trial component.
Type: [TrialComponent](API_TrialComponent.md) object
Required: No

## See Also
<a name="API_SearchRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/SearchRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/SearchRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/SearchRecord)
