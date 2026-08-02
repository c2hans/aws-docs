---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_Receipt.html
---

# Receipt
<a name="API_SSMContacts_Receipt"></a>

Records events during an engagement.

## Contents
<a name="API_SSMContacts_Receipt_Contents"></a>

 ** ReceiptTime **   <a name="IncidentManager-Type-SSMContacts_Receipt-ReceiptTime"></a>
The time receipt was `SENT`, `DELIVERED`, or `READ`.
Type: Timestamp
Required: Yes

 ** ReceiptType **   <a name="IncidentManager-Type-SSMContacts_Receipt-ReceiptType"></a>
The type follows the engagement cycle, `SENT`, `DELIVERED`, and `READ`.
Type: String
Valid Values: `DELIVERED | ERROR | READ | SENT | STOP`
Required: Yes

 ** ContactChannelArn **   <a name="IncidentManager-Type-SSMContacts_Receipt-ContactChannelArn"></a>
The Amazon Resource Name (ARN) of the contact channel Incident Manager engaged.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: No

 ** ReceiptInfo **   <a name="IncidentManager-Type-SSMContacts_Receipt-ReceiptInfo"></a>
Information provided during the page acknowledgement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[.\s\S]*$`
Required: No

## See Also
<a name="API_SSMContacts_Receipt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/Receipt)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/Receipt)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/Receipt)
