---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/es.html
---

# .es (Spain)

[Return to index](registrar-tld-list.md#index)

**Domain purchase or transfer**
You currently can purchase new .es domain names or transfer .es domains to Route 53 . The contact type for the registrant contact has no restriction. Admin / Tech / Billing contact type must be a **person**.

**Lease period for registration and renewal**
One to five years.

**Restrictions**
Open to the public, for those who have an interest in or connection with Spain.
The .es registry requires contacts located in the following countries to provide an identification number in the format listed for that country. The format depends on whether the contact is an individual (contact type **Person**) or an organization.
Provide the identification number in the `ES_IDENTIFICATION` extra parameter. For contacts located outside Spain, set `ES_IDENTIFICATION_TYPE` to `OTHER`. For more information, see [ExtraParam](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ExtraParam.html).
For a contact that is an individual, provide the identification number in the following format:
+ Spain: for Spanish nationals, the tax identification number (NIF), 8 digits followed by a letter, for example `12345678A`; for foreign nationals, the foreigner identification number (NIE), a letter followed by 7 digits and a letter, for example `X1234567L`.
+ United States: the Social Security Number (SSN), 9 digits in the format `XXX-XX-XXXX`, for example `123-45-6789`.
+ Germany: the tax identification number (Steuer-ID), 11 digits with no spaces, for example `12345678901`.
+ Netherlands: the citizen service number (BSN), 9 digits, for example `123456789`.
+ France: 13 digits, for example `1800275012345`.
+ Italy: the tax code (Codice Fiscale), 16 alphanumeric characters, for example `RSSMRA85T10A562S`.
+ Great Britain: the Unique Taxpayer Reference (UTR), 10 digits, for example `1234567890`.
+ Switzerland: the social insurance number (AHV), 13 digits with no spaces, for example `7561234567897`.
+ Poland: the national identification number (PESEL), 11 digits, for example `44051401458`.
+ Mexico: the Federal Taxpayer Registry number (RFC), 13 alphanumeric characters, for example `ABCD800101XYZ`.
+ Sweden: the personal identity number (Personnummer), in the format `YYYYMMDD-XXXX`, for example `19800101-1234`.
+ Russia: the taxpayer identification number (INN), 12 digits, for example `123456789012`.
+ Mainland China: the Resident Identity Card number, 18 characters that can include a letter, for example `11010519491231002X`.
For a registrant contact that is an organization, provide the identification number in the following format:
+ Spain: the tax identification number (NIF), either a letter followed by 8 digits, for example `A12345678`, or a letter followed by 7 digits and a letter, for example `A1234567B`.
+ United States: the Employer Identification Number (EIN), in the format `12-3456789`.
+ Germany: the economic identification number (W-IdNr), 9 digits, for example `123456789`.
+ Netherlands: the Chamber of Commerce number (KVK), 8 digits, for example `12345678`.
+ France: the business identification number (SIREN), 9 digits, for example `123456789`.
+ Italy: the value-added tax number (Partita IVA), 11 digits, for example `12345678901`.
+ Great Britain: the company number, 8 digits, for example `12345678`.
+ Switzerland: the business identification number (UID), 9 digits, for example `123456789`.
+ Poland: the tax identification number (NIP), 10 digits, for example `1234567890`.
+ Mexico: the Federal Taxpayer Registry number (RFC), for example `ABC010101ABC`.
+ Sweden: the organization number (Organisationsnummer), for example `1234567890`.
+ Russia: the primary state registration number (OGRN), 13 digits, for example `1234567890123`.
+ Mainland China: the Unified Social Credit Code, 18 alphanumeric characters, for example `9154030671527786PG`.
As of 2016, the .ES domain registrants must provide a registrant contact email. If you haven't provided this information, you need to do so at the current registrar before you transfer your domain to Route 53.
You will need the following information:
+ ESNIC identifier similar to {{AAAA0-ESNIC-F0}}.
+ If you don't know your ESNIC identifier, you can get it from the current registrar. You can find your registrar at: [https://www.dominios.es/en](https://www.dominios.es/en).
Depending on whether you remember your password at the registrar, or not, you can follow one of the following procedures to update your registrant email:
+ If you remember you password, sign in at [https://www.nic.es/sgnd/login.action](https://www.nic.es/sgnd/login.action) by using you ESNIC identifies and password.

  After you have signed in, you can edit the registrant email contact by choosing the **Edit** tab on the registry page.
+ If you forgot your password, browse to [https://www.nic.es/sgnd/peticion/editCorreo.action?request\_locale=en](https://www.nic.es/sgnd/peticion/editCorreo.action?request_locale=en).

  Fill out the form with your ESNIC identifier, your new and valid registrant email contact. Then, validate the form by choosing **Processing without eID/Certificate**, and upload the requested identity document.

**Privacy protection**
Not supported.

**Domain locking to prevent unauthorized transfers**
Not supported. We recommend that you prevent unauthorized transfers by restricting access to the [RetrieveDomainAuthCode](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RetrieveDomainAuthCode.html) operation. (When you restrict access to this Route 53 API, you also restrict who can generate an authorization code using the Route 53 console, AWS SDKs, and other programmatic methods.) For more information, see [Identity and access management in Amazon Route 53](security-iam.md).

**Internationalized domain names**
Supported.

**Authorization code required for transfers**
Yes
The .es registry manages the authorization code with a time-to-live, so it might expire. If your authorization code doesn't work, contact [AWS Support](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-contact-support.html).

**DNSSEC**
Supported for domain registration. For more information, see [Configuring DNSSEC for a domain](domain-configure-dnssec.md).

**Deadlines for renewing and restoring domains**
+ Renewal is possible: Until 6 days before the expiration date
+ Late renewal with Route 53 is possible: No
+ Domain is deleted from Route 53: 6 days before expiration
+ Restoration with the registry is possible: Between 6 days before and 4 days after expiration
+ Domain is deleted from the registry: 4 days after expiration
