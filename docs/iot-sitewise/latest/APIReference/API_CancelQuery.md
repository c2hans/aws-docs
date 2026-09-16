---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CancelQuery.html
---

# CancelQuery
<a name="API_CancelQuery"></a>

Cancels a running query.

## Request Syntax
<a name="API_CancelQuery_RequestSyntax"></a>

```
POST /workspaces/{{workspaceName}}/queries/{{queryId}}/cancel HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelQuery_RequestParameters"></a>

The request uses the following URI parameters.

 ** [queryId](#API_CancelQuery_RequestSyntax) **   <a name="iotsitewise-CancelQuery-request-uri-queryId"></a>
The unique identifier for the query execution to cancel.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [workspaceName](#API_CancelQuery_RequestSyntax) **   <a name="iotsitewise-CancelQuery-request-uri-workspaceName"></a>
The name of the workspace associated with the query.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_CancelQuery_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelQuery_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "queryId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CancelQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [queryId](#API_CancelQuery_ResponseSyntax) **   <a name="iotsitewise-CancelQuery-response-queryId"></a>
The unique identifier for the cancelled query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

 ** [status](#API_CancelQuery_ResponseSyntax) **   <a name="iotsitewise-CancelQuery-response-status"></a>
The current query status.
Type: String
Valid Values: `SUBMITTED | RUNNING | COMPLETED | FAILED | CANCELED | CANCELING`

## Errors
<a name="API_CancelQuery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** ConflictingOperationException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resourceArn **
The ARN of the resource that conflicts with this operation.
 ** resourceId **
The ID of the resource that conflicts with this operation.
HTTP Status Code: 409

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_CancelQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/CancelQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/CancelQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CancelQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/CancelQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CancelQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/CancelQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/CancelQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/CancelQuery)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/CancelQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CancelQuery)
