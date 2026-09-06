---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_GetService.html
---

# GetService
<a name="API_GetService"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Gets an AWS Migration Hub Refactor Spaces service.

## Request Syntax
<a name="API_GetService_RequestSyntax"></a>

```
GET /environments/{{EnvironmentIdentifier}}/applications/{{ApplicationIdentifier}}/services/{{ServiceIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetService_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationIdentifier](#API_GetService_RequestSyntax) **   <a name="migrationhubrefactorspaces-GetService-request-uri-ApplicationIdentifier"></a>
The ID of the application.
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`
Required: Yes

 ** [EnvironmentIdentifier](#API_GetService_RequestSyntax) **   <a name="migrationhubrefactorspaces-GetService-request-uri-EnvironmentIdentifier"></a>
The ID of the environment.
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`
Required: Yes

 ** [ServiceIdentifier](#API_GetService_RequestSyntax) **   <a name="migrationhubrefactorspaces-GetService-request-uri-ServiceIdentifier"></a>
The ID of the service.
Length Constraints: Fixed length of 14.
Pattern: `svc-[0-9A-Za-z]{10}`
Required: Yes

## Request Body
<a name="API_GetService_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetService_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationId": "string",
   "Arn": "string",
   "CreatedByAccountId": "string",
   "CreatedTime": number,
   "Description": "string",
   "EndpointType": "string",
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
   "LambdaEndpoint": {
      "Arn": "string"
   },
   "LastUpdatedTime": number,
   "Name": "string",
   "OwnerAccountId": "string",
   "ServiceId": "string",
   "State": "string",
   "Tags": {
      "string" : "string"
   },
   "UrlEndpoint": {
      "HealthUrl": "string",
      "Url": "string"
   },
   "VpcId": "string"
}
```

## Response Elements
<a name="API_GetService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationId](#API_GetService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetService-response-ApplicationId"></a>
The ID of the application.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`

 ** [Arn](#API_GetService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetService-response-Arn"></a>
The Amazon Resource Name (ARN) of the service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:refactor-spaces:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+`

 ** [CreatedByAccountId](#API_GetService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetService-response-CreatedByAccountId"></a>
The AWS account ID of the service creator.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

 ** [CreatedTime](#API_GetService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetService-response-CreatedTime"></a>
The timestamp of when the service is created.
Type: Timestamp

 ** [Description](#API_GetService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetService-response-Description"></a>
The description of the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-_\s\.\!\*\#\@\']+`

 ** [EndpointType](#API_GetService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetService-response-EndpointType"></a>
The endpoint type of the service.
Type: String
Valid Values: `LAMBDA | URL`

 ** [EnvironmentId](#API_GetService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetService-response-EnvironmentId"></a>
The unique identifier of the environment.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`

 ** [Error](#API_GetService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetService-response-Error"></a>
Any error associated with the service resource.
Type: [ErrorResponse](API_ErrorResponse.md) object

 ** [LambdaEndpoint](#API_GetService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetService-response-LambdaEndpoint"></a>
The configuration for the AWS Lambda endpoint type.
The **Arn** is the Amazon Resource Name (ARN) of the Lambda function associated with this service.
Type: [LambdaEndpointConfig](API_LambdaEndpointConfig.md) object

 ** [LastUpdatedTime](#API_GetService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetService-response-LastUpdatedTime"></a>
A timestamp that indicates when the service was last updated.
Type: Timestamp

 ** [Name](#API_GetService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetService-response-Name"></a>
The name of the service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!svc-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+`

 ** [OwnerAccountId](#API_GetService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetService-response-OwnerAccountId"></a>
The AWS account ID of the service owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

 ** [ServiceId](#API_GetService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetService-response-ServiceId"></a>
The unique identifier of the service.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `svc-[0-9A-Za-z]{10}`

 ** [State](#API_GetService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetService-response-State"></a>
The current state of the service.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED`

 ** [Tags](#API_GetService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetService-response-Tags"></a>
The tags assigned to the service. A tag is a label that you assign to an AWS resource. Each tag consists of a key-value pair.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:).+.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [UrlEndpoint](#API_GetService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetService-response-UrlEndpoint"></a>
The configuration for the URL endpoint type.
The **Url** isthe URL of the endpoint type.
The **HealthUrl** is the health check URL of the endpoint type.
Type: [UrlEndpointConfig](API_UrlEndpointConfig.md) object

 ** [VpcId](#API_GetService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetService-response-VpcId"></a>
The ID of the virtual private cloud (VPC).
Type: String
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-[-a-f0-9]{8}([-a-f0-9]{9})?`

## Errors
<a name="API_GetService_Errors"></a>

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
<a name="API_GetService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migration-hub-refactor-spaces-2021-10-26/GetService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migration-hub-refactor-spaces-2021-10-26/GetService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/GetService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migration-hub-refactor-spaces-2021-10-26/GetService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/GetService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migration-hub-refactor-spaces-2021-10-26/GetService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migration-hub-refactor-spaces-2021-10-26/GetService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migration-hub-refactor-spaces-2021-10-26/GetService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migration-hub-refactor-spaces-2021-10-26/GetService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/GetService)
