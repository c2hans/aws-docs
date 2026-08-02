---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ContactTargetInfo.html
---

# ContactTargetInfo
<a name="API_SSMContacts_ContactTargetInfo"></a>

The contact that Incident Manager is engaging during an incident.

## Contents
<a name="API_SSMContacts_ContactTargetInfo_Contents"></a>

 ** IsEssential **   <a name="IncidentManager-Type-SSMContacts_ContactTargetInfo-IsEssential"></a>
A Boolean value determining if the contact's acknowledgement stops the progress of stages in the plan.
Type: Boolean
Required: Yes

 ** ContactId **   <a name="IncidentManager-Type-SSMContacts_ContactTargetInfo-ContactId"></a>
The Amazon Resource Name (ARN) of the contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: No

## See Also
<a name="API_SSMContacts_ContactTargetInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/ContactTargetInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/ContactTargetInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/ContactTargetInfo)
