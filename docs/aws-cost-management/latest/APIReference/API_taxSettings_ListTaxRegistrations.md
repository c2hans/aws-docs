---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_ListTaxRegistrations.html
---

# ListTaxRegistrations
<a name="API_taxSettings_ListTaxRegistrations"></a>

Retrieves the tax registration of accounts listed in a consolidated billing family. This can be used to retrieve up to 100 accounts' tax registrations in one call (default 50).

## Request Syntax
<a name="API_taxSettings_ListTaxRegistrations_RequestSyntax"></a>

```
POST /ListTaxRegistrations HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_taxSettings_ListTaxRegistrations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_taxSettings_ListTaxRegistrations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_taxSettings_ListTaxRegistrations_RequestSyntax) **   <a name="awscostmanagement-taxSettings_ListTaxRegistrations-request-maxResults"></a>
Number of `accountDetails` results you want in one response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_taxSettings_ListTaxRegistrations_RequestSyntax) **   <a name="awscostmanagement-taxSettings_ListTaxRegistrations-request-nextToken"></a>
The token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `[-A-Za-z0-9_+\=\/]+`
Required: No

## Response Syntax
<a name="API_taxSettings_ListTaxRegistrations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accountDetails": [
      {
         "accountId": "string",
         "accountMetaData": {
            "accountName": "string",
            "address": {
               "addressLine1": "string",
               "addressLine2": "string",
               "addressLine3": "string",
               "city": "string",
               "countryCode": "string",
               "districtOrCounty": "string",
               "postalCode": "string",
               "stateOrRegion": "string"
            },
            "addressRoleMap": {
               "string" : {
                  "countryCode": "string",
                  "stateOrRegion": "string"
               }
            },
            "addressType": "string",
            "seller": "string"
         },
         "taxInheritanceDetails": {
            "inheritanceObtainedReason": "string",
            "parentEntityId": "string"
         },
         "taxRegistration": {
            "additionalTaxInformation": {
               "belgiumAdditionalInfo": {
                  "isMercuriusBoxEnabled": boolean,
                  "peppolId": "string"
               },
               "brazilAdditionalInfo": {
                  "ccmCode": "string",
                  "legalNatureCode": "string"
               },
               "canadaAdditionalInfo": {
                  "canadaQuebecSalesTaxNumber": "string",
                  "canadaRetailSalesTaxNumber": "string",
                  "isResellerAccount": boolean,
                  "provincialSalesTaxId": "string"
               },
               "chileAdditionalInfo": {
                  "businessActivity": "string",
                  "documentType": "string"
               },
               "egyptAdditionalInfo": {
                  "uniqueIdentificationNumber": "string",
                  "uniqueIdentificationNumberExpirationDate": "string"
               },
               "estoniaAdditionalInfo": {
                  "registryCommercialCode": "string"
               },
               "franceAdditionalInfo": {
                  "sirenNumber": "string"
               },
               "georgiaAdditionalInfo": {
                  "personType": "string"
               },
               "greeceAdditionalInfo": {
                  "contractingAuthorityCode": "string"
               },
               "indiaAdditionalInfo": {
                  "pan": "string"
               },
               "indonesiaAdditionalInfo": {
                  "decisionNumber": "string",
                  "ppnExceptionDesignationCode": "string",
                  "taxRegistrationNumberType": "string"
               },
               "israelAdditionalInfo": {
                  "customerType": "string",
                  "dealerType": "string"
               },
               "italyAdditionalInfo": {
                  "cigNumber": "string",
                  "cupNumber": "string",
                  "customerType": "string",
                  "sdiAccountId": "string",
                  "taxCode": "string"
               },
               "kenyaAdditionalInfo": {
                  "personType": "string"
               },
               "malaysiaAdditionalInfo": {
                  "businessRegistrationNumber": "string",
                  "serviceTaxCodes": [ "string" ],
                  "taxInformationNumber": "string"
               },
               "philippinesAdditionalInfo": {
                  "isVatRegistered": boolean
               },
               "polandAdditionalInfo": {
                  "individualRegistrationNumber": "string",
                  "isGroupVatEnabled": boolean,
                  "taxRegistrationNumberType": "string"
               },
               "romaniaAdditionalInfo": {
                  "taxRegistrationNumberType": "string"
               },
               "saudiArabiaAdditionalInfo": {
                  "taxRegistrationNumberType": "string"
               },
               "southKoreaAdditionalInfo": {
                  "businessRepresentativeName": "string",
                  "itemOfBusiness": "string",
                  "lineOfBusiness": "string"
               },
               "spainAdditionalInfo": {
                  "registrationType": "string"
               },
               "turkeyAdditionalInfo": {
                  "industries": "string",
                  "kepEmailId": "string",
                  "secondaryTaxId": "string",
                  "taxOffice": "string"
               },
               "ukraineAdditionalInfo": {
                  "ukraineTrnType": "string"
               },
               "uzbekistanAdditionalInfo": {
                  "taxRegistrationNumberType": "string",
                  "vatRegistrationNumber": "string"
               },
               "vietnamAdditionalInfo": {
                  "electronicTransactionCodeNumber": "string",
                  "enterpriseIdentificationNumber": "string",
                  "paymentVoucherNumber": "string",
                  "paymentVoucherNumberDate": "string"
               }
            },
            "certifiedEmailId": "string",
            "jurisdiction": {
               "countryCode": "string",
               "stateOrRegion": "string"
            },
            "legalName": "string",
            "registrationId": "string",
            "registrationType": "string",
            "sector": "string",
            "status": "string",
            "taxDocumentMetadatas": [
               {
                  "taxDocumentAccessToken": "string",
                  "taxDocumentName": "string"
               }
            ]
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_taxSettings_ListTaxRegistrations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountDetails](#API_taxSettings_ListTaxRegistrations_ResponseSyntax) **   <a name="awscostmanagement-taxSettings_ListTaxRegistrations-response-accountDetails"></a>
The list of account details. This contains account Ids and TRN Information for each of the linked accounts.
Type: Array of [AccountDetails](API_taxSettings_AccountDetails.md) objects

 ** [nextToken](#API_taxSettings_ListTaxRegistrations_ResponseSyntax) **   <a name="awscostmanagement-taxSettings_ListTaxRegistrations-response-nextToken"></a>
 The token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `[-A-Za-z0-9_+\=\/]+`

## Errors
<a name="API_taxSettings_ListTaxRegistrations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The exception thrown when an unexpected error occurs when processing a request.
 ** errorCode **
500
HTTP Status Code: 500

 ** ResourceNotFoundException **
The exception thrown when the input doesn't have a resource associated to it.
 ** errorCode **
404
HTTP Status Code: 404

 ** ValidationException **
The exception when the input doesn't pass validation for at least one of the input parameters.
 ** errorCode **
400
 ** fieldList **
400
HTTP Status Code: 400

## See Also
<a name="API_taxSettings_ListTaxRegistrations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/taxsettings-2018-05-10/ListTaxRegistrations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/taxsettings-2018-05-10/ListTaxRegistrations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/ListTaxRegistrations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/taxsettings-2018-05-10/ListTaxRegistrations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/ListTaxRegistrations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/taxsettings-2018-05-10/ListTaxRegistrations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/taxsettings-2018-05-10/ListTaxRegistrations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/taxsettings-2018-05-10/ListTaxRegistrations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/taxsettings-2018-05-10/ListTaxRegistrations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/ListTaxRegistrations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
