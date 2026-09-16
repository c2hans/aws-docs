---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetApplication.html
---

# GetApplication
<a name="API_GetApplication"></a>

Retrieves the configuration and status of an existing OpenSearch application.

## Request Syntax
<a name="API_GetApplication_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/application/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetApplication_RequestSyntax) **   <a name="opensearchservice-GetApplication-request-uri-id"></a>
The unique identifier of the OpenSearch application to retrieve.
Pattern: `[a-z0-9]{3,30}`
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
   "endpoint": "string",
   "iamIdentityCenterOptions": {
      "enabled": boolean,
      "iamIdentityCenterApplicationArn": "string",
      "iamIdentityCenterInstanceArn": "string",
      "iamRoleForIdentityCenterApplicationArn": "string"
   },
   "id": "string",
   "kmsKeyArn": "string",
   "lastUpdatedAt": number,
   "name": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_GetApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appConfigs](#API_GetApplication_ResponseSyntax) **   <a name="opensearchservice-GetApplication-response-appConfigs"></a>
The configuration settings of the OpenSearch application.
Type: Array of [AppConfig](API_AppConfig.md) objects
Array Members: Maximum number of 200 items.

 ** [arn](#API_GetApplication_ResponseSyntax) **   <a name="opensearchservice-GetApplication-response-arn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`

 ** [createdAt](#API_GetApplication_ResponseSyntax) **   <a name="opensearchservice-GetApplication-response-createdAt"></a>
The timestamp when the OpenSearch application was created.
Type: Timestamp

 ** [dataSources](#API_GetApplication_ResponseSyntax) **   <a name="opensearchservice-GetApplication-response-dataSources"></a>
The data sources associated with the OpenSearch application.
Type: Array of [DataSource](API_DataSource.md) objects

 ** [endpoint](#API_GetApplication_ResponseSyntax) **   <a name="opensearchservice-GetApplication-response-endpoint"></a>
The endpoint URL of the OpenSearch application.
Type: String

 ** [iamIdentityCenterOptions](#API_GetApplication_ResponseSyntax) **   <a name="opensearchservice-GetApplication-response-iamIdentityCenterOptions"></a>
The IAM Identity Center settings configured for the OpenSearch application.
Type: [IamIdentityCenterOptions](API_IamIdentityCenterOptions.md) object

 ** [id](#API_GetApplication_ResponseSyntax) **   <a name="opensearchservice-GetApplication-response-id"></a>
The unique identifier of the OpenSearch application.
Type: String
Pattern: `[a-z0-9]{3,30}`

 ** [kmsKeyArn](#API_GetApplication_ResponseSyntax) **   <a name="opensearchservice-GetApplication-response-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key used to encrypt the application's data at rest.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

 ** [lastUpdatedAt](#API_GetApplication_ResponseSyntax) **   <a name="opensearchservice-GetApplication-response-lastUpdatedAt"></a>
The timestamp of the last update to the OpenSearch application.
Type: Timestamp

 ** [name](#API_GetApplication_ResponseSyntax) **   <a name="opensearchservice-GetApplication-response-name"></a>
The name of the OpenSearch application.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `[a-z][a-z0-9\-]+`

 ** [status](#API_GetApplication_ResponseSyntax) **   <a name="opensearchservice-GetApplication-response-status"></a>
The current status of the OpenSearch application. Possible values: `CREATING`, `UPDATING`, `DELETING`, `FAILED`, `ACTIVE`, and `DELETED`.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | FAILED`

## Errors
<a name="API_GetApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An error occurred because you don't have permissions to access the resource.
HTTP Status Code: 403

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_GetApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/GetApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/GetApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/GetApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/GetApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/GetApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/GetApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/GetApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/GetApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/GetApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/GetApplication)
