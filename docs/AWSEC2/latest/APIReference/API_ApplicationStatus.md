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
The current instance-level application status. This status is derived from application status checks with `Aggregation` set to `included`. Possible values:
+  `ok` – All included checks passed.
+  `impaired` – At least one included check failed.
+  `initializing` – At least one included check is initializing, and no included check is impaired.
+  `insufficient-data` – At least one included check has insufficient data, and no included check is impaired or initializing.
+  `not-applicable` – No checks with `Aggregation` set to `included` apply to the instance.
+  `suppressed` – Application status reporting is suppressed for the instance.
Checks with `Aggregation` set to `excluded` do not affect this value.
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
