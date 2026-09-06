---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_CreateInstance.html
---

# CreateInstance
<a name="API_CreateInstance"></a>

Enables you to programmatically create an AWS Supply Chain instance by applying KMS keys and relevant information associated with the API without using the AWS console.

This is an asynchronous operation. Upon receiving a CreateInstance request, AWS Supply Chain immediately returns the instance resource, instance ID, and the initializing state while simultaneously creating all required AWS resources for an instance creation. You can use GetInstance to check the status of the instance. If the instance results in an unhealthy state, you need to check the error message, delete the current instance, and recreate a new one based on the mitigation from the error message.

## Request Syntax
<a name="API_CreateInstance_RequestSyntax"></a>

```
POST /api/instance HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "instanceDescription": "{{string}}",
   "instanceName": "{{string}}",
   "kmsKeyArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "webAppDnsDomain": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateInstance_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateInstance_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateInstance_RequestSyntax) **   <a name="supplychain-CreateInstance-request-clientToken"></a>
The client token for idempotency.
Type: String
Length Constraints: Minimum length of 33. Maximum length of 126.
Required: No

 ** [instanceDescription](#API_CreateInstance_RequestSyntax) **   <a name="supplychain-CreateInstance-request-instanceDescription"></a>
The AWS Supply Chain instance description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 501.
Pattern: `([a-zA-Z0-9., _ʼ'%-]){0,500}`
Required: No

 ** [instanceName](#API_CreateInstance_RequestSyntax) **   <a name="supplychain-CreateInstance-request-instanceName"></a>
The AWS Supply Chain instance name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `(?![ _ʼ'%-])[a-zA-Z0-9 _ʼ'%-]{0,62}[a-zA-Z0-9]`
Required: No

 ** [kmsKeyArn](#API_CreateInstance_RequestSyntax) **   <a name="supplychain-CreateInstance-request-kmsKeyArn"></a>
The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the AWS owned KMS key. If you don't provide anything here, AWS Supply Chain uses the AWS owned KMS key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:[a-z0-9][-.a-z0-9]{0,62}:kms:([a-z0-9][-.a-z0-9]{0,62})?:([a-z0-9][-.a-z0-9]{0,62})?:key/.{0,1019}`
Required: No

 ** [tags](#API_CreateInstance_RequestSyntax) **   <a name="supplychain-CreateInstance-request-tags"></a>
The AWS tags of an instance to be created.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [webAppDnsDomain](#API_CreateInstance_RequestSyntax) **   <a name="supplychain-CreateInstance-request-webAppDnsDomain"></a>
The DNS subdomain of the web app. This would be "example" in the URL "example.scn.global.on.aws". You can set this to a custom value, as long as the domain isn't already being used by someone else. The name may only include alphanumeric characters and hyphens.
Type: String
Pattern: `(?![-])[a-zA-Z0-9-]{1,62}[a-zA-Z0-9]`
Required: No

## Response Syntax
<a name="API_CreateInstance_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "instance": {
      "awsAccountId": "string",
      "createdTime": number,
      "errorMessage": "string",
      "instanceDescription": "string",
      "instanceId": "string",
      "instanceName": "string",
      "kmsKeyArn": "string",
      "lastModifiedTime": number,
      "state": "string",
      "versionNumber": number,
      "webAppDnsDomain": "string"
   }
}
```

## Response Elements
<a name="API_CreateInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [instance](#API_CreateInstance_ResponseSyntax) **   <a name="supplychain-CreateInstance-response-instance"></a>
The AWS Supply Chain instance resource data details.
Type: [Instance](API_Instance.md) object

## Errors
<a name="API_CreateInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have the required privileges to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supplychain-2024-01-01/CreateInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supplychain-2024-01-01/CreateInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/CreateInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supplychain-2024-01-01/CreateInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/CreateInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supplychain-2024-01-01/CreateInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supplychain-2024-01-01/CreateInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supplychain-2024-01-01/CreateInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/supplychain-2024-01-01/CreateInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/CreateInstance)
