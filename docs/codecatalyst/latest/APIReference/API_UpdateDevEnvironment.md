---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_UpdateDevEnvironment.html
---

# UpdateDevEnvironment
<a name="API_UpdateDevEnvironment"></a>

Changes one or more values for a Dev Environment. Updating certain values of the Dev Environment will cause a restart.

## Request Syntax
<a name="API_UpdateDevEnvironment_RequestSyntax"></a>

```
PATCH /v1/spaces/{{spaceName}}/projects/{{projectName}}/devEnvironments/{{id}} HTTP/1.1
Content-type: application/json

{
   "alias": "{{string}}",
   "clientToken": "{{string}}",
   "ides": [
      {
         "name": "{{string}}",
         "runtime": "{{string}}"
      }
   ],
   "inactivityTimeoutMinutes": {{number}},
   "instanceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDevEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_UpdateDevEnvironment_RequestSyntax) **   <a name="codecatalyst-UpdateDevEnvironment-request-uri-id"></a>
The system-generated unique ID of the Dev Environment.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** [projectName](#API_UpdateDevEnvironment_RequestSyntax) **   <a name="codecatalyst-UpdateDevEnvironment-request-uri-projectName"></a>
The name of the project in the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** [spaceName](#API_UpdateDevEnvironment_RequestSyntax) **   <a name="codecatalyst-UpdateDevEnvironment-request-uri-spaceName"></a>
The name of the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

## Request Body
<a name="API_UpdateDevEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [alias](#API_UpdateDevEnvironment_RequestSyntax) **   <a name="codecatalyst-UpdateDevEnvironment-request-alias"></a>
The user-specified alias for the Dev Environment. Changing this value will not cause a restart.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `$|^[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: No

 ** [clientToken](#API_UpdateDevEnvironment_RequestSyntax) **   <a name="codecatalyst-UpdateDevEnvironment-request-clientToken"></a>
A user-specified idempotency token. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries return the result from the original successful request and have no additional effect.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [ides](#API_UpdateDevEnvironment_RequestSyntax) **   <a name="codecatalyst-UpdateDevEnvironment-request-ides"></a>
Information about the integrated development environment (IDE) configured for a Dev Environment.
Type: Array of [IdeConfiguration](API_IdeConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [inactivityTimeoutMinutes](#API_UpdateDevEnvironment_RequestSyntax) **   <a name="codecatalyst-UpdateDevEnvironment-request-inactivityTimeoutMinutes"></a>
The amount of time the Dev Environment will run without any activity detected before stopping, in minutes. Only whole integers are allowed. Dev Environments consume compute minutes when running.
Changing this value will cause a restart of the Dev Environment if it is running.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1200.
Required: No

 ** [instanceType](#API_UpdateDevEnvironment_RequestSyntax) **   <a name="codecatalyst-UpdateDevEnvironment-request-instanceType"></a>
The Amazon EC2 instace type to use for the Dev Environment.
Changing this value will cause a restart of the Dev Environment if it is running.
Type: String
Valid Values: `dev.standard1.small | dev.standard1.medium | dev.standard1.large | dev.standard1.xlarge`
Required: No

## Response Syntax
<a name="API_UpdateDevEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "alias": "string",
   "clientToken": "string",
   "id": "string",
   "ides": [
      {
         "name": "string",
         "runtime": "string"
      }
   ],
   "inactivityTimeoutMinutes": number,
   "instanceType": "string",
   "projectName": "string",
   "spaceName": "string"
}
```

## Response Elements
<a name="API_UpdateDevEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [alias](#API_UpdateDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-UpdateDevEnvironment-response-alias"></a>
The user-specified alias for the Dev Environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [clientToken](#API_UpdateDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-UpdateDevEnvironment-response-clientToken"></a>
A user-specified idempotency token. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries return the result from the original successful request and have no additional effect.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [id](#API_UpdateDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-UpdateDevEnvironment-response-id"></a>
The system-generated unique ID of the Dev Environment.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

 ** [ides](#API_UpdateDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-UpdateDevEnvironment-response-ides"></a>
Information about the integrated development environment (IDE) configured for the Dev Environment.
Type: Array of [IdeConfiguration](API_IdeConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [inactivityTimeoutMinutes](#API_UpdateDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-UpdateDevEnvironment-response-inactivityTimeoutMinutes"></a>
The amount of time the Dev Environment will run without any activity detected before stopping, in minutes.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1200.

 ** [instanceType](#API_UpdateDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-UpdateDevEnvironment-response-instanceType"></a>
The Amazon EC2 instace type to use for the Dev Environment.
Type: String
Valid Values: `dev.standard1.small | dev.standard1.medium | dev.standard1.large | dev.standard1.xlarge`

 ** [projectName](#API_UpdateDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-UpdateDevEnvironment-response-projectName"></a>
The name of the project in the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [spaceName](#API_UpdateDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-UpdateDevEnvironment-response-spaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

## Errors
<a name="API_UpdateDevEnvironment_Errors"></a>

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
<a name="API_UpdateDevEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/UpdateDevEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/UpdateDevEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/UpdateDevEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/UpdateDevEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/UpdateDevEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/UpdateDevEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/UpdateDevEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/UpdateDevEnvironment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/UpdateDevEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/UpdateDevEnvironment)
