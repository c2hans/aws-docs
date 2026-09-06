---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_GetTaxRegistration.html
---

# GetTaxRegistration
<a name="API_taxSettings_GetTaxRegistration"></a>

Retrieves tax registration for a single account.

## Request Syntax
<a name="API_taxSettings_GetTaxRegistration_RequestSyntax"></a>

```
POST /GetTaxRegistration HTTP/1.1
Content-type: application/json

{
   "accountId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_taxSettings_GetTaxRegistration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_taxSettings_GetTaxRegistration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountId](#API_taxSettings_GetTaxRegistration_RequestSyntax) **   <a name="awscostmanagement-taxSettings_GetTaxRegistration-request-accountId"></a>
Your unique account identifier.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

## Response Syntax
<a name="API_taxSettings_GetTaxRegistration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
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
      "legalAddress": {
         "addressLine1": "string",
         "addressLine2": "string",
         "addressLine3": "string",
         "city": "string",
         "countryCode": "string",
         "districtOrCounty": "string",
         "postalCode": "string",
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
```

## Response Elements
<a name="API_taxSettings_GetTaxRegistration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [taxRegistration](#API_taxSettings_GetTaxRegistration_ResponseSyntax) **   <a name="awscostmanagement-taxSettings_GetTaxRegistration-response-taxRegistration"></a>
TRN information of the account mentioned in the request.
Type: [TaxRegistration](API_taxSettings_TaxRegistration.md) object

## Errors
<a name="API_taxSettings_GetTaxRegistration_Errors"></a>

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
<a name="API_taxSettings_GetTaxRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/taxsettings-2018-05-10/GetTaxRegistration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/taxsettings-2018-05-10/GetTaxRegistration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/GetTaxRegistration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/taxsettings-2018-05-10/GetTaxRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/GetTaxRegistration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/taxsettings-2018-05-10/GetTaxRegistration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/taxsettings-2018-05-10/GetTaxRegistration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/taxsettings-2018-05-10/GetTaxRegistration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/taxsettings-2018-05-10/GetTaxRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/GetTaxRegistration)
