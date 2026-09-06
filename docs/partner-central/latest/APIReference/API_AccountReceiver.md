---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AccountReceiver.html
---

# AccountReceiver
<a name="API_AccountReceiver"></a>

Contains the account details of the partner who received the Engagement Invitation, including the AWS account ID and company name.

## Contents
<a name="API_AccountReceiver_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AwsAccountId **   <a name="AWSPartnerCentral-Type-AccountReceiver-AwsAccountId"></a>
Indicates the AWS account ID of the partner who received the Engagement Invitation. This is a unique identifier for managing engagements with specific AWS accounts.
Type: String
Pattern: `([0-9]{12}|\w{1,12})`
Required: Yes

 ** Alias **   <a name="AWSPartnerCentral-Type-AccountReceiver-Alias"></a>
Represents the alias of the partner account receiving the Engagement Invitation, making it easier to identify and track the recipient in reports or logs.
Type: String
Pattern: `(?s).{0,80}`
Required: No

## See Also
<a name="API_AccountReceiver_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AccountReceiver)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AccountReceiver)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AccountReceiver)
