---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_EngagementCustomer.html
---

# EngagementCustomer
<a name="API_EngagementCustomer"></a>

Contains details about the customer associated with the Engagement Invitation, including company information and industry.

## Contents
<a name="API_EngagementCustomer_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CompanyName **   <a name="AWSPartnerCentral-Type-EngagementCustomer-CompanyName"></a>
Represents the name of the customer’s company associated with the Engagement Invitation. This field is used to identify the customer.
Type: String
Pattern: `(?s).{1,120}`
Required: Yes

 ** CountryCode **   <a name="AWSPartnerCentral-Type-EngagementCustomer-CountryCode"></a>
Indicates the country in which the customer’s company operates. This field is useful for understanding regional requirements or compliance needs.
Type: String
Valid Values: `US | AF | AX | AL | DZ | AS | AD | AO | AI | AQ | AG | AR | AM | AW | AU | AT | AZ | BS | BH | BD | BB | BY | BE | BZ | BJ | BM | BT | BO | BQ | BA | BW | BV | BR | IO | BN | BG | BF | BI | KH | CM | CA | CV | KY | CF | TD | CL | CN | CX | CC | CO | KM | CG | CK | CR | CI | HR | CU | CW | CY | CZ | CD | DK | DJ | DM | DO | EC | EG | SV | GQ | ER | EE | ET | FK | FO | FJ | FI | FR | GF | PF | TF | GA | GM | GE | DE | GH | GI | GR | GL | GD | GP | GU | GT | GG | GN | GW | GY | HT | HM | VA | HN | HK | HU | IS | IN | ID | IR | IQ | IE | IM | IL | IT | JM | JP | JE | JO | KZ | KE | KI | KR | KW | KG | LA | LV | LB | LS | LR | LY | LI | LT | LU | MO | MK | MG | MW | MY | MV | ML | MT | MH | MQ | MR | MU | YT | MX | FM | MD | MC | MN | ME | MS | MA | MZ | MM | NA | NR | NP | NL | AN | NC | NZ | NI | NE | NG | NU | NF | MP | NO | OM | PK | PW | PS | PA | PG | PY | PE | PH | PN | PL | PT | PR | QA | RE | RO | RU | RW | BL | SH | KN | LC | MF | PM | VC | WS | SM | ST | SA | SN | RS | SC | SL | SG | SX | SK | SI | SB | SO | ZA | GS | SS | ES | LK | SD | SR | SJ | SZ | SE | CH | SY | TW | TJ | TZ | TH | TL | TG | TK | TO | TT | TN | TR | TM | TC | TV | UG | UA | AE | GB | UM | UY | UZ | VU | VE | VN | VG | VI | WF | EH | YE | ZM | ZW`
Required: Yes

 ** Industry **   <a name="AWSPartnerCentral-Type-EngagementCustomer-Industry"></a>
Specifies the industry to which the customer’s company belongs. This field helps categorize the opportunity based on the customer’s business sector.
Type: String
Valid Values: `Aerospace | Agriculture | Automotive | Computers and Electronics | Consumer Goods | Education | Energy - Oil and Gas | Energy - Power and Utilities | Financial Services | Gaming | Government | Healthcare | Hospitality | Life Sciences | Manufacturing | Marketing and Advertising | Media and Entertainment | Mining | Non-Profit Organization | Professional Services | Real Estate and Construction | Retail | Software and Internet | Telecommunications | Transportation and Logistics | Travel | Wholesale and Distribution | Other`
Required: Yes

 ** WebsiteUrl **   <a name="AWSPartnerCentral-Type-EngagementCustomer-WebsiteUrl"></a>
Provides the website URL of the customer’s company. This field helps partners verify the legitimacy and size of the customer organization.
Type: String
Pattern: `(?=.{4,255}$)((http|https)://)??(www[.])??([a-zA-Z0-9]|-)+?([.][a-zA-Z0-9(-|/|=|?)??]+?)+?`
Required: Yes

## See Also
<a name="API_EngagementCustomer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/EngagementCustomer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/EngagementCustomer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/EngagementCustomer)
