---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_PutSupplementalTaxRegistration.html
---

# PutSupplementalTaxRegistration
<a name="API_taxSettings_PutSupplementalTaxRegistration"></a>

 Stores supplemental tax registration for a single account.

## Request Syntax
<a name="API_taxSettings_PutSupplementalTaxRegistration_RequestSyntax"></a>

```
POST /PutSupplementalTaxRegistration HTTP/1.1
Content-type: application/json

{
   "taxRegistrationEntry": {
      "address": {
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
      "registrationType": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_taxSettings_PutSupplementalTaxRegistration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_taxSettings_PutSupplementalTaxRegistration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [taxRegistrationEntry](#API_taxSettings_PutSupplementalTaxRegistration_RequestSyntax) **   <a name="awscostmanagement-taxSettings_PutSupplementalTaxRegistration-request-taxRegistrationEntry"></a>
 The supplemental TRN information that will be stored for the caller account ID.
Type: [SupplementalTaxRegistrationEntry](API_taxSettings_SupplementalTaxRegistrationEntry.md) object
Required: Yes

## Response Syntax
<a name="API_taxSettings_PutSupplementalTaxRegistration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "authorityId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_taxSettings_PutSupplementalTaxRegistration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [authorityId](#API_taxSettings_PutSupplementalTaxRegistration_ResponseSyntax) **   <a name="awscostmanagement-taxSettings_PutSupplementalTaxRegistration-response-authorityId"></a>
 Unique authority ID for the supplemental TRN information that was stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[\s\S]*`

 ** [status](#API_taxSettings_PutSupplementalTaxRegistration_ResponseSyntax) **   <a name="awscostmanagement-taxSettings_PutSupplementalTaxRegistration-response-status"></a>
 The status of the supplemental TRN stored in the system after processing. Based on the validation occurring on the TRN, the status can be `Verified`, `Pending`, `Rejected`, or `Deleted`.
Type: String
Valid Values: `Verified | Pending | Deleted | Rejected`

## Errors
<a name="API_taxSettings_PutSupplementalTaxRegistration_Errors"></a>

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
<a name="API_taxSettings_PutSupplementalTaxRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/taxsettings-2018-05-10/PutSupplementalTaxRegistration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/taxsettings-2018-05-10/PutSupplementalTaxRegistration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/PutSupplementalTaxRegistration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/taxsettings-2018-05-10/PutSupplementalTaxRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/PutSupplementalTaxRegistration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/taxsettings-2018-05-10/PutSupplementalTaxRegistration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/taxsettings-2018-05-10/PutSupplementalTaxRegistration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/taxsettings-2018-05-10/PutSupplementalTaxRegistration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/taxsettings-2018-05-10/PutSupplementalTaxRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/PutSupplementalTaxRegistration)
