---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_GetTaxRegistrationDocument.html
---

# GetTaxRegistrationDocument
<a name="API_taxSettings_GetTaxRegistrationDocument"></a>

Downloads your tax documents to the Amazon S3 bucket that you specify in your request.

## Request Syntax
<a name="API_taxSettings_GetTaxRegistrationDocument_RequestSyntax"></a>

```
POST /GetTaxRegistrationDocument HTTP/1.1
Content-type: application/json

{
   "destinationS3Location": {
      "bucket": "{{string}}",
      "prefix": "{{string}}"
   },
   "taxDocumentMetadata": {
      "taxDocumentAccessToken": "{{string}}",
      "taxDocumentName": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_taxSettings_GetTaxRegistrationDocument_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_taxSettings_GetTaxRegistrationDocument_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [destinationS3Location](#API_taxSettings_GetTaxRegistrationDocument_RequestSyntax) **   <a name="awscostmanagement-taxSettings_GetTaxRegistrationDocument-request-destinationS3Location"></a>
The Amazon S3 bucket that you specify to download your tax documents to.
Type: [DestinationS3Location](API_taxSettings_DestinationS3Location.md) object
Required: No

 ** [taxDocumentMetadata](#API_taxSettings_GetTaxRegistrationDocument_RequestSyntax) **   <a name="awscostmanagement-taxSettings_GetTaxRegistrationDocument-request-taxDocumentMetadata"></a>
The metadata for your tax document.
Type: [TaxDocumentMetadata](API_taxSettings_TaxDocumentMetadata.md) object
Required: Yes

## Response Syntax
<a name="API_taxSettings_GetTaxRegistrationDocument_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "destinationFilePath": "string",
   "presignedS3Url": "string"
}
```

## Response Elements
<a name="API_taxSettings_GetTaxRegistrationDocument_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [destinationFilePath](#API_taxSettings_GetTaxRegistrationDocument_ResponseSyntax) **   <a name="awscostmanagement-taxSettings_GetTaxRegistrationDocument-response-destinationFilePath"></a>
The file path of the Amazon S3 bucket where you want to download your tax document to.
Type: String
Pattern: `[\s\S]*`

 ** [presignedS3Url](#API_taxSettings_GetTaxRegistrationDocument_ResponseSyntax) **   <a name="awscostmanagement-taxSettings_GetTaxRegistrationDocument-response-presignedS3Url"></a>
The Amazon S3 presigned URL of the tax registration document.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `https.*\S.*`

## Errors
<a name="API_taxSettings_GetTaxRegistrationDocument_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_taxSettings_GetTaxRegistrationDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/taxsettings-2018-05-10/GetTaxRegistrationDocument)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/taxsettings-2018-05-10/GetTaxRegistrationDocument)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/GetTaxRegistrationDocument)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/taxsettings-2018-05-10/GetTaxRegistrationDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/GetTaxRegistrationDocument)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/taxsettings-2018-05-10/GetTaxRegistrationDocument)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/taxsettings-2018-05-10/GetTaxRegistrationDocument)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/taxsettings-2018-05-10/GetTaxRegistrationDocument)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/taxsettings-2018-05-10/GetTaxRegistrationDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/GetTaxRegistrationDocument)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
