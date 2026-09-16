---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateAppBlock.html
---

# CreateAppBlock
<a name="API_CreateAppBlock"></a>

Creates an app block.

App blocks are a WorkSpaces Applications resource that stores the details about the virtual hard disk in an S3 bucket. It also stores the setup script with details about how to mount the virtual hard disk. The virtual hard disk includes the application binaries and other files necessary to launch your applications. Multiple applications can be assigned to a single app block.

This is only supported for Elastic fleets.

## Request Syntax
<a name="API_CreateAppBlock_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "DisplayName": "{{string}}",
   "Name": "{{string}}",
   "PackagingType": "{{string}}",
   "PostSetupScriptDetails": {
      "ExecutableParameters": "{{string}}",
      "ExecutablePath": "{{string}}",
      "ScriptS3Location": {
         "S3Bucket": "{{string}}",
         "S3Key": "{{string}}"
      },
      "TimeoutInSeconds": {{number}}
   },
   "SetupScriptDetails": {
      "ExecutableParameters": "{{string}}",
      "ExecutablePath": "{{string}}",
      "ScriptS3Location": {
         "S3Bucket": "{{string}}",
         "S3Key": "{{string}}"
      },
      "TimeoutInSeconds": {{number}}
   },
   "SourceS3Location": {
      "S3Bucket": "{{string}}",
      "S3Key": "{{string}}"
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateAppBlock_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_CreateAppBlock_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlock-request-Description"></a>
The description of the app block.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [DisplayName](#API_CreateAppBlock_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlock-request-DisplayName"></a>
The display name of the app block. This is not displayed to the user.
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Name](#API_CreateAppBlock_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlock-request-Name"></a>
The name of the app block.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [PackagingType](#API_CreateAppBlock_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlock-request-PackagingType"></a>
The packaging type of the app block.
Type: String
Valid Values: `CUSTOM | APPSTREAM2`
Required: No

 ** [PostSetupScriptDetails](#API_CreateAppBlock_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlock-request-PostSetupScriptDetails"></a>
The post setup script details of the app block. This can only be provided for the `APPSTREAM2` PackagingType.
Type: [ScriptDetails](API_ScriptDetails.md) object
Required: No

 ** [SetupScriptDetails](#API_CreateAppBlock_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlock-request-SetupScriptDetails"></a>
The setup script details of the app block. This must be provided for the `CUSTOM` PackagingType.
Type: [ScriptDetails](API_ScriptDetails.md) object
Required: No

 ** [SourceS3Location](#API_CreateAppBlock_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlock-request-SourceS3Location"></a>
The source S3 location of the app block.
Type: [S3Location](API_S3Location.md) object
Required: Yes

 ** [Tags](#API_CreateAppBlock_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlock-request-Tags"></a>
The tags assigned to the app block.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(^(?!aws:).[\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_CreateAppBlock_ResponseSyntax"></a>

```
{
   "AppBlock": {
      "AppBlockErrors": [
         {
            "ErrorCode": "string",
            "ErrorMessage": "string"
         }
      ],
      "Arn": "string",
      "CreatedTime": number,
      "Description": "string",
      "DisplayName": "string",
      "Name": "string",
      "PackagingType": "string",
      "PostSetupScriptDetails": {
         "ExecutableParameters": "string",
         "ExecutablePath": "string",
         "ScriptS3Location": {
            "S3Bucket": "string",
            "S3Key": "string"
         },
         "TimeoutInSeconds": number
      },
      "SetupScriptDetails": {
         "ExecutableParameters": "string",
         "ExecutablePath": "string",
         "ScriptS3Location": {
            "S3Bucket": "string",
            "S3Key": "string"
         },
         "TimeoutInSeconds": number
      },
      "SourceS3Location": {
         "S3Bucket": "string",
         "S3Key": "string"
      },
      "State": "string"
   }
}
```

## Response Elements
<a name="API_CreateAppBlock_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppBlock](#API_CreateAppBlock_ResponseSyntax) **   <a name="WorkSpacesApplications-CreateAppBlock-response-AppBlock"></a>
The app block.
Type: [AppBlock](API_AppBlock.md) object

## Errors
<a name="API_CreateAppBlock_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** LimitExceededException **
The requested limit exceeds the permitted limit for an account.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The specified resource already exists.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateAppBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/CreateAppBlock)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/CreateAppBlock)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/CreateAppBlock)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/CreateAppBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/CreateAppBlock)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/CreateAppBlock)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/CreateAppBlock)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/CreateAppBlock)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/CreateAppBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/CreateAppBlock)
