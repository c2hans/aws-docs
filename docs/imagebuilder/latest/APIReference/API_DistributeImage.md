---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DistributeImage.html
---

# DistributeImage
<a name="API_DistributeImage"></a>

Distributes an existing AMI to target Regions and accounts without running the full image build process. This operation only runs the distribution phase on an image that has already been built.

## Request Syntax
<a name="API_DistributeImage_RequestSyntax"></a>

```
PUT /DistributeImage HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "distributionConfigurationArn": "{{string}}",
   "executionRole": "{{string}}",
   "loggingConfiguration": {
      "logGroupName": "{{string}}"
   },
   "sourceImage": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_DistributeImage_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DistributeImage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_DistributeImage_RequestSyntax) **   <a name="imagebuilder-DistributeImage-request-clientToken"></a>
Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [distributionConfigurationArn](#API_DistributeImage_RequestSyntax) **   <a name="imagebuilder-DistributeImage-request-distributionConfigurationArn"></a>
The Amazon Resource Name (ARN) of the distribution configuration. The configuration defines target Regions, accounts, and AMI settings. The distribution configuration must be in the same Region as this operation.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):distribution-configuration/[a-z0-9-_]+$`
Required: Yes

 ** [executionRole](#API_DistributeImage_RequestSyntax) **   <a name="imagebuilder-DistributeImage-request-executionRole"></a>
The name or Amazon Resource Name (ARN) of the IAM role that Image Builder assumes to distribute the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(?:arn:aws(?:-[a-z]+)*:iam::[0-9]{12}:role/)?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: Yes

 ** [loggingConfiguration](#API_DistributeImage_RequestSyntax) **   <a name="imagebuilder-DistributeImage-request-loggingConfiguration"></a>
The logging configuration for the distribution.
Type: [ImageLoggingConfiguration](API_ImageLoggingConfiguration.md) object
Required: No

 ** [sourceImage](#API_DistributeImage_RequestSyntax) **   <a name="imagebuilder-DistributeImage-request-sourceImage"></a>
The source image to distribute. Specify an AMI identifier, SSM parameter path, or Image Builder image Amazon Resource Name (ARN). When you specify an Image Builder image Amazon Resource Name (ARN), the image must be in the `AVAILABLE` state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [tags](#API_DistributeImage_RequestSyntax) **   <a name="imagebuilder-DistributeImage-request-tags"></a>
The tags to apply to the distributed image.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_DistributeImage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "imageBuildVersionArn": "string"
}
```

## Response Elements
<a name="API_DistributeImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_DistributeImage_ResponseSyntax) **   <a name="imagebuilder-DistributeImage-response-clientToken"></a>
The client token that uniquely identifies the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [imageBuildVersionArn](#API_DistributeImage_ResponseSyntax) **   <a name="imagebuilder-DistributeImage-response-imageBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the image to be distributed.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

## Errors
<a name="API_DistributeImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permissions to perform the requested operation.
HTTP Status Code: 403

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the specific operation.
HTTP Status Code: 429

 ** ClientException **
These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** IdempotentParameterMismatchException **
You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.
HTTP Status Code: 400

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ResourceNotFoundException **
At least one of the resources referenced by your request does not exist.
HTTP Status Code: 404

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
You have exceeded the number of permitted resources or operations for this service. For service quotas, see [EC2 Image Builder endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder).
HTTP Status Code: 402

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

 ** TooManyRequestsException **
You have attempted too many requests for the specific operation.
HTTP Status Code: 429

## See Also
<a name="API_DistributeImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/DistributeImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/DistributeImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/DistributeImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/DistributeImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/DistributeImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/DistributeImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/DistributeImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/DistributeImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/DistributeImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/DistributeImage)
