---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeDefaultEncryptionConfiguration.html
---

# DescribeDefaultEncryptionConfiguration
<a name="API_DescribeDefaultEncryptionConfiguration"></a>

Retrieves information about the default encryption configuration for the AWS account in the default or specified Region. For more information, see [Key management](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html) in the * AWS IoT SiteWise User Guide*.

## Request Syntax
<a name="API_DescribeDefaultEncryptionConfiguration_RequestSyntax"></a>

```
GET /configuration/account/encryption HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDefaultEncryptionConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeDefaultEncryptionConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDefaultEncryptionConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configurationStatus": {
      "error": {
         "code": "string",
         "message": "string"
      },
      "state": "string"
   },
   "encryptionType": "string",
   "kmsKeyArn": "string"
}
```

## Response Elements
<a name="API_DescribeDefaultEncryptionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configurationStatus](#API_DescribeDefaultEncryptionConfiguration_ResponseSyntax) **   <a name="iotsitewise-DescribeDefaultEncryptionConfiguration-response-configurationStatus"></a>
The status of the account configuration. This contains the `ConfigurationState`. If there's an error, it also contains the `ErrorDetails`.
Type: [ConfigurationStatus](API_ConfigurationStatus.md) object

 ** [encryptionType](#API_DescribeDefaultEncryptionConfiguration_ResponseSyntax) **   <a name="iotsitewise-DescribeDefaultEncryptionConfiguration-response-encryptionType"></a>
The type of encryption used for the encryption configuration.
Type: String
Valid Values: `SITEWISE_DEFAULT_ENCRYPTION | KMS_BASED_ENCRYPTION`

 ** [kmsKeyArn](#API_DescribeDefaultEncryptionConfiguration_ResponseSyntax) **   <a name="iotsitewise-DescribeDefaultEncryptionConfiguration-response-kmsKeyArn"></a>
The key ARN of the customer managed key used for AWS KMS encryption if you use `KMS_BASED_ENCRYPTION`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

## Errors
<a name="API_DescribeDefaultEncryptionConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_DescribeDefaultEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeDefaultEncryptionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeDefaultEncryptionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeDefaultEncryptionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeDefaultEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeDefaultEncryptionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeDefaultEncryptionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeDefaultEncryptionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeDefaultEncryptionConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeDefaultEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeDefaultEncryptionConfiguration)
