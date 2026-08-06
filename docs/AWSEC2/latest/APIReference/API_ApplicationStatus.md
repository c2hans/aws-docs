---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ApplicationStatus.html
---

# ApplicationStatus
<a name="API_ApplicationStatus"></a>

Describes the application-level health status for an instance.

## Contents
<a name="API_ApplicationStatus_Contents"></a>

 ** DetailSet.N **
Details about the application status checks for the instance.
Type: Array of [ApplicationStatusDetail](API_ApplicationStatusDetail.md) objects
Required: No

 ** resumeAt **
The date and time when application status reporting resumes after suppression.
Type: Timestamp
Required: No

 ** status **
The current instance-level application status. This status is derived from the aggregated results of all application status checks with the aggregation setting set to `included`. Checks with aggregation set to `excluded` do not affect this value. When suppression is active on the instance, this status is not updated.
Type: String
Valid Values: `ok | impaired | initializing | insufficient-data | not-applicable | suppressed`
Required: No

 ** statusSince **
The date and time when the current status started.
Type: Timestamp
Required: No

 ** statusTimeStamp **
The date and time of the last status update.
Type: Timestamp
Required: No

## See Also
<a name="API_ApplicationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ApplicationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ApplicationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ApplicationStatus)
