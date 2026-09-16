---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_CreateDevEnvironment.html
---

# CreateDevEnvironment
<a name="API_CreateDevEnvironment"></a>

Creates a Dev Environment in Amazon CodeCatalyst, a cloud-based development environment that you can use to quickly work on the code stored in the source repositories of your project.

**Note**
When created in the Amazon CodeCatalyst console, by default a Dev Environment is configured to have a 2 core processor, 4GB of RAM, and 16GB of persistent storage. None of these defaults apply to a Dev Environment created programmatically.

## Request Syntax
<a name="API_CreateDevEnvironment_RequestSyntax"></a>

```
PUT /v1/spaces/{{spaceName}}/projects/{{projectName}}/devEnvironments HTTP/1.1
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
   "instanceType": "{{string}}",
   "persistentStorage": {
      "sizeInGiB": {{number}}
   },
   "repositories": [
      {
         "branchName": "{{string}}",
         "repositoryName": "{{string}}"
      }
   ],
   "vpcConnectionName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateDevEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [projectName](#API_CreateDevEnvironment_RequestSyntax) **   <a name="codecatalyst-CreateDevEnvironment-request-uri-projectName"></a>
The name of the project in the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** [spaceName](#API_CreateDevEnvironment_RequestSyntax) **   <a name="codecatalyst-CreateDevEnvironment-request-uri-spaceName"></a>
The name of the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

## Request Body
<a name="API_CreateDevEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [alias](#API_CreateDevEnvironment_RequestSyntax) **   <a name="codecatalyst-CreateDevEnvironment-request-alias"></a>
The user-defined alias for a Dev Environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: No

 ** [clientToken](#API_CreateDevEnvironment_RequestSyntax) **   <a name="codecatalyst-CreateDevEnvironment-request-clientToken"></a>
A user-specified idempotency token. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries return the result from the original successful request and have no additional effect.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [ides](#API_CreateDevEnvironment_RequestSyntax) **   <a name="codecatalyst-CreateDevEnvironment-request-ides"></a>
Information about the integrated development environment (IDE) configured for a Dev Environment.
An IDE is required to create a Dev Environment. For Dev Environment creation, this field contains configuration information and must be provided.
Type: Array of [IdeConfiguration](API_IdeConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [inactivityTimeoutMinutes](#API_CreateDevEnvironment_RequestSyntax) **   <a name="codecatalyst-CreateDevEnvironment-request-inactivityTimeoutMinutes"></a>
The amount of time the Dev Environment will run without any activity detected before stopping, in minutes. Only whole integers are allowed. Dev Environments consume compute minutes when running.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1200.
Required: No

 ** [instanceType](#API_CreateDevEnvironment_RequestSyntax) **   <a name="codecatalyst-CreateDevEnvironment-request-instanceType"></a>
The Amazon EC2 instace type to use for the Dev Environment.
Type: String
Valid Values: `dev.standard1.small | dev.standard1.medium | dev.standard1.large | dev.standard1.xlarge`
Required: Yes

 ** [persistentStorage](#API_CreateDevEnvironment_RequestSyntax) **   <a name="codecatalyst-CreateDevEnvironment-request-persistentStorage"></a>
Information about the amount of storage allocated to the Dev Environment.
By default, a Dev Environment is configured to have 16GB of persistent storage when created from the Amazon CodeCatalyst console, but there is no default when programmatically creating a Dev Environment. Valid values for persistent storage are based on memory sizes in 16GB increments. Valid values are 16, 32, and 64.
Type: [PersistentStorageConfiguration](API_PersistentStorageConfiguration.md) object
Required: Yes

 ** [repositories](#API_CreateDevEnvironment_RequestSyntax) **   <a name="codecatalyst-CreateDevEnvironment-request-repositories"></a>
The source repository that contains the branch to clone into the Dev Environment.
Type: Array of [RepositoryInput](API_RepositoryInput.md) objects
Required: No

 ** [vpcConnectionName](#API_CreateDevEnvironment_RequestSyntax) **   <a name="codecatalyst-CreateDevEnvironment-request-vpcConnectionName"></a>
The name of the connection that will be used to connect to Amazon VPC, if any.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: No

## Response Syntax
<a name="API_CreateDevEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "id": "string",
   "projectName": "string",
   "spaceName": "string",
   "vpcConnectionName": "string"
}
```

## Response Elements
<a name="API_CreateDevEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [id](#API_CreateDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-CreateDevEnvironment-response-id"></a>
The system-generated unique ID of the Dev Environment.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

 ** [projectName](#API_CreateDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-CreateDevEnvironment-response-projectName"></a>
The name of the project in the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [spaceName](#API_CreateDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-CreateDevEnvironment-response-spaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [vpcConnectionName](#API_CreateDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-CreateDevEnvironment-response-vpcConnectionName"></a>
The name of the connection used to connect to Amazon VPC used when the Dev Environment was created, if any.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

## Errors
<a name="API_CreateDevEnvironment_Errors"></a>

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
<a name="API_CreateDevEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/CreateDevEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/CreateDevEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/CreateDevEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/CreateDevEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/CreateDevEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/CreateDevEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/CreateDevEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/CreateDevEnvironment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/CreateDevEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/CreateDevEnvironment)
