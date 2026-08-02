---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetEncryptionKey.html
---

# GetEncryptionKey
<a name="API_GetEncryptionKey"></a>

Gets an encryption key.

## Request Syntax
<a name="API_GetEncryptionKey_RequestSyntax"></a>

```
GET /encryptionkey/get?resourceType={{resourceType}}&scanType={{scanType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEncryptionKey_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceType](#API_GetEncryptionKey_RequestSyntax) **   <a name="inspector2-GetEncryptionKey-request-uri-resourceType"></a>
The resource type the key encrypts.
Valid Values: `AWS_EC2_INSTANCE | AWS_ECR_CONTAINER_IMAGE | AWS_ECR_REPOSITORY | AWS_LAMBDA_FUNCTION | CODE_REPOSITORY | Microsoft.Compute/virtualMachines | Microsoft.ContainerRegistry/registry/containerImage | Microsoft.Web/sites`
Required: Yes

 ** [scanType](#API_GetEncryptionKey_RequestSyntax) **   <a name="inspector2-GetEncryptionKey-request-uri-scanType"></a>
The scan type the key encrypts.
Valid Values: `NETWORK | PACKAGE | CODE`
Required: Yes

## Request Body
<a name="API_GetEncryptionKey_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEncryptionKey_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "kmsKeyId": "string"
}
```

## Response Elements
<a name="API_GetEncryptionKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [kmsKeyId](#API_GetEncryptionKey_ResponseSyntax) **   <a name="inspector2-GetEncryptionKey-response-kmsKeyId"></a>
A kms key ID.
Type: String
Pattern: `arn:aws(-(us-gov|cn))?:kms:([a-z0-9][-.a-z0-9]{0,62})?:[0-9]{12}?:key/(([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(mrk-[0-9a-zA-Z]{32}))`

## Errors
<a name="API_GetEncryptionKey_Errors"></a>

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
<a name="API_GetEncryptionKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/GetEncryptionKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/GetEncryptionKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/GetEncryptionKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/GetEncryptionKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/GetEncryptionKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/GetEncryptionKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/GetEncryptionKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/GetEncryptionKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/GetEncryptionKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/GetEncryptionKey)
