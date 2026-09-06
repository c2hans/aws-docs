---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_UpdateLocationFsxOpenZfs.html
---

# UpdateLocationFsxOpenZfs
<a name="API_UpdateLocationFsxOpenZfs"></a>

Modifies the following configuration parameters of the Amazon FSx for OpenZFS transfer location that you're using with AWS DataSync.

For more information, see [Configuring DataSync transfers with FSx for OpenZFS](https://docs.aws.amazon.com/datasync/latest/userguide/create-openzfs-location.html).

**Note**
Request parameters related to `SMB` aren't supported with the `UpdateLocationFsxOpenZfs` operation.

## Request Syntax
<a name="API_UpdateLocationFsxOpenZfs_RequestSyntax"></a>

```
{
   "LocationArn": "{{string}}",
   "Protocol": {
      "NFS": {
         "MountOptions": {
            "Version": "{{string}}"
         }
      },
      "SMB": {
         "CmkSecretConfig": {
            "KmsKeyArn": "{{string}}",
            "SecretArn": "{{string}}"
         },
         "CustomSecretConfig": {
            "SecretAccessRoleArn": "{{string}}",
            "SecretArn": "{{string}}"
         },
         "Domain": "{{string}}",
         "ManagedSecretConfig": {
            "SecretArn": "{{string}}"
         },
         "MountOptions": {
            "Version": "{{string}}"
         },
         "Password": "{{string}}",
         "User": "{{string}}"
      }
   },
   "Subdirectory": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateLocationFsxOpenZfs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LocationArn](#API_UpdateLocationFsxOpenZfs_RequestSyntax) **   <a name="DataSync-UpdateLocationFsxOpenZfs-request-LocationArn"></a>
Specifies the Amazon Resource Name (ARN) of the FSx for OpenZFS transfer location that you're updating.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`
Required: Yes

 ** [Protocol](#API_UpdateLocationFsxOpenZfs_RequestSyntax) **   <a name="DataSync-UpdateLocationFsxOpenZfs-request-Protocol"></a>
Specifies the data transfer protocol that AWS DataSync uses to access your Amazon FSx file system.
Type: [FsxProtocol](API_FsxProtocol.md) object
Required: No

 ** [Subdirectory](#API_UpdateLocationFsxOpenZfs_RequestSyntax) **   <a name="DataSync-UpdateLocationFsxOpenZfs-request-Subdirectory"></a>
Specifies a subdirectory in the location's path that must begin with `/fsx`. DataSync uses this subdirectory to read or write data (depending on whether the file system is a source or destination location).
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`
Required: No

## Response Elements
<a name="API_UpdateLocationFsxOpenZfs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateLocationFsxOpenZfs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateLocationFsxOpenZfs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/UpdateLocationFsxOpenZfs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/UpdateLocationFsxOpenZfs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/UpdateLocationFsxOpenZfs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationFsxOpenZfs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationFsxOpenZfs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationFsxOpenZfs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationFsxOpenZfs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationFsxOpenZfs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/UpdateLocationFsxOpenZfs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationFsxOpenZfs)
