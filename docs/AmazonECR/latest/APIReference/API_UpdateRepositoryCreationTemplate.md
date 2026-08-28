---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_UpdateRepositoryCreationTemplate.html
---

# UpdateRepositoryCreationTemplate
<a name="API_UpdateRepositoryCreationTemplate"></a>

Updates an existing repository creation template.

## Request Syntax
<a name="API_UpdateRepositoryCreationTemplate_RequestSyntax"></a>

```
{
   "appliedFor": [ "{{string}}" ],
   "customRoleArn": "{{string}}",
   "description": "{{string}}",
   "encryptionConfiguration": {
      "encryptionType": "{{string}}",
      "kmsKey": "{{string}}"
   },
   "imageTagMutability": "{{string}}",
   "imageTagMutabilityExclusionFilters": [
      {
         "filter": "{{string}}",
         "filterType": "{{string}}"
      }
   ],
   "lifecyclePolicy": "{{string}}",
   "prefix": "{{string}}",
   "repositoryPolicy": "{{string}}",
   "resourceTags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateRepositoryCreationTemplate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [appliedFor](#API_UpdateRepositoryCreationTemplate_RequestSyntax) **   <a name="ECR-UpdateRepositoryCreationTemplate-request-appliedFor"></a>
Updates the list of enumerable strings representing the Amazon ECR repository creation scenarios that this template will apply towards. The supported scenarios are `PULL_THROUGH_CACHE`, `REPLICATION`, and `CREATE_ON_PUSH`
Type: Array of strings
Valid Values: `REPLICATION | PULL_THROUGH_CACHE | CREATE_ON_PUSH`
Required: No

 ** [customRoleArn](#API_UpdateRepositoryCreationTemplate_RequestSyntax) **   <a name="ECR-UpdateRepositoryCreationTemplate-request-customRoleArn"></a>
The ARN of the role to be assumed by Amazon ECR. This role must be in the same account as the registry that you are configuring. Amazon ECR will assume your supplied role when the customRoleArn is specified. When this field isn't specified, Amazon ECR will use the service-linked role for the repository creation template.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [description](#API_UpdateRepositoryCreationTemplate_RequestSyntax) **   <a name="ECR-UpdateRepositoryCreationTemplate-request-description"></a>
A description for the repository creation template.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [encryptionConfiguration](#API_UpdateRepositoryCreationTemplate_RequestSyntax) **   <a name="ECR-UpdateRepositoryCreationTemplate-request-encryptionConfiguration"></a>
The encryption configuration to associate with the repository creation template.
Type: [EncryptionConfigurationForRepositoryCreationTemplate](API_EncryptionConfigurationForRepositoryCreationTemplate.md) object
Required: No

 ** [imageTagMutability](#API_UpdateRepositoryCreationTemplate_RequestSyntax) **   <a name="ECR-UpdateRepositoryCreationTemplate-request-imageTagMutability"></a>
Updates the tag mutability setting for the repository. If this parameter is omitted, the default setting of `MUTABLE` will be used which will allow image tags to be overwritten. If `IMMUTABLE` is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.
Type: String
Valid Values: `MUTABLE | IMMUTABLE | IMMUTABLE_WITH_EXCLUSION | MUTABLE_WITH_EXCLUSION`
Required: No

 ** [imageTagMutabilityExclusionFilters](#API_UpdateRepositoryCreationTemplate_RequestSyntax) **   <a name="ECR-UpdateRepositoryCreationTemplate-request-imageTagMutabilityExclusionFilters"></a>
A list of filters that specify which image tags should be excluded from the repository creation template's image tag mutability setting.
Type: Array of [ImageTagMutabilityExclusionFilter](API_ImageTagMutabilityExclusionFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [lifecyclePolicy](#API_UpdateRepositoryCreationTemplate_RequestSyntax) **   <a name="ECR-UpdateRepositoryCreationTemplate-request-lifecyclePolicy"></a>
Updates the lifecycle policy associated with the specified repository creation template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 30720.
Required: No

 ** [prefix](#API_UpdateRepositoryCreationTemplate_RequestSyntax) **   <a name="ECR-UpdateRepositoryCreationTemplate-request-prefix"></a>
The repository namespace prefix that matches an existing repository creation template in the registry. All repositories created using this namespace prefix will have the settings defined in this template applied. For example, a prefix of `prod` would apply to all repositories beginning with `prod/`. This includes a repository named `prod/team1` as well as a repository named `prod/repository1`.
To apply a template to all repositories in your registry that don't have an associated creation template, you can use `ROOT` as the prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`
Required: Yes

 ** [repositoryPolicy](#API_UpdateRepositoryCreationTemplate_RequestSyntax) **   <a name="ECR-UpdateRepositoryCreationTemplate-request-repositoryPolicy"></a>
Updates the repository policy created using the template. A repository policy is a permissions policy associated with a repository to control access permissions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Required: No

 ** [resourceTags](#API_UpdateRepositoryCreationTemplate_RequestSyntax) **   <a name="ECR-UpdateRepositoryCreationTemplate-request-resourceTags"></a>
The metadata to apply to the repository to help you categorize and organize. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_UpdateRepositoryCreationTemplate_ResponseSyntax"></a>

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
<a name="API_UpdateRepositoryCreationTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [registryId](#API_UpdateRepositoryCreationTemplate_ResponseSyntax) **   <a name="ECR-UpdateRepositoryCreationTemplate-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [repositoryCreationTemplate](#API_UpdateRepositoryCreationTemplate_ResponseSyntax) **   <a name="ECR-UpdateRepositoryCreationTemplate-response-repositoryCreationTemplate"></a>
The details of the repository creation template associated with the request.
Type: [RepositoryCreationTemplate](API_RepositoryCreationTemplate.md) object

## Errors
<a name="API_UpdateRepositoryCreationTemplate_Errors"></a>

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
<a name="API_UpdateRepositoryCreationTemplate_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_UpdateRepositoryCreationTemplate_Example_1"></a>

This example updates a repository creation template in the default registry for an account.

#### Sample Request
<a name="API_UpdateRepositoryCreationTemplate_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length:240
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.UpdateRepositoryCreationTemplate
X-Amz-Date: 20231216T195356Z
User-Agent: aws-cli/1.11.22 Python/2.7.12 Darwin/16.3.0 botocore/1.4.79
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
 "prefix": "eng/test",
 "resourceTags":
  [
    {"Key": "environment",
     "Value": "test"}
  ],
  "appliedFor":
  ["REPLICATION"]
}
```

#### Sample Response
<a name="API_UpdateRepositoryCreationTemplate_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Sat, 16 Dec 2023 19:54:56 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 950
Connection: keep-alive
x-amzn-RequestId: 60dc1ea1-c3c9-11e6-aa04-25c3a5fb1b54

{
 "registryId": "012345678901",
 "repositoryCreationTemplate":
  {
   "appliedFor":
    ["REPLICATION"],
   "description": "Repos for testing images",
   "encryptionConfiguration":
    {
        "encryptionType": "AES256"
    },
   "imageTagMutability": "MUTABLE",
   "lifecyclePolicy": "{\r\n    \"rules\": [\r\n        {\r\n            \"rulePriority\": 1,\r\n            \"description\": \"Expire images older than 14 days\",\r\n            \"selection\": {\r\n                \"tagStatus\": \"untagged\",\r\n                \"countType\": \"sinceImagePushed\",\r\n                \"countUnit\": \"days\",\r\n                \"countNumber\": 14\r\n            },\r\n            \"action\": {\r\n                \"type\": \"expire\"\r\n            }\r\n        }\r\n    ]\r\n}",
   "prefix": "eng/test",
   "repositoryPolicy": "{\n  \"Version\" : \"2012-10-17\",\n  \"Statement\" : [ {\n    \"Sid\" : \"LambdaECRPullPolicy\",\n    \"Effect\" : \"Allow\",\n    \"Principal\" : {\n      \"Service\" : \"lambda.amazonaws.com\"\n    },\n    \"Action\" : \"ecr:BatchGetImage\"\n  } ]\n}",
   "resourceTags":
    [
      {"Key": "environment",
       "Value": "test"}
    ],
   "createdAt": "2023-12-16T17:29:02-07:00",
   "updatedAt": "2023-12-16T19:55:02-07:00"
  }
}
```

## See Also
<a name="API_UpdateRepositoryCreationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/UpdateRepositoryCreationTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/UpdateRepositoryCreationTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/UpdateRepositoryCreationTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/UpdateRepositoryCreationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/UpdateRepositoryCreationTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/UpdateRepositoryCreationTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/UpdateRepositoryCreationTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/UpdateRepositoryCreationTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/UpdateRepositoryCreationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/UpdateRepositoryCreationTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
