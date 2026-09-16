---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateApplication.html
---

# CreateApplication
<a name="API_CreateApplication"></a>

Creates an OpenSearch UI application. For more information, see [Using the OpenSearch user interface in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application.html).

## Request Syntax
<a name="API_CreateApplication_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/application HTTP/1.1
Content-type: application/json

{
   "appConfigs": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "clientToken": "{{string}}",
   "dataSources": [
      {
         "dataSourceArn": "{{string}}",
         "dataSourceDescription": "{{string}}",
         "iamRoleForDataSourceArn": "{{string}}"
      }
   ],
   "iamIdentityCenterOptions": {
      "enabled": {{boolean}},
      "iamIdentityCenterInstanceArn": "{{string}}",
      "iamRoleForIdentityCenterApplicationArn": "{{string}}"
   },
   "kmsKeyArn": "{{string}}",
   "name": "{{string}}",
   "tagList": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateApplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [appConfigs](#API_CreateApplication_RequestSyntax) **   <a name="opensearchservice-CreateApplication-request-appConfigs"></a>
Configuration settings for the OpenSearch application, including administrative options.
Type: Array of [AppConfig](API_AppConfig.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** [clientToken](#API_CreateApplication_RequestSyntax) **   <a name="opensearchservice-CreateApplication-request-clientToken"></a>
Unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [dataSources](#API_CreateApplication_RequestSyntax) **   <a name="opensearchservice-CreateApplication-request-dataSources"></a>
The data sources to link to the OpenSearch application.
Type: Array of [DataSource](API_DataSource.md) objects
Required: No

 ** [iamIdentityCenterOptions](#API_CreateApplication_RequestSyntax) **   <a name="opensearchservice-CreateApplication-request-iamIdentityCenterOptions"></a>
Configuration settings for integrating AWS IAM Identity Center with the OpenSearch application.
Type: [IamIdentityCenterOptionsInput](API_IamIdentityCenterOptionsInput.md) object
Required: No

 ** [kmsKeyArn](#API_CreateApplication_RequestSyntax) **   <a name="opensearchservice-CreateApplication-request-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key used to encrypt the application's data at rest. If provided, the application uses your customer-managed key for encryption. If omitted, the application uses an AWS-managed key. The KMS key must be in the same region as the application.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** [name](#API_CreateApplication_RequestSyntax) **   <a name="opensearchservice-CreateApplication-request-name"></a>
The unique name of the OpenSearch application. Names must be unique within an AWS Region for each account.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** [tagList](#API_CreateApplication_RequestSyntax) **   <a name="opensearchservice-CreateApplication-request-tagList"></a>
A list of tags attached to a domain.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appConfigs": [
      {
         "key": "string",
         "value": "string"
      }
   ],
   "arn": "string",
   "createdAt": number,
   "dataSources": [
      {
         "dataSourceArn": "string",
         "dataSourceDescription": "string",
         "iamRoleForDataSourceArn": "string"
      }
   ],
   "iamIdentityCenterOptions": {
      "enabled": boolean,
      "iamIdentityCenterApplicationArn": "string",
      "iamIdentityCenterInstanceArn": "string",
      "iamRoleForIdentityCenterApplicationArn": "string"
   },
   "id": "string",
   "kmsKeyArn": "string",
   "name": "string",
   "tagList": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appConfigs](#API_CreateApplication_ResponseSyntax) **   <a name="opensearchservice-CreateApplication-response-appConfigs"></a>
Configuration settings for the OpenSearch application, including administrative options.
Type: Array of [AppConfig](API_AppConfig.md) objects
Array Members: Maximum number of 200 items.

 ** [arn](#API_CreateApplication_ResponseSyntax) **   <a name="opensearchservice-CreateApplication-response-arn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`

 ** [createdAt](#API_CreateApplication_ResponseSyntax) **   <a name="opensearchservice-CreateApplication-response-createdAt"></a>
The timestamp indicating when the OpenSearch application was created.
Type: Timestamp

 ** [dataSources](#API_CreateApplication_ResponseSyntax) **   <a name="opensearchservice-CreateApplication-response-dataSources"></a>
The data sources linked to the OpenSearch application.
Type: Array of [DataSource](API_DataSource.md) objects

 ** [iamIdentityCenterOptions](#API_CreateApplication_ResponseSyntax) **   <a name="opensearchservice-CreateApplication-response-iamIdentityCenterOptions"></a>
The IAM Identity Center settings configured for the OpenSearch application.
Type: [IamIdentityCenterOptions](API_IamIdentityCenterOptions.md) object

 ** [id](#API_CreateApplication_ResponseSyntax) **   <a name="opensearchservice-CreateApplication-response-id"></a>
The unique identifier assigned to the OpenSearch application.
Type: String
Pattern: `[a-z0-9]{3,30}`

 ** [kmsKeyArn](#API_CreateApplication_ResponseSyntax) **   <a name="opensearchservice-CreateApplication-response-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key used to encrypt the application's data at rest.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

 ** [name](#API_CreateApplication_ResponseSyntax) **   <a name="opensearchservice-CreateApplication-response-name"></a>
The name of the OpenSearch application.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `[a-z][a-z0-9\-]+`

 ** [tagList](#API_CreateApplication_ResponseSyntax) **   <a name="opensearchservice-CreateApplication-response-tagList"></a>
A list of tags attached to a domain.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_CreateApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An error occurred because you don't have permissions to access the resource.
HTTP Status Code: 403

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** ConflictException **
An error occurred because the client attempts to remove a resource that is currently in use.
HTTP Status Code: 409

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_CreateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/CreateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/CreateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/CreateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/CreateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/CreateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/CreateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/CreateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/CreateApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/CreateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/CreateApplication)
