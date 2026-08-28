---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_OptedOutNumberInformation.html
---

# OptedOutNumberInformation
<a name="API_OptedOutNumberInformation"></a>

The information for an opted out number in an AWS account.

## Contents
<a name="API_OptedOutNumberInformation_Contents"></a>

 ** EndUserOptedOut **   <a name="pinpoint-Type-OptedOutNumberInformation-EndUserOptedOut"></a>
This is set to true if it was the end recipient that opted out.
Type: Boolean
Required: Yes

 ** OptedOutNumber **   <a name="pinpoint-Type-OptedOutNumberInformation-OptedOutNumber"></a>
The phone number that is opted out.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`
Required: Yes

 ** OptedOutTimestamp **   <a name="pinpoint-Type-OptedOutNumberInformation-OptedOutTimestamp"></a>
The time that the op tout occurred, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: Yes

## See Also
<a name="API_OptedOutNumberInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/OptedOutNumberInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/OptedOutNumberInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/OptedOutNumberInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
