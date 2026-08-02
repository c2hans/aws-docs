---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteRepositoryCreationTemplate.html
---

# DeleteRepositoryCreationTemplate
<a name="API_DeleteRepositoryCreationTemplate"></a>

Deletes a repository creation template.

## Request Syntax
<a name="API_DeleteRepositoryCreationTemplate_RequestSyntax"></a>

```
{
   "prefix": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteRepositoryCreationTemplate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [prefix](#API_DeleteRepositoryCreationTemplate_RequestSyntax) **   <a name="ECR-DeleteRepositoryCreationTemplate-request-prefix"></a>
The repository namespace prefix associated with the repository creation template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`
Required: Yes

## Response Syntax
<a name="API_DeleteRepositoryCreationTemplate_ResponseSyntax"></a>

```
{
   "registryId": "string",
   "repositoryCreationTemplate": {
      "appliedFor": [ "string" ],
      "createdAt": number,
      "customRoleArn": "string",
      "description": "string",
      "encryptionConfiguration": {
         "encryptionType": "string",
         "kmsKey": "string"
      },
      "imageTagMutability": "string",
      "imageTagMutabilityExclusionFilters": [
         {
            "filter": "string",
            "filterType": "string"
         }
      ],
      "lifecyclePolicy": "string",
      "prefix": "string",
      "repositoryPolicy": "string",
      "resourceTags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_DeleteRepositoryCreationTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [registryId](#API_DeleteRepositoryCreationTemplate_ResponseSyntax) **   <a name="ECR-DeleteRepositoryCreationTemplate-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [repositoryCreationTemplate](#API_DeleteRepositoryCreationTemplate_ResponseSyntax) **   <a name="ECR-DeleteRepositoryCreationTemplate-response-repositoryCreationTemplate"></a>
The details of the repository creation template that was deleted.
Type: [RepositoryCreationTemplate](API_RepositoryCreationTemplate.md) object

## Errors
<a name="API_DeleteRepositoryCreationTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** message **
The error message associated with the exception.
HTTP Status Code: 500

 ** TemplateNotFoundException **
The specified repository creation template can't be found. Verify the registry ID and prefix and try again.
HTTP Status Code: 400

 ** ValidationException **
There was an exception validating this request.
HTTP Status Code: 400

## Examples
<a name="API_DeleteRepositoryCreationTemplate_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DeleteRepositoryCreationTemplate_Example_1"></a>

This example deletes a repository creation template in the default registry for an account.

#### Sample Request
<a name="API_DeleteRepositoryCreationTemplate_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 88
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.DescribeRepositoryCreationTemplates
X-Amz-Date: 20231216T195356Z
User-Agent: aws-cli/1.11.22 Python/2.7.12 Darwin/16.3.0 botocore/1.4.79
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
 "prefix": "eng"
}
```

#### Sample Response
<a name="API_DeleteRepositoryCreationTemplate_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Sat, 16 Dec 2023 19:54:56 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 666
Connection: keep-alive
x-amzn-RequestId: 60dc1ea1-c3c9-11e6-aa04-25c3a5fb1b54

{
    "registryId": "012345678901",
    "repositoryCreationTemplate": {
        "prefix": "eng",
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        },
        "imageTagMutability": "MUTABLE"
        "createdAt": "2023-12-03T16:27:57.933000-08:00",
        "updatedAt": "2023-12-03T16:27:57.933000-08:00"
    }
}
```

## See Also
<a name="API_DeleteRepositoryCreationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/DeleteRepositoryCreationTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/DeleteRepositoryCreationTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/DeleteRepositoryCreationTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/DeleteRepositoryCreationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DeleteRepositoryCreationTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/DeleteRepositoryCreationTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/DeleteRepositoryCreationTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/DeleteRepositoryCreationTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DeleteRepositoryCreationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/DeleteRepositoryCreationTemplate)
