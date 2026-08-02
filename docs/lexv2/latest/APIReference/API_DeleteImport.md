---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteImport.html
---

# DeleteImport
<a name="API_DeleteImport"></a>

Removes a previous import and the associated file stored in an S3 bucket.

## Request Syntax
<a name="API_DeleteImport_RequestSyntax"></a>

```
DELETE /imports/{{importId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteImport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [importId](#API_DeleteImport_RequestSyntax) **   <a name="lexv2-DeleteImport-request-uri-importId"></a>
The unique identifier of the import to delete.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_DeleteImport_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteImport_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "importId": "string",
   "importStatus": "string"
}
```

## Response Elements
<a name="API_DeleteImport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [importId](#API_DeleteImport_ResponseSyntax) **   <a name="lexv2-DeleteImport-response-importId"></a>
The unique identifier of the deleted import.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [importStatus](#API_DeleteImport_ResponseSyntax) **   <a name="lexv2-DeleteImport-response-importStatus"></a>
The current status of the deletion. When the deletion is complete, the import will no longer be returned by the [ListImports](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListImports.html) operation and calls to the [DescribeImport](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeImport.html) operation with the import identifier will fail.
Type: String
Valid Values: `InProgress | Completed | Failed | Deleting`

## Errors
<a name="API_DeleteImport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** PreconditionFailedException **
Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.
HTTP Status Code: 412

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
<a name="API_DeleteImport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DeleteImport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DeleteImport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DeleteImport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DeleteImport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DeleteImport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DeleteImport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DeleteImport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DeleteImport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DeleteImport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DeleteImport)
