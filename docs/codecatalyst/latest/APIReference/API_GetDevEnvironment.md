---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_GetDevEnvironment.html
---

# GetDevEnvironment
<a name="API_GetDevEnvironment"></a>

Returns information about a Dev Environment for a source repository in a project. Dev Environments are specific to the user who creates them.

## Request Syntax
<a name="API_GetDevEnvironment_RequestSyntax"></a>

```
GET /v1/spaces/{{spaceName}}/projects/{{projectName}}/devEnvironments/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDevEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetDevEnvironment_RequestSyntax) **   <a name="codecatalyst-GetDevEnvironment-request-uri-id"></a>
The system-generated unique ID of the Dev Environment for which you want to view information. To retrieve a list of Dev Environment IDs, use [ListDevEnvironments](API_ListDevEnvironments.md).
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** [projectName](#API_GetDevEnvironment_RequestSyntax) **   <a name="codecatalyst-GetDevEnvironment-request-uri-projectName"></a>
The name of the project in the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** [spaceName](#API_GetDevEnvironment_RequestSyntax) **   <a name="codecatalyst-GetDevEnvironment-request-uri-spaceName"></a>
The name of the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

## Request Body
<a name="API_GetDevEnvironment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDevEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "alias": "string",
   "creatorId": "string",
   "id": "string",
   "ides": [
      {
         "name": "string",
         "runtime": "string"
      }
   ],
   "inactivityTimeoutMinutes": number,
   "instanceType": "string",
   "lastUpdatedTime": "string",
   "persistentStorage": {
      "sizeInGiB": number
   },
   "projectName": "string",
   "repositories": [
      {
         "branchName": "string",
         "repositoryName": "string"
      }
   ],
   "spaceName": "string",
   "status": "string",
   "statusReason": "string",
   "vpcConnectionName": "string"
}
```

## Response Elements
<a name="API_GetDevEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [alias](#API_GetDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-GetDevEnvironment-response-alias"></a>
The user-specified alias for the Dev Environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [creatorId](#API_GetDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-GetDevEnvironment-response-creatorId"></a>
The system-generated unique ID of the user who created the Dev Environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [id](#API_GetDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-GetDevEnvironment-response-id"></a>
The system-generated unique ID of the Dev Environment.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

 ** [ides](#API_GetDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-GetDevEnvironment-response-ides"></a>
Information about the integrated development environment (IDE) configured for the Dev Environment.
Type: Array of [Ide](API_Ide.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [inactivityTimeoutMinutes](#API_GetDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-GetDevEnvironment-response-inactivityTimeoutMinutes"></a>
The amount of time the Dev Environment will run without any activity detected before stopping, in minutes.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1200.

 ** [instanceType](#API_GetDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-GetDevEnvironment-response-instanceType"></a>
The Amazon EC2 instace type to use for the Dev Environment.
Type: String
Valid Values: `dev.standard1.small | dev.standard1.medium | dev.standard1.large | dev.standard1.xlarge`

 ** [lastUpdatedTime](#API_GetDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-GetDevEnvironment-response-lastUpdatedTime"></a>
The time when the Dev Environment was last updated, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6).
Type: Timestamp

 ** [persistentStorage](#API_GetDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-GetDevEnvironment-response-persistentStorage"></a>
Information about the amount of storage allocated to the Dev Environment. By default, a Dev Environment is configured to have 16GB of persistent storage.
Type: [PersistentStorage](API_PersistentStorage.md) object

 ** [projectName](#API_GetDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-GetDevEnvironment-response-projectName"></a>
The name of the project in the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [repositories](#API_GetDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-GetDevEnvironment-response-repositories"></a>
The source repository that contains the branch cloned into the Dev Environment.
Type: Array of [DevEnvironmentRepositorySummary](API_DevEnvironmentRepositorySummary.md) objects

 ** [spaceName](#API_GetDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-GetDevEnvironment-response-spaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [status](#API_GetDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-GetDevEnvironment-response-status"></a>
The current status of the Dev Environment.
Type: String
Valid Values: `PENDING | RUNNING | STARTING | STOPPING | STOPPED | FAILED | DELETING | DELETED`

 ** [statusReason](#API_GetDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-GetDevEnvironment-response-statusReason"></a>
The reason for the status.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [vpcConnectionName](#API_GetDevEnvironment_ResponseSyntax) **   <a name="codecatalyst-GetDevEnvironment-response-vpcConnectionName"></a>
The name of the connection used to connect to Amazon VPC used when the Dev Environment was created, if any.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

## Errors
<a name="API_GetDevEnvironment_Errors"></a>

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
<a name="API_GetDevEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/GetDevEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/GetDevEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/GetDevEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/GetDevEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/GetDevEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/GetDevEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/GetDevEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/GetDevEnvironment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/GetDevEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/GetDevEnvironment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
