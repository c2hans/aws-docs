---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ProspectingResultCustomer.html
---

# ProspectingResultCustomer
<a name="API_ProspectingResultCustomer"></a>

Contains detailed information about the prospected customer account, including company identifiers, geographic classification, industry segmentation, and program eligibility.

## Contents
<a name="API_ProspectingResultCustomer_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AccountName **   <a name="AWSPartnerCentral-Type-ProspectingResultCustomer-AccountName"></a>
The name of the prospected customer account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** CompanySize **   <a name="AWSPartnerCentral-Type-ProspectingResultCustomer-CompanySize"></a>
The company size classification of the prospected customer account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** Country **   <a name="AWSPartnerCentral-Type-ProspectingResultCustomer-Country"></a>
The country code of the prospected customer account.
Type: String
Valid Values: `US | AF | AX | AL | DZ | AS | AD | AO | AI | AQ | AG | AR | AM | AW | AU | AT | AZ | BS | BH | BD | BB | BY | BE | BZ | BJ | BM | BT | BO | BQ | BA | BW | BV | BR | IO | BN | BG | BF | BI | KH | CM | CA | CV | KY | CF | TD | CL | CN | CX | CC | CO | KM | CG | CK | CR | CI | HR | CU | CW | CY | CZ | CD | DK | DJ | DM | DO | EC | EG | SV | GQ | ER | EE | ET | FK | FO | FJ | FI | FR | GF | PF | TF | GA | GM | GE | DE | GH | GI | GR | GL | GD | GP | GU | GT | GG | GN | GW | GY | HT | HM | VA | HN | HK | HU | IS | IN | ID | IR | IQ | IE | IM | IL | IT | JM | JP | JE | JO | KZ | KE | KI | KR | KW | KG | LA | LV | LB | LS | LR | LY | LI | LT | LU | MO | MK | MG | MW | MY | MV | ML | MT | MH | MQ | MR | MU | YT | MX | FM | MD | MC | MN | ME | MS | MA | MZ | MM | NA | NR | NP | NL | AN | NC | NZ | NI | NE | NG | NU | NF | MP | NO | OM | PK | PW | PS | PA | PG | PY | PE | PH | PN | PL | PT | PR | QA | RE | RO | RU | RW | BL | SH | KN | LC | MF | PM | VC | WS | SM | ST | SA | SN | RS | SC | SL | SG | SX | SK | SI | SB | SO | ZA | GS | SS | ES | LK | SD | SR | SJ | SZ | SE | CH | SY | TW | TJ | TZ | TH | TL | TG | TK | TO | TT | TN | TR | TM | TC | TV | UG | UA | AE | GB | UM | UY | UZ | VU | VE | VN | VG | VI | WF | EH | YE | ZM | ZW`
Required: No

 ** EligiblePrograms **   <a name="AWSPartnerCentral-Type-ProspectingResultCustomer-EligiblePrograms"></a>
A list of AWS Greenfield programs that the prospected customer is eligible for. Use this list to identify relevant go-to-market opportunities.
Type: Array of strings
Required: No

 ** Geo **   <a name="AWSPartnerCentral-Type-ProspectingResultCustomer-Geo"></a>
The geographic region classification of the prospected customer account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** Industry **   <a name="AWSPartnerCentral-Type-ProspectingResultCustomer-Industry"></a>
The industry classification of the prospected customer account.
Type: String
Valid Values: `Aerospace | Agriculture | Automotive | Computers and Electronics | Consumer Goods | Education | Energy - Oil and Gas | Energy - Power and Utilities | Financial Services | Gaming | Government | Healthcare | Hospitality | Life Sciences | Manufacturing | Marketing and Advertising | Media and Entertainment | Mining | Non-Profit Organization | Professional Services | Real Estate and Construction | Retail | Software and Internet | Telecommunications | Transportation and Logistics | Travel | Wholesale and Distribution | Other`
Required: No

 ** PublicProfileSummary **   <a name="AWSPartnerCentral-Type-ProspectingResultCustomer-PublicProfileSummary"></a>
A summary of publicly available information about the prospected customer. The system uses this summary to generate customer insights and inform engagement strategies.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 5000.
Required: No

 ** Region **   <a name="AWSPartnerCentral-Type-ProspectingResultCustomer-Region"></a>
The specific region of the prospected customer account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** Segment **   <a name="AWSPartnerCentral-Type-ProspectingResultCustomer-Segment"></a>
The market segment classification of the prospected customer account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** SubIndustry **   <a name="AWSPartnerCentral-Type-ProspectingResultCustomer-SubIndustry"></a>
The sub-industry classification of the prospected customer account. This provides more granular categorization within the primary industry.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** SubRegion **   <a name="AWSPartnerCentral-Type-ProspectingResultCustomer-SubRegion"></a>
The subregion classification of the prospected customer account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_ProspectingResultCustomer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ProspectingResultCustomer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ProspectingResultCustomer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ProspectingResultCustomer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
