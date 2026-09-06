---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeExport.html
---

# DescribeExport
<a name="API_DescribeExport"></a>

Gets information about a specific export.

## Request Syntax
<a name="API_DescribeExport_RequestSyntax"></a>

```
GET /exports/{{exportId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeExport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [exportId](#API_DescribeExport_RequestSyntax) **   <a name="lexv2-DescribeExport-request-uri-exportId"></a>
The unique identifier of the export to describe.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_DescribeExport_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeExport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationDateTime": number,
   "downloadUrl": "string",
   "exportId": "string",
   "exportStatus": "string",
   "failureReasons": [ "string" ],
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
<a name="API_DescribeExport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDateTime](#API_DescribeExport_ResponseSyntax) **   <a name="lexv2-DescribeExport-response-creationDateTime"></a>
The date and time that the export was created.
Type: Timestamp

 ** [downloadUrl](#API_DescribeExport_ResponseSyntax) **   <a name="lexv2-DescribeExport-response-downloadUrl"></a>
A pre-signed S3 URL that points to the bot or bot locale archive. The URL is only available for 5 minutes after calling the `DescribeExport` operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [exportId](#API_DescribeExport_ResponseSyntax) **   <a name="lexv2-DescribeExport-response-exportId"></a>
The unique identifier of the described export.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [exportStatus](#API_DescribeExport_ResponseSyntax) **   <a name="lexv2-DescribeExport-response-exportStatus"></a>
The status of the export. When the status is `Complete` the export archive file is available for download.
Type: String
Valid Values: `InProgress | Completed | Failed | Deleting`

 ** [failureReasons](#API_DescribeExport_ResponseSyntax) **   <a name="lexv2-DescribeExport-response-failureReasons"></a>
If the `exportStatus` is failed, contains one or more reasons why the export could not be completed.
Type: Array of strings

 ** [fileFormat](#API_DescribeExport_ResponseSyntax) **   <a name="lexv2-DescribeExport-response-fileFormat"></a>
The file format used in the files that describe the resource.
Type: String
Valid Values: `LexJson | TSV | CSV`

 ** [lastUpdatedDateTime](#API_DescribeExport_ResponseSyntax) **   <a name="lexv2-DescribeExport-response-lastUpdatedDateTime"></a>
The last date and time that the export was updated.
Type: Timestamp

 ** [resourceSpecification](#API_DescribeExport_ResponseSyntax) **   <a name="lexv2-DescribeExport-response-resourceSpecification"></a>
The bot, bot ID, and optional locale ID of the exported bot or bot locale.
Type: [ExportResourceSpecification](API_ExportResourceSpecification.md) object

## Errors
<a name="API_DescribeExport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.
HTTP Status Code: 404

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_DescribeExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DescribeExport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DescribeExport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DescribeExport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DescribeExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DescribeExport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DescribeExport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DescribeExport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DescribeExport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DescribeExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DescribeExport)
