---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeregisterPullTimeUpdateExclusion.html
---

# DeregisterPullTimeUpdateExclusion
<a name="API_DeregisterPullTimeUpdateExclusion"></a>

Removes a principal from the pull time update exclusion list for a registry. Once removed, Amazon ECR will resume updating the pull time if the specified principal pulls an image.

## Request Syntax
<a name="API_DeregisterPullTimeUpdateExclusion_RequestSyntax"></a>

```
{
   "principalArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeregisterPullTimeUpdateExclusion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [principalArn](#API_DeregisterPullTimeUpdateExclusion_RequestSyntax) **   <a name="ECR-DeregisterPullTimeUpdateExclusion-request-principalArn"></a>
The ARN of the IAM principal to remove from the pull time update exclusion list.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `^arn:aws(-[a-z]+)*:iam::[0-9]{12}:(role|user)/[\w+=,.@-]+(/[\w+=,.@-]+)*$`
Required: Yes

## Response Syntax
<a name="API_DeregisterPullTimeUpdateExclusion_ResponseSyntax"></a>

```
{
   "principalArn": "string"
}
```

## Response Elements
<a name="API_DeregisterPullTimeUpdateExclusion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [principalArn](#API_DeregisterPullTimeUpdateExclusion_ResponseSyntax) **   <a name="ECR-DeregisterPullTimeUpdateExclusion-response-principalArn"></a>
The ARN of the IAM principal that was removed from the pull time update exclusion list.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `^arn:aws(-[a-z]+)*:iam::[0-9]{12}:(role|user)/[\w+=,.@-]+(/[\w+=,.@-]+)*$`

## Errors
<a name="API_DeregisterPullTimeUpdateExclusion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ExclusionNotFoundException **
The specified pull time update exclusion was not found.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** LimitExceededException **
The operation did not succeed because it would have exceeded a service limit for your account. For more information, see [Amazon ECR service quotas](https://docs.aws.amazon.com/AmazonECR/latest/userguide/service-quotas.html) in the Amazon Elastic Container Registry User Guide.
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

## Examples
<a name="API_DeregisterPullTimeUpdateExclusion_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### To remove a principal from the pull time exclusion list
<a name="API_DeregisterPullTimeUpdateExclusion_Example_1"></a>

This example removes an IAM role from the pull time update exclusion list.

#### Sample Request
<a name="API_DeregisterPullTimeUpdateExclusion_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: api.ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.DeregisterPullTimeUpdateExclusion
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0 Python/3.8.0 Darwin/20.0.0 botocore/2.0.0
X-Amz-Date: 20251117T220830Z
Authorization: AUTHPARAMS
Content-Length: 73

{
   "principalArn": "arn:aws:iam::012345678910:role/ECRAccess"
}
```

#### Sample Response
<a name="API_DeregisterPullTimeUpdateExclusion_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f
Content-Type: application/x-amz-json-1.1
Content-Length: 73
Connection: keep-alive

{
   "principalArn": "arn:aws:iam::012345678910:role/ECRAccess"
}
```

## See Also
<a name="API_DeregisterPullTimeUpdateExclusion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/DeregisterPullTimeUpdateExclusion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/DeregisterPullTimeUpdateExclusion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/DeregisterPullTimeUpdateExclusion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/DeregisterPullTimeUpdateExclusion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DeregisterPullTimeUpdateExclusion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/DeregisterPullTimeUpdateExclusion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/DeregisterPullTimeUpdateExclusion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/DeregisterPullTimeUpdateExclusion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DeregisterPullTimeUpdateExclusion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/DeregisterPullTimeUpdateExclusion)
