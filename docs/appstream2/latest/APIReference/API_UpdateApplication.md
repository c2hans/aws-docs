---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateApplication.html
---

# UpdateApplication
<a name="API_UpdateApplication"></a>

Updates the specified application.

## Request Syntax
<a name="API_UpdateApplication_RequestSyntax"></a>

```
{
   "AppBlockArn": "{{string}}",
   "AttributesToDelete": [ "{{string}}" ],
   "Description": "{{string}}",
   "DisplayName": "{{string}}",
   "IconS3Location": {
      "S3Bucket": "{{string}}",
      "S3Key": "{{string}}"
   },
   "LaunchParameters": "{{string}}",
   "LaunchPath": "{{string}}",
   "Name": "{{string}}",
   "WorkingDirectory": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateApplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AppBlockArn](#API_UpdateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateApplication-request-AppBlockArn"></a>
The ARN of the app block.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** [AttributesToDelete](#API_UpdateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateApplication-request-AttributesToDelete"></a>
The attributes to delete for an application.
Type: Array of strings
Array Members: Maximum number of 2 items.
Valid Values: `LAUNCH_PARAMETERS | WORKING_DIRECTORY`
Required: No

 ** [Description](#API_UpdateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateApplication-request-Description"></a>
The description of the application.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [DisplayName](#API_UpdateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateApplication-request-DisplayName"></a>
The display name of the application. This name is visible to users in the application catalog.
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [IconS3Location](#API_UpdateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateApplication-request-IconS3Location"></a>
The icon S3 location of the application.
Type: [S3Location](API_S3Location.md) object
Required: No

 ** [LaunchParameters](#API_UpdateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateApplication-request-LaunchParameters"></a>
The launch parameters of the application.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [LaunchPath](#API_UpdateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateApplication-request-LaunchPath"></a>
The launch path of the application.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [Name](#API_UpdateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateApplication-request-Name"></a>
The name of the application. This name is visible to users when display name is not specified.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [WorkingDirectory](#API_UpdateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateApplication-request-WorkingDirectory"></a>
The working directory of the application.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_UpdateApplication_ResponseSyntax"></a>

```
{
   "Application": {
      "AppBlockArn": "string",
      "Arn": "string",
      "CreatedTime": number,
      "Description": "string",
      "DisplayName": "string",
      "Enabled": boolean,
      "IconS3Location": {
         "S3Bucket": "string",
         "S3Key": "string"
      },
      "IconURL": "string",
      "InstanceFamilies": [ "string" ],
      "LaunchParameters": "string",
      "LaunchPath": "string",
      "Metadata": {
         "string" : "string"
      },
      "Name": "string",
      "Platforms": [ "string" ],
      "WorkingDirectory": "string"
   }
}
```

## Response Elements
<a name="API_UpdateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Application](#API_UpdateApplication_ResponseSyntax) **   <a name="WorkSpacesApplications-UpdateApplication-response-Application"></a>
Describes an application in the application catalog.
Type: [Application](API_Application.md) object

## Errors
<a name="API_UpdateApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/UpdateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/UpdateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/UpdateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/UpdateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/UpdateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/UpdateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/UpdateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/UpdateApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/UpdateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/UpdateApplication)
