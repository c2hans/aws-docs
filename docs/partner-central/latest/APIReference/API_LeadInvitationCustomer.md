---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_LeadInvitationCustomer.html
---

# LeadInvitationCustomer
<a name="API_LeadInvitationCustomer"></a>

Contains customer information included in a lead invitation payload. This structure provides essential details about the customer to help partners evaluate the lead opportunity and determine their interest in engagement.

## Contents
<a name="API_LeadInvitationCustomer_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CompanyName **   <a name="AWSPartnerCentral-Type-LeadInvitationCustomer-CompanyName"></a>
The name of the customer company associated with the lead invitation. This field identifies the target organization for the lead engagement opportunity.
Type: String
Pattern: `(?s).{1,120}`
Required: Yes

 ** CountryCode **   <a name="AWSPartnerCentral-Type-LeadInvitationCustomer-CountryCode"></a>
The country code indicating the geographic location of the customer company. This information helps partners understand regional requirements and assess their ability to serve the customer effectively.
Type: String
Valid Values: `US | AF | AX | AL | DZ | AS | AD | AO | AI | AQ | AG | AR | AM | AW | AU | AT | AZ | BS | BH | BD | BB | BY | BE | BZ | BJ | BM | BT | BO | BQ | BA | BW | BV | BR | IO | BN | BG | BF | BI | KH | CM | CA | CV | KY | CF | TD | CL | CN | CX | CC | CO | KM | CG | CK | CR | CI | HR | CU | CW | CY | CZ | CD | DK | DJ | DM | DO | EC | EG | SV | GQ | ER | EE | ET | FK | FO | FJ | FI | FR | GF | PF | TF | GA | GM | GE | DE | GH | GI | GR | GL | GD | GP | GU | GT | GG | GN | GW | GY | HT | HM | VA | HN | HK | HU | IS | IN | ID | IR | IQ | IE | IM | IL | IT | JM | JP | JE | JO | KZ | KE | KI | KR | KW | KG | LA | LV | LB | LS | LR | LY | LI | LT | LU | MO | MK | MG | MW | MY | MV | ML | MT | MH | MQ | MR | MU | YT | MX | FM | MD | MC | MN | ME | MS | MA | MZ | MM | NA | NR | NP | NL | AN | NC | NZ | NI | NE | NG | NU | NF | MP | NO | OM | PK | PW | PS | PA | PG | PY | PE | PH | PN | PL | PT | PR | QA | RE | RO | RU | RW | BL | SH | KN | LC | MF | PM | VC | WS | SM | ST | SA | SN | RS | SC | SL | SG | SX | SK | SI | SB | SO | ZA | GS | SS | ES | LK | SD | SR | SJ | SZ | SE | CH | SY | TW | TJ | TZ | TH | TL | TG | TK | TO | TT | TN | TR | TM | TC | TV | UG | UA | AE | GB | UM | UY | UZ | VU | VE | VN | VG | VI | WF | EH | YE | ZM | ZW`
Required: Yes

 ** AwsMaturity **   <a name="AWSPartnerCentral-Type-LeadInvitationCustomer-AwsMaturity"></a>
Indicates the customer's level of experience and adoption with AWS services. This assessment helps partners understand the customer's cloud maturity and tailor their engagement approach accordingly.
Type: String
Pattern: `(?s).{1,20}`
Required: No

 ** Industry **   <a name="AWSPartnerCentral-Type-LeadInvitationCustomer-Industry"></a>
Specifies the industry sector of the customer company associated with the lead invitation. This categorization helps partners understand the customer's business context and assess solution fit.
Type: String
Valid Values: `Aerospace | Agriculture | Automotive | Computers and Electronics | Consumer Goods | Education | Energy - Oil and Gas | Energy - Power and Utilities | Financial Services | Gaming | Government | Healthcare | Hospitality | Life Sciences | Manufacturing | Marketing and Advertising | Media and Entertainment | Mining | Non-Profit Organization | Professional Services | Real Estate and Construction | Retail | Software and Internet | Telecommunications | Transportation and Logistics | Travel | Wholesale and Distribution | Other`
Required: No

 ** MarketSegment **   <a name="AWSPartnerCentral-Type-LeadInvitationCustomer-MarketSegment"></a>
Specifies the market segment classification of the customer, such as enterprise, mid-market, or small business. This segmentation helps partners determine the appropriate solution complexity and engagement strategy.
Type: String
Valid Values: `Enterprise | Large | Medium | Small | Micro`
Required: No

 ** WebsiteUrl **   <a name="AWSPartnerCentral-Type-LeadInvitationCustomer-WebsiteUrl"></a>
The website URL of the customer company. This provides additional context about the customer organization and helps partners verify company details and assess business size and legitimacy.
Type: String
Pattern: `(?=.{4,255}$)((http|https)://)??(www[.])??([a-zA-Z0-9]|-)+?([.][a-zA-Z0-9(-|/|=|?)??]+?)+?`
Required: No

## See Also
<a name="API_LeadInvitationCustomer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/LeadInvitationCustomer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/LeadInvitationCustomer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/LeadInvitationCustomer)
