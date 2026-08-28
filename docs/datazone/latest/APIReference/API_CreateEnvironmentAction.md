---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateEnvironmentAction.html
---

# CreateEnvironmentAction
<a name="API_CreateEnvironmentAction"></a>

Creates an action for the environment, for example, creates a console link for an analytics tool that is available in this environment.

## Request Syntax
<a name="API_CreateEnvironmentAction_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/environments/{{environmentIdentifier}}/actions HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "name": "{{string}}",
   "parameters": { ... }
}
```

## URI Request Parameters
<a name="API_CreateEnvironmentAction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateEnvironmentAction_RequestSyntax) **   <a name="datazone-CreateEnvironmentAction-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which the environment action is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [environmentIdentifier](#API_CreateEnvironmentAction_RequestSyntax) **   <a name="datazone-CreateEnvironmentAction-request-uri-environmentIdentifier"></a>
The ID of the environment in which the environment action is created.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateEnvironmentAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateEnvironmentAction_RequestSyntax) **   <a name="datazone-CreateEnvironmentAction-request-description"></a>
The description of the environment action that is being created in the environment.
Type: String
Required: No

 ** [name](#API_CreateEnvironmentAction_RequestSyntax) **   <a name="datazone-CreateEnvironmentAction-request-name"></a>
The name of the environment action.
Type: String
Required: Yes

 ** [parameters](#API_CreateEnvironmentAction_RequestSyntax) **   <a name="datazone-CreateEnvironmentAction-request-parameters"></a>
The parameters of the environment action.
Type: [ActionParameters](API_ActionParameters.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_CreateEnvironmentAction_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateEnvironmentAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [description](#API_CreateEnvironmentAction_ResponseSyntax) **   <a name="datazone-CreateEnvironmentAction-response-description"></a>
The description of the environment action.
Type: String

 ** [domainId](#API_CreateEnvironmentAction_ResponseSyntax) **   <a name="datazone-CreateEnvironmentAction-response-domainId"></a>
The ID of the domain in which the environment action is created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [environmentId](#API_CreateEnvironmentAction_ResponseSyntax) **   <a name="datazone-CreateEnvironmentAction-response-environmentId"></a>
The ID of the environment in which the environment is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_CreateEnvironmentAction_ResponseSyntax) **   <a name="datazone-CreateEnvironmentAction-response-id"></a>
The ID of the environment action.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [name](#API_CreateEnvironmentAction_ResponseSyntax) **   <a name="datazone-CreateEnvironmentAction-response-name"></a>
The name of the environment action.
Type: String

 ** [parameters](#API_CreateEnvironmentAction_ResponseSyntax) **   <a name="datazone-CreateEnvironmentAction-response-parameters"></a>
The parameters of the environment action.
Type: [ActionParameters](API_ActionParameters.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_CreateEnvironmentAction_Errors"></a>

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
<a name="API_CreateEnvironmentAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateEnvironmentAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateEnvironmentAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateEnvironmentAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateEnvironmentAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateEnvironmentAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateEnvironmentAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateEnvironmentAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateEnvironmentAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateEnvironmentAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateEnvironmentAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
