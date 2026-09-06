---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_UpdateLocationEfs.html
---

# UpdateLocationEfs
<a name="API_UpdateLocationEfs"></a>

Modifies the following configuration parameters of the Amazon EFS transfer location that you're using with AWS DataSync.

For more information, see [Configuring DataSync transfers with Amazon EFS](https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html).

## Request Syntax
<a name="API_UpdateLocationEfs_RequestSyntax"></a>

```
{
   "AccessPointArn": "{{string}}",
   "FileSystemAccessRoleArn": "{{string}}",
   "InTransitEncryption": "{{string}}",
   "LocationArn": "{{string}}",
   "Subdirectory": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateLocationEfs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessPointArn](#API_UpdateLocationEfs_RequestSyntax) **   <a name="DataSync-UpdateLocationEfs-request-AccessPointArn"></a>
Specifies the Amazon Resource Name (ARN) of the access point that DataSync uses to mount your Amazon EFS file system.
For more information, see [Accessing restricted Amazon EFS file systems](https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html#create-efs-location-iam).
Type: String
Length Constraints: Maximum length of 128.
Pattern: `(^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):elasticfilesystem:[a-z\-0-9]+:[0-9]{12}:access-point/fsap-[0-9a-f]{8,40}$)|(^$)`
Required: No

 ** [FileSystemAccessRoleArn](#API_UpdateLocationEfs_RequestSyntax) **   <a name="DataSync-UpdateLocationEfs-request-FileSystemAccessRoleArn"></a>
Specifies an AWS Identity and Access Management (IAM) role that allows DataSync to access your Amazon EFS file system.
For information on creating this role, see [Creating a DataSync IAM role for Amazon EFS file system access](https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html#create-efs-location-iam-role).
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `(^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*$)|(^$)`
Required: No

 ** [InTransitEncryption](#API_UpdateLocationEfs_RequestSyntax) **   <a name="DataSync-UpdateLocationEfs-request-InTransitEncryption"></a>
Specifies whether you want DataSync to use Transport Layer Security (TLS) 1.2 encryption when it transfers data to or from your Amazon EFS file system.
If you specify an access point using `AccessPointArn` or an IAM role using `FileSystemAccessRoleArn`, you must set this parameter to `TLS1_2`.
Type: String
Valid Values: `NONE | TLS1_2`
Required: No

 ** [LocationArn](#API_UpdateLocationEfs_RequestSyntax) **   <a name="DataSync-UpdateLocationEfs-request-LocationArn"></a>
Specifies the Amazon Resource Name (ARN) of the Amazon EFS transfer location that you're updating.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`
Required: Yes

 ** [Subdirectory](#API_UpdateLocationEfs_RequestSyntax) **   <a name="DataSync-UpdateLocationEfs-request-Subdirectory"></a>
Specifies a mount path for your Amazon EFS file system. This is where DataSync reads or writes data on your file system (depending on if this is a source or destination location).
By default, DataSync uses the root directory (or [access point](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html) if you provide one by using `AccessPointArn`). You can also include subdirectories using forward slashes (for example, `/path/to/folder`).
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]*$`
Required: No

## Response Elements
<a name="API_UpdateLocationEfs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateLocationEfs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateLocationEfs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/UpdateLocationEfs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/UpdateLocationEfs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/UpdateLocationEfs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationEfs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationEfs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationEfs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationEfs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationEfs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/UpdateLocationEfs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationEfs)
