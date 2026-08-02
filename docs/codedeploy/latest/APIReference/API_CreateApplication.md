---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateApplication.html
---

# CreateApplication
<a name="API_CreateApplication"></a>

Creates an application.

## Request Syntax
<a name="API_CreateApplication_RequestSyntax"></a>

```
{
   "applicationName": "{{string}}",
   "computePlatform": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateApplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [applicationName](#API_CreateApplication_RequestSyntax) **   <a name="CodeDeploy-CreateApplication-request-applicationName"></a>
The name of the application. This name must be unique with the applicable user or AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [computePlatform](#API_CreateApplication_RequestSyntax) **   <a name="CodeDeploy-CreateApplication-request-computePlatform"></a>
 The destination platform type for the deployment (`Lambda`, `Server`, or `ECS`).
Type: String
Valid Values: `Server | Lambda | ECS | Kubernetes`
Required: No

 ** [tags](#API_CreateApplication_RequestSyntax) **   <a name="CodeDeploy-CreateApplication-request-tags"></a>
 The metadata that you apply to CodeDeploy applications to help you organize and categorize them. Each tag consists of a key and an optional value, both of which you define.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateApplication_ResponseSyntax"></a>

```
{
   "applicationId": "string"
}
```

## Response Elements
<a name="API_CreateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationId](#API_CreateApplication_ResponseSyntax) **   <a name="CodeDeploy-CreateApplication-response-applicationId"></a>
A unique application ID.
Type: String

## Errors
<a name="API_CreateApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApplicationAlreadyExistsException **
An application with the specified name with the user or AWS account already exists.
HTTP Status Code: 400

 ** ApplicationLimitExceededException **
More applications were attempted to be created than are allowed.
HTTP Status Code: 400

 ** ApplicationNameRequiredException **
The minimum number of required application names was not specified.
HTTP Status Code: 400

 ** InvalidApplicationNameException **
The application name was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidComputePlatformException **
The computePlatform is invalid. The computePlatform should be `Lambda`, `Server`, or `ECS`.
HTTP Status Code: 400

 ** InvalidTagsToAddException **
 The specified tags are not valid.
HTTP Status Code: 400

## Examples
<a name="API_CreateApplication_Examples"></a>

### Example
<a name="API_CreateApplication_Example_1"></a>

This example illustrates one usage of CreateApplication.

#### Sample Request
<a name="API_CreateApplication_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 37
X-Amz-Target: CodeDeploy_20141006.CreateApplication
X-Amz-Date: 20160707T233029Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "applicationName": "TestApp-ap-southeast-2"
}
```

#### Sample Response
<a name="API_CreateApplication_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 32431157-88cc-11e5-a908-6dc86959d022
Content-Type: application/x-amz-json-1.1
Content-Length: 56

{
    "applicationId": "767c40ba-2c8d-4ec1-8649-3gd18EXAMPLE"
}
```

## See Also
<a name="API_CreateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/CreateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/CreateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/CreateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/CreateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/CreateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/CreateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/CreateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/CreateApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/CreateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/CreateApplication)
