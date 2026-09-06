---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CloudTrailProperties.html
---

# CloudTrailProperties
<a name="API_CloudTrailProperties"></a>

Contains information about CloudTrail access.

## Contents
<a name="API_CloudTrailProperties_Contents"></a>

 ** endTime **   <a name="accessanalyzer-Type-CloudTrailProperties-endTime"></a>
The end of the time range for which IAM Access Analyzer reviews your CloudTrail events. Events with a timestamp after this time are not considered to generate a policy. If this is not included in the request, the default value is the current time.
Type: Timestamp
Required: Yes

 ** startTime **   <a name="accessanalyzer-Type-CloudTrailProperties-startTime"></a>
The start of the time range for which IAM Access Analyzer reviews your CloudTrail events. Events with a timestamp before this time are not considered to generate a policy.
Type: Timestamp
Required: Yes

 ** trailProperties **   <a name="accessanalyzer-Type-CloudTrailProperties-trailProperties"></a>
A `TrailProperties` object that contains settings for trail properties.
Type: Array of [TrailProperties](API_TrailProperties.md) objects
Required: Yes

## See Also
<a name="API_CloudTrailProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/CloudTrailProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/CloudTrailProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/CloudTrailProperties)
