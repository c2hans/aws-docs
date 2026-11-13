---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_S3Analysis.html
---

# S3Analysis
<a name="API_S3Analysis"></a>

Contains an analysis of Amazon S3 activity or exposure. The members that can be set depend on `AnalysisType`: `S3_EXPOSURE` (`FindingSubtype`, `EffectivePermission`, `BlockPublicAccessSettings`, and `Exposure`), `S3_ACTOR_CONTEXT` (`UserAgent`, `UserAgentClassification`, `SourceIp`, `IpReputation`, and `ActorAssessment`), and `S3_PEN_TEST` (`UserAgent`, `S3ApiActivity`, `SourceContext`, and `AuthorizationAssessment`).

## Contents
<a name="API_S3Analysis_Contents"></a>

 ** actorAssessment **   <a name="guardduty-Type-S3Analysis-actorAssessment"></a>
An assessment of the identity that performed the activity.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** authorizationAssessment **   <a name="guardduty-Type-S3Analysis-authorizationAssessment"></a>
An assessment of whether the activity was authorized.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** blockPublicAccessSettings **   <a name="guardduty-Type-S3Analysis-blockPublicAccessSettings"></a>
A description of the Amazon S3 Block Public Access settings.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** effectivePermission **   <a name="guardduty-Type-S3Analysis-effectivePermission"></a>
The effective permission of the Amazon S3 resource.
Type: String
Required: No

 ** exposure **   <a name="guardduty-Type-S3Analysis-exposure"></a>
An assessment of the exposure of the Amazon S3 resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** findingSubtype **   <a name="guardduty-Type-S3Analysis-findingSubtype"></a>
The subtype of the finding.
Type: String
Required: No

 ** ipReputation **   <a name="guardduty-Type-S3Analysis-ipReputation"></a>
The reputation of the source IP address.
Type: String
Required: No

 ** s3ApiActivity **   <a name="guardduty-Type-S3Analysis-s3ApiActivity"></a>
A description of the Amazon S3 API activity.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** sourceContext **   <a name="guardduty-Type-S3Analysis-sourceContext"></a>
Context about the source of the activity.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** sourceIp **   <a name="guardduty-Type-S3Analysis-sourceIp"></a>
The source address of the activity, or a description of the source.
Type: String
Required: No

 ** userAgent **   <a name="guardduty-Type-S3Analysis-userAgent"></a>
The user agent of the caller.
Type: String
Required: No

 ** userAgentClassification **   <a name="guardduty-Type-S3Analysis-userAgentClassification"></a>
The classification of the user agent.
Type: String
Required: No

## See Also
<a name="API_S3Analysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/S3Analysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/S3Analysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/S3Analysis)
