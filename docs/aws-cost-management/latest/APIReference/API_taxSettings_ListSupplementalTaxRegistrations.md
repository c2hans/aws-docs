---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_ListSupplementalTaxRegistrations.html
---

# ListSupplementalTaxRegistrations
<a name="API_taxSettings_ListSupplementalTaxRegistrations"></a>

 Retrieves supplemental tax registrations for a single account.

## Request Syntax
<a name="API_taxSettings_ListSupplementalTaxRegistrations_RequestSyntax"></a>

```
POST /ListSupplementalTaxRegistrations HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_taxSettings_ListSupplementalTaxRegistrations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_taxSettings_ListSupplementalTaxRegistrations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_taxSettings_ListSupplementalTaxRegistrations_RequestSyntax) **   <a name="awscostmanagement-taxSettings_ListSupplementalTaxRegistrations-request-maxResults"></a>
 The number of `taxRegistrations` results you want in one response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_taxSettings_ListSupplementalTaxRegistrations_RequestSyntax) **   <a name="awscostmanagement-taxSettings_ListSupplementalTaxRegistrations-request-nextToken"></a>
 The token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `[-A-Za-z0-9_+\=\/]+`
Required: No

## Response Syntax
<a name="API_taxSettings_ListSupplementalTaxRegistrations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "taxRegistrations": [
      {
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
         "authorityId": "string",
         "legalName": "string",
         "registrationId": "string",
         "registrationType": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_taxSettings_ListSupplementalTaxRegistrations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_taxSettings_ListSupplementalTaxRegistrations_ResponseSyntax) **   <a name="awscostmanagement-taxSettings_ListSupplementalTaxRegistrations-response-nextToken"></a>
 The token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `[-A-Za-z0-9_+\=\/]+`

 ** [taxRegistrations](#API_taxSettings_ListSupplementalTaxRegistrations_ResponseSyntax) **   <a name="awscostmanagement-taxSettings_ListSupplementalTaxRegistrations-response-taxRegistrations"></a>
 The list of supplemental tax registrations.
Type: Array of [SupplementalTaxRegistration](API_taxSettings_SupplementalTaxRegistration.md) objects

## Errors
<a name="API_taxSettings_ListSupplementalTaxRegistrations_Errors"></a>

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
<a name="API_taxSettings_ListSupplementalTaxRegistrations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/taxsettings-2018-05-10/ListSupplementalTaxRegistrations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/taxsettings-2018-05-10/ListSupplementalTaxRegistrations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/ListSupplementalTaxRegistrations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/taxsettings-2018-05-10/ListSupplementalTaxRegistrations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/ListSupplementalTaxRegistrations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/taxsettings-2018-05-10/ListSupplementalTaxRegistrations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/taxsettings-2018-05-10/ListSupplementalTaxRegistrations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/taxsettings-2018-05-10/ListSupplementalTaxRegistrations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/taxsettings-2018-05-10/ListSupplementalTaxRegistrations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/ListSupplementalTaxRegistrations)
