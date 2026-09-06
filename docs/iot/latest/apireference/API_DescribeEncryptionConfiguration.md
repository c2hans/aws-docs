---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeEncryptionConfiguration.html
---

# DescribeEncryptionConfiguration
<a name="API_DescribeEncryptionConfiguration"></a>

Retrieves the encryption configuration for resources and data of your AWS account in AWS IoT Core. For more information, see [Data encryption at rest](https://docs.aws.amazon.com/iot/latest/developerguide/encryption-at-rest.html) in the * AWS IoT Core Developer Guide*.

## Request Syntax
<a name="API_DescribeEncryptionConfiguration_RequestSyntax"></a>

```
GET /encryption-configuration HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeEncryptionConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeEncryptionConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeEncryptionConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configurationDetails": {
      "configurationStatus": "string",
      "errorCode": "string",
      "errorMessage": "string"
   },
   "encryptionType": "string",
   "kmsAccessRoleArn": "string",
   "kmsKeyArn": "string",
   "lastModifiedDate": number
}
```

## Response Elements
<a name="API_DescribeEncryptionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configurationDetails](#API_DescribeEncryptionConfiguration_ResponseSyntax) **   <a name="iot-DescribeEncryptionConfiguration-response-configurationDetails"></a>
The encryption configuration details that include the status information of the KMS key and the AWS KMS access role.
Type: [ConfigurationDetails](API_ConfigurationDetails.md) object

 ** [encryptionType](#API_DescribeEncryptionConfiguration_ResponseSyntax) **   <a name="iot-DescribeEncryptionConfiguration-response-encryptionType"></a>
The type of the KMS key.
Type: String
Valid Values: `CUSTOMER_MANAGED_KMS_KEY | AWS_OWNED_KMS_KEY`

 ** [kmsAccessRoleArn](#API_DescribeEncryptionConfiguration_ResponseSyntax) **   <a name="iot-DescribeEncryptionConfiguration-response-kmsAccessRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role assumed by AWS IoT Core to call AWS KMS on behalf of the customer.
Type: String
Length Constraints: Maximum length of 2048.

 ** [kmsKeyArn](#API_DescribeEncryptionConfiguration_ResponseSyntax) **   <a name="iot-DescribeEncryptionConfiguration-response-kmsKeyArn"></a>
The ARN of the customer managed KMS key.
Type: String
Length Constraints: Maximum length of 2048.

 ** [lastModifiedDate](#API_DescribeEncryptionConfiguration_ResponseSyntax) **   <a name="iot-DescribeEncryptionConfiguration-response-lastModifiedDate"></a>
The date when encryption configuration is last updated.
Type: Timestamp

## Errors
<a name="API_DescribeEncryptionConfiguration_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_DescribeEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeEncryptionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeEncryptionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeEncryptionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeEncryptionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeEncryptionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeEncryptionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeEncryptionConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeEncryptionConfiguration)
