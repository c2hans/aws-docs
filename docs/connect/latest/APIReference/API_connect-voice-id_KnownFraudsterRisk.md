---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-voice-id_KnownFraudsterRisk.html
---

# KnownFraudsterRisk
<a name="API_connect-voice-id_KnownFraudsterRisk"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Contains details produced as a result of performing known fraudster risk analysis on a speaker.

## Contents
<a name="API_connect-voice-id_KnownFraudsterRisk_Contents"></a>

 ** RiskScore **   <a name="connect-Type-connect-voice-id_KnownFraudsterRisk-RiskScore"></a>
The score indicating the likelihood the speaker is a known fraudster.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: Yes

 ** GeneratedFraudsterId **   <a name="connect-Type-connect-voice-id_KnownFraudsterRisk-GeneratedFraudsterId"></a>
The identifier of the fraudster that is the closest match to the speaker. If there are no fraudsters registered in a given domain, or if there are no fraudsters with a non-zero RiskScore, this value is `null`.
Type: String
Length Constraints: Fixed length of 25.
Pattern: `id#[a-zA-Z0-9]{22}`
Required: No

## See Also
<a name="API_connect-voice-id_KnownFraudsterRisk_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/KnownFraudsterRisk)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/KnownFraudsterRisk)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/KnownFraudsterRisk)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
