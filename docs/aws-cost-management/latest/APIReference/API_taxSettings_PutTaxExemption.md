---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_PutTaxExemption.html
---

# PutTaxExemption
<a name="API_taxSettings_PutTaxExemption"></a>

Adds the tax exemption for a single account or all accounts listed in a consolidated billing family. The IAM action is `tax:UpdateExemptions`.

## Request Syntax
<a name="API_taxSettings_PutTaxExemption_RequestSyntax"></a>

```
POST /PutTaxExemption HTTP/1.1
Content-type: application/json

{
   "accountIds": [ "{{string}}" ],
   "authority": {
      "country": "{{string}}",
      "state": "{{string}}"
   },
   "exemptionCertificate": {
      "documentFile": {{blob}},
      "documentName": "{{string}}"
   },
   "exemptionType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_taxSettings_PutTaxExemption_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_taxSettings_PutTaxExemption_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountIds](#API_taxSettings_PutTaxExemption_RequestSyntax) **   <a name="awscostmanagement-taxSettings_PutTaxExemption-request-accountIds"></a>
 The list of unique account identifiers.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 550 items.
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** [authority](#API_taxSettings_PutTaxExemption_RequestSyntax) **   <a name="awscostmanagement-taxSettings_PutTaxExemption-request-authority"></a>
The address domain associate with the tax information.
Type: [Authority](API_taxSettings_Authority.md) object
Required: Yes

 ** [exemptionCertificate](#API_taxSettings_PutTaxExemption_RequestSyntax) **   <a name="awscostmanagement-taxSettings_PutTaxExemption-request-exemptionCertificate"></a>
The exemption certificate.
Type: [ExemptionCertificate](API_taxSettings_ExemptionCertificate.md) object
Required: Yes

 ** [exemptionType](#API_taxSettings_PutTaxExemption_RequestSyntax) **   <a name="awscostmanagement-taxSettings_PutTaxExemption-request-exemptionType"></a>
The exemption type. Use the supported tax exemption type description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[\s\S]*`
Required: Yes

## Response Syntax
<a name="API_taxSettings_PutTaxExemption_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "caseId": "string"
}
```

## Response Elements
<a name="API_taxSettings_PutTaxExemption_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [caseId](#API_taxSettings_PutTaxExemption_ResponseSyntax) **   <a name="awscostmanagement-taxSettings_PutTaxExemption-response-caseId"></a>
The customer support case ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[\s\S]*`

## Errors
<a name="API_taxSettings_PutTaxExemption_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The access is denied for the Support API.
HTTP Status Code: 401

 ** AttachmentUploadException **
Failed to upload the tax exemption document to Support case.
HTTP Status Code: 400

 ** CaseCreationLimitExceededException **
You've exceeded the Support case creation limit for your account.
HTTP Status Code: 413

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
<a name="API_taxSettings_PutTaxExemption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/taxsettings-2018-05-10/PutTaxExemption)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/taxsettings-2018-05-10/PutTaxExemption)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/PutTaxExemption)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/taxsettings-2018-05-10/PutTaxExemption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/PutTaxExemption)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/taxsettings-2018-05-10/PutTaxExemption)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/taxsettings-2018-05-10/PutTaxExemption)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/taxsettings-2018-05-10/PutTaxExemption)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/taxsettings-2018-05-10/PutTaxExemption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/PutTaxExemption)
