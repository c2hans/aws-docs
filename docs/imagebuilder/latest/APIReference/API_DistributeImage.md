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
A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
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
The source image to distribute. You can specify the source in any of the following formats:
+ An AMI ID.
+ An AWS Systems Manager Parameter Store reference, prefixed by `ssm:`, followed by the parameter name or ARN.
+ An Image Builder image Amazon Resource Name (ARN). An image version ARN resolves to the latest available build version.
Whichever format you use, the source must resolve to an AMI in the current AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [tags](#API_DistributeImage_RequestSyntax) **   <a name="imagebuilder-DistributeImage-request-tags"></a>
The tags to apply to the new Image Builder image resource that this operation creates. To tag the output AMIs, use `amiTags` in the distribution configuration.
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
The Amazon Resource Name (ARN) of the new Image Builder image resource that this operation creates to track the distribution. Use this ARN with [GetImage](API_GetImage.md) to monitor distribution progress.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

## Errors
<a name="API_DistributeImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permissions to perform the requested operation.
HTTP Status Code: 403

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** IdempotentParameterMismatchException **
You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ResourceNotFoundException **
At least one of the resources referenced by your request does not exist.
HTTP Status Code: 404

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
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

## Examples
<a name="API_DistributeImage_Examples"></a>

### Distribute an existing AMI
<a name="API_DistributeImage_Example_1"></a>

The following example distributes an AMI that you own to the targets defined in the specified distribution configuration. It returns the ARN of a new Image Builder image resource that you can use with GetImage to monitor distribution progress.

#### Sample Request
<a name="API_DistributeImage_Example_1_Request"></a>

```
PUT /DistributeImage HTTP/1.1
Content-type: application/json

{
    "sourceImage": "ami-1234567890abcdef0",
    "distributionConfigurationArn": "arn:aws:imagebuilder:us-west-2:111122223333:distribution-configuration/my-example-distribution-configuration",
    "executionRole": "arn:aws:iam::111122223333:role/aws-service-role/imagebuilder.amazonaws.com/AWSServiceRoleForImageBuilder",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE86420"
}
```

#### Sample Response
<a name="API_DistributeImage_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE86420",
    "imageBuildVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-source-ami/1.0.0/1"
}
```

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
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/DistributeImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/DistributeImage)
