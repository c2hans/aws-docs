---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_GetEnvironment.html
---

# GetEnvironment
<a name="API_GetEnvironment"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Gets an AWS Migration Hub Refactor Spaces environment.

## Request Syntax
<a name="API_GetEnvironment_RequestSyntax"></a>

```
GET /environments/{{EnvironmentIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EnvironmentIdentifier](#API_GetEnvironment_RequestSyntax) **   <a name="migrationhubrefactorspaces-GetEnvironment-request-uri-EnvironmentIdentifier"></a>
The ID of the environment.
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`
Required: Yes

## Request Body
<a name="API_GetEnvironment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreatedTime": number,
   "Description": "string",
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
   "NetworkFabricType": "string",
   "OwnerAccountId": "string",
   "State": "string",
   "Tags": {
      "string" : "string"
   },
   "TransitGatewayId": "string"
}
```

## Response Elements
<a name="API_GetEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetEnvironment-response-Arn"></a>
The Amazon Resource Name (ARN) of the environment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:refactor-spaces:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+`

 ** [CreatedTime](#API_GetEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetEnvironment-response-CreatedTime"></a>
A timestamp that indicates when the environment is created.
Type: Timestamp

 ** [Description](#API_GetEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetEnvironment-response-Description"></a>
The description of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-_\s\.\!\*\#\@\']+`

 ** [EnvironmentId](#API_GetEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetEnvironment-response-EnvironmentId"></a>
The unique identifier of the environment.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`

 ** [Error](#API_GetEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetEnvironment-response-Error"></a>
Any error associated with the environment resource.
Type: [ErrorResponse](API_ErrorResponse.md) object

 ** [LastUpdatedTime](#API_GetEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetEnvironment-response-LastUpdatedTime"></a>
A timestamp that indicates when the environment was last updated.
Type: Timestamp

 ** [Name](#API_GetEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetEnvironment-response-Name"></a>
The name of the environment.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!env-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+`

 ** [NetworkFabricType](#API_GetEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetEnvironment-response-NetworkFabricType"></a>
The network fabric type of the environment.
Type: String
Valid Values: `TRANSIT_GATEWAY | NONE`

 ** [OwnerAccountId](#API_GetEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetEnvironment-response-OwnerAccountId"></a>
The AWS account ID of the environment owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

 ** [State](#API_GetEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetEnvironment-response-State"></a>
The current state of the environment.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED`

 ** [Tags](#API_GetEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetEnvironment-response-Tags"></a>
The tags to assign to the environment. A tag is a label that you assign to an AWS resource. Each tag consists of a key-value pair.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:).+.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [TransitGatewayId](#API_GetEnvironment_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetEnvironment-response-TransitGatewayId"></a>
The ID of the AWS Transit Gateway set up by the environment, if applicable.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `tgw-[-a-f0-9]{17}`

## Errors
<a name="API_GetEnvironment_Errors"></a>

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
<a name="API_GetEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migration-hub-refactor-spaces-2021-10-26/GetEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migration-hub-refactor-spaces-2021-10-26/GetEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/GetEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migration-hub-refactor-spaces-2021-10-26/GetEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/GetEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migration-hub-refactor-spaces-2021-10-26/GetEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migration-hub-refactor-spaces-2021-10-26/GetEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migration-hub-refactor-spaces-2021-10-26/GetEnvironment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/migration-hub-refactor-spaces-2021-10-26/GetEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/GetEnvironment)
