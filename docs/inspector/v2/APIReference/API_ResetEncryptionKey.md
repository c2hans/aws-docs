---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ResetEncryptionKey.html
---

# ResetEncryptionKey
<a name="API_ResetEncryptionKey"></a>

Resets an encryption key. After the key is reset your resources will be encrypted by an AWS owned key.

## Request Syntax
<a name="API_ResetEncryptionKey_RequestSyntax"></a>

```
PUT /encryptionkey/reset HTTP/1.1
Content-type: application/json

{
   "resourceType": "{{string}}",
   "scanType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ResetEncryptionKey_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ResetEncryptionKey_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourceType](#API_ResetEncryptionKey_RequestSyntax) **   <a name="inspector2-ResetEncryptionKey-request-resourceType"></a>
The resource type the key encrypts.
Type: String
Valid Values: `AWS_EC2_INSTANCE | AWS_ECR_CONTAINER_IMAGE | AWS_ECR_REPOSITORY | AWS_LAMBDA_FUNCTION | CODE_REPOSITORY | Microsoft.Compute/virtualMachines | Microsoft.ContainerRegistry/registry/containerImage | Microsoft.Web/sites`
Required: Yes

 ** [scanType](#API_ResetEncryptionKey_RequestSyntax) **   <a name="inspector2-ResetEncryptionKey-request-scanType"></a>
The scan type the key encrypts.
Type: String
Valid Values: `NETWORK | PACKAGE | CODE`
Required: Yes

## Response Syntax
<a name="API_ResetEncryptionKey_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_ResetEncryptionKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ResetEncryptionKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access an invalid resource. Make sure the resource is specified correctly.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ResetEncryptionKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/ResetEncryptionKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/ResetEncryptionKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ResetEncryptionKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/ResetEncryptionKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ResetEncryptionKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/ResetEncryptionKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/ResetEncryptionKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/ResetEncryptionKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/ResetEncryptionKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ResetEncryptionKey)
