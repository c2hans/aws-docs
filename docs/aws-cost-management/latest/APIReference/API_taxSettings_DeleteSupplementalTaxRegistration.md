---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_DeleteSupplementalTaxRegistration.html
---

# DeleteSupplementalTaxRegistration
<a name="API_taxSettings_DeleteSupplementalTaxRegistration"></a>

 Deletes a supplemental tax registration for a single account.

## Request Syntax
<a name="API_taxSettings_DeleteSupplementalTaxRegistration_RequestSyntax"></a>

```
POST /DeleteSupplementalTaxRegistration HTTP/1.1
Content-type: application/json

{
   "authorityId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_taxSettings_DeleteSupplementalTaxRegistration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_taxSettings_DeleteSupplementalTaxRegistration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authorityId](#API_taxSettings_DeleteSupplementalTaxRegistration_RequestSyntax) **   <a name="awscostmanagement-taxSettings_DeleteSupplementalTaxRegistration-request-authorityId"></a>
 The unique authority Id for the supplemental TRN information that needs to be deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[\s\S]*`
Required: Yes

## Response Syntax
<a name="API_taxSettings_DeleteSupplementalTaxRegistration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_taxSettings_DeleteSupplementalTaxRegistration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_taxSettings_DeleteSupplementalTaxRegistration_Errors"></a>

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
<a name="API_taxSettings_DeleteSupplementalTaxRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/taxsettings-2018-05-10/DeleteSupplementalTaxRegistration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/taxsettings-2018-05-10/DeleteSupplementalTaxRegistration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/DeleteSupplementalTaxRegistration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/taxsettings-2018-05-10/DeleteSupplementalTaxRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/DeleteSupplementalTaxRegistration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/taxsettings-2018-05-10/DeleteSupplementalTaxRegistration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/taxsettings-2018-05-10/DeleteSupplementalTaxRegistration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/taxsettings-2018-05-10/DeleteSupplementalTaxRegistration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/taxsettings-2018-05-10/DeleteSupplementalTaxRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/DeleteSupplementalTaxRegistration)
