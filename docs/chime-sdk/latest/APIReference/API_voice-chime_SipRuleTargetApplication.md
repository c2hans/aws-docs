---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SipRuleTargetApplication.html
---

# SipRuleTargetApplication
<a name="API_voice-chime_SipRuleTargetApplication"></a>

A target SIP media application and other details, such as priority and AWS Region, to be specified in the SIP rule. Only one SIP rule per AWS Region can be provided.

## Contents
<a name="API_voice-chime_SipRuleTargetApplication_Contents"></a>

 ** AwsRegion **   <a name="chimesdk-Type-voice-chime_SipRuleTargetApplication-AwsRegion"></a>
The AWS Region of a rule's target SIP media application.
Type: String
Required: No

 ** Priority **   <a name="chimesdk-Type-voice-chime_SipRuleTargetApplication-Priority"></a>
The priority setting of a rule's target SIP media application.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** SipMediaApplicationId **   <a name="chimesdk-Type-voice-chime_SipRuleTargetApplication-SipMediaApplicationId"></a>
The ID of a rule's target SIP media application.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_voice-chime_SipRuleTargetApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/SipRuleTargetApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/SipRuleTargetApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/SipRuleTargetApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
