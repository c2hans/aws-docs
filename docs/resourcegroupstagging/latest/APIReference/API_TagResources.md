---
source_url: https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources.html
---

# TagResources
<a name="API_TagResources"></a>

Applies one or more tags to the specified resources. Note the following:
+ Not all resources can have tags. For a list of services with resources that support tagging using this operation, see [Services that support the Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html). If the resource doesn't yet support this operation, the resource's service might support tagging using its own API operations. For more information, refer to the documentation for that service.
+ Each resource can have up to 50 tags. For other limits, see [Tag Naming and Usage Conventions](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions) in the * AWS General Reference.*
+ You can only tag resources that are located in the specified AWS Region for the AWS account.
+ To add tags to a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for adding tags. For more information, see the documentation for each service.
+ When you use the [AWS Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/overview.html) to update tags for AWS CloudFormation stack sets, AWS calls the [AWS CloudFormation `UpdateStack`](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStack.html) operation. This operation may initiate additional resource property updates in addition to the desired tag updates. To avoid unexpected resource updates, AWS recommends that you only apply or update tags to your CloudFormation stack sets using AWS CloudFormation.

**Important**
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use tags to provide you with billing and administration services. Tags are not intended to be used for private or sensitive data.

 **Minimum permissions**

In addition to the `tag:TagResources` permission required by this operation, you must also have the tagging permission defined by the service that created the resource. For example, to tag an Amazon EC2 instance using the `TagResources` operation, you must have both of the following permissions:
+  `tag:TagResources`
+  `ec2:CreateTags`

**Note**
In addition, some services might have specific requirements for tagging some types of resources. For example, to tag an Amazon S3 bucket, you must also have the `s3:GetBucketTagging` permission. If the expected minimum permissions don't work, check the documentation for that service's tagging APIs for more information.

## Request Syntax
<a name="API_TagResources_RequestSyntax"></a>

```
{
   "ResourceARNList": [ "{{string}}" ],
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_TagResources_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceARNList](#API_TagResources_RequestSyntax) **   <a name="resourcegrouptagging-TagResources-request-ResourceARNList"></a>
Specifies the list of ARNs of the resources that you want to apply tags to.
An ARN (Amazon Resource Name) uniquely identifies a resource. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `[\s\S]*`
Required: Yes

 ** [Tags](#API_TagResources_RequestSyntax) **   <a name="resourcegrouptagging-TagResources-request-Tags"></a>
Specifies a list of tags that you want to add to the specified resources. A tag consists of a key and a value that you define.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\s\S]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\s\S]*`
Required: Yes

## Response Syntax
<a name="API_TagResources_ResponseSyntax"></a>

```
{
   "FailedResourcesMap": {
      "string" : {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "StatusCode": number
      }
   }
}
```

## Response Elements
<a name="API_TagResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedResourcesMap](#API_TagResources_ResponseSyntax) **   <a name="resourcegrouptagging-TagResources-response-FailedResourcesMap"></a>
A map containing a key-value pair for each failed item that couldn't be tagged. The key is the ARN of the failed resource. The value is a `FailureInfo` object that contains an error code, a status code, and an error message. If there are no errors, the `FailedResourcesMap` is empty.
Type: String to [FailureInfo](API_FailureInfo.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 1011.
Key Pattern: `[\s\S]*`

## Errors
<a name="API_TagResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The request processing failed because of an unknown error, exception, or failure. You can retry the request.
HTTP Status Code: 500

 ** InvalidParameterException **
The request failed because of one of the following reasons:
+ A required parameter is missing.
+ A provided string parameter is malformed.
+ An provided parameter value is out of range.
+ The target ID is invalid, unsupported, or doesn't exist.
+ You can't access the Amazon S3 bucket for report storage. For more information, see [Amazon S3 bucket policy for report storage](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy) in the *Tagging AWS resources and Tag Editor* user guide.
+ The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.
HTTP Status Code: 400

 ** ThrottledException **
The request failed because it exceeded the allowed frequency of submitted requests.
HTTP Status Code: 400

## Examples
<a name="API_TagResources_Examples"></a>

### Example
<a name="API_TagResources_Example_1"></a>

This example illustrates one usage of TagResources.

#### Sample Request
<a name="API_TagResources_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: tagging.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 82
X-Amz-Target: ResourceGroupsTaggingAPI_20170126.TagResources
X-Amz-Date: 20170421T214834Z
User-Agent: aws-cli/1.11.79 Python/2.7.9 Windows/7 botocore/1.5.42
Content-Type: application/x-amz-json-1.1
Authorization:  AUTHPARAMS
{
    "ResourceARNList": [
        "arn:aws:s3:::amzn-s3-demo-bucket"
    ],
    "Tags": {
        "key": "Example_key"
    }
}
```

#### Sample Response
<a name="API_TagResources_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 45352206-26dc-11e7-8812-6fb02084e31d
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Fri, 21 Apr 2017 21:48:35 GMT
```

## See Also
<a name="API_TagResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resourcegroupstaggingapi-2017-01-26/TagResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resourcegroupstaggingapi-2017-01-26/TagResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/TagResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resourcegroupstaggingapi-2017-01-26/TagResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/TagResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resourcegroupstaggingapi-2017-01-26/TagResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resourcegroupstaggingapi-2017-01-26/TagResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resourcegroupstaggingapi-2017-01-26/TagResources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resourcegroupstaggingapi-2017-01-26/TagResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/TagResources)
