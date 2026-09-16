---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_AssociateServiceRoleToAccount.html
---

# AssociateServiceRoleToAccount
<a name="API_AssociateServiceRoleToAccount"></a>

Associates a Greengrass service role with AWS IoT Greengrass for your AWS account in this AWS Region. AWS IoT Greengrass uses this role to verify the identity of client devices and manage core device connectivity information. The role must include the [AWSGreengrassResourceAccessRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:awsiam::aws:policy/service-role/AWSGreengrassResourceAccessRolePolicy) managed policy or a custom policy that defines equivalent permissions for the AWS IoT Greengrass features that you use. For more information, see [Greengrass service role](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-service-role.html) in the * AWS IoT Greengrass Version 2 Developer Guide*.

## Request Syntax
<a name="API_AssociateServiceRoleToAccount_RequestSyntax"></a>

```
PUT /greengrass/servicerole HTTP/1.1
Content-type: application/json

{
   "RoleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateServiceRoleToAccount_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AssociateServiceRoleToAccount_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RoleArn](#API_AssociateServiceRoleToAccount_RequestSyntax) **   <a name="greengrassv2-AssociateServiceRoleToAccount-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the service role to associate with AWS IoT Greengrass for your AWS account in this AWS Region.
Type: String
Required: Yes

## Response Syntax
<a name="API_AssociateServiceRoleToAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AssociatedAt": "string"
}
```

## Response Elements
<a name="API_AssociateServiceRoleToAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssociatedAt](#API_AssociateServiceRoleToAccount_ResponseSyntax) **   <a name="greengrassv2-AssociateServiceRoleToAccount-response-AssociatedAt"></a>
The time when the service role was associated with AWS IoT Greengrass for your AWS account in this AWS Region.
Type: String

## Errors
<a name="API_AssociateServiceRoleToAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
 AWS IoT Greengrass can't process your request right now. Try again later.
 ** retryAfterSeconds **
The amount of time to wait before you retry the request.
HTTP Status Code: 500

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** fields **
The list of fields that failed to validate.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_AssociateServiceRoleToAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/greengrassv2-2020-11-30/AssociateServiceRoleToAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/greengrassv2-2020-11-30/AssociateServiceRoleToAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/AssociateServiceRoleToAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/greengrassv2-2020-11-30/AssociateServiceRoleToAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/AssociateServiceRoleToAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/greengrassv2-2020-11-30/AssociateServiceRoleToAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/greengrassv2-2020-11-30/AssociateServiceRoleToAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/greengrassv2-2020-11-30/AssociateServiceRoleToAccount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/AssociateServiceRoleToAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/AssociateServiceRoleToAccount)
