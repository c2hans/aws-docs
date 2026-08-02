---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-reference.html
---

# API Reference guide for Autopilot
<a name="autopilot-reference"></a>

This section provides a subset of the HTTP service REST APIs for creating and managing Amazon SageMaker Autopilot resources (AutoML jobs) programmatically.

If your language of choice is Python, you can refer to [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html) or the [AutoMLV2 object](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html) of the Amazon SageMaker Python SDK directly.

## AutoML API Actions
<a name="autopilot-api-actions"></a>

This list details the operations available in the Reference API to manage AutoML jobs programmatically.
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJob.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJob.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListAutoMLJobs.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListAutoMLJobs.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListCandidatesForAutoMLJob.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListCandidatesForAutoMLJob.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopAutoMLJob.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopAutoMLJob.html)

**Note**
[CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html) and [DescribeAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html) are new versions of [CreateAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html) and [DescribeAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJob.html) which offer backward compatibility.
We recommend using the `CreateAutoMLJobV2`. `CreateAutoMLJobV2` can manage tabular problem types identical to those of its previous version `CreateAutoMLJob`, as well as non-tabular problem types such as image or text classification, or time-series forecasting.
Find guidelines about how to migrate a `CreateAutoMLJob` to `CreateAutoMLJobV2` in [Migrate a CreateAutoMLJob to CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development-create-experiment.html#autopilot-create-experiment-api-migrate-v1-v2).

## AutoML API Data Types
<a name="autopilot-api-data-types"></a>

This list details the API AutoML objects used by the actions above as inbound requests or outbound responses.
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLCandidate.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLCandidate.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLCandidateGenerationConfig.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLCandidateGenerationConfig.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLCandidateStep.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLCandidateStep.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLChannel.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLChannel.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLContainerDefinition.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLContainerDefinition.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLDataSource.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLDataSource.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLDataSplitConfig.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLDataSplitConfig.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLInferenceContainerDefinitions.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLInferenceContainerDefinitions.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobArtifacts.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobArtifacts.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobChannel.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobChannel.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobCompletionCriteria.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobCompletionCriteria.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobInputDataConfig.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobInputDataConfig.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobConfig.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobConfig.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobObjective.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobObjective.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobStepMetadata.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobStepMetadata.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobSummary.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobSummary.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLOutputDataConfig.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLOutputDataConfig.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLProblemTypeConfig.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLProblemTypeConfig.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobCompletionCriteria.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobCompletionCriteria.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobSummary.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobSummary.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLOutputDataConfig.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLOutputDataConfig.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLPartialFailureReason.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLPartialFailureReason.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLProblemTypeConfig.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLProblemTypeConfig.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLProblemTypeResolvedAttributes.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLProblemTypeResolvedAttributes.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLResolvedAttributes.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLResolvedAttributes.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLSecurityConfig.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLSecurityConfig.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLS3DataSource.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLS3DataSource.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CandidateArtifactLocations.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CandidateArtifactLocations.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CandidateGenerationConfig.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CandidateGenerationConfig.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CandidateProperties.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CandidateProperties.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FinalAutoMLJobObjectiveMetric.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FinalAutoMLJobObjectiveMetric.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HolidayConfigAttributes.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HolidayConfigAttributes.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ImageClassificationJobConfig.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ImageClassificationJobConfig.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricDatum.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricDatum.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelDeployConfig.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelDeployConfig.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelDeployResult.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelDeployResult.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResolvedAttributes.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResolvedAttributes.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularResolvedAttributes.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularResolvedAttributes.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TextGenerationJobConfig.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TextGenerationJobConfig.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TextGenerationResolvedAttribute.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TextGenerationResolvedAttribute.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TimeSeriesConfig.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TimeSeriesConfig.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TimeSeriesForecastingJobConfig.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TimeSeriesForecastingJobConfig.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TimeSeriesTransformations.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TimeSeriesTransformations.html)
+ [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TuningJobCompletionCriteria.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TuningJobCompletionCriteria.html)
