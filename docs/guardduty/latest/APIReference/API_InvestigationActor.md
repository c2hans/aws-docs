---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InvestigationActor.html
---

# InvestigationActor
<a name="API_InvestigationActor"></a>

Contains information about the identity that performed an activity.

## Contents
<a name="API_InvestigationActor_Contents"></a>

 ** accessKeyId **   <a name="guardduty-Type-InvestigationActor-accessKeyId"></a>
The access key ID that the identity used.
Type: String
Required: No

 ** principalId **   <a name="guardduty-Type-InvestigationActor-principalId"></a>
The ID of the principal.
Type: String
Required: No

 ** userAgent **   <a name="guardduty-Type-InvestigationActor-userAgent"></a>
The user agent that the identity used.
Type: String
Required: No

 ** userName **   <a name="guardduty-Type-InvestigationActor-userName"></a>
The name of the user.
Type: String
Required: No

 ** userType **   <a name="guardduty-Type-InvestigationActor-userType"></a>
The type of the identity, such as `IAMUser`, `AssumedRole`, or `Root`.
Type: String
Required: No

## See Also
<a name="API_InvestigationActor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/InvestigationActor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/InvestigationActor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/InvestigationActor)
