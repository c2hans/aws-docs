---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AddressSummary.html
---

# AddressSummary
<a name="API_AddressSummary"></a>

An object that contains an `Address` object's subset of fields.

## Contents
<a name="API_AddressSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** City **   <a name="AWSPartnerCentral-Type-AddressSummary-City"></a>
Specifies the end `Customer`'s city associated with the `Opportunity`.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** CountryCode **   <a name="AWSPartnerCentral-Type-AddressSummary-CountryCode"></a>
Specifies the end `Customer`'s country associated with the `Opportunity`.
Type: String
Valid Values: `US | AF | AX | AL | DZ | AS | AD | AO | AI | AQ | AG | AR | AM | AW | AU | AT | AZ | BS | BH | BD | BB | BY | BE | BZ | BJ | BM | BT | BO | BQ | BA | BW | BV | BR | IO | BN | BG | BF | BI | KH | CM | CA | CV | KY | CF | TD | CL | CN | CX | CC | CO | KM | CG | CK | CR | CI | HR | CU | CW | CY | CZ | CD | DK | DJ | DM | DO | EC | EG | SV | GQ | ER | EE | ET | FK | FO | FJ | FI | FR | GF | PF | TF | GA | GM | GE | DE | GH | GI | GR | GL | GD | GP | GU | GT | GG | GN | GW | GY | HT | HM | VA | HN | HK | HU | IS | IN | ID | IR | IQ | IE | IM | IL | IT | JM | JP | JE | JO | KZ | KE | KI | KR | KW | KG | LA | LV | LB | LS | LR | LY | LI | LT | LU | MO | MK | MG | MW | MY | MV | ML | MT | MH | MQ | MR | MU | YT | MX | FM | MD | MC | MN | ME | MS | MA | MZ | MM | NA | NR | NP | NL | AN | NC | NZ | NI | NE | NG | NU | NF | MP | NO | OM | PK | PW | PS | PA | PG | PY | PE | PH | PN | PL | PT | PR | QA | RE | RO | RU | RW | BL | SH | KN | LC | MF | PM | VC | WS | SM | ST | SA | SN | RS | SC | SL | SG | SX | SK | SI | SB | SO | ZA | GS | SS | ES | LK | SD | SR | SJ | SZ | SE | CH | SY | TW | TJ | TZ | TH | TL | TG | TK | TO | TT | TN | TR | TM | TC | TV | UG | UA | AE | GB | UM | UY | UZ | VU | VE | VN | VG | VI | WF | EH | YE | ZM | ZW`
Required: No

 ** PostalCode **   <a name="AWSPartnerCentral-Type-AddressSummary-PostalCode"></a>
Specifies the end `Customer`'s postal code associated with the `Opportunity`.
Type: String
Pattern: `(?s).{0,20}`
Required: No

 ** StateOrRegion **   <a name="AWSPartnerCentral-Type-AddressSummary-StateOrRegion"></a>
Specifies the end `Customer`'s state or region associated with the `Opportunity`.
Valid values: `Alabama | Alaska | American Samoa | Arizona | Arkansas | California | Colorado | Connecticut | Delaware | Dist. of Columbia | Federated States of Micronesia | Florida | Georgia | Guam | Hawaii | Idaho | Illinois | Indiana | Iowa | Kansas | Kentucky | Louisiana | Maine | Marshall Islands | Maryland | Massachusetts | Michigan | Minnesota | Mississippi | Missouri | Montana | Nebraska | Nevada | New Hampshire | New Jersey | New Mexico | New York | North Carolina | North Dakota | Northern Mariana Islands | Ohio | Oklahoma | Oregon | Palau | Pennsylvania | Puerto Rico | Rhode Island | South Carolina | South Dakota | Tennessee | Texas | Utah | Vermont | Virginia | Virgin Islands | Washington | West Virginia | Wisconsin | Wyoming | APO/AE | AFO/FPO | FPO, AP`
Type: String
Required: No

## See Also
<a name="API_AddressSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AddressSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AddressSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AddressSummary)
