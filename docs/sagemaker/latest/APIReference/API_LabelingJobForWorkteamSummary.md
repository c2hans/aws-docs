---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LabelingJobForWorkteamSummary.html
---

# LabelingJobForWorkteamSummary
<a name="API_LabelingJobForWorkteamSummary"></a>

Provides summary information for a work team.

## Contents
<a name="API_LabelingJobForWorkteamSummary_Contents"></a>

 ** JobReferenceCode **   <a name="sagemaker-Type-LabelingJobForWorkteamSummary-JobReferenceCode"></a>
A unique identifier for a labeling job. You can use this to refer to a specific labeling job.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `.+`
Required: Yes

 ** WorkRequesterAccountId **   <a name="sagemaker-Type-LabelingJobForWorkteamSummary-WorkRequesterAccountId"></a>
The AWS account ID of the account used to start the labeling job.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** LabelCounters **   <a name="sagemaker-Type-LabelingJobForWorkteamSummary-LabelCounters"></a>
Provides information about the progress of a labeling job.
Type: [LabelCountersForWorkteam](API_LabelCountersForWorkteam.md) object
Required: No

 ** LabelingJobName **   <a name="sagemaker-Type-LabelingJobForWorkteamSummary-LabelingJobName"></a>
The name of the labeling job that the work team is assigned to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** NumberOfHumanWorkersPerDataObject **   <a name="sagemaker-Type-LabelingJobForWorkteamSummary-NumberOfHumanWorkersPerDataObject"></a>
The configured number of workers per data object.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 9.
Required: No

## See Also
<a name="API_LabelingJobForWorkteamSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/LabelingJobForWorkteamSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/LabelingJobForWorkteamSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/LabelingJobForWorkteamSummary)
