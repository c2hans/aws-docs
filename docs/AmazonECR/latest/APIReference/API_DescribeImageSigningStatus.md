---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImageSigningStatus.html
---

# DescribeImageSigningStatus
<a name="API_DescribeImageSigningStatus"></a>

Returns the signing status for a specified image. If the image matched signing rules that reference different signing profiles, a status is returned for each profile.

For more information, see [Managed signing](https://docs.aws.amazon.com/AmazonECR/latest/userguide/managed-signing.html) in the *Amazon Elastic Container Registry User Guide*.

## Request Syntax
<a name="API_DescribeImageSigningStatus_RequestSyntax"></a>

```
{
   "imageId": {
      "imageDigest": "{{string}}",
      "imageTag": "{{string}}"
   },
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeImageSigningStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [imageId](#API_DescribeImageSigningStatus_RequestSyntax) **   <a name="ECR-DescribeImageSigningStatus-request-imageId"></a>
An object containing identifying information for an image.
Type: [ImageIdentifier](API_ImageIdentifier.md) object
Required: Yes

 ** [registryId](#API_DescribeImageSigningStatus_RequestSyntax) **   <a name="ECR-DescribeImageSigningStatus-request-registryId"></a>
The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_DescribeImageSigningStatus_RequestSyntax) **   <a name="ECR-DescribeImageSigningStatus-request-repositoryName"></a>
The name of the repository that contains the image.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

## Response Syntax
<a name="API_DescribeImageSigningStatus_ResponseSyntax"></a>

```
{
   "imageId": {
      "imageDigest": "string",
      "imageTag": "string"
   },
   "registryId": "string",
   "repositoryName": "string",
   "signingStatuses": [
      {
         "failureCode": "string",
         "failureReason": "string",
         "signingProfileArn": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeImageSigningStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageId](#API_DescribeImageSigningStatus_ResponseSyntax) **   <a name="ECR-DescribeImageSigningStatus-response-imageId"></a>
An object with identifying information for the image.
Type: [ImageIdentifier](API_ImageIdentifier.md) object

 ** [registryId](#API_DescribeImageSigningStatus_ResponseSyntax) **   <a name="ECR-DescribeImageSigningStatus-response-registryId"></a>
The AWS account ID associated with the registry.
Type: String
Pattern: `[0-9]{12}`

 ** [repositoryName](#API_DescribeImageSigningStatus_ResponseSyntax) **   <a name="ECR-DescribeImageSigningStatus-response-repositoryName"></a>
The name of the repository.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`

 ** [signingStatuses](#API_DescribeImageSigningStatus_ResponseSyntax) **   <a name="ECR-DescribeImageSigningStatus-response-signingStatuses"></a>
A list of signing statuses for the specified image. Each status corresponds to a signing profile.
Type: Array of [ImageSigningStatus](API_ImageSigningStatus.md) objects

## Errors
<a name="API_DescribeImageSigningStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ImageNotFoundException **
The image requested does not exist in the specified repository.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** RepositoryNotFoundException **
The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** message **
The error message associated with the exception.
HTTP Status Code: 500

 ** ValidationException **
There was an exception validating this request.
HTTP Status Code: 400

## See Also
<a name="API_DescribeImageSigningStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/DescribeImageSigningStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/DescribeImageSigningStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/DescribeImageSigningStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/DescribeImageSigningStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DescribeImageSigningStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/DescribeImageSigningStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/DescribeImageSigningStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/DescribeImageSigningStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DescribeImageSigningStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/DescribeImageSigningStatus)
