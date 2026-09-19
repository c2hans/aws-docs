---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_BatchPutTaxRegistration.html
---

# BatchPutTaxRegistration
<a name="API_taxSettings_BatchPutTaxRegistration"></a>

Adds or updates tax registration for multiple accounts in batch. This can be used to add or update tax registrations for up to five accounts in one batch. You can't set a TRN if there's a pending TRN. You'll need to delete the pending TRN first.

To call this API operation for specific countries, see the following country-specific requirements.

 **Bangladesh**
+ You must specify the tax registration certificate document in the `taxRegistrationDocuments` field of the `VerificationDetails` object.

 **Brazil**
+ You must complete the tax registration process in the [Payment preferences](https://console.aws.amazon.com/billing/home#/paymentpreferences/paymentmethods) page in the AWS Billing and Cost Management console. After your TRN and billing address are verified, you can call this API operation.
+ For AWS accounts created through AWS Organizations, you can call this API operation when you don't have a billing address.

 **Georgia**
+ The valid `personType` values are `Physical Person` and `Business`.

 **Indonesia**
+  `PutTaxRegistration`: The use of this operation to submit tax information is subject to the [AWS service terms](http://aws.amazon.com/service-terms/). By submitting, you’re providing consent for AWS to validate NIK, NPWP, and NITKU data, provided by you with the Directorate General of Taxes of Indonesia in accordance with the Minister of Finance Regulation (PMK) Number 112/PMK.03/2022.
+  `BatchPutTaxRegistration`: The use of this operation to submit tax information is subject to the [AWS service terms](http://aws.amazon.com/service-terms/). By submitting, you’re providing consent for AWS to validate NIK, NPWP, and NITKU data, provided by you with the Directorate General of Taxes of Indonesia in accordance with the Minister of Finance Regulation (PMK) Number 112/PMK.03/2022, through our third-party partner PT Achilles Advanced Management (OnlinePajak).
+ You must specify the `taxRegistrationNumberType` in the `indonesiaAdditionalInfo` field of the `additionalTaxInformation` object.
+ If you specify `decisionNumber`, you must specify the `ppnExceptionDesignationCode` in the `indonesiaAdditionalInfo` field of the `additionalTaxInformation` object. If the `taxRegistrationNumberType` is set to NPWP or NITKU, valid values for `ppnExceptionDesignationCode` are either `01`, `02`, `03`, `07`, or `08`.

  For other `taxRegistrationNumberType` values, `ppnExceptionDesignationCode` must be either `01`, `07`, or `08`.
+ If `ppnExceptionDesignationCode` is `07` or `08`, you must specify the `decisionNumber` in the `indonesiaAdditionalInfo` field of the `additionalTaxInformation` object.

 **Kenya**
+ You must specify the `personType` in the `kenyaAdditionalInfo` field of the `additionalTaxInformation` object.
+ If the `personType` is `Physical Person`, you must specify the tax registration certificate document in the `taxRegistrationDocuments` field of the `VerificationDetails` object.

 **Malaysia**
+ The sector valid values are `Business` and `Individual`.
+  `RegistrationType` valid values are `NRIC` for individual, and TIN and sales and service tax (SST) for Business.
+ For individual, you can specify the `taxInformationNumber` in `MalaysiaAdditionalInfo` with NRIC type, and a valid `MyKad` or NRIC number.
+ For business, you must specify a `businessRegistrationNumber` in `MalaysiaAdditionalInfo` with a TIN type and tax identification number.
+ For business resellers, you must specify a `businessRegistrationNumber` and `taxInformationNumber` in `MalaysiaAdditionalInfo` with a sales and service tax (SST) type and a valid SST number.
+ For business resellers with service codes, you must specify `businessRegistrationNumber`, `taxInformationNumber`, and distinct `serviceTaxCodes` in `MalaysiaAdditionalInfo` with a SST type and valid sales and service tax (SST) number. By using this API operation, AWS registers your self-declaration that you’re an authorized business reseller registered with the Royal Malaysia Customs Department (RMCD), and have a valid SST number.
+  AWS reserves the right to seek additional information and/or take other actions to support your self-declaration as appropriate.
+  AWS is currently registered under the following service tax codes. You must include at least one of the service tax codes in the service tax code strings to declare yourself as an authorized registered business reseller.

  Taxable service and service tax codes:

  Consultancy - 9907061674

  Training or coaching service - 9907071685

  IT service - 9907101676

  Digital services and electronic medium - 9907121690

 **Mexico**
+ You must provide a Constancia de Situación fiscal (CSF) document in the **verificationDetails** field.
+ You do not need to provide address and legal name. These will be populated based on your tax registration number.

 **Nepal**
+ The sector valid values are `Business` and `Individual`.

 **Saudi Arabia**
+ For `address`, you must specify `addressLine3`.

 **South Korea**
+ You must specify the `certifiedEmailId` and `legalName` in the `TaxRegistrationEntry` object. Use Korean characters for `legalName`.
+ You must specify the `businessRepresentativeName`, `itemOfBusiness`, and `lineOfBusiness` in the `southKoreaAdditionalInfo` field of the `additionalTaxInformation` object. Use Korean characters for these fields.
+ You must specify the tax registration certificate document in the `taxRegistrationDocuments` field of the `VerificationDetails` object.
+ For the `address` object, use Korean characters for `addressLine1`, `addressLine2` `city`, `postalCode`, and `stateOrRegion`.

 **Spain**
+ You must specify the `registrationType` in the `spainAdditionalInfo` field of the `additionalTaxInformation` object.
+ If the `registrationType` is `Local`, you must specify the tax registration certificate document in the `taxRegistrationDocuments` field of the `VerificationDetails` object.

 **Turkey**
+ You must specify the `sector` in the `taxRegistrationEntry` object.
+ If your `sector` is `Business`, `Individual`, or `Government`:
  + Specify the `taxOffice`. If your `sector` is `Individual`, don't enter this value.
  + (Optional) Specify the `kepEmailId`. If your `sector` is `Individual`, don't enter this value.
  +  **Note:** In the **Tax Settings** page of the AWS Billing console, `Government` appears as **Public institutions**
+ If your `sector` is `Business` and you're subject to KDV tax, you must specify your industry in the `industries` field.
+ For `address`, you must specify `districtOrCounty`.

 **Ukraine**
+ The sector valid values are `Business` and `Individual`.

 **Philippines**
+ You can optionally specify the `isVatRegistered` in the `philippinesAdditionalInfo` field of the `additionalTaxInformation` object to indicate your VAT registration status with the Bureau of Internal Revenue (BIR).

 **Belgium**
+ You can optionally specify the `peppolId` in the `belgiumAdditionalInfo` field of the `additionalTaxInformation` object.

 **Chile**
+ You can optionally specify the `documentType` and `businessActivity` in the `chileAdditionalInfo` field of the `additionalTaxInformation` object.

 **France**
+ You must specify the `sirenNumber` in the `franceAdditionalInfo` field of the `additionalTaxInformation` object.
+ You can optionally specify the `eInvoiceRoutingCode` in the `franceAdditionalInfo` field of the `additionalTaxInformation` object.

 **Monaco**
+ You must specify the `businessNumber` in the `monacoAdditionalInfo` field of the `additionalTaxInformation` object.

 **Germany**
+ You must provide at least one of the following: a Tax Registration Number (TRN) (`registrationId`), the `economicIdentificationNumber`, or the `steuernummer`.
+ You can optionally specify the `economicIdentificationNumber` (Wirtschafts-Identifikationsnummer, or W-IdNr) and the `steuernummer` (tax number issued by the local tax office) in the `germanyAdditionalInfo` field of the `additionalTaxInformation` object.

 **Poland**
+ You can optionally specify the `taxRegistrationNumberType` in the `polandAdditionalInfo` field of the `additionalTaxInformation` object. Valid values are `EUTaxRegistrationNumber`, `LocalTaxRegistrationNumber`, or `LocalRegistrationNumber`.

## Request Syntax
<a name="API_taxSettings_BatchPutTaxRegistration_RequestSyntax"></a>

```
POST /BatchPutTaxRegistration HTTP/1.1
Content-type: application/json

{
   "accountIds": [ "{{string}}" ],
   "taxRegistrationEntry": {
      "additionalTaxInformation": {
         "belgiumAdditionalInfo": {
            "isMercuriusBoxEnabled": {{boolean}},
            "peppolId": "{{string}}"
         },
         "canadaAdditionalInfo": {
            "canadaQuebecSalesTaxNumber": "{{string}}",
            "canadaRetailSalesTaxNumber": "{{string}}",
            "isResellerAccount": {{boolean}},
            "provincialSalesTaxId": "{{string}}"
         },
         "chileAdditionalInfo": {
            "businessActivity": "{{string}}",
            "documentType": "{{string}}"
         },
         "egyptAdditionalInfo": {
            "uniqueIdentificationNumber": "{{string}}",
            "uniqueIdentificationNumberExpirationDate": "{{string}}"
         },
         "estoniaAdditionalInfo": {
            "registryCommercialCode": "{{string}}"
         },
         "franceAdditionalInfo": {
            "eInvoiceRoutingCode": "{{string}}",
            "sirenNumber": "{{string}}"
         },
         "georgiaAdditionalInfo": {
            "personType": "{{string}}"
         },
         "germanyAdditionalInfo": {
            "economicIdentificationNumber": "{{string}}",
            "steuernummer": "{{string}}"
         },
         "greeceAdditionalInfo": {
            "contractingAuthorityCode": "{{string}}"
         },
         "indonesiaAdditionalInfo": {
            "decisionNumber": "{{string}}",
            "ppnExceptionDesignationCode": "{{string}}",
            "taxRegistrationNumberType": "{{string}}"
         },
         "israelAdditionalInfo": {
            "customerType": "{{string}}",
            "dealerType": "{{string}}"
         },
         "italyAdditionalInfo": {
            "cigNumber": "{{string}}",
            "cupNumber": "{{string}}",
            "customerType": "{{string}}",
            "sdiAccountId": "{{string}}",
            "taxCode": "{{string}}"
         },
         "kenyaAdditionalInfo": {
            "personType": "{{string}}"
         },
         "malaysiaAdditionalInfo": {
            "businessRegistrationNumber": "{{string}}",
            "serviceTaxCodes": [ "{{string}}" ],
            "taxInformationNumber": "{{string}}"
         },
         "monacoAdditionalInfo": {
            "businessNumber": "{{string}}"
         },
         "philippinesAdditionalInfo": {
            "isVatRegistered": {{boolean}}
         },
         "polandAdditionalInfo": {
            "individualRegistrationNumber": "{{string}}",
            "isGroupVatEnabled": {{boolean}},
            "taxRegistrationNumberType": "{{string}}"
         },
         "romaniaAdditionalInfo": {
            "taxRegistrationNumberType": "{{string}}"
         },
         "saudiArabiaAdditionalInfo": {
            "taxRegistrationNumberType": "{{string}}"
         },
         "southKoreaAdditionalInfo": {
            "businessRepresentativeName": "{{string}}",
            "itemOfBusiness": "{{string}}",
            "lineOfBusiness": "{{string}}"
         },
         "spainAdditionalInfo": {
            "registrationType": "{{string}}"
         },
         "turkeyAdditionalInfo": {
            "industries": "{{string}}",
            "kepEmailId": "{{string}}",
            "secondaryTaxId": "{{string}}",
            "taxOffice": "{{string}}"
         },
         "ukraineAdditionalInfo": {
            "ukraineTrnType": "{{string}}"
         },
         "uzbekistanAdditionalInfo": {
            "taxRegistrationNumberType": "{{string}}",
            "vatRegistrationNumber": "{{string}}"
         },
         "vietnamAdditionalInfo": {
            "electronicTransactionCodeNumber": "{{string}}",
            "enterpriseIdentificationNumber": "{{string}}",
            "paymentVoucherNumber": "{{string}}",
            "paymentVoucherNumberDate": "{{string}}"
         }
      },
      "certifiedEmailId": "{{string}}",
      "legalAddress": {
         "addressLine1": "{{string}}",
         "addressLine2": "{{string}}",
         "addressLine3": "{{string}}",
         "city": "{{string}}",
         "countryCode": "{{string}}",
         "districtOrCounty": "{{string}}",
         "postalCode": "{{string}}",
         "stateOrRegion": "{{string}}"
      },
      "legalName": "{{string}}",
      "registrationId": "{{string}}",
      "registrationType": "{{string}}",
      "sector": "{{string}}",
      "verificationDetails": {
         "dateOfBirth": "{{string}}",
         "taxRegistrationDocuments": [
            {
               "file": {
                  "fileContent": {{blob}},
                  "fileName": "{{string}}"
               },
               "s3Location": {
                  "bucket": "{{string}}",
                  "key": "{{string}}"
               }
            }
         ]
      }
   }
}
```

## URI Request Parameters
<a name="API_taxSettings_BatchPutTaxRegistration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_taxSettings_BatchPutTaxRegistration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountIds](#API_taxSettings_BatchPutTaxRegistration_RequestSyntax) **   <a name="awscostmanagement-taxSettings_BatchPutTaxRegistration-request-accountIds"></a>
 List of unique account identifiers.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 550 items.
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** [taxRegistrationEntry](#API_taxSettings_BatchPutTaxRegistration_RequestSyntax) **   <a name="awscostmanagement-taxSettings_BatchPutTaxRegistration-request-taxRegistrationEntry"></a>
Your TRN information that will be stored to the accounts mentioned in `putEntries`.
Type: [TaxRegistrationEntry](API_taxSettings_TaxRegistrationEntry.md) object
Required: Yes

## Response Syntax
<a name="API_taxSettings_BatchPutTaxRegistration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "accountId": "string",
         "code": "string",
         "message": "string"
      }
   ],
   "status": "string"
}
```

## Response Elements
<a name="API_taxSettings_BatchPutTaxRegistration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_taxSettings_BatchPutTaxRegistration_ResponseSyntax) **   <a name="awscostmanagement-taxSettings_BatchPutTaxRegistration-response-errors"></a>
List of errors for the accounts the TRN information could not be added or updated to.
Type: Array of [BatchPutTaxRegistrationError](API_taxSettings_BatchPutTaxRegistrationError.md) objects

 ** [status](#API_taxSettings_BatchPutTaxRegistration_ResponseSyntax) **   <a name="awscostmanagement-taxSettings_BatchPutTaxRegistration-response-status"></a>
The status of your TRN stored in the system after processing. Based on the validation occurring on the TRN, the status can be `Verified`, `Pending` or `Rejected`.
Type: String
Valid Values: `Verified | Pending | Deleted | Rejected`

## Errors
<a name="API_taxSettings_BatchPutTaxRegistration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The exception when the input is creating conflict with the given state.
 ** errorCode **
409
HTTP Status Code: 409

 ** InternalServerException **
The exception thrown when an unexpected error occurs when processing a request.
 ** errorCode **
500
HTTP Status Code: 500

 ** ValidationException **
The exception when the input doesn't pass validation for at least one of the input parameters.
 ** errorCode **
400
 ** fieldList **
400
HTTP Status Code: 400

## See Also
<a name="API_taxSettings_BatchPutTaxRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/taxsettings-2018-05-10/BatchPutTaxRegistration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/taxsettings-2018-05-10/BatchPutTaxRegistration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/BatchPutTaxRegistration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/taxsettings-2018-05-10/BatchPutTaxRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/BatchPutTaxRegistration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/taxsettings-2018-05-10/BatchPutTaxRegistration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/taxsettings-2018-05-10/BatchPutTaxRegistration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/taxsettings-2018-05-10/BatchPutTaxRegistration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/taxsettings-2018-05-10/BatchPutTaxRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/BatchPutTaxRegistration)
