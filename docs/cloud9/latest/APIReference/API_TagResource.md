---
source_url: https://docs.aws.amazon.com/cloud9/latest/APIReference/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Adds tags to an AWS Cloud9 development environment.

**Important**
 AWS Cloud9 is no longer available to new customers. Existing customers of AWS Cloud9 can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/)

**Important**
Tags that you add to an AWS Cloud9 environment by using this method will NOT be automatically propagated to underlying resources.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
{
   "ResourceARN": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_TagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceARN](#API_TagResource_RequestSyntax) **   <a name="cloud9-TagResource-request-ResourceARN"></a>
The Amazon Resource Name (ARN) of the AWS Cloud9 development environment to add tags to.
Type: String
Pattern: `arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):cloud9:([a-z]{2}-[a-z]+-\d{1}):[0-9]{12}:environment:[a-zA-Z0-9]{8,32}`
Required: Yes

 ** [Tags](#API_TagResource_RequestSyntax) **   <a name="cloud9-TagResource-request-Tags"></a>
The list of tags to add to the given AWS Cloud9 development environment.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: Yes

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The target request is invalid.
HTTP Status Code: 400

 ** ConcurrentAccessException **
A concurrent access issue occurred.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error occurred.
HTTP Status Code: 500

 ** NotFoundException **
The target resource cannot be found.
HTTP Status Code: 400

## Examples
<a name="API_TagResource_Examples"></a>

### Example
<a name="API_TagResource_Example_1"></a>

The following example shows how to add tags to an AWS Cloud9 development environment.

#### Sample Request
<a name="API_TagResource_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: cloud9.<region>.amazonaws.com
Accept-Encoding: identity
Content-Type: application/x-amz-json-1.1
X-Amz-Date: <Date>
User-Agent: <UserAgentString>
X-Amz-Target: AWSCloud9WorkspaceManagementService.TagResource
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>

{
  "ResourceARN": "arn:aws:cloud9:eu-west-1:123456789012:environment:8d9967e2f0624182b74e7690ad69ebEX",
  "Tags": [
    {
      "Key": "key",
      "Value": "orange"
    }
  ]
}
```

#### Sample Response
<a name="API_TagResource_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: <Date>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
x-amzn-RequestId: <RequestId>
Connection: Keep-alive

{}
```

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloud9-2017-09-23/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloud9-2017-09-23/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloud9-2017-09-23/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloud9-2017-09-23/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloud9-2017-09-23/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloud9-2017-09-23/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloud9-2017-09-23/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/TagResource)
