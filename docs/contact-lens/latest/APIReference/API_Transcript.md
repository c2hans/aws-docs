---
source_url: https://docs.aws.amazon.com/contact-lens/latest/APIReference/API_Transcript.html
---

# Transcript
<a name="API_connect-contact-lens_Transcript"></a>

A list of messages in the session.

## Contents
<a name="API_connect-contact-lens_Transcript_Contents"></a>

 ** BeginOffsetMillis **   <a name="connect-Type-connect-contact-lens_Transcript-BeginOffsetMillis"></a>
The beginning offset in the contact for this transcript.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** Content **   <a name="connect-Type-connect-contact-lens_Transcript-Content"></a>
The content of the transcript.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `.*\S.*`
Required: Yes

 ** EndOffsetMillis **   <a name="connect-Type-connect-contact-lens_Transcript-EndOffsetMillis"></a>
The end offset in the contact for this transcript.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** Id **   <a name="connect-Type-connect-contact-lens_Transcript-Id"></a>
The identifier of the transcript.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** ParticipantId **   <a name="connect-Type-connect-contact-lens_Transcript-ParticipantId"></a>
The identifier of the participant. Valid values are CUSTOMER or AGENT.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** ParticipantRole **   <a name="connect-Type-connect-contact-lens_Transcript-ParticipantRole"></a>
The role of participant. For example, is it a customer, agent, or system.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** Sentiment **   <a name="connect-Type-connect-contact-lens_Transcript-Sentiment"></a>
The sentiment detected for this piece of transcript.
Type: String
Valid Values: `POSITIVE | NEUTRAL | NEGATIVE`
Required: Yes

 ** IssuesDetected **   <a name="connect-Type-connect-contact-lens_Transcript-IssuesDetected"></a>
List of positions where issues were detected on the transcript.
Type: Array of [IssueDetected](API_connect-contact-lens_IssueDetected.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

## See Also
<a name="API_connect-contact-lens_Transcript_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-contact-lens-2020-08-21/Transcript)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-contact-lens-2020-08-21/Transcript)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-contact-lens-2020-08-21/Transcript)
