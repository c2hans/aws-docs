---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateApplication.html
---

# UpdateApplication
<a name="API_UpdateApplication"></a>

Updates the configuration and settings of an existing OpenSearch application.

## Request Syntax
<a name="API_UpdateApplication_RequestSyntax"></a>

```
PUT /2021-01-01/opensearch/application/{{id}} HTTP/1.1
Content-type: application/json

{
   "appConfigs": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
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
   }
}
```

## URI Request Parameters
<a name="API_UpdateApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_UpdateApplication_RequestSyntax) **   <a name="opensearchservice-UpdateApplication-request-uri-id"></a>
The unique identifier for the OpenSearch application to be updated.
Pattern: `[a-z0-9]{3,30}`
Required: Yes

## Request Body
<a name="API_UpdateApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [appConfigs](#API_UpdateApplication_RequestSyntax) **   <a name="opensearchservice-UpdateApplication-request-appConfigs"></a>
The configuration settings to modify for the OpenSearch application.
Type: Array of [AppConfig](API_AppConfig.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** [dataSources](#API_UpdateApplication_RequestSyntax) **   <a name="opensearchservice-UpdateApplication-request-dataSources"></a>
The data sources to associate with the OpenSearch application.
Type: Array of [DataSource](API_DataSource.md) objects
Required: No

 ** [iamIdentityCenterOptions](#API_UpdateApplication_RequestSyntax) **   <a name="opensearchservice-UpdateApplication-request-iamIdentityCenterOptions"></a>
Configuration settings for integrating IAM Identity Center with the OpenSearch application.
Type: [IamIdentityCenterOptionsInput](API_IamIdentityCenterOptionsInput.md) object
Required: No

## Response Syntax
<a name="API_UpdateApplication_ResponseSyntax"></a>

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
   "lastUpdatedAt": number,
   "name": "string"
}
```

## Response Elements
<a name="API_UpdateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appConfigs](#API_UpdateApplication_ResponseSyntax) **   <a name="opensearchservice-UpdateApplication-response-appConfigs"></a>
The configuration settings for the updated OpenSearch application.
Type: Array of [AppConfig](API_AppConfig.md) objects
Array Members: Maximum number of 200 items.

 ** [arn](#API_UpdateApplication_ResponseSyntax) **   <a name="opensearchservice-UpdateApplication-response-arn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`

 ** [createdAt](#API_UpdateApplication_ResponseSyntax) **   <a name="opensearchservice-UpdateApplication-response-createdAt"></a>
The timestamp when the OpenSearch application was originally created.
Type: Timestamp

 ** [dataSources](#API_UpdateApplication_ResponseSyntax) **   <a name="opensearchservice-UpdateApplication-response-dataSources"></a>
The data sources associated with the updated OpenSearch application.
Type: Array of [DataSource](API_DataSource.md) objects

 ** [iamIdentityCenterOptions](#API_UpdateApplication_ResponseSyntax) **   <a name="opensearchservice-UpdateApplication-response-iamIdentityCenterOptions"></a>
The IAM Identity Center configuration for the updated OpenSearch application.
Type: [IamIdentityCenterOptions](API_IamIdentityCenterOptions.md) object

 ** [id](#API_UpdateApplication_ResponseSyntax) **   <a name="opensearchservice-UpdateApplication-response-id"></a>
The unique identifier of the updated OpenSearch application.
Type: String
Pattern: `[a-z0-9]{3,30}`

 ** [lastUpdatedAt](#API_UpdateApplication_ResponseSyntax) **   <a name="opensearchservice-UpdateApplication-response-lastUpdatedAt"></a>
The timestamp when the OpenSearch application was last updated.
Type: Timestamp

 ** [name](#API_UpdateApplication_ResponseSyntax) **   <a name="opensearchservice-UpdateApplication-response-name"></a>
The name of the updated OpenSearch application.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `[a-z][a-z0-9\-]+`

## Errors
<a name="API_UpdateApplication_Errors"></a>

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

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_UpdateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/UpdateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/UpdateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/UpdateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/UpdateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/UpdateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/UpdateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/UpdateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/UpdateApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/UpdateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/UpdateApplication)
