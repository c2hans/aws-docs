---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_UpdateSessionData.html
---

# UpdateSessionData
<a name="API_amazon-q-connect_UpdateSessionData"></a>

Updates the data stored on an Amazon Q in Connect Session.

## Request Syntax
<a name="API_amazon-q-connect_UpdateSessionData_RequestSyntax"></a>

```
PATCH /assistants/{{assistantId}}/sessions/{{sessionId}}/data HTTP/1.1
Content-type: application/json

{
   "data": [
      {
         "key": "{{string}}",
         "value": { ... }
      }
   ],
   "namespace": "{{string}}"
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_UpdateSessionData_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assistantId](#API_amazon-q-connect_UpdateSessionData_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateSessionData-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [sessionId](#API_amazon-q-connect_UpdateSessionData_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateSessionData-request-uri-sessionId"></a>
The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_UpdateSessionData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [data](#API_amazon-q-connect_UpdateSessionData_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateSessionData-request-data"></a>
The data stored on the Amazon Q in Connect Session.
Type: Array of [RuntimeSessionData](API_amazon-q-connect_RuntimeSessionData.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: Yes

 ** [namespace](#API_amazon-q-connect_UpdateSessionData_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateSessionData-request-namespace"></a>
The namespace into which the session data is stored. Supported namespaces are: Custom
Type: String
Valid Values: `Custom`
Required: No

## Response Syntax
<a name="API_amazon-q-connect_UpdateSessionData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "data": [
      {
         "key": "string",
         "value": { ... }
      }
   ],
   "namespace": "string",
   "sessionArn": "string",
   "sessionId": "string"
}
```

## Response Elements
<a name="API_amazon-q-connect_UpdateSessionData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [data](#API_amazon-q-connect_UpdateSessionData_ResponseSyntax) **   <a name="connect-amazon-q-connect_UpdateSessionData-response-data"></a>
Data stored in the session.
Type: Array of [RuntimeSessionData](API_amazon-q-connect_RuntimeSessionData.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [namespace](#API_amazon-q-connect_UpdateSessionData_ResponseSyntax) **   <a name="connect-amazon-q-connect_UpdateSessionData-response-namespace"></a>
The namespace into which the session data is stored. Supported namespaces are: Custom
Type: String
Valid Values: `Custom`

 ** [sessionArn](#API_amazon-q-connect_UpdateSessionData_ResponseSyntax) **   <a name="connect-amazon-q-connect_UpdateSessionData-response-sessionArn"></a>
The Amazon Resource Name (ARN) of the session.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`

 ** [sessionId](#API_amazon-q-connect_UpdateSessionData_ResponseSyntax) **   <a name="connect-amazon-q-connect_UpdateSessionData-response-sessionId"></a>
The identifier of the session.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_amazon-q-connect_UpdateSessionData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_UpdateSessionData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/UpdateSessionData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/UpdateSessionData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/UpdateSessionData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/UpdateSessionData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/UpdateSessionData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/UpdateSessionData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/UpdateSessionData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/UpdateSessionData)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/UpdateSessionData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/UpdateSessionData)
