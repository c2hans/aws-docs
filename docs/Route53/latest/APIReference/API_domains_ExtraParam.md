---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ExtraParam.html
---

# ExtraParam
<a name="API_domains_ExtraParam"></a>

ExtraParam includes the following elements.

## Contents
<a name="API_domains_ExtraParam_Contents"></a>

 ** Name **   <a name="Route53Domains-Type-domains_ExtraParam-Name"></a>
The name of an additional parameter that is required by a top-level domain. Here are the top-level domains that require additional parameters and the names of the parameters that they require:
.au, .com.au, and .net.au
+  `AU_REGISTRANT_NAME`
+  `AU_ID_NUMBER`
+  `AU_ID_TYPE`

  Valid values include the following:
  +  `ABN` (Australian business number)
  +  `ACN` (Australian company number)
  +  `TM` (Trademark number)
+  `AU_ELIGIBILITY_TYPE`

  Valid values include the following:
  + CHARITABLE\_TRUST (Charitable trust)
  + CHARITY (Charity)
  + CHILD\_CARE\_CENTRE (Child care centre)
  + CLUB (Club)
  + COMMERCIAL\_STATUTORY\_BODY (Commercial statutory body)
  + COMMONWEALTH\_ENTITY (Commonwealth entity)
  + COMPANY (Company)
  + COMPANY\_LIMITED\_BY\_GUARANTEE (Company limited by guarantee)
  + EDUCATIONAL\_INSTITUTION (Educational institution)
  + GOVERNMENT\_SCHOOL (Government school)
  + HIGHER\_EDUCATION\_INSTITUTION (Higher education institution)
  + INCORPORATED\_ASSOCIATION (Incorporated association)
  + INDIGENOUS\_CORPORATION (Indigenous corporation)
  + INDUSTRY\_BODY (Industry body)
  + INDUSTRY\_ORGANISATION (Industry association)
  + NATIONAL\_BODY (National body)
  + NON\_DISTRIBUTING\_COOPERATIVE (Non-distributing cooperative)
  + NON\_GOVERNMENT\_SCHOOL (Non-government school)
  + NON\_PROFIT\_ORGANISATION (Non-profit organisation)
  + NON\_TRADING\_COOPERATIVE (Non-trading cooperative)
  + NOT\_FOR\_PROFIT\_COMMUNITY\_GROUP (Not-for-profit community group)
  + PARTNERSHIP (Partnership)
  + PEAK\_STATE\_TERRITORY\_BODY (Peak state/territory body)
  + PENDING\_TM\_OWNER (Pending TM owner)
  + POLITICAL\_PARTY (Political party)
  + PRESCHOOL (Pre-school)
  + PUBLIC\_PRIVATE\_ANCILLARY\_FUND (Public/private ancillary fund)
  + REGISTERED\_BUSINESS (Registered business)
  + REGISTERED\_ORGANISATION (Registered organisation)
  + REGISTRABLE\_BODY (Registrable body)
  + RESEARCH\_ORGANISATION (Research organisation)
  + STATUTORY\_BODY (Statutory body)
  + TRADE\_UNION (Trade union)
  + TRADEMARK\_OWNER (Trademark owner)
  + TRADING\_COOPERATIVE (Trading cooperative)
  + TRAINING\_ORGANISATION (Training organisation)
  + TRUST (Trust)
  + UNINCORPORATED\_ASSOCIATION (Unincorporated association)
  + EDUCATION\_AND\_CARE\_SERVICES\_CHILDCARE (Education and care services (child care))
  + GOVERNMENT\_BODY (Government body)
  + PROVIDER\_OF\_NON\_ACCREDITED\_TRAINING (Provider of non-accredited training)
  + RELIGIOUS\_CHURCH\_GROUP (Religious/church group)
  + SOLE\_TRADER (Sole trader)
+  `AU_POLICY_REASON`

  Valid values include the following:
  +  `POLICY_REASON_1`

     `POLICY_REASON_2`
.ca
+  `BRAND_NUMBER`
+  `CA_BUSINESS_ENTITY_TYPE`

  Valid values include the following:
  +  `BANK` (Bank)
  +  `COMMERCIAL_COMPANY` (Commercial company)
  +  `COMPANY` (Company)
  +  `COOPERATION` (Cooperation)
  +  `COOPERATIVE` (Cooperative)
  +  `COOPRIX` (Cooprix)
  +  `CORP` (Corporation)
  +  `CREDIT_UNION` (Credit union)
  +  `FOMIA` (Federation of mutual insurance associations)
  +  `INC` (Incorporated)
  +  `LTD` (Limited)
  +  `LTEE` (Limitée)
  +  `LLC` (Limited liability corporation)
  +  `LLP` (Limited liability partnership)
  +  `LTE` (Lte.)
  +  `MBA` (Mutual benefit association)
  +  `MIC` (Mutual insurance company)
  +  `NFP` (Not-for-profit corporation)
  +  `SA` (S.A.)
  +  `SAVINGS_COMPANY` (Savings company)
  +  `SAVINGS_UNION` (Savings union)
  +  `SARL` (Société à responsabilité limitée)
  +  `TRUST` (Trust)
  +  `ULC` (Unlimited liability corporation)
+  `CA_LEGAL_TYPE`

  When `ContactType` is `PERSON`, valid values include the following:
  +  `ABO` (Aboriginal Peoples indigenous to Canada)
  +  `CCT` (Canadian citizen)
  +  `LGR` (Legal Representative of a Canadian Citizen or Permanent Resident)
  +  `RES` (Permanent resident of Canada)

  When `ContactType` is a value other than `PERSON`, valid values include the following:
  +  `ASS` (Canadian unincorporated association)
  +  `CCO` (Canadian corporation)
  +  `EDU` (Canadian educational institution)
  +  `GOV` (Government or government entity in Canada)
  +  `HOP` (Canadian Hospital)
  +  `INB` (Indian Band recognized by the Indian Act of Canada)
  +  `LAM` (Canadian Library, Archive, or Museum)
  +  `MAJ` (Her/His Majesty the Queen/King)
  +  `OMK` (Official mark registered in Canada)
  +  `PLT` (Canadian Political Party)
  +  `PRT` (Partnership Registered in Canada)
  +  `TDM` (Trademark registered in Canada)
  +  `TRD` (Canadian Trade Union)
  +  `TRS` (Trust established in Canada)
.es
+  `ES_IDENTIFICATION`

  The value of `ES_IDENTIFICATION` depends on the following values:
  + The value of `ES_LEGAL_FORM`
  + The value of `ES_IDENTIFICATION_TYPE`

   **If `ES_LEGAL_FORM` is any value other than `INDIVIDUAL`:**
  + Specify 1 letter \+ 8 numbers (CIF [Certificado de Identificación Fiscal])
  + Example: B12345678

   **If `ES_LEGAL_FORM` is `INDIVIDUAL`, the value that you specify for `ES_IDENTIFICATION` depends on the value of `ES_IDENTIFICATION_TYPE`:**
  + If `ES_IDENTIFICATION_TYPE` is `DNI_AND_NIF` (for Spanish contacts):
    + Specify 8 numbers \+ 1 letter (DNI [Documento Nacional de Identidad], NIF [Número de Identificación Fiscal])
    + Example: 12345678M
  + If `ES_IDENTIFICATION_TYPE` is `NIE` (for foreigners with legal residence):
    + Specify 1 letter \+ 7 numbers \+ 1 letter ( NIE [Número de Identidad de Extranjero])
    + Example: Y1234567X
  + If `ES_IDENTIFICATION_TYPE` is `OTHER` (for contacts outside of Spain):
    + Specify a passport number, drivers license number, or national identity card number
+  `ES_IDENTIFICATION_TYPE`

  Valid values include the following:
  +  `DNI_AND_NIF` (For Spanish contacts)
  +  `NIE` (For foreigners with legal residence)
  +  `OTHER` (For contacts outside of Spain)
+  `ES_LEGAL_FORM`

  Valid values include the following:
  +  `ASSOCIATION`
  +  `CENTRAL_GOVERNMENT_BODY`
  +  `CIVIL_SOCIETY`
  +  `COMMUNITY_OF_OWNERS`
  +  `COMMUNITY_PROPERTY`
  +  `CONSULATE`
  +  `COOPERATIVE`
  +  `DESIGNATION_OF_ORIGIN_SUPERVISORY_COUNCIL`
  +  `ECONOMIC_INTEREST_GROUP`
  +  `EMBASSY`
  +  `ENTITY_MANAGING_NATURAL_AREAS`
  +  `FARM_PARTNERSHIP`
  +  `FOUNDATION`
  +  `GENERAL_AND_LIMITED_PARTNERSHIP`
  +  `GENERAL_PARTNERSHIP`
  +  `INDIVIDUAL`
  +  `LIMITED_COMPANY`
  +  `LOCAL_AUTHORITY`
  +  `LOCAL_PUBLIC_ENTITY`
  +  `MUTUAL_INSURANCE_COMPANY`
  +  `NATIONAL_PUBLIC_ENTITY`
  +  `ORDER_OR_RELIGIOUS_INSTITUTION`
  +  `OTHERS (Only for contacts outside of Spain)`
  +  `POLITICAL_PARTY`
  +  `PROFESSIONAL_ASSOCIATION`
  +  `PUBLIC_LAW_ASSOCIATION`
  +  `PUBLIC_LIMITED_COMPANY`
  +  `REGIONAL_GOVERNMENT_BODY`
  +  `REGIONAL_PUBLIC_ENTITY`
  +  `SAVINGS_BANK`
  +  `SPANISH_OFFICE`
  +  `SPORTS_ASSOCIATION`
  +  `SPORTS_FEDERATION`
  +  `SPORTS_LIMITED_COMPANY`
  +  `TEMPORARY_ALLIANCE_OF_ENTERPRISES`
  +  `TRADE_UNION`
  +  `WORKER_OWNED_COMPANY`
  +  `WORKER_OWNED_LIMITED_COMPANY`
.eu
+  ` EU_COUNTRY_OF_CITIZENSHIP`
.fi
+  `BIRTH_DATE_IN_YYYY_MM_DD`
+  `FI_BUSINESS_NUMBER`
+  `FI_ID_NUMBER`
+  `FI_NATIONALITY`

  Valid values include the following:
  +  `FINNISH`
  +  `NOT_FINNISH`
+  `FI_ORGANIZATION_TYPE`

  Valid values include the following:
  +  `COMPANY`
  +  `CORPORATION`
  +  `GOVERNMENT`
  +  `INSTITUTION`
  +  `POLITICAL_PARTY`
  +  `PUBLIC_COMMUNITY`
  +  `TOWNSHIP`
.it
+  `IT_NATIONALITY`
+  `IT_PIN`
+  `IT_REGISTRANT_ENTITY_TYPE`

  Valid values include the following:
  +  `FOREIGNERS`
  +  `FREELANCE_WORKERS` (Freelance workers and professionals)
  +  `ITALIAN_COMPANIES` (Italian companies and one-person companies)
  +  `NON_PROFIT_ORGANIZATIONS`
  +  `OTHER_SUBJECTS`
  +  `PUBLIC_ORGANIZATIONS`
.ru
+  `BIRTH_DATE_IN_YYYY_MM_DD`
+  `RU_PASSPORT_DATA`
.se
+  `BIRTH_COUNTRY`
+  `SE_ID_NUMBER`
.sg
+  `SG_ID_NUMBER`
.uk, .co.uk, .me.uk, and .org.uk
+  `UK_CONTACT_TYPE`

  Valid values include the following:
  +  `CRC` (UK Corporation by Royal Charter)
  +  `FCORP` (Non-UK Corporation)
  +  `FIND` (Non-UK Individual, representing self)
  +  `FOTHER` (Non-UK Entity that does not fit into any other category)
  +  `GOV` (UK Government Body)
  +  `IND` (UK Individual (representing self))
  +  `IP` (UK Industrial/Provident Registered Company)
  +  `LLP` (UK Limited Liability Partnership)
  +  `LTD` (UK Limited Company)
  +  `OTHER` (UK Entity that does not fit into any other category)
  +  `PLC` (UK Public Limited Company)
  +  `PTNR` (UK Partnership)
  +  `RCHAR` (UK Registered Charity)
  +  `SCH` (UK School)
  +  `STAT` (UK Statutory Body)
  +  `STRA` (UK Sole Trader)
+  `UK_COMPANY_NUMBER`
In addition, many TLDs require a `VAT_NUMBER`.
Type: String
Valid Values: `DUNS_NUMBER | BRAND_NUMBER | BIRTH_DEPARTMENT | BIRTH_DATE_IN_YYYY_MM_DD | BIRTH_COUNTRY | BIRTH_CITY | DOCUMENT_NUMBER | AU_ID_NUMBER | AU_ID_TYPE | CA_LEGAL_TYPE | CA_BUSINESS_ENTITY_TYPE | CA_LEGAL_REPRESENTATIVE | CA_LEGAL_REPRESENTATIVE_CAPACITY | ES_IDENTIFICATION | ES_IDENTIFICATION_TYPE | ES_LEGAL_FORM | FI_BUSINESS_NUMBER | FI_ID_NUMBER | FI_NATIONALITY | FI_ORGANIZATION_TYPE | IT_NATIONALITY | IT_PIN | IT_REGISTRANT_ENTITY_TYPE | RU_PASSPORT_DATA | SE_ID_NUMBER | SG_ID_NUMBER | VAT_NUMBER | UK_CONTACT_TYPE | UK_COMPANY_NUMBER | EU_COUNTRY_OF_CITIZENSHIP | AU_PRIORITY_TOKEN | AU_ELIGIBILITY_TYPE | AU_POLICY_REASON | AU_REGISTRANT_NAME`
Required: Yes

 ** Value **   <a name="Route53Domains-Type-domains_ExtraParam-Value"></a>
The value that corresponds with the name of an extra parameter.
Type: String
Length Constraints: Maximum length of 2048.
Required: Yes

## See Also
<a name="API_domains_ExtraParam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/ExtraParam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/ExtraParam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/ExtraParam)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
