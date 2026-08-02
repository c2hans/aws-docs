---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetApplication.html
---

# GetApplication
<a name="API_GetApplication"></a>

Gets information about an application.

## Request Syntax
<a name="API_GetApplication_RequestSyntax"></a>

```
{
   "applicationName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetApplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [applicationName](#API_GetApplication_RequestSyntax) **   <a name="CodeDeploy-GetApplication-request-applicationName"></a>
The name of an AWS CodeDeploy application associated with the user or AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_GetApplication_ResponseSyntax"></a>

```
{
   "application": {
      "applicationId": "string",
      "applicationName": "string",
      "computePlatform": "string",
      "createTime": number,
      "gitHubAccountName": "string",
      "linkedToGitHub": boolean
   }
}
```

## Response Elements
<a name="API_GetApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [application](#API_GetApplication_ResponseSyntax) **   <a name="CodeDeploy-GetApplication-response-application"></a>
Information about the application.
Type: [ApplicationInfo](API_ApplicationInfo.md) object

## Errors
<a name="API_GetApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApplicationDoesNotExistException **
The application does not exist with the user or AWS account.
HTTP Status Code: 400

 ** ApplicationNameRequiredException **
The minimum number of required application names was not specified.
HTTP Status Code: 400

 ** InvalidApplicationNameException **
The application name was specified in an invalid format.
HTTP Status Code: 400

## Examples
<a name="API_GetApplication_Examples"></a>

### Example
<a name="API_GetApplication_Example_1"></a>

This example illustrates one usage of GetApplication.

#### Sample Request
<a name="API_GetApplication_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 45
X-Amz-Target: CodeDeploy_20141006.GetApplication
X-Amz-Date: 20160707T014559Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "applicationName": "TestApp-us-east-1"
}
```

#### Sample Response
<a name="API_GetApplication_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 2010bbbd-88df-11e5-9749-bba241db97da
Content-Type: application/x-amz-json-1.1
Content-Length: 168

{
    "application": {
        "applicationId": "d3be67e5-e7l6-457b-946b-7a457EXAMPLE",
        "applicationName": "TestApp-us-east-1",
        "createTime": 1446229001.211,
        "linkedToGitHub": false
    }
}
```

## See Also
<a name="API_GetApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/GetApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/GetApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/GetApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/GetApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/GetApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/GetApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/GetApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/GetApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/GetApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/GetApplication)
