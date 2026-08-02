---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html
---

# CreateEnvironment
<a name="API_CreateEnvironment"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Creates an AWS Migration Hub Refactor Spaces environment. The caller owns the environment resource, and all Refactor Spaces applications, services, and routes created within the environment. They are referred to as the *environment owner*. The environment owner has cross-account visibility and control of Refactor Spaces resources that are added to the environment by other accounts that the environment is shared with.

When creating an environment with a [CreateEnvironment:NetworkFabricType](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType) of `TRANSIT_GATEWAY`, Refactor Spaces provisions a transit gateway to enable services in VPCs to communicate directly across accounts. If [CreateEnvironment:NetworkFabricType](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType) is `NONE`, Refactor Spaces does not create a transit gateway and you must use your network infrastructure to route traffic to services with private URL endpoints.

## Request Syntax
<a name="API_CreateEnvironment_RequestSyntax"></a>

```
POST /environments HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "Name": "{{string}}",
   "NetworkFabricType": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateEnvironment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateEnvironment_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateEnvironment-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\x20-\x7E]{1,64}`
Required: No

 ** [Description](#API_CreateEnvironment_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateEnvironment-request-Description"></a>
The description of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-_\s\.\!\*\#\@\']+`
Required: No

 ** [Name](#API_CreateEnvironment_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateEnvironment-request-Name"></a>
The name of the environment.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!env-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+`
Required: Yes

 ** [NetworkFabricType](#API_CreateEnvironment_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType"></a>
The network fabric type of the environment.
Type: String
Valid Values: `TRANSIT_GATEWAY | NONE`
Required: Yes

 ** [Tags](#API_CreateEnvironment_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateEnvironment-request-Tags"></a>
The tags to assign to the environment. A tag is a label that you assign to an AWS resource. Each tag consists of a key-value pair.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:).+.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreatedTime": number,
   "Description": "string",
   "EnvironmentId": "string",
   "LastUpdatedTime": number,
   "Name": "string",
   "NetworkFabricType": "string",
   "OwnerAccountId": "string",
   "State": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_CreateEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateEnvironment-response-Arn"></a>
The Amazon Resource Name (ARN) of the environment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:refactor-spaces:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+`

 ** [CreatedTime](#API_CreateEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateEnvironment-response-CreatedTime"></a>
A timestamp that indicates when the environment is created.
Type: Timestamp

 ** [Description](#API_CreateEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateEnvironment-response-Description"></a>
A description of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-_\s\.\!\*\#\@\']+`

 ** [EnvironmentId](#API_CreateEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateEnvironment-response-EnvironmentId"></a>
The unique identifier of the environment.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`

 ** [LastUpdatedTime](#API_CreateEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateEnvironment-response-LastUpdatedTime"></a>
A timestamp that indicates when the environment was last updated.
Type: Timestamp

 ** [Name](#API_CreateEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateEnvironment-response-Name"></a>
The name of the environment.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!env-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+`

 ** [NetworkFabricType](#API_CreateEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateEnvironment-response-NetworkFabricType"></a>
The network fabric type of the environment.
Type: String
Valid Values: `TRANSIT_GATEWAY | NONE`

 ** [OwnerAccountId](#API_CreateEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateEnvironment-response-OwnerAccountId"></a>
The AWS account ID of environment owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

 ** [State](#API_CreateEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateEnvironment-response-State"></a>
The current state of the environment.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED`

 ** [Tags](#API_CreateEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateEnvironment-response-Tags"></a>
The tags assigned to the created environment. A tag is a label that you assign to an AWS resource. Each tag consists of a key-value pair..
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:).+.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_CreateEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The type of resource.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The type of resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** QuotaCode **
Service quota requirement to identify originating quota. Reached throttling quota exception.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The type of resource.
 ** ServiceCode **
Service quota requirement to identify originating service. Reached throttling quota exception service code.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied because the request was throttled.
 ** QuotaCode **
Service quota requirement to identify originating quota. Reached throttling quota exception.
 ** RetryAfterSeconds **
The number of seconds to wait before retrying.
 ** ServiceCode **
Service quota requirement to identify originating service. Reached throttling quota exception service code.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migration-hub-refactor-spaces-2021-10-26/CreateEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migration-hub-refactor-spaces-2021-10-26/CreateEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/CreateEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migration-hub-refactor-spaces-2021-10-26/CreateEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/CreateEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migration-hub-refactor-spaces-2021-10-26/CreateEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migration-hub-refactor-spaces-2021-10-26/CreateEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migration-hub-refactor-spaces-2021-10-26/CreateEnvironment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migration-hub-refactor-spaces-2021-10-26/CreateEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/CreateEnvironment)
