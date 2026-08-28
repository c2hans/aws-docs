---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AvailableNumberSummary.html
---

# AvailableNumberSummary
<a name="API_AvailableNumberSummary"></a>

Information about available phone numbers.

## Contents
<a name="API_AvailableNumberSummary_Contents"></a>

 ** PhoneNumber **   <a name="connect-Type-AvailableNumberSummary-PhoneNumber"></a>
The phone number. Phone numbers are formatted `[+] [country code] [subscriber number including area code]`.
Type: String
Pattern: `\\+[1-9]\\d{1,14}$`
Required: No

 ** PhoneNumberCountryCode **   <a name="connect-Type-AvailableNumberSummary-PhoneNumberCountryCode"></a>
The ISO country code.
Type: String
Valid Values: `AF | AL | DZ | AS | AD | AO | AI | AQ | AG | AR | AM | AW | AU | AT | AZ | BS | BH | BD | BB | BY | BE | BZ | BJ | BM | BT | BO | BA | BW | BR | IO | VG | BN | BG | BF | BI | KH | CM | CA | CV | KY | CF | TD | CL | CN | CX | CC | CO | KM | CK | CR | HR | CU | CW | CY | CZ | CD | DK | DJ | DM | DO | TL | EC | EG | SV | GQ | ER | EE | ET | FK | FO | FJ | FI | FR | PF | GA | GM | GE | DE | GH | GI | GR | GL | GD | GU | GT | GG | GN | GW | GY | HT | HN | HK | HU | IS | IN | ID | IR | IQ | IE | IM | IL | IT | CI | JM | JP | JE | JO | KZ | KE | KI | KW | KG | LA | LV | LB | LS | LR | LY | LI | LT | LU | MO | MK | MG | MW | MY | MV | ML | MT | MH | MR | MU | YT | MX | FM | MD | MC | MN | ME | MS | MA | MZ | MM | NA | NR | NP | NL | AN | NC | NZ | NI | NE | NG | NU | KP | MP | NO | OM | PK | PW | PA | PG | PY | PE | PH | PN | PL | PT | PR | QA | CG | RE | RO | RU | RW | BL | SH | KN | LC | MF | PM | VC | WS | SM | ST | SA | SN | RS | SC | SL | SG | SX | SK | SI | SB | SO | ZA | KR | ES | LK | SD | SR | SJ | SZ | SE | CH | SY | TW | TJ | TZ | TH | TG | TK | TO | TT | TN | TR | TM | TC | TV | VI | UG | UA | AE | GB | US | UY | UZ | VU | VA | VE | VN | WF | EH | YE | ZM | ZW`
Required: No

 ** PhoneNumberType **   <a name="connect-Type-AvailableNumberSummary-PhoneNumberType"></a>
The type of phone number.
Type: String
Valid Values: `TOLL_FREE | DID | UIFN | SHARED | THIRD_PARTY_TF | THIRD_PARTY_DID | SHORT_CODE`
Required: No

## See Also
<a name="API_AvailableNumberSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AvailableNumberSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AvailableNumberSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AvailableNumberSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
