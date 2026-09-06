---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbersSummary.html
---

# ListPhoneNumbersSummary
<a name="API_ListPhoneNumbersSummary"></a>

Information about phone numbers that have been claimed to your Connect Customer instance or traffic distribution group.

## Contents
<a name="API_ListPhoneNumbersSummary_Contents"></a>

 ** InstanceId **   <a name="connect-Type-ListPhoneNumbersSummary-InstanceId"></a>
The identifier of the Connect Customer instance that phone numbers are claimed to. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** PhoneNumber **   <a name="connect-Type-ListPhoneNumbersSummary-PhoneNumber"></a>
The phone number. Phone numbers are formatted `[+] [country code] [subscriber number including area code]`.
Type: String
Pattern: `\\+[1-9]\\d{1,14}$`
Required: No

 ** PhoneNumberArn **   <a name="connect-Type-ListPhoneNumbersSummary-PhoneNumberArn"></a>
The Amazon Resource Name (ARN) of the phone number.
Type: String
Required: No

 ** PhoneNumberCountryCode **   <a name="connect-Type-ListPhoneNumbersSummary-PhoneNumberCountryCode"></a>
The ISO country code.
Type: String
Valid Values: `AF | AL | DZ | AS | AD | AO | AI | AQ | AG | AR | AM | AW | AU | AT | AZ | BS | BH | BD | BB | BY | BE | BZ | BJ | BM | BT | BO | BA | BW | BR | IO | VG | BN | BG | BF | BI | KH | CM | CA | CV | KY | CF | TD | CL | CN | CX | CC | CO | KM | CK | CR | HR | CU | CW | CY | CZ | CD | DK | DJ | DM | DO | TL | EC | EG | SV | GQ | ER | EE | ET | FK | FO | FJ | FI | FR | PF | GA | GM | GE | DE | GH | GI | GR | GL | GD | GU | GT | GG | GN | GW | GY | HT | HN | HK | HU | IS | IN | ID | IR | IQ | IE | IM | IL | IT | CI | JM | JP | JE | JO | KZ | KE | KI | KW | KG | LA | LV | LB | LS | LR | LY | LI | LT | LU | MO | MK | MG | MW | MY | MV | ML | MT | MH | MR | MU | YT | MX | FM | MD | MC | MN | ME | MS | MA | MZ | MM | NA | NR | NP | NL | AN | NC | NZ | NI | NE | NG | NU | KP | MP | NO | OM | PK | PW | PA | PG | PY | PE | PH | PN | PL | PT | PR | QA | CG | RE | RO | RU | RW | BL | SH | KN | LC | MF | PM | VC | WS | SM | ST | SA | SN | RS | SC | SL | SG | SX | SK | SI | SB | SO | ZA | KR | ES | LK | SD | SR | SJ | SZ | SE | CH | SY | TW | TJ | TZ | TH | TG | TK | TO | TT | TN | TR | TM | TC | TV | VI | UG | UA | AE | GB | US | UY | UZ | VU | VA | VE | VN | WF | EH | YE | ZM | ZW`
Required: No

 ** PhoneNumberDescription **   <a name="connect-Type-ListPhoneNumbersSummary-PhoneNumberDescription"></a>
The description of the phone number.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `^[\W\S_]*`
Required: No

 ** PhoneNumberId **   <a name="connect-Type-ListPhoneNumbersSummary-PhoneNumberId"></a>
A unique identifier for the phone number.
Type: String
Required: No

 ** PhoneNumberType **   <a name="connect-Type-ListPhoneNumbersSummary-PhoneNumberType"></a>
The type of phone number.
Type: String
Valid Values: `TOLL_FREE | DID | UIFN | SHARED | THIRD_PARTY_TF | THIRD_PARTY_DID | SHORT_CODE`
Required: No

 ** SourcePhoneNumberArn **   <a name="connect-Type-ListPhoneNumbersSummary-SourcePhoneNumberArn"></a>
The claimed phone number ARN that was previously imported from the external service, such as AWS End User Messaging. If it is from AWS End User Messaging, it looks like the ARN of the phone number that was imported from AWS End User Messaging.
Type: String
Required: No

 ** TargetArn **   <a name="connect-Type-ListPhoneNumbersSummary-TargetArn"></a>
The Amazon Resource Name (ARN) for Connect Customer instances or traffic distribution groups that phone number inbound traffic is routed through.
Type: String
Required: No

## See Also
<a name="API_ListPhoneNumbersSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListPhoneNumbersSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListPhoneNumbersSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListPhoneNumbersSummary)
