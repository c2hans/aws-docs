---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AccountCustomer.html
---

# AccountCustomer

A snapshot of the customer company's identity for an account-planning engagement. The caller can supply these details so that an account can be identified even when it isn't yet mapped to an AWS account.

## Contents
<a name="API_AccountCustomer_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CompanyName **   <a name="AWSPartnerCentral-Type-AccountCustomer-CompanyName"></a>
The name of the customer company.
Type: String
Pattern: `(?s).{1,120}`
Required: Yes

 ** CountryCode **   <a name="AWSPartnerCentral-Type-AccountCustomer-CountryCode"></a>
The country of the customer company, as an ISO 3166-1 alpha-2 country code.
Type: String
Valid Values: `US | AF | AX | AL | DZ | AS | AD | AO | AI | AQ | AG | AR | AM | AW | AU | AT | AZ | BS | BH | BD | BB | BY | BE | BZ | BJ | BM | BT | BO | BQ | BA | BW | BV | BR | IO | BN | BG | BF | BI | KH | CM | CA | CV | KY | CF | TD | CL | CN | CX | CC | CO | KM | CG | CK | CR | CI | HR | CU | CW | CY | CZ | CD | DK | DJ | DM | DO | EC | EG | SV | GQ | ER | EE | ET | FK | FO | FJ | FI | FR | GF | PF | TF | GA | GM | GE | DE | GH | GI | GR | GL | GD | GP | GU | GT | GG | GN | GW | GY | HT | HM | VA | HN | HK | HU | IS | IN | ID | IR | IQ | IE | IM | IL | IT | JM | JP | JE | JO | KZ | KE | KI | KR | KW | KG | LA | LV | LB | LS | LR | LY | LI | LT | LU | MO | MK | MG | MW | MY | MV | ML | MT | MH | MQ | MR | MU | YT | MX | FM | MD | MC | MN | ME | MS | MA | MZ | MM | NA | NR | NP | NL | AN | NC | NZ | NI | NE | NG | NU | NF | MP | NO | OM | PK | PW | PS | PA | PG | PY | PE | PH | PN | PL | PT | PR | QA | RE | RO | RU | RW | BL | SH | KN | LC | MF | PM | VC | WS | SM | ST | SA | SN | RS | SC | SL | SG | SX | SK | SI | SB | SO | ZA | GS | SS | ES | LK | SD | SR | SJ | SZ | SE | CH | SY | TW | TJ | TZ | TH | TL | TG | TK | TO | TT | TN | TR | TM | TC | TV | UG | UA | AE | GB | UM | UY | UZ | VU | VE | VN | VG | VI | WF | EH | YE | ZM | ZW`
Required: No

 ** Industry **   <a name="AWSPartnerCentral-Type-AccountCustomer-Industry"></a>
The industry classification of the customer company.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** WebsiteUrl **   <a name="AWSPartnerCentral-Type-AccountCustomer-WebsiteUrl"></a>
The website URL of the customer company.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_AccountCustomer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AccountCustomer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AccountCustomer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AccountCustomer)
