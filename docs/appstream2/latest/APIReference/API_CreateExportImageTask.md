---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateExportImageTask.html
---

# CreateExportImageTask
<a name="API_CreateExportImageTask"></a>

Creates a task to export a WorkSpaces Applications image to an EC2 AMI. This allows you to use your customized WorkSpaces Applications images with other AWS services or for backup purposes.

## Request Syntax
<a name="API_CreateExportImageTask_RequestSyntax"></a>

```
{
   "AmiDescription": "{{string}}",
   "AmiName": "{{string}}",
   "IamRoleArn": "{{string}}",
   "ImageName": "{{string}}",
   "TagSpecifications": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateExportImageTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AmiDescription](#API_CreateExportImageTask_RequestSyntax) **   <a name="WorkSpacesApplications-CreateExportImageTask-request-AmiDescription"></a>
An optional description for the exported AMI. This description will be applied to the resulting EC2 AMI.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [AmiName](#API_CreateExportImageTask_RequestSyntax) **   <a name="WorkSpacesApplications-CreateExportImageTask-request-AmiName"></a>
The name for the exported EC2 AMI. This is a required field that must be unique within your account and region.
Type: String
Pattern: `^[a-zA-Z0-9().\-/_]{3,128}$`
Required: Yes

 ** [IamRoleArn](#API_CreateExportImageTask_RequestSyntax) **   <a name="WorkSpacesApplications-CreateExportImageTask-request-IamRoleArn"></a>
The ARN of the IAM role that allows WorkSpaces Applications to create the AMI. The role must have permissions to copy images, describe images, and create tags, with a trust relationship allowing appstream.amazonaws.com to assume the role.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: Yes

 ** [ImageName](#API_CreateExportImageTask_RequestSyntax) **   <a name="WorkSpacesApplications-CreateExportImageTask-request-ImageName"></a>
The name of the WorkSpaces Applications image to export. The image must be in an available state and owned by your account.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [TagSpecifications](#API_CreateExportImageTask_RequestSyntax) **   <a name="WorkSpacesApplications-CreateExportImageTask-request-TagSpecifications"></a>
The tags to apply to the exported AMI. These tags help you organize and manage your EC2 AMIs.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(^(?!aws:).[\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_CreateExportImageTask_ResponseSyntax"></a>

```
{
   "ExportImageTask": {
      "AmiDescription": "string",
      "AmiId": "string",
      "AmiName": "string",
      "CreatedDate": number,
      "ErrorDetails": [
         {
            "ErrorCode": "string",
            "ErrorMessage": "string"
         }
      ],
      "ImageArn": "string",
      "State": "string",
      "TagSpecifications": {
         "string" : "string"
      },
      "TaskId": "string"
   }
}
```

## Response Elements
<a name="API_CreateExportImageTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExportImageTask](#API_CreateExportImageTask_ResponseSyntax) **   <a name="WorkSpacesApplications-CreateExportImageTask-response-ExportImageTask"></a>
Information about the export image task that was created, including the task ID and initial state.
Type: [ExportImageTask](API_ExportImageTask.md) object

## Errors
<a name="API_CreateExportImageTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidAccountStatusException **
The resource cannot be created because your AWS account is suspended. For assistance, contact AWS Support.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidRoleException **
The specified role is invalid.
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

 ** ResourceNotAvailableException **
The specified resource exists and is not in use, but isn't available.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateExportImageTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/CreateExportImageTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/CreateExportImageTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/CreateExportImageTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/CreateExportImageTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/CreateExportImageTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/CreateExportImageTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/CreateExportImageTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/CreateExportImageTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/CreateExportImageTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/CreateExportImageTask)
