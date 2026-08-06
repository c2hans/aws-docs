---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ApplicationStatusDetail.html
---

# ApplicationStatusDetail
<a name="API_ApplicationStatusDetail"></a>

Describes the details of an application status check for an instance.

## Contents
<a name="API_ApplicationStatusDetail_Contents"></a>

 ** aggregation **
The aggregation setting for the application status check. When set to `included`, the result of this check contributes to the instance-level application status. When set to `excluded`, the check runs independently and does not affect the instance-level status.
Type: String
Valid Values: `included | excluded`
Required: No

 ** applicationStatusCheckId **
The ID of the application status check.
Type: String
Required: No

 ** checkUpdateTime **
The date and time when the check was last updated.
Type: Timestamp
Required: No

 ** reason **
The reason for the current status.
Type: [ApplicationStatusReason](API_ApplicationStatusReason.md) object
Required: No

 ** status **
The status of the individual application status check. This value reflects the actual health check result and is not affected by the aggregation setting or suppression. Only the instance-level `ApplicationStatus$status` is affected by those settings.
Type: String
Valid Values: `passed | failed | initializing | insufficient-data | not-applicable`
Required: No

 ** statusSince **
The date and time when the current status started for this check.
Type: Timestamp
Required: No

 ** statusTimeStamp **
The date and time of the last status update for this check.
Type: Timestamp
Required: No

## See Also
<a name="API_ApplicationStatusDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ApplicationStatusDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ApplicationStatusDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ApplicationStatusDetail)
