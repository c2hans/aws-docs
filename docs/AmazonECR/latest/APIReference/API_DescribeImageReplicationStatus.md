---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImageReplicationStatus.html
---

# DescribeImageReplicationStatus
<a name="API_DescribeImageReplicationStatus"></a>

Returns the replication status for a specified image.

## Request Syntax
<a name="API_DescribeImageReplicationStatus_RequestSyntax"></a>

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
<a name="API_DescribeImageReplicationStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [imageId](#API_DescribeImageReplicationStatus_RequestSyntax) **   <a name="ECR-DescribeImageReplicationStatus-request-imageId"></a>
An object with identifying information for an image in an Amazon ECR repository.
Type: [ImageIdentifier](API_ImageIdentifier.md) object
Required: Yes

 ** [registryId](#API_DescribeImageReplicationStatus_RequestSyntax) **   <a name="ECR-DescribeImageReplicationStatus-request-registryId"></a>
The AWS account ID associated with the registry. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_DescribeImageReplicationStatus_RequestSyntax) **   <a name="ECR-DescribeImageReplicationStatus-request-repositoryName"></a>
The name of the repository that the image is in.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

## Response Syntax
<a name="API_DescribeImageReplicationStatus_ResponseSyntax"></a>

```
{
   "imageId": {
      "imageDigest": "string",
      "imageTag": "string"
   },
   "replicationStatuses": [
      {
         "failureCode": "string",
         "region": "string",
         "registryId": "string",
         "status": "string"
      }
   ],
   "repositoryName": "string"
}
```

## Response Elements
<a name="API_DescribeImageReplicationStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageId](#API_DescribeImageReplicationStatus_ResponseSyntax) **   <a name="ECR-DescribeImageReplicationStatus-response-imageId"></a>
An object with identifying information for an image in an Amazon ECR repository.
Type: [ImageIdentifier](API_ImageIdentifier.md) object

 ** [replicationStatuses](#API_DescribeImageReplicationStatus_ResponseSyntax) **   <a name="ECR-DescribeImageReplicationStatus-response-replicationStatuses"></a>
The replication status details for the images in the specified repository.
Type: Array of [ImageReplicationStatus](API_ImageReplicationStatus.md) objects

 ** [repositoryName](#API_DescribeImageReplicationStatus_ResponseSyntax) **   <a name="ECR-DescribeImageReplicationStatus-response-repositoryName"></a>
The repository name associated with the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`

## Errors
<a name="API_DescribeImageReplicationStatus_Errors"></a>

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
<a name="API_DescribeImageReplicationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/DescribeImageReplicationStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/DescribeImageReplicationStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/DescribeImageReplicationStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/DescribeImageReplicationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DescribeImageReplicationStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/DescribeImageReplicationStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/DescribeImageReplicationStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/DescribeImageReplicationStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DescribeImageReplicationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/DescribeImageReplicationStatus)
