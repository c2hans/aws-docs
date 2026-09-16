---
source_url: https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_UntagResources.html
---

# UntagResources
<a name="API_UntagResources"></a>

Removes the specified tags from the specified resources. When you specify a tag key, the action removes both that key and its associated value. The operation succeeds even if you attempt to remove tags from a resource that were already removed. Note the following:
+ To remove tags from a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for removing tags. For more information, see the documentation for the service whose resource you want to untag.
+ You can only tag resources that are located in the specified AWS Region for the calling AWS account.

 **Minimum permissions**

In addition to the `tag:UntagResources` permission required by this operation, you must also have the remove tags permission defined by the service that created the resource. For example, to remove the tags from an Amazon EC2 instance using the `UntagResources` operation, you must have both of the following permissions:
+  `tag:UntagResources`
+  `ec2:DeleteTags`

**Note**
In addition, some services might have specific requirements for untagging some types of resources. For example, to untag AWS Glue Connection, you must also have the `glue:GetConnection` permission. If the expected minimum permissions don't work, check the documentation for that service's tagging APIs for more information.

## Request Syntax
<a name="API_UntagResources_RequestSyntax"></a>

```
{
   "ResourceARNList": [ "{{string}}" ],
   "TagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UntagResources_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceARNList](#API_UntagResources_RequestSyntax) **   <a name="resourcegrouptagging-UntagResources-request-ResourceARNList"></a>
Specifies a list of ARNs of the resources that you want to remove tags from.
An ARN (Amazon Resource Name) uniquely identifies a resource. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `[\s\S]*`
Required: Yes

 ** [TagKeys](#API_UntagResources_RequestSyntax) **   <a name="resourcegrouptagging-UntagResources-request-TagKeys"></a>
Specifies a list of tag keys that you want to remove from the specified resources.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\s\S]*`
Required: Yes

## Response Syntax
<a name="API_UntagResources_ResponseSyntax"></a>

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
<a name="API_UntagResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedResourcesMap](#API_UntagResources_ResponseSyntax) **   <a name="resourcegrouptagging-UntagResources-response-FailedResourcesMap"></a>
A map containing a key-value pair for each failed item that couldn't be untagged. The key is the ARN of the failed resource. The value is a `FailureInfo` object that contains an error code, a status code, and an error message. If there are no errors, the `FailedResourcesMap` is empty.
Type: String to [FailureInfo](API_FailureInfo.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 1011.
Key Pattern: `[\s\S]*`

## Errors
<a name="API_UntagResources_Errors"></a>

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
<a name="API_UntagResources_Examples"></a>

### Example
<a name="API_UntagResources_Example_1"></a>

This example illustrates one usage of UntagResources.

#### Sample Request
<a name="API_UntagResources_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: tagging.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 74
X-Amz-Target: ResourceGroupsTaggingAPI_20170126.UntagResources
X-Amz-Date: 20170421T215122Z
User-Agent: aws-cli/1.11.79 Python/2.7.9 Windows/7 botocore/1.5.42
Content-Type: application/x-amz-json-1.1
Authorization:  AUTHPARAMS
{
    "TagKeys": [
        "key"
    ],
    "ResourceARNList": [
        "arn:aws:s3:::amzn-s3-demo-bucket"
    ]
}
```

#### Sample Response
<a name="API_UntagResources_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: a923ddd9-26dc-11e7-bf86-49f2fe9ee8df
Content-Type: application/x-amz-json-1.1
Content-Length: 25
Date: Fri, 21 Apr 2017 21:51:23 GMT

{
    "FailedResourcesMap": {}
}
```

## See Also
<a name="API_UntagResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resourcegroupstaggingapi-2017-01-26/UntagResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resourcegroupstaggingapi-2017-01-26/UntagResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/UntagResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resourcegroupstaggingapi-2017-01-26/UntagResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/UntagResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resourcegroupstaggingapi-2017-01-26/UntagResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resourcegroupstaggingapi-2017-01-26/UntagResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resourcegroupstaggingapi-2017-01-26/UntagResources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resourcegroupstaggingapi-2017-01-26/UntagResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/UntagResources)
