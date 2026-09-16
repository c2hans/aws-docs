---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateExtension.html
---

# CreateExtension
<a name="API_CreateExtension"></a>

Creates an AWS AppConfig extension. An extension augments your ability to inject logic or behavior at different points during the AWS AppConfig workflow of creating or deploying a configuration.

You can create your own extensions or use the AWS authored extensions provided by AWS AppConfig. For an AWS AppConfig extension that uses AWS Lambda, you must create a Lambda function to perform any computation and processing defined in the extension. If you plan to create custom versions of the AWS authored notification extensions, you only need to specify an Amazon Resource Name (ARN) in the `Uri` field for the new extension version.
+ For a custom EventBridge notification extension, enter the ARN of the EventBridge default events in the `Uri` field.
+ For a custom Amazon SNS notification extension, enter the ARN of an Amazon SNS topic in the `Uri` field.
+ For a custom Amazon SQS notification extension, enter the ARN of an Amazon SQS message queue in the `Uri` field.

For more information about extensions, see [Extending workflows](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html) in the * AWS AppConfig User Guide*.

## Request Syntax
<a name="API_CreateExtension_RequestSyntax"></a>

```
POST /extensions HTTP/1.1
Latest-Version-Number: {{LatestVersionNumber}}
Content-type: application/json

{
   "Actions": {
      "{{string}}" : [
         {
            "Description": "{{string}}",
            "Name": "{{string}}",
            "RoleArn": "{{string}}",
            "Uri": "{{string}}"
         }
      ]
   },
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Parameters": {
      "{{string}}" : {
         "Description": "{{string}}",
         "Dynamic": {{boolean}},
         "Required": {{boolean}}
      }
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateExtension_RequestParameters"></a>

The request uses the following URI parameters.

 ** [LatestVersionNumber](#API_CreateExtension_RequestSyntax) **   <a name="appconfig-CreateExtension-request-LatestVersionNumber"></a>
You can omit this field when you create an extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field.

## Request Body
<a name="API_CreateExtension_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Actions](#API_CreateExtension_RequestSyntax) **   <a name="appconfig-CreateExtension-request-Actions"></a>
The actions defined in the extension.
Type: String to array of [Action](API_Action.md) objects map
Map Entries: Maximum number of 5 items.
Valid Keys: `PRE_CREATE_HOSTED_CONFIGURATION_VERSION | PRE_START_DEPLOYMENT | AT_DEPLOYMENT_TICK | ON_DEPLOYMENT_START | ON_DEPLOYMENT_STEP | ON_DEPLOYMENT_BAKING | ON_DEPLOYMENT_COMPLETE | ON_DEPLOYMENT_ROLLED_BACK`
Array Members: Fixed number of 1 item.
Required: Yes

 ** [Description](#API_CreateExtension_RequestSyntax) **   <a name="appconfig-CreateExtension-request-Description"></a>
Information about the extension.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [Name](#API_CreateExtension_RequestSyntax) **   <a name="appconfig-CreateExtension-request-Name"></a>
A name for the extension. Each extension name in your account must be unique. Extension versions use the same name.
Type: String
Pattern: `^[^\/#:\n]{1,64}$`
Required: Yes

 ** [Parameters](#API_CreateExtension_RequestSyntax) **   <a name="appconfig-CreateExtension-request-Parameters"></a>
The parameters accepted by the extension. You specify parameter values when you associate the extension to an AWS AppConfig resource by using the `CreateExtensionAssociation` API action. For AWS Lambda extension actions, these parameters are included in the Lambda request object.
Type: String to [Parameter](API_Parameter.md) object map
Map Entries: Maximum number of 10 items.
Key Pattern: `^[^\/#:\n]{1,64}$`
Required: No

 ** [Tags](#API_CreateExtension_RequestSyntax) **   <a name="appconfig-CreateExtension-request-Tags"></a>
Adds one or more tags for the specified extension. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateExtension_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Actions": {
      "string" : [
         {
            "Description": "string",
            "Name": "string",
            "RoleArn": "string",
            "Uri": "string"
         }
      ]
   },
   "Arn": "string",
   "Description": "string",
   "Id": "string",
   "Name": "string",
   "Parameters": {
      "string" : {
         "Description": "string",
         "Dynamic": boolean,
         "Required": boolean
      }
   },
   "VersionNumber": number
}
```

## Response Elements
<a name="API_CreateExtension_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Actions](#API_CreateExtension_ResponseSyntax) **   <a name="appconfig-CreateExtension-response-Actions"></a>
The actions defined in the extension.
Type: String to array of [Action](API_Action.md) objects map
Map Entries: Maximum number of 5 items.
Valid Keys: `PRE_CREATE_HOSTED_CONFIGURATION_VERSION | PRE_START_DEPLOYMENT | AT_DEPLOYMENT_TICK | ON_DEPLOYMENT_START | ON_DEPLOYMENT_STEP | ON_DEPLOYMENT_BAKING | ON_DEPLOYMENT_COMPLETE | ON_DEPLOYMENT_ROLLED_BACK`
Array Members: Fixed number of 1 item.

 ** [Arn](#API_CreateExtension_ResponseSyntax) **   <a name="appconfig-CreateExtension-response-Arn"></a>
The system-generated Amazon Resource Name (ARN) for the extension.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:[a-z]+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`

 ** [Description](#API_CreateExtension_ResponseSyntax) **   <a name="appconfig-CreateExtension-response-Description"></a>
Information about the extension.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [Id](#API_CreateExtension_ResponseSyntax) **   <a name="appconfig-CreateExtension-response-Id"></a>
The system-generated ID of the extension.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [Name](#API_CreateExtension_ResponseSyntax) **   <a name="appconfig-CreateExtension-response-Name"></a>
The extension name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [Parameters](#API_CreateExtension_ResponseSyntax) **   <a name="appconfig-CreateExtension-response-Parameters"></a>
The parameters accepted by the extension. You specify parameter values when you associate the extension to an AWS AppConfig resource by using the `CreateExtensionAssociation` API action. For AWS Lambda extension actions, these parameters are included in the Lambda request object.
Type: String to [Parameter](API_Parameter.md) object map
Map Entries: Maximum number of 10 items.
Key Pattern: `^[^\/#:\n]{1,64}$`

 ** [VersionNumber](#API_CreateExtension_ResponseSyntax) **   <a name="appconfig-CreateExtension-response-VersionNumber"></a>
The extension version number.
Type: Integer

## Errors
<a name="API_CreateExtension_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The number of one more AWS AppConfig resources exceeds the maximum allowed. Verify that your environment doesn't exceed the following service quotas:
Applications: 100 max
To resolve this issue, you can delete one or more resources and try again. Or, you can request a quota increase. For more information about quotas and to request an increase, see [Service quotas for AWS AppConfig](https://docs.aws.amazon.com/general/latest/gr/appconfig.html#limits_appconfig) in the Amazon Web Services General Reference.
HTTP Status Code: 402

## Examples
<a name="API_CreateExtension_Examples"></a>

### Example
<a name="API_CreateExtension_Example_1"></a>

This example illustrates one usage of CreateExtension.

#### Sample Request
<a name="API_CreateExtension_Example_1_Request"></a>

```
POST /extensions HTTP/1.1
Host: appconfig.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Type: application/json
User-Agent: aws-cli/2.7.19 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/appconfig.create-extension
X-Amz-Date: 20220803T202954Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220803/us-west-2/appconfig/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 304

{
	"Name": "my-test-extension",
	"Actions": {
		"PRE_CREATE_HOSTED_CONFIGURATION_VERSION": [{
			"Name": "S3backup",
			"Uri": "arn:aws:lambda:us-west-2:111122223333:function:mytestfunction",
			"RoleArn": "arn:aws:iam::111122223333:role/mytestextensionrole"
		}]
	},
	"Parameters": {
		"MyParamKey": {
			"Required": true
		}
	}
}
```

#### Sample Response
<a name="API_CreateExtension_Example_1_Response"></a>

```
{
	"Actions": {
		"PRE_CREATE_HOSTED_CONFIGURATION_VERSION": [{
			"Description": null,
			"Name": "S3backup",
			"RoleArn": "arn:aws:iam::111122223333:role/mytestextensionrole",
			"Uri": "arn:aws:lambda:us-west-2:111122223333:function:mytestfunction"
		}]
	}
```

## See Also
<a name="API_CreateExtension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/CreateExtension)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/CreateExtension)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/CreateExtension)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/CreateExtension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/CreateExtension)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/CreateExtension)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/CreateExtension)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/CreateExtension)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/CreateExtension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/CreateExtension)
