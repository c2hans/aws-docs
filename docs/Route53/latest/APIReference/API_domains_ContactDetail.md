---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html
---

# ContactDetail
<a name="API_domains_ContactDetail"></a>

ContactDetail includes the following elements.

## Contents
<a name="API_domains_ContactDetail_Contents"></a>

 ** AddressLine1 **   <a name="Route53Domains-Type-domains_ContactDetail-AddressLine1"></a>
First line of the contact's address.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** AddressLine2 **   <a name="Route53Domains-Type-domains_ContactDetail-AddressLine2"></a>
Second line of contact's address, if any.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** City **   <a name="Route53Domains-Type-domains_ContactDetail-City"></a>
The city of the contact's address.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** ContactType **   <a name="Route53Domains-Type-domains_ContactDetail-ContactType"></a>
Indicates whether the contact is a person, company, association, or public organization. Note the following:
+ If you specify a value other than `PERSON`, you must also specify a value for `OrganizationName`.
+ For some TLDs, the privacy protection available depends on the value that you specify for `Contact Type`. For the privacy protection settings for your TLD, see [Domains that You Can Register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html) in the *Amazon Route 53 Developer Guide*
+ For .es domains, the value of `ContactType` must be `PERSON` for all three contacts.
Type: String
Valid Values: `PERSON | COMPANY | ASSOCIATION | PUBLIC_BODY | RESELLER`
Required: No

 ** CountryCode **   <a name="Route53Domains-Type-domains_ContactDetail-CountryCode"></a>
Code for the country of the contact's address.
Type: String
Valid Values: `AC | AD | AE | AF | AG | AI | AL | AM | AN | AO | AQ | AR | AS | AT | AU | AW | AX | AZ | BA | BB | BD | BE | BF | BG | BH | BI | BJ | BL | BM | BN | BO | BQ | BR | BS | BT | BV | BW | BY | BZ | CA | CC | CD | CF | CG | CH | CI | CK | CL | CM | CN | CO | CR | CU | CV | CW | CX | CY | CZ | DE | DJ | DK | DM | DO | DZ | EC | EE | EG | EH | ER | ES | ET | FI | FJ | FK | FM | FO | FR | GA | GB | GD | GE | GF | GG | GH | GI | GL | GM | GN | GP | GQ | GR | GS | GT | GU | GW | GY | HK | HM | HN | HR | HT | HU | ID | IE | IL | IM | IN | IO | IQ | IR | IS | IT | JE | JM | JO | JP | KE | KG | KH | KI | KM | KN | KP | KR | KW | KY | KZ | LA | LB | LC | LI | LK | LR | LS | LT | LU | LV | LY | MA | MC | MD | ME | MF | MG | MH | MK | ML | MM | MN | MO | MP | MQ | MR | MS | MT | MU | MV | MW | MX | MY | MZ | NA | NC | NE | NF | NG | NI | NL | NO | NP | NR | NU | NZ | OM | PA | PE | PF | PG | PH | PK | PL | PM | PN | PR | PS | PT | PW | PY | QA | RE | RO | RS | RU | RW | SA | SB | SC | SD | SE | SG | SH | SI | SJ | SK | SL | SM | SN | SO | SR | SS | ST | SV | SX | SY | SZ | TC | TD | TF | TG | TH | TJ | TK | TL | TM | TN | TO | TP | TR | TT | TV | TW | TZ | UA | UG | US | UY | UZ | VA | VC | VE | VG | VI | VN | VU | WF | WS | YE | YT | ZA | ZM | ZW`
Required: No

 ** Email **   <a name="Route53Domains-Type-domains_ContactDetail-Email"></a>
Email address of the contact.
Type: String
Length Constraints: Maximum length of 254.
Required: No

 ** ExtraParams **   <a name="Route53Domains-Type-domains_ContactDetail-ExtraParams"></a>
A list of name-value pairs for parameters required by certain top-level domains.
Type: Array of [ExtraParam](API_domains_ExtraParam.md) objects
Required: No

 ** Fax **   <a name="Route53Domains-Type-domains_ContactDetail-Fax"></a>
Fax number of the contact.
Constraints: Phone number must be specified in the format "\+[country dialing code].[number including any area code]". For example, a US phone number might appear as `"+1.1234567890"`.
Type: String
Length Constraints: Maximum length of 30.
Required: No

 ** FirstName **   <a name="Route53Domains-Type-domains_ContactDetail-FirstName"></a>
First name of contact.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** LastName **   <a name="Route53Domains-Type-domains_ContactDetail-LastName"></a>
Last name of contact.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** OrganizationName **   <a name="Route53Domains-Type-domains_ContactDetail-OrganizationName"></a>
Name of the organization for contact types other than `PERSON`.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** PhoneNumber **   <a name="Route53Domains-Type-domains_ContactDetail-PhoneNumber"></a>
The phone number of the contact.
Constraints: Phone number must be specified in the format "\+[country dialing code].[number including any area code>]". For example, a US phone number might appear as `"+1.1234567890"`.
Type: String
Length Constraints: Maximum length of 30.
Required: No

 ** State **   <a name="Route53Domains-Type-domains_ContactDetail-State"></a>
The state or province of the contact's city.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** ZipCode **   <a name="Route53Domains-Type-domains_ContactDetail-ZipCode"></a>
The zip or postal code of the contact's address.
Type: String
Length Constraints: Maximum length of 255.
Required: No

## See Also
<a name="API_domains_ContactDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/ContactDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/ContactDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/ContactDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
