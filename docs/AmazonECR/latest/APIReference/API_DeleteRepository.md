---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteRepository.html
---

# DeleteRepository
<a name="API_DeleteRepository"></a>

Deletes a repository. If the repository isn't empty, you must either delete the contents of the repository or use the `force` option to delete the repository and have Amazon ECR delete all of its contents on your behalf.

## Request Syntax
<a name="API_DeleteRepository_RequestSyntax"></a>

```
{
   "force": {{boolean}},
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteRepository_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [force](#API_DeleteRepository_RequestSyntax) **   <a name="ECR-DeleteRepository-request-force"></a>
If true, deleting the repository force deletes the contents of the repository. If false, the repository must be empty before attempting to delete it.
Type: Boolean
Required: No

 ** [registryId](#API_DeleteRepository_RequestSyntax) **   <a name="ECR-DeleteRepository-request-registryId"></a>
The AWS account ID associated with the registry that contains the repository to delete. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_DeleteRepository_RequestSyntax) **   <a name="ECR-DeleteRepository-request-repositoryName"></a>
The name of the repository to delete.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

## Response Syntax
<a name="API_DeleteRepository_ResponseSyntax"></a>

```
{
   "repository": {
      "createdAt": number,
      "encryptionConfiguration": {
         "encryptionType": "string",
         "kmsKey": "string"
      },
      "imageScanningConfiguration": {
         "scanOnPush": boolean
      },
      "imageTagMutability": "string",
      "imageTagMutabilityExclusionFilters": [
         {
            "filter": "string",
            "filterType": "string"
         }
      ],
      "registryId": "string",
      "repositoryArn": "string",
      "repositoryName": "string",
      "repositoryUri": "string"
   }
}
```

## Response Elements
<a name="API_DeleteRepository_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [repository](#API_DeleteRepository_ResponseSyntax) **   <a name="ECR-DeleteRepository-response-repository"></a>
The repository that was deleted.
Type: [Repository](API_Repository.md) object

## Errors
<a name="API_DeleteRepository_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** KmsException **
The operation failed due to a KMS exception.
 ** kmsError **
The error code returned by AWS KMS.
HTTP Status Code: 400

 ** RepositoryNotEmptyException **
The specified repository contains images. To delete a repository that contains images, you must force the deletion with the `force` parameter.
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

## Examples
<a name="API_DeleteRepository_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DeleteRepository_Example_1"></a>

This example deletes a repository named `ubuntu` in the default registry for an account.

#### Sample Request
<a name="API_DeleteRepository_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: api.ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.DeleteRepository
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.16.190 Python/3.6.1 Darwin/16.7.0 botocore/1.12.180
X-Amz-Date: 20190715T205933Z
Authorization: AUTHPARAMS
Content-Length: 33

{
   "repositoryName":"sample-repo"
}
```

#### Sample Response
<a name="API_DeleteRepository_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f
Content-Type: application/x-amz-json-1.1
Content-Length: 252
Connection: keep-alive

{
   "repository":{
      "createdAt":1.563223656E9,
      "registryId":"012345678910",
      "repositoryArn":"arn:aws:ecr:us-west-2:012345678910:repository/sample-repo",
      "repositoryName":"sample-repo",
      "repositoryUri":"012345678910.dkr.ecr.us-west-2.amazonaws.com/sample-repo"
   }
}
```

## See Also
<a name="API_DeleteRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/DeleteRepository)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/DeleteRepository)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/DeleteRepository)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/DeleteRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DeleteRepository)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/DeleteRepository)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/DeleteRepository)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/DeleteRepository)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DeleteRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/DeleteRepository)
