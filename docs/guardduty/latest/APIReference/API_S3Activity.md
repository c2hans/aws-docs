---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_S3Activity.html
---

# S3Activity
<a name="API_S3Activity"></a>

Contains details about Amazon S3 activity.

## Contents
<a name="API_S3Activity_Contents"></a>

 ** activityWindow **   <a name="guardduty-Type-S3Activity-activityWindow"></a>
The time range of the activity.
Type: [ActivityWindow](API_ActivityWindow.md) object
Required: No

 ** actor **   <a name="guardduty-Type-S3Activity-actor"></a>
The identity that performed the activity.
Type: [InvestigationActor](API_InvestigationActor.md) object
Required: No

 ** affectedBucket **   <a name="guardduty-Type-S3Activity-affectedBucket"></a>
The name of the affected bucket, or `account-wide` if the activity isn't limited to one bucket.
Type: String
Required: No

 ** api **   <a name="guardduty-Type-S3Activity-api"></a>
The Amazon S3 API operation that was called.
Type: String
Required: No

 ** enrichment **   <a name="guardduty-Type-S3Activity-enrichment"></a>
Additional context about the activity, such as geolocation information.
Type: [Enrichment](API_Enrichment.md) object
Required: No

 ** eventCount **   <a name="guardduty-Type-S3Activity-eventCount"></a>
The number of events.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** nonS3Activity **   <a name="guardduty-Type-S3Activity-nonS3Activity"></a>
Related activity on AWS services other than Amazon S3.
Type: String
Required: No

 ** otherS3Activity **   <a name="guardduty-Type-S3Activity-otherS3Activity"></a>
Other Amazon S3 activity that is related to the observation.
Type: String
Required: No

 ** sessionAssessment **   <a name="guardduty-Type-S3Activity-sessionAssessment"></a>
An assessment of the session in which the activity occurred.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** sourceIp **   <a name="guardduty-Type-S3Activity-sourceIp"></a>
The source address of the activity, or a description of the source.
Type: String
Required: No

## See Also
<a name="API_S3Activity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/S3Activity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/S3Activity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/S3Activity)
