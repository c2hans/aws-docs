---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_OptOutListInformation.html
---

# OptOutListInformation
<a name="API_OptOutListInformation"></a>

The information for all OptOutList in an AWS account.

## Contents
<a name="API_OptOutListInformation_Contents"></a>

 ** CreatedTimestamp **   <a name="pinpoint-Type-OptOutListInformation-CreatedTimestamp"></a>
The time when the OutOutList was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: Yes

 ** OptOutListArn **   <a name="pinpoint-Type-OptOutListInformation-OptOutListArn"></a>
The Amazon Resource Name (ARN) of the OptOutList.
Type: String
Required: Yes

 ** OptOutListName **   <a name="pinpoint-Type-OptOutListInformation-OptOutListName"></a>
The name of the OptOutList.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

## See Also
<a name="API_OptOutListInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/OptOutListInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/OptOutListInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/OptOutListInformation)
