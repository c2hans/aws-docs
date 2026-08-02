---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_BatchDeleteUniqueId.html
---

# BatchDeleteUniqueId
<a name="API_BatchDeleteUniqueId"></a>

Deletes multiple unique IDs in a matching workflow.

## Request Syntax
<a name="API_BatchDeleteUniqueId_RequestSyntax"></a>

```
DELETE /matchingworkflows/{{workflowName}}/uniqueids HTTP/1.1
inputSource: {{inputSource}}
uniqueIds: {{uniqueIds}}
```

## URI Request Parameters
<a name="API_BatchDeleteUniqueId_RequestParameters"></a>

The request uses the following URI parameters.

 ** [inputSource](#API_BatchDeleteUniqueId_RequestSyntax) **   <a name="API-BatchDeleteUniqueId-request-inputSource"></a>
The input source for the batch delete unique ID operation.
Pattern: `arn:(aws|aws-us-gov|aws-cn):glue:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(table/[a-zA-Z_0-9-]{1,255}/[a-zA-Z_0-9-]{1,255})`

 ** [uniqueIds](#API_BatchDeleteUniqueId_RequestSyntax) **   <a name="API-BatchDeleteUniqueId-request-uniqueIds"></a>
The unique IDs to delete.
Length Constraints: Minimum length of 1. Maximum length of 780.
Pattern: `[a-zA-Z_0-9-+=/,]*`
Required: Yes

 ** [workflowName](#API_BatchDeleteUniqueId_RequestSyntax) **   <a name="API-BatchDeleteUniqueId-request-uri-workflowName"></a>
The name of the workflow.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

## Request Body
<a name="API_BatchDeleteUniqueId_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_BatchDeleteUniqueId_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "deleted": [
      {
         "uniqueId": "string"
      }
   ],
   "disconnectedUniqueIds": [ "string" ],
   "errors": [
      {
         "errorType": "string",
         "uniqueId": "string"
      }
   ],
   "status": "string"
}
```

## Response Elements
<a name="API_BatchDeleteUniqueId_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deleted](#API_BatchDeleteUniqueId_ResponseSyntax) **   <a name="API-BatchDeleteUniqueId-response-deleted"></a>
The unique IDs that were deleted.
Type: Array of [DeletedUniqueId](API_DeletedUniqueId.md) objects

 ** [disconnectedUniqueIds](#API_BatchDeleteUniqueId_ResponseSyntax) **   <a name="API-BatchDeleteUniqueId-response-disconnectedUniqueIds"></a>
The unique IDs that were disconnected.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 780.
Pattern: `[a-zA-Z_0-9-+=/,]*`

 ** [errors](#API_BatchDeleteUniqueId_ResponseSyntax) **   <a name="API-BatchDeleteUniqueId-response-errors"></a>
 The errors from deleting multiple unique IDs.
Type: Array of [DeleteUniqueIdError](API_DeleteUniqueIdError.md) objects

 ** [status](#API_BatchDeleteUniqueId_ResponseSyntax) **   <a name="API-BatchDeleteUniqueId-response-status"></a>
The status of the batch delete unique ID operation.
Type: String
Valid Values: `COMPLETED | ACCEPTED`

## Errors
<a name="API_BatchDeleteUniqueId_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Entity Resolution service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by AWS Entity Resolution.
HTTP Status Code: 400

## See Also
<a name="API_BatchDeleteUniqueId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/BatchDeleteUniqueId)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/BatchDeleteUniqueId)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/BatchDeleteUniqueId)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/BatchDeleteUniqueId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/BatchDeleteUniqueId)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/BatchDeleteUniqueId)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/BatchDeleteUniqueId)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/BatchDeleteUniqueId)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/BatchDeleteUniqueId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/BatchDeleteUniqueId)
