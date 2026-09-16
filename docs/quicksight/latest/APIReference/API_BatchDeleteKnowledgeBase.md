---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BatchDeleteKnowledgeBase.html
---

# BatchDeleteKnowledgeBase
<a name="API_BatchDeleteKnowledgeBase"></a>

Deletes one or more knowledge bases.

## Request Syntax
<a name="API_BatchDeleteKnowledgeBase_RequestSyntax"></a>

```
POST /v1/accounts/{{AwsAccountId}}/knowledge-bases/batch-delete HTTP/1.1
Content-type: application/json

{
   "KnowledgeBaseIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchDeleteKnowledgeBase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_BatchDeleteKnowledgeBase_RequestSyntax) **   <a name="QS-BatchDeleteKnowledgeBase-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the knowledge base.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]*`
Required: Yes

## Request Body
<a name="API_BatchDeleteKnowledgeBase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [KnowledgeBaseIds](#API_BatchDeleteKnowledgeBase_RequestSyntax) **   <a name="QS-BatchDeleteKnowledgeBase-request-KnowledgeBaseIds"></a>
A list of knowledge base identifiers to delete.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z-_=.+]+`
Required: Yes

## Response Syntax
<a name="API_BatchDeleteKnowledgeBase_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Deleted": [
      {
         "KnowledgeBaseArn": "string",
         "KnowledgeBaseId": "string"
      }
   ],
   "Errors": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "KnowledgeBaseId": "string"
      }
   ],
   "RequestId": "string"
}
```

## Response Elements
<a name="API_BatchDeleteKnowledgeBase_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_BatchDeleteKnowledgeBase_ResponseSyntax) **   <a name="QS-BatchDeleteKnowledgeBase-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Deleted](#API_BatchDeleteKnowledgeBase_ResponseSyntax) **   <a name="QS-BatchDeleteKnowledgeBase-response-Deleted"></a>
A list of knowledge bases that were successfully deleted.
Type: Array of [BatchDeleteKnowledgeBaseSuccess](API_BatchDeleteKnowledgeBaseSuccess.md) objects

 ** [Errors](#API_BatchDeleteKnowledgeBase_ResponseSyntax) **   <a name="QS-BatchDeleteKnowledgeBase-response-Errors"></a>
A list of knowledge bases that failed to be deleted.
Type: Array of [BatchDeleteKnowledgeBaseFailure](API_BatchDeleteKnowledgeBaseFailure.md) objects

 ** [RequestId](#API_BatchDeleteKnowledgeBase_ResponseSyntax) **   <a name="QS-BatchDeleteKnowledgeBase-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_BatchDeleteKnowledgeBase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** InvalidRequestException **
You don't have this feature activated for your account. To fix this issue, contact AWS support.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** PreconditionNotMetException **
One or more preconditions aren't met.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_BatchDeleteKnowledgeBase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/BatchDeleteKnowledgeBase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/BatchDeleteKnowledgeBase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BatchDeleteKnowledgeBase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/BatchDeleteKnowledgeBase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BatchDeleteKnowledgeBase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/BatchDeleteKnowledgeBase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/BatchDeleteKnowledgeBase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/BatchDeleteKnowledgeBase)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/BatchDeleteKnowledgeBase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BatchDeleteKnowledgeBase)
