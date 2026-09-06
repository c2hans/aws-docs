---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_StartQuery.html
---

# StartQuery
<a name="API_StartQuery"></a>

Starts an asynchronous SQL query against workspace telemetry, annotations, data segment, and dataset data.

## Request Syntax
<a name="API_StartQuery_RequestSyntax"></a>

```
POST /workspaces/{{workspaceName}}/queries HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "queryStatement": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartQuery_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceName](#API_StartQuery_RequestSyntax) **   <a name="iotsitewise-StartQuery-request-uri-workspaceName"></a>
The name of the workspace to query.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_StartQuery_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartQuery_RequestSyntax) **   <a name="iotsitewise-StartQuery-request-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [queryStatement](#API_StartQuery_RequestSyntax) **   <a name="iotsitewise-StartQuery-request-queryStatement"></a>
The SQL query to execute against the workspace telemetry, annotations, data segment, and dataset data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Required: Yes

## Response Syntax
<a name="API_StartQuery_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "queryId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_StartQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [queryId](#API_StartQuery_ResponseSyntax) **   <a name="iotsitewise-StartQuery-response-queryId"></a>
The unique identifier for the query execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

 ** [status](#API_StartQuery_ResponseSyntax) **   <a name="iotsitewise-StartQuery-response-status"></a>
The initial query status. The value is always SUBMITTED upon creation.
Type: String
Valid Values: `SUBMITTED | RUNNING | COMPLETED | FAILED | CANCELED | CANCELING`

## Errors
<a name="API_StartQuery_Errors"></a>

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
<a name="API_StartQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/StartQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/StartQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/StartQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/StartQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/StartQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/StartQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/StartQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/StartQuery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/StartQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/StartQuery)
