---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimedPhoneNumberSummary.html
---

# ClaimedPhoneNumberSummary
<a name="API_ClaimedPhoneNumberSummary"></a>

Information about a phone number that has been claimed to your Connect Customer instance or traffic distribution group.

## Contents
<a name="API_ClaimedPhoneNumberSummary_Contents"></a>

 ** InstanceId **   <a name="connect-Type-ClaimedPhoneNumberSummary-InstanceId"></a>
The identifier of the Connect Customer instance that phone numbers are claimed to. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** PhoneNumber **   <a name="connect-Type-ClaimedPhoneNumberSummary-PhoneNumber"></a>
The phone number. Phone numbers are formatted `[+] [country code] [subscriber number including area code]`.
Type: String
Pattern: `\\+[1-9]\\d{1,14}$`
Required: No

 ** PhoneNumberArn **   <a name="connect-Type-ClaimedPhoneNumberSummary-PhoneNumberArn"></a>
The Amazon Resource Name (ARN) of the phone number.
Type: String
Required: No

 ** PhoneNumberCountryCode **   <a name="connect-Type-ClaimedPhoneNumberSummary-PhoneNumberCountryCode"></a>
The ISO country code.
Type: String
Valid Values: `AF | AL | DZ | AS | AD | AO | AI | AQ | AG | AR | AM | AW | AU | AT | AZ | BS | BH | BD | BB | BY | BE | BZ | BJ | BM | BT | BO | BA | BW | BR | IO | VG | BN | BG | BF | BI | KH | CM | CA | CV | KY | CF | TD | CL | CN | CX | CC | CO | KM | CK | CR | HR | CU | CW | CY | CZ | CD | DK | DJ | DM | DO | TL | EC | EG | SV | GQ | ER | EE | ET | FK | FO | FJ | FI | FR | PF | GA | GM | GE | DE | GH | GI | GR | GL | GD | GU | GT | GG | GN | GW | GY | HT | HN | HK | HU | IS | IN | ID | IR | IQ | IE | IM | IL | IT | CI | JM | JP | JE | JO | KZ | KE | KI | KW | KG | LA | LV | LB | LS | LR | LY | LI | LT | LU | MO | MK | MG | MW | MY | MV | ML | MT | MH | MR | MU | YT | MX | FM | MD | MC | MN | ME | MS | MA | MZ | MM | NA | NR | NP | NL | AN | NC | NZ | NI | NE | NG | NU | KP | MP | NO | OM | PK | PW | PA | PG | PY | PE | PH | PN | PL | PT | PR | QA | CG | RE | RO | RU | RW | BL | SH | KN | LC | MF | PM | VC | WS | SM | ST | SA | SN | RS | SC | SL | SG | SX | SK | SI | SB | SO | ZA | KR | ES | LK | SD | SR | SJ | SZ | SE | CH | SY | TW | TJ | TZ | TH | TG | TK | TO | TT | TN | TR | TM | TC | TV | VI | UG | UA | AE | GB | US | UY | UZ | VU | VA | VE | VN | WF | EH | YE | ZM | ZW`
Required: No

 ** PhoneNumberDescription **   <a name="connect-Type-ClaimedPhoneNumberSummary-PhoneNumberDescription"></a>
The description of the phone number.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `^[\W\S_]*`
Required: No

 ** PhoneNumberId **   <a name="connect-Type-ClaimedPhoneNumberSummary-PhoneNumberId"></a>
A unique identifier for the phone number.
Type: String
Required: No

 ** PhoneNumberStatus **   <a name="connect-Type-ClaimedPhoneNumberSummary-PhoneNumberStatus"></a>
The status of the phone number.
+  `CLAIMED` means the previous [ClaimPhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimPhoneNumber.html) or [UpdatePhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumber.html) operation succeeded.
+  `IN_PROGRESS` means a [ClaimPhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimPhoneNumber.html), [UpdatePhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumber.html), or [UpdatePhoneNumberMetadata](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumberMetadata.html) operation is still in progress and has not yet completed. You can call [DescribePhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribePhoneNumber.html) at a later time to verify if the previous operation has completed.
+  `FAILED` indicates that the previous [ClaimPhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimPhoneNumber.html) or [UpdatePhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumber.html) operation has failed. It will include a message indicating the failure reason. A common reason for a failure may be that the `TargetArn` value you are claiming or updating a phone number to has reached its limit of total claimed numbers. If you received a `FAILED` status from a `ClaimPhoneNumber` API call, you have one day to retry claiming the phone number before the number is released back to the inventory for other customers to claim.
You will not be billed for the phone number during the 1-day period if number claiming fails.
Type: [PhoneNumberStatus](API_PhoneNumberStatus.md) object
Required: No

 ** PhoneNumberType **   <a name="connect-Type-ClaimedPhoneNumberSummary-PhoneNumberType"></a>
The type of phone number.
Type: String
Valid Values: `TOLL_FREE | DID | UIFN | SHARED | THIRD_PARTY_TF | THIRD_PARTY_DID | SHORT_CODE`
Required: No

 ** SourcePhoneNumberArn **   <a name="connect-Type-ClaimedPhoneNumberSummary-SourcePhoneNumberArn"></a>
The claimed phone number ARN that was previously imported from the external service, such as AWS End User Messaging. If it is from AWS End User Messaging, it looks like the ARN of the phone number that was imported from AWS End User Messaging.
Type: String
Required: No

 ** Tags **   <a name="connect-Type-ClaimedPhoneNumberSummary-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** TargetArn **   <a name="connect-Type-ClaimedPhoneNumberSummary-TargetArn"></a>
The Amazon Resource Name (ARN) for Connect Customer instances or traffic distribution groups that phone number inbound traffic is routed through.
Type: String
Required: No

## See Also
<a name="API_ClaimedPhoneNumberSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ClaimedPhoneNumberSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ClaimedPhoneNumberSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ClaimedPhoneNumberSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
