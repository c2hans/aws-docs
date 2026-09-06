---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CloudTrailDetails.html
---

# CloudTrailDetails
<a name="API_CloudTrailDetails"></a>

Contains information about CloudTrail access.

## Contents
<a name="API_CloudTrailDetails_Contents"></a>

 ** accessRole **   <a name="accessanalyzer-Type-CloudTrailDetails-accessRole"></a>
The ARN of the service role that IAM Access Analyzer uses to access your CloudTrail trail and service last accessed information.
Type: String
Pattern: `arn:[^:]*:iam::[^:]*:role/.{1,576}`
Required: Yes

 ** startTime **   <a name="accessanalyzer-Type-CloudTrailDetails-startTime"></a>
The start of the time range for which IAM Access Analyzer reviews your CloudTrail events. Events with a timestamp before this time are not considered to generate a policy.
Type: Timestamp
Required: Yes

 ** trails **   <a name="accessanalyzer-Type-CloudTrailDetails-trails"></a>
A `Trail` object that contains settings for a trail.
Type: Array of [Trail](API_Trail.md) objects
Required: Yes

 ** endTime **   <a name="accessanalyzer-Type-CloudTrailDetails-endTime"></a>
The end of the time range for which IAM Access Analyzer reviews your CloudTrail events. Events with a timestamp after this time are not considered to generate a policy. If this is not included in the request, the default value is the current time.
Type: Timestamp
Required: No

## See Also
<a name="API_CloudTrailDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/CloudTrailDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/CloudTrailDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/CloudTrailDetails)
