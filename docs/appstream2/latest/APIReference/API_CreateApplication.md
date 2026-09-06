---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateApplication.html
---

# CreateApplication
<a name="API_CreateApplication"></a>

Creates an application.

Applications are a WorkSpaces Applications resource that stores the details about how to launch applications on Elastic fleet streaming instances. An application consists of the launch details, icon, and display name. Applications are associated with an app block that contains the application binaries and other files. The applications assigned to an Elastic fleet are the applications users can launch.

This is only supported for Elastic fleets.

## Request Syntax
<a name="API_CreateApplication_RequestSyntax"></a>

```
{
   "AppBlockArn": "{{string}}",
   "Description": "{{string}}",
   "DisplayName": "{{string}}",
   "IconS3Location": {
      "S3Bucket": "{{string}}",
      "S3Key": "{{string}}"
   },
   "InstanceFamilies": [ "{{string}}" ],
   "LaunchParameters": "{{string}}",
   "LaunchPath": "{{string}}",
   "Name": "{{string}}",
   "Platforms": [ "{{string}}" ],
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "WorkingDirectory": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateApplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AppBlockArn](#API_CreateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-CreateApplication-request-AppBlockArn"></a>
The app block ARN to which the application should be associated
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: Yes

 ** [Description](#API_CreateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-CreateApplication-request-Description"></a>
The description of the application.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [DisplayName](#API_CreateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-CreateApplication-request-DisplayName"></a>
The display name of the application. This name is visible to users in the application catalog.
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [IconS3Location](#API_CreateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-CreateApplication-request-IconS3Location"></a>
The location in S3 of the application icon.
Type: [S3Location](API_S3Location.md) object
Required: Yes

 ** [InstanceFamilies](#API_CreateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-CreateApplication-request-InstanceFamilies"></a>
The instance families the application supports. Valid values are GENERAL\_PURPOSE and GRAPHICS\_G4.
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: Yes

 ** [LaunchParameters](#API_CreateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-CreateApplication-request-LaunchParameters"></a>
The launch parameters of the application.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [LaunchPath](#API_CreateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-CreateApplication-request-LaunchPath"></a>
The launch path of the application.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [Name](#API_CreateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-CreateApplication-request-Name"></a>
The name of the application. This name is visible to users when display name is not specified.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [Platforms](#API_CreateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-CreateApplication-request-Platforms"></a>
The platforms the application supports. WINDOWS\_SERVER\_2019, AMAZON\_LINUX2 and UBUNTU\_PRO\_2404 are supported for Elastic fleets.
Type: Array of strings
Array Members: Maximum number of 4 items.
Valid Values: `WINDOWS | WINDOWS_SERVER_2016 | WINDOWS_SERVER_2019 | WINDOWS_SERVER_2022 | WINDOWS_SERVER_2025 | WINDOWS_11 | AMAZON_LINUX2 | RHEL8 | ROCKY_LINUX8 | UBUNTU_PRO_2404`
Required: Yes

 ** [Tags](#API_CreateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-CreateApplication-request-Tags"></a>
The tags assigned to the application.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(^(?!aws:).[\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** [WorkingDirectory](#API_CreateApplication_RequestSyntax) **   <a name="WorkSpacesApplications-CreateApplication-request-WorkingDirectory"></a>
The working directory of the application.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_CreateApplication_ResponseSyntax"></a>

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
<a name="API_CreateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Application](#API_CreateApplication_ResponseSyntax) **   <a name="WorkSpacesApplications-CreateApplication-response-Application"></a>
Describes an application in the application catalog.
Type: [Application](API_Application.md) object

## Errors
<a name="API_CreateApplication_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/CreateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/CreateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/CreateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/CreateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/CreateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/CreateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/CreateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/CreateApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/CreateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/CreateApplication)
