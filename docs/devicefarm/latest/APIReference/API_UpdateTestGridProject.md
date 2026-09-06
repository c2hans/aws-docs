---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_UpdateTestGridProject.html
---

# UpdateTestGridProject
<a name="API_UpdateTestGridProject"></a>

Change details of a project.

## Request Syntax
<a name="API_UpdateTestGridProject_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "name": "{{string}}",
   "projectArn": "{{string}}",
   "vpcConfig": {
      "securityGroupIds": [ "{{string}}" ],
      "subnetIds": [ "{{string}}" ],
      "vpcId": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateTestGridProject_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_UpdateTestGridProject_RequestSyntax) **   <a name="devicefarm-UpdateTestGridProject-request-description"></a>
Human-readable description for the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** [name](#API_UpdateTestGridProject_RequestSyntax) **   <a name="devicefarm-UpdateTestGridProject-request-name"></a>
Human-readable name for the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: No

 ** [projectArn](#API_UpdateTestGridProject_RequestSyntax) **   <a name="devicefarm-UpdateTestGridProject-request-projectArn"></a>
ARN of the project to update.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [vpcConfig](#API_UpdateTestGridProject_RequestSyntax) **   <a name="devicefarm-UpdateTestGridProject-request-vpcConfig"></a>
The VPC security groups and subnets that are attached to a project.
Type: [TestGridVpcConfig](API_TestGridVpcConfig.md) object
Required: No

## Response Syntax
<a name="API_UpdateTestGridProject_ResponseSyntax"></a>

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
<a name="API_UpdateTestGridProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [testGridProject](#API_UpdateTestGridProject_ResponseSyntax) **   <a name="devicefarm-UpdateTestGridProject-response-testGridProject"></a>
The project, including updated information.
Type: [TestGridProject](API_TestGridProject.md) object

## Errors
<a name="API_UpdateTestGridProject_Errors"></a>

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

 ** NotFoundException **
The specified entity was not found.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateTestGridProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/UpdateTestGridProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/UpdateTestGridProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/UpdateTestGridProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/UpdateTestGridProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/UpdateTestGridProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/UpdateTestGridProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/UpdateTestGridProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/UpdateTestGridProject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/UpdateTestGridProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/UpdateTestGridProject)
