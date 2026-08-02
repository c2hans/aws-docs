---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateTestGridProject.html
---

# CreateTestGridProject
<a name="API_CreateTestGridProject"></a>

Creates a Selenium testing project. Projects are used to track [TestGridSession](API_TestGridSession.md) instances.

## Request Syntax
<a name="API_CreateTestGridProject_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "name": "{{string}}",
   "vpcConfig": {
      "securityGroupIds": [ "{{string}}" ],
      "subnetIds": [ "{{string}}" ],
      "vpcId": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateTestGridProject_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_CreateTestGridProject_RequestSyntax) **   <a name="devicefarm-CreateTestGridProject-request-description"></a>
Human-readable description of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** [name](#API_CreateTestGridProject_RequestSyntax) **   <a name="devicefarm-CreateTestGridProject-request-name"></a>
Human-readable name of the Selenium testing project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: Yes

 ** [vpcConfig](#API_CreateTestGridProject_RequestSyntax) **   <a name="devicefarm-CreateTestGridProject-request-vpcConfig"></a>
The VPC security groups and subnets that are attached to a project.
Type: [TestGridVpcConfig](API_TestGridVpcConfig.md) object
Required: No

## Response Syntax
<a name="API_CreateTestGridProject_ResponseSyntax"></a>

```
{
   "testGridProject": {
      "arn": "string",
      "created": number,
      "description": "string",
      "name": "string",
      "vpcConfig": {
         "securityGroupIds": [ "string" ],
         "subnetIds": [ "string" ],
         "vpcId": "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateTestGridProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [testGridProject](#API_CreateTestGridProject_ResponseSyntax) **   <a name="devicefarm-CreateTestGridProject-response-testGridProject"></a>
ARN of the Selenium testing project that was created.
Type: [TestGridProject](API_TestGridProject.md) object

## Errors
<a name="API_CreateTestGridProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** InternalServiceException **
An internal exception was raised in the service. Contact [aws-devicefarm-support@amazon.com](mailto:aws-devicefarm-support@amazon.com) if you see this error.
HTTP Status Code: 500

 ** LimitExceededException **
A limit was exceeded.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateTestGridProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/CreateTestGridProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/CreateTestGridProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/CreateTestGridProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/CreateTestGridProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/CreateTestGridProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/CreateTestGridProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/CreateTestGridProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/CreateTestGridProject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/CreateTestGridProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/CreateTestGridProject)
