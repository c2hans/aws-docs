---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_PutFeedback.html
---

# PutFeedback
<a name="API_amazon-q-connect_PutFeedback"></a>

Provides feedback against the specified assistant for the specified target. This API only supports generative targets.

## Request Syntax
<a name="API_amazon-q-connect_PutFeedback_RequestSyntax"></a>

```
PUT /assistants/{{assistantId}}/feedback HTTP/1.1
Content-type: application/json

{
   "contentFeedback": { ... },
   "targetId": "{{string}}",
   "targetType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_PutFeedback_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assistantId](#API_amazon-q-connect_PutFeedback_RequestSyntax) **   <a name="connect-amazon-q-connect_PutFeedback-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_PutFeedback_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [contentFeedback](#API_amazon-q-connect_PutFeedback_RequestSyntax) **   <a name="connect-amazon-q-connect_PutFeedback-request-contentFeedback"></a>
Information about the feedback provided.
Type: [ContentFeedbackData](API_amazon-q-connect_ContentFeedbackData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [targetId](#API_amazon-q-connect_PutFeedback_RequestSyntax) **   <a name="connect-amazon-q-connect_PutFeedback-request-targetId"></a>
The identifier of the feedback target.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [targetType](#API_amazon-q-connect_PutFeedback_RequestSyntax) **   <a name="connect-amazon-q-connect_PutFeedback-request-targetType"></a>
The type of the feedback target.
Type: String
Valid Values: `RECOMMENDATION | RESULT | MESSAGE`
Required: Yes

## Response Syntax
<a name="API_amazon-q-connect_PutFeedback_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assistantArn": "string",
   "assistantId": "string",
   "contentFeedback": { ... },
   "targetId": "string",
   "targetType": "string"
}
```

## Response Elements
<a name="API_amazon-q-connect_PutFeedback_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assistantArn](#API_amazon-q-connect_PutFeedback_ResponseSyntax) **   <a name="connect-amazon-q-connect_PutFeedback-response-assistantArn"></a>
The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`

 ** [assistantId](#API_amazon-q-connect_PutFeedback_ResponseSyntax) **   <a name="connect-amazon-q-connect_PutFeedback-response-assistantId"></a>
The identifier of the Amazon Q in Connect assistant.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [contentFeedback](#API_amazon-q-connect_PutFeedback_ResponseSyntax) **   <a name="connect-amazon-q-connect_PutFeedback-response-contentFeedback"></a>
Information about the feedback provided.
Type: [ContentFeedbackData](API_amazon-q-connect_ContentFeedbackData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [targetId](#API_amazon-q-connect_PutFeedback_ResponseSyntax) **   <a name="connect-amazon-q-connect_PutFeedback-response-targetId"></a>
The identifier of the feedback target.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [targetType](#API_amazon-q-connect_PutFeedback_ResponseSyntax) **   <a name="connect-amazon-q-connect_PutFeedback-response-targetType"></a>
The type of the feedback target.
Type: String
Valid Values: `RECOMMENDATION | RESULT | MESSAGE`

## Errors
<a name="API_amazon-q-connect_PutFeedback_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_PutFeedback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/PutFeedback)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/PutFeedback)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/PutFeedback)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/PutFeedback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/PutFeedback)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/PutFeedback)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/PutFeedback)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/PutFeedback)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/PutFeedback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/PutFeedback)
