---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_GetApplication.html
---

# GetApplication
<a name="API_GetApplication"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Gets an AWS Migration Hub Refactor Spaces application.

## Request Syntax
<a name="API_GetApplication_RequestSyntax"></a>

```
GET /environments/{{EnvironmentIdentifier}}/applications/{{ApplicationIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationIdentifier](#API_GetApplication_RequestSyntax) **   <a name="migrationhubrefactorspaces-GetApplication-request-uri-ApplicationIdentifier"></a>
The ID of the application.
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`
Required: Yes

 ** [EnvironmentIdentifier](#API_GetApplication_RequestSyntax) **   <a name="migrationhubrefactorspaces-GetApplication-request-uri-EnvironmentIdentifier"></a>
The ID of the environment.
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`
Required: Yes

## Request Body
<a name="API_GetApplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApiGatewayProxy": {
      "ApiGatewayId": "string",
      "EndpointType": "string",
      "NlbArn": "string",
      "NlbName": "string",
      "ProxyUrl": "string",
      "StageName": "string",
      "VpcLinkId": "string"
   },
   "ApplicationId": "string",
   "Arn": "string",
   "CreatedByAccountId": "string",
   "CreatedTime": number,
   "EnvironmentId": "string",
   "Error": {
      "AccountId": "string",
      "AdditionalDetails": {
         "string" : "string"
      },
      "Code": "string",
      "Message": "string",
      "ResourceIdentifier": "string",
      "ResourceType": "string"
   },
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
<a name="API_GetApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApiGatewayProxy](#API_GetApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetApplication-response-ApiGatewayProxy"></a>
The endpoint URL of the API Gateway proxy.
Type: [ApiGatewayProxyConfig](API_ApiGatewayProxyConfig.md) object

 ** [ApplicationId](#API_GetApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetApplication-response-ApplicationId"></a>
The unique identifier of the application.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`

 ** [Arn](#API_GetApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetApplication-response-Arn"></a>
The Amazon Resource Name (ARN) of the application.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:refactor-spaces:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+`

 ** [CreatedByAccountId](#API_GetApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetApplication-response-CreatedByAccountId"></a>
The AWS account ID of the application creator.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

 ** [CreatedTime](#API_GetApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetApplication-response-CreatedTime"></a>
A timestamp that indicates when the application is created.
Type: Timestamp

 ** [EnvironmentId](#API_GetApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetApplication-response-EnvironmentId"></a>
The unique identifier of the environment.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`

 ** [Error](#API_GetApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetApplication-response-Error"></a>
Any error associated with the application resource.
Type: [ErrorResponse](API_ErrorResponse.md) object

 ** [LastUpdatedTime](#API_GetApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetApplication-response-LastUpdatedTime"></a>
A timestamp that indicates when the application was last updated.
Type: Timestamp

 ** [Name](#API_GetApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetApplication-response-Name"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!app-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+`

 ** [OwnerAccountId](#API_GetApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetApplication-response-OwnerAccountId"></a>
The AWS account ID of the application owner (which is always the same as the environment owner account ID).
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

 ** [ProxyType](#API_GetApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetApplication-response-ProxyType"></a>
The proxy type of the proxy created within the application.
Type: String
Valid Values: `API_GATEWAY`

 ** [State](#API_GetApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetApplication-response-State"></a>
The current state of the application.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED | UPDATING`

 ** [Tags](#API_GetApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetApplication-response-Tags"></a>
The tags assigned to the application. A tag is a label that you assign to an AWS resource. Each tag consists of a key-value pair.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:).+.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [VpcId](#API_GetApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetApplication-response-VpcId"></a>
The ID of the virtual private cloud (VPC).
Type: String
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-[-a-f0-9]{8}([-a-f0-9]{9})?`

## Errors
<a name="API_GetApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migration-hub-refactor-spaces-2021-10-26/GetApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migration-hub-refactor-spaces-2021-10-26/GetApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/GetApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migration-hub-refactor-spaces-2021-10-26/GetApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/GetApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migration-hub-refactor-spaces-2021-10-26/GetApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migration-hub-refactor-spaces-2021-10-26/GetApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migration-hub-refactor-spaces-2021-10-26/GetApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migration-hub-refactor-spaces-2021-10-26/GetApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/GetApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub Refactor Spaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-refactor-spaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
