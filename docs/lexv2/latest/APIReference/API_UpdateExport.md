---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateExport.html
---

# UpdateExport
<a name="API_UpdateExport"></a>

Updates the password used to protect an export zip archive.

The password is not required. If you don't supply a password, Amazon Lex generates a zip file that is not protected by a password. This is the archive that is available at the pre-signed S3 URL provided by the [DescribeExport](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeExport.html) operation.

## Request Syntax
<a name="API_UpdateExport_RequestSyntax"></a>

```
PUT /exports/{{exportId}}/ HTTP/1.1
Content-type: application/json

{
   "filePassword": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateExport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [exportId](#API_UpdateExport_RequestSyntax) **   <a name="lexv2-UpdateExport-request-uri-exportId"></a>
The unique identifier Amazon Lex assigned to the export.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_UpdateExport_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filePassword](#API_UpdateExport_RequestSyntax) **   <a name="lexv2-UpdateExport-request-filePassword"></a>
The new password to use to encrypt the export zip archive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_UpdateExport_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "creationDateTime": number,
   "exportId": "string",
   "exportStatus": "string",
   "fileFormat": "string",
   "lastUpdatedDateTime": number,
   "resourceSpecification": {
      "botExportSpecification": {
         "botId": "string",
         "botVersion": "string"
      },
      "botLocaleExportSpecification": {
         "botId": "string",
         "botVersion": "string",
         "localeId": "string"
      },
      "customVocabularyExportSpecification": {
         "botId": "string",
         "botVersion": "string",
         "localeId": "string"
      },
      "testSetExportSpecification": {
         "testSetId": "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdateExport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [creationDateTime](#API_UpdateExport_ResponseSyntax) **   <a name="lexv2-UpdateExport-response-creationDateTime"></a>
The date and time that the export was created.
Type: Timestamp

 ** [exportId](#API_UpdateExport_ResponseSyntax) **   <a name="lexv2-UpdateExport-response-exportId"></a>
The unique identifier Amazon Lex assigned to the export.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [exportStatus](#API_UpdateExport_ResponseSyntax) **   <a name="lexv2-UpdateExport-response-exportStatus"></a>
The status of the export. When the status is `Completed` the export archive is available for download.
Type: String
Valid Values: `InProgress | Completed | Failed | Deleting`

 ** [fileFormat](#API_UpdateExport_ResponseSyntax) **   <a name="lexv2-UpdateExport-response-fileFormat"></a>
The file format used for the files that define the resource. The `TSV` format is required to export a custom vocabulary only; otherwise use `LexJson` format.
Type: String
Valid Values: `LexJson | TSV | CSV`

 ** [lastUpdatedDateTime](#API_UpdateExport_ResponseSyntax) **   <a name="lexv2-UpdateExport-response-lastUpdatedDateTime"></a>
The date and time that the export was last updated.
Type: Timestamp

 ** [resourceSpecification](#API_UpdateExport_ResponseSyntax) **   <a name="lexv2-UpdateExport-response-resourceSpecification"></a>
A description of the type of resource that was exported, either a bot or a bot locale.
Type: [ExportResourceSpecification](API_ExportResourceSpecification.md) object

## Errors
<a name="API_UpdateExport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again.
HTTP Status Code: 409

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have reached a quota for your bot.
HTTP Status Code: 402

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_UpdateExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/UpdateExport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/UpdateExport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/UpdateExport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/UpdateExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/UpdateExport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/UpdateExport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/UpdateExport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/UpdateExport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/UpdateExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/UpdateExport)
