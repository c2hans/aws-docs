---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ProtectedJob.html
---

# ProtectedJob
<a name="API_ProtectedJob"></a>

The parameters for an AWS Clean Rooms protected job.

## Contents
<a name="API_ProtectedJob_Contents"></a>

 ** createTime **   <a name="API-Type-ProtectedJob-createTime"></a>
 The creation time of the protected job.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-ProtectedJob-id"></a>
The identifier for a protected job instance.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** membershipArn **   <a name="API-Type-ProtectedJob-membershipArn"></a>
The ARN of the membership.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: Yes

 ** membershipId **   <a name="API-Type-ProtectedJob-membershipId"></a>
he identifier for the membership.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** status **   <a name="API-Type-ProtectedJob-status"></a>
 The status of the protected job.
Type: String
Valid Values: `SUBMITTED | STARTED | CANCELLED | CANCELLING | FAILED | SUCCESS`
Required: Yes

 ** computeConfiguration **   <a name="API-Type-ProtectedJob-computeConfiguration"></a>
The compute configuration for the protected job.
Type: [ProtectedJobComputeConfiguration](API_ProtectedJobComputeConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** error **   <a name="API-Type-ProtectedJob-error"></a>
 The error from the protected job.
Type: [ProtectedJobError](API_ProtectedJobError.md) object
Required: No

 ** jobComputePayerAccountId **   <a name="API-Type-ProtectedJob-jobComputePayerAccountId"></a>
The account ID of the member that pays for the job compute costs.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** jobParameters **   <a name="API-Type-ProtectedJob-jobParameters"></a>
 The job parameters for the protected job.
Type: [ProtectedJobParameters](API_ProtectedJobParameters.md) object
Required: No

 ** result **   <a name="API-Type-ProtectedJob-result"></a>
 The result of the protected job.
Type: [ProtectedJobResult](API_ProtectedJobResult.md) object
Required: No

 ** resultConfiguration **   <a name="API-Type-ProtectedJob-resultConfiguration"></a>
Contains any details needed to write the job results.
Type: [ProtectedJobResultConfigurationOutput](API_ProtectedJobResultConfigurationOutput.md) object
Required: No

 ** statistics **   <a name="API-Type-ProtectedJob-statistics"></a>
 The statistics of the protected job.
Type: [ProtectedJobStatistics](API_ProtectedJobStatistics.md) object
Required: No

## See Also
<a name="API_ProtectedJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ProtectedJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ProtectedJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ProtectedJob)
