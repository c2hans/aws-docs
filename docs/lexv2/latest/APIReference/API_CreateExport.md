---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateExport.html
---

# CreateExport
<a name="API_CreateExport"></a>

Creates a zip archive containing the contents of a bot or a bot locale. The archive contains a directory structure that contains JSON files that define the bot.

You can create an archive that contains the complete definition of a bot, or you can specify that the archive contain only the definition of a single bot locale.

For more information about exporting bots, and about the structure of the export archive, see [ Importing and exporting bots ](https://docs.aws.amazon.com/lexv2/latest/dg/importing-exporting.html)

## Request Syntax
<a name="API_CreateExport_RequestSyntax"></a>

```
PUT /exports/ HTTP/1.1
Content-type: application/json

{
   "fileFormat": "{{string}}",
   "filePassword": "{{string}}",
   "resourceSpecification": {
      "botExportSpecification": {
         "botId": "{{string}}",
         "botVersion": "{{string}}"
      },
      "botLocaleExportSpecification": {
         "botId": "{{string}}",
         "botVersion": "{{string}}",
         "localeId": "{{string}}"
      },
      "customVocabularyExportSpecification": {
         "botId": "{{string}}",
         "botVersion": "{{string}}",
         "localeId": "{{string}}"
      },
      "testSetExportSpecification": {
         "testSetId": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_CreateExport_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateExport_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [fileFormat](#API_CreateExport_RequestSyntax) **   <a name="lexv2-CreateExport-request-fileFormat"></a>
The file format of the bot or bot locale definition files.
Type: String
Valid Values: `LexJson | TSV | CSV`
Required: Yes

 ** [filePassword](#API_CreateExport_RequestSyntax) **   <a name="lexv2-CreateExport-request-filePassword"></a>
An password to use to encrypt the exported archive. Using a password is optional, but you should encrypt the archive to protect the data in transit between Amazon Lex and your local computer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [resourceSpecification](#API_CreateExport_RequestSyntax) **   <a name="lexv2-CreateExport-request-resourceSpecification"></a>
Specifies the type of resource to export, either a bot or a bot locale. You can only specify one type of resource to export.
Type: [ExportResourceSpecification](API_ExportResourceSpecification.md) object
Required: Yes

## Response Syntax
<a name="API_CreateExport_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "creationDateTime": number,
   "exportId": "string",
   "exportStatus": "string",
   "fileFormat": "string",
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
<a name="API_CreateExport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [creationDateTime](#API_CreateExport_ResponseSyntax) **   <a name="lexv2-CreateExport-response-creationDateTime"></a>
The date and time that the request to export a bot was created.
Type: Timestamp

 ** [exportId](#API_CreateExport_ResponseSyntax) **   <a name="lexv2-CreateExport-response-exportId"></a>
An identifier for a specific request to create an export.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [exportStatus](#API_CreateExport_ResponseSyntax) **   <a name="lexv2-CreateExport-response-exportStatus"></a>
The status of the export. When the status is `Completed`, you can use the [DescribeExport](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeExport.html) operation to get the pre-signed S3 URL link to your exported bot or bot locale.
Type: String
Valid Values: `InProgress | Completed | Failed | Deleting`

 ** [fileFormat](#API_CreateExport_ResponseSyntax) **   <a name="lexv2-CreateExport-response-fileFormat"></a>
The file format used for the bot or bot locale definition files.
Type: String
Valid Values: `LexJson | TSV | CSV`

 ** [resourceSpecification](#API_CreateExport_ResponseSyntax) **   <a name="lexv2-CreateExport-response-resourceSpecification"></a>
A description of the type of resource that was exported, either a bot or a bot locale.
Type: [ExportResourceSpecification](API_ExportResourceSpecification.md) object

## Errors
<a name="API_CreateExport_Errors"></a>

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
<a name="API_CreateExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/CreateExport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/CreateExport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/CreateExport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/CreateExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/CreateExport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/CreateExport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/CreateExport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/CreateExport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/CreateExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/CreateExport)
