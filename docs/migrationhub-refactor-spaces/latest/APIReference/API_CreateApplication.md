---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateApplication.html
---

# CreateApplication
<a name="API_CreateApplication"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Creates an AWS Migration Hub Refactor Spaces application. The account that owns the environment also owns the applications created inside the environment, regardless of the account that creates the application. Refactor Spaces provisions an Amazon API Gateway, API Gateway VPC link, and Network Load Balancer for the application proxy inside your account.

In environments created with a [CreateEnvironment:NetworkFabricType](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType) of `NONE` you need to configure [ VPC to VPC connectivity](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.html) between your service VPC and the application proxy VPC to route traffic through the application proxy to a service with a private URL endpoint. For more information, see [ Create an application](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/getting-started-create-application.html) in the *Refactor Spaces User Guide*.

## Request Syntax
<a name="API_CreateApplication_RequestSyntax"></a>

```
POST /environments/{{EnvironmentIdentifier}}/applications HTTP/1.1
Content-type: application/json

{
   "ApiGatewayProxy": {
      "EndpointType": "{{string}}",
      "StageName": "{{string}}"
   },
   "ClientToken": "{{string}}",
   "Name": "{{string}}",
   "ProxyType": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "VpcId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EnvironmentIdentifier](#API_CreateApplication_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-request-uri-EnvironmentIdentifier"></a>
The unique identifier of the environment.
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`
Required: Yes

## Request Body
<a name="API_CreateApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApiGatewayProxy](#API_CreateApplication_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-request-ApiGatewayProxy"></a>
A wrapper object holding the API Gateway endpoint type and stage name for the proxy.
Type: [ApiGatewayProxyInput](API_ApiGatewayProxyInput.md) object
Required: No

 ** [ClientToken](#API_CreateApplication_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\x20-\x7E]{1,64}`
Required: No

 ** [Name](#API_CreateApplication_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-request-Name"></a>
The name to use for the application.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!app-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+`
Required: Yes

 ** [ProxyType](#API_CreateApplication_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-request-ProxyType"></a>
The proxy type of the proxy created within the application.
Type: String
Valid Values: `API_GATEWAY`
Required: Yes

 ** [Tags](#API_CreateApplication_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-request-Tags"></a>
The tags to assign to the application. A tag is a label that you assign to an AWS resource. Each tag consists of a key-value pair.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:).+.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [VpcId](#API_CreateApplication_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-request-VpcId"></a>
The ID of the virtual private cloud (VPC).
Type: String
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-[-a-f0-9]{8}([-a-f0-9]{9})?`
Required: Yes

## Response Syntax
<a name="API_CreateApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApiGatewayProxy": {
      "EndpointType": "string",
      "StageName": "string"
   },
   "ApplicationId": "string",
   "Arn": "string",
   "CreatedByAccountId": "string",
   "CreatedTime": number,
   "EnvironmentId": "string",
   "LastUpdatedTime": number,
   "Name": "string",
   "OwnerAccountId": "string",
   "ProxyType": "string",
   "State": "string",
   "Tags": {
      "string" : "string"
   },
   "VpcId": "string"
}
```

## Response Elements
<a name="API_CreateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApiGatewayProxy](#API_CreateApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-response-ApiGatewayProxy"></a>
A wrapper object holding the API Gateway endpoint type and stage name for the proxy.
Type: [ApiGatewayProxyInput](API_ApiGatewayProxyInput.md) object

 ** [ApplicationId](#API_CreateApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-response-ApplicationId"></a>
The unique identifier of the application.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`

 ** [Arn](#API_CreateApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-response-Arn"></a>
The Amazon Resource Name (ARN) of the application. The format for this ARN is `arn:aws:refactor-spaces:region:account-id:resource-type/resource-id `. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:refactor-spaces:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+`

 ** [CreatedByAccountId](#API_CreateApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-response-CreatedByAccountId"></a>
The AWS account ID of application creator.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

 ** [CreatedTime](#API_CreateApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-response-CreatedTime"></a>
A timestamp that indicates when the application is created.
Type: Timestamp

 ** [EnvironmentId](#API_CreateApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-response-EnvironmentId"></a>
The ID of the environment in which the application is created.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`

 ** [LastUpdatedTime](#API_CreateApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-response-LastUpdatedTime"></a>
A timestamp that indicates when the application was last updated.
Type: Timestamp

 ** [Name](#API_CreateApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-response-Name"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!app-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+`

 ** [OwnerAccountId](#API_CreateApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-response-OwnerAccountId"></a>
The AWS account ID of the application owner (which is always the same as the environment owner account ID).
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

 ** [ProxyType](#API_CreateApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-response-ProxyType"></a>
The proxy type of the proxy created within the application.
Type: String
Valid Values: `API_GATEWAY`

 ** [State](#API_CreateApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-response-State"></a>
The current state of the application.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED | UPDATING`

 ** [Tags](#API_CreateApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-response-Tags"></a>
The tags assigned to the application. A tag is a label that you assign to an AWS resource. Each tag consists of a key-value pair.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:).+.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [VpcId](#API_CreateApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateApplication-response-VpcId"></a>
The ID of the Amazon VPC.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-[-a-f0-9]{8}([-a-f0-9]{9})?`

## Errors
<a name="API_CreateApplication_Errors"></a>

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
<a name="API_CreateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migration-hub-refactor-spaces-2021-10-26/CreateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migration-hub-refactor-spaces-2021-10-26/CreateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/CreateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migration-hub-refactor-spaces-2021-10-26/CreateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/CreateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migration-hub-refactor-spaces-2021-10-26/CreateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migration-hub-refactor-spaces-2021-10-26/CreateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migration-hub-refactor-spaces-2021-10-26/CreateApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migration-hub-refactor-spaces-2021-10-26/CreateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/CreateApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub Refactor Spaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-refactor-spaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
