---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_StopDevEnvironment.html
---

# StopDevEnvironment
<a name="API_StopDevEnvironment"></a>

Pauses a specified Dev Environment and places it in a non-running state. Stopped Dev Environments do not consume compute minutes.

## Request Syntax
<a name="API_StopDevEnvironment_RequestSyntax"></a>

```
PUT /v1/spaces/{{spaceName}}/projects/{{projectName}}/devEnvironments/{{id}}/stop HTTP/1.1
```

## URI Request Parameters
<a name="API_StopDevEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_StopDevEnvironment_RequestSyntax) **   <a name="codecatalyst-StopDevEnvironment-request-uri-id"></a>
The system-generated unique ID of the Dev Environment.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** [projectName](#API_StopDevEnvironment_RequestSyntax) **   <a name="codecatalyst-StopDevEnvironment-request-uri-projectName"></a>
The name of the project in the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** [spaceName](#API_StopDevEnvironment_RequestSyntax) **   <a name="codecatalyst-StopDevEnvironment-request-uri-spaceName"></a>
The name of the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

## Request Body
<a name="API_StopDevEnvironment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StopDevEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "id": "string",
   "projectName": "string",
   "spaceName": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_StopDevEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [id](#API_StopDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-StopDevEnvironment-response-id"></a>
The system-generated unique ID of the Dev Environment.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

 ** [projectName](#API_StopDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-StopDevEnvironment-response-projectName"></a>
The name of the project in the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [spaceName](#API_StopDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-StopDevEnvironment-response-spaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [status](#API_StopDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-StopDevEnvironment-response-status"></a>
The status of the Dev Environment.
Type: String
Valid Values: `PENDING | RUNNING | STARTING | STOPPING | STOPPED | FAILED | DELETING | DELETED`

## Errors
<a name="API_StopDevEnvironment_Errors"></a>

 ** AccessDeniedException **
The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.
HTTP Status Code: 403

 ** ConflictException **
The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.
HTTP Status Code: 400

## See Also
<a name="API_StopDevEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/StopDevEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/StopDevEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/StopDevEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/StopDevEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/StopDevEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/StopDevEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/StopDevEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/StopDevEnvironment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/StopDevEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/StopDevEnvironment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
