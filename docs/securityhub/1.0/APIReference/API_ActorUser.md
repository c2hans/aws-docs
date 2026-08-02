---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ActorUser.html
---

# ActorUser
<a name="API_ActorUser"></a>

 Contains information about the credentials used by the threat actor identified in an Amazon GuardDuty Extended Threat Detection attack sequence. GuardDuty generates an attack sequence finding when multiple events align to a potentially suspicious activity. To receive GuardDuty attack sequence findings in AWS Security Hub CSPM, you must have GuardDuty enabled. For more information, see [GuardDuty Extended Threat Detection ](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-extended-threat-detection.html) in the *Amazon GuardDuty User Guide*.

## Contents
<a name="API_ActorUser_Contents"></a>

 ** Account **   <a name="securityhub-Type-ActorUser-Account"></a>
 The account of the threat actor.
Type: [UserAccount](API_UserAccount.md) object
Required: No

 ** CredentialUid **   <a name="securityhub-Type-ActorUser-CredentialUid"></a>
 Unique identifier of the threat actor’s user credentials.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-ActorUser-Name"></a>
 The name of the threat actor.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-ActorUser-Type"></a>
 The type of user.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Uid **   <a name="securityhub-Type-ActorUser-Uid"></a>
 The unique identifier of the threat actor.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ActorUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ActorUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ActorUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ActorUser)
