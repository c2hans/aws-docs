---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_TrainedModelInferenceJobSummary.html
---

# TrainedModelInferenceJobSummary
<a name="API_TrainedModelInferenceJobSummary"></a>

Provides information about the trained model inference job.

## Contents
<a name="API_TrainedModelInferenceJobSummary_Contents"></a>

 ** collaborationIdentifier **   <a name="API-Type-TrainedModelInferenceJobSummary-collaborationIdentifier"></a>
The collaboration ID of the collaboration that contains the trained model inference job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-TrainedModelInferenceJobSummary-createTime"></a>
The time at which the trained model inference job was created.
Type: Timestamp
Required: Yes

 ** membershipIdentifier **   <a name="API-Type-TrainedModelInferenceJobSummary-membershipIdentifier"></a>
The membership ID of the membership that contains the trained model inference job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-TrainedModelInferenceJobSummary-name"></a>
The name of the trained model inference job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** outputConfiguration **   <a name="API-Type-TrainedModelInferenceJobSummary-outputConfiguration"></a>
The output configuration information of the trained model job.
Type: [InferenceOutputConfiguration](API_InferenceOutputConfiguration.md) object
Required: Yes

 ** status **   <a name="API-Type-TrainedModelInferenceJobSummary-status"></a>
The status of the trained model inference job.
Type: String
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | CANCEL_PENDING | CANCEL_IN_PROGRESS | CANCEL_FAILED | INACTIVE`
Required: Yes

 ** trainedModelArn **   <a name="API-Type-TrainedModelInferenceJobSummary-trainedModelArn"></a>
The Amazon Resource Name (ARN) of the trained model that is used for the trained model inference job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** trainedModelInferenceJobArn **   <a name="API-Type-TrainedModelInferenceJobSummary-trainedModelInferenceJobArn"></a>
The Amazon Resource Name (ARN) of the trained model inference job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model-inference-job/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** updateTime **   <a name="API-Type-TrainedModelInferenceJobSummary-updateTime"></a>
The most recent time at which the trained model inference job was updated.
Type: Timestamp
Required: Yes

 ** configuredModelAlgorithmAssociationArn **   <a name="API-Type-TrainedModelInferenceJobSummary-configuredModelAlgorithmAssociationArn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm association that is used for the trained model inference job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/configured-model-algorithm-association/[-a-zA-Z0-9_/.]+`
Required: No

 ** description **   <a name="API-Type-TrainedModelInferenceJobSummary-description"></a>
The description of the trained model inference job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** logsStatus **   <a name="API-Type-TrainedModelInferenceJobSummary-logsStatus"></a>
The log status of the trained model inference job.
Type: String
Valid Values: `PUBLISH_SUCCEEDED | PUBLISH_FAILED`
Required: No

 ** logsStatusDetails **   <a name="API-Type-TrainedModelInferenceJobSummary-logsStatusDetails"></a>
Details about the log status for the trained model inference job.
Type: String
Required: No

 ** metricsStatus **   <a name="API-Type-TrainedModelInferenceJobSummary-metricsStatus"></a>
The metric status of the trained model inference job.
Type: String
Valid Values: `PUBLISH_SUCCEEDED | PUBLISH_FAILED`
Required: No

 ** metricsStatusDetails **   <a name="API-Type-TrainedModelInferenceJobSummary-metricsStatusDetails"></a>
Details about the metrics status for the trained model inference job.
Type: String
Required: No

 ** mlModelInferencePayerAccountId **   <a name="API-Type-TrainedModelInferenceJobSummary-mlModelInferencePayerAccountId"></a>
The account ID of the member that is responsible for paying for model inference costs.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** trainedModelVersionIdentifier **   <a name="API-Type-TrainedModelInferenceJobSummary-trainedModelVersionIdentifier"></a>
The version identifier of the trained model that was used for inference in this job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## See Also
<a name="API_TrainedModelInferenceJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/TrainedModelInferenceJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/TrainedModelInferenceJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/TrainedModelInferenceJobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
