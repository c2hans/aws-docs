---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_JobDetails.html
---

# JobDetails
<a name="API_JobDetails"></a>

Contains details about the policy generation request.

## Contents
<a name="API_JobDetails_Contents"></a>

 ** jobId **   <a name="accessanalyzer-Type-JobDetails-jobId"></a>
The `JobId` that is returned by the `StartPolicyGeneration` operation. The `JobId` can be used with `GetGeneratedPolicy` to retrieve the generated policies or used with `CancelPolicyGeneration` to cancel the policy generation request.
Type: String
Required: Yes

 ** startedOn **   <a name="accessanalyzer-Type-JobDetails-startedOn"></a>
A timestamp of when the job was started.
Type: Timestamp
Required: Yes

 ** status **   <a name="accessanalyzer-Type-JobDetails-status"></a>
The status of the job request.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED | CANCELED`
Required: Yes

 ** completedOn **   <a name="accessanalyzer-Type-JobDetails-completedOn"></a>
A timestamp of when the job was completed.
Type: Timestamp
Required: No

 ** jobError **   <a name="accessanalyzer-Type-JobDetails-jobError"></a>
The job error for the policy generation request.
Type: [JobError](API_JobError.md) object
Required: No

## See Also
<a name="API_JobDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/JobDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/JobDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/JobDetails)
