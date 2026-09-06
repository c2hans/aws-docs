---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UpdateEnvironmentAction.html
---

# UpdateEnvironmentAction
<a name="API_UpdateEnvironmentAction"></a>

Updates an environment action.

## Request Syntax
<a name="API_UpdateEnvironmentAction_RequestSyntax"></a>

```
PATCH /v2/domains/{{domainIdentifier}}/environments/{{environmentIdentifier}}/actions/{{identifier}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "name": "{{string}}",
   "parameters": { ... }
}
```

## URI Request Parameters
<a name="API_UpdateEnvironmentAction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_UpdateEnvironmentAction_RequestSyntax) **   <a name="datazone-UpdateEnvironmentAction-request-uri-domainIdentifier"></a>
The domain ID of the environment action.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [environmentIdentifier](#API_UpdateEnvironmentAction_RequestSyntax) **   <a name="datazone-UpdateEnvironmentAction-request-uri-environmentIdentifier"></a>
The environment ID of the environment action.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_UpdateEnvironmentAction_RequestSyntax) **   <a name="datazone-UpdateEnvironmentAction-request-uri-identifier"></a>
The ID of the environment action.
Required: Yes

## Request Body
<a name="API_UpdateEnvironmentAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateEnvironmentAction_RequestSyntax) **   <a name="datazone-UpdateEnvironmentAction-request-description"></a>
The description of the environment action.
Type: String
Required: No

 ** [name](#API_UpdateEnvironmentAction_RequestSyntax) **   <a name="datazone-UpdateEnvironmentAction-request-name"></a>
The name of the environment action.
Type: String
Required: No

 ** [parameters](#API_UpdateEnvironmentAction_RequestSyntax) **   <a name="datazone-UpdateEnvironmentAction-request-parameters"></a>
The parameters of the environment action.
Type: [ActionParameters](API_ActionParameters.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_UpdateEnvironmentAction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "description": "string",
   "domainId": "string",
   "environmentId": "string",
   "id": "string",
   "name": "string",
   "parameters": { ... }
}
```

## Response Elements
<a name="API_UpdateEnvironmentAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_UpdateEnvironmentAction_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentAction-response-description"></a>
The description of the environment action.
Type: String

 ** [domainId](#API_UpdateEnvironmentAction_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentAction-response-domainId"></a>
The domain ID of the environment action.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [environmentId](#API_UpdateEnvironmentAction_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentAction-response-environmentId"></a>
The environment ID of the environment action.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_UpdateEnvironmentAction_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentAction-response-id"></a>
The ID of the environment action.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [name](#API_UpdateEnvironmentAction_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentAction-response-name"></a>
The name of the environment action.
Type: String

 ** [parameters](#API_UpdateEnvironmentAction_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentAction-response-parameters"></a>
The parameters of the environment action.
Type: [ActionParameters](API_ActionParameters.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_UpdateEnvironmentAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateEnvironmentAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/UpdateEnvironmentAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/UpdateEnvironmentAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UpdateEnvironmentAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/UpdateEnvironmentAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UpdateEnvironmentAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/UpdateEnvironmentAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/UpdateEnvironmentAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/UpdateEnvironmentAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/UpdateEnvironmentAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UpdateEnvironmentAction)
