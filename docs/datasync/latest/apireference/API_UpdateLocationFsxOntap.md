---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_UpdateLocationFsxOntap.html
---

# UpdateLocationFsxOntap
<a name="API_UpdateLocationFsxOntap"></a>

Modifies the following configuration parameters of the Amazon FSx for NetApp ONTAP transfer location that you're using with AWS DataSync.

For more information, see [Configuring DataSync transfers with FSx for ONTAP](https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html).

## Request Syntax
<a name="API_UpdateLocationFsxOntap_RequestSyntax"></a>

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
<a name="API_UpdateLocationFsxOntap_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LocationArn](#API_UpdateLocationFsxOntap_RequestSyntax) **   <a name="DataSync-UpdateLocationFsxOntap-request-LocationArn"></a>
Specifies the Amazon Resource Name (ARN) of the FSx for ONTAP transfer location that you're updating.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`
Required: Yes

 ** [Protocol](#API_UpdateLocationFsxOntap_RequestSyntax) **   <a name="DataSync-UpdateLocationFsxOntap-request-Protocol"></a>
Specifies the data transfer protocol that DataSync uses to access your Amazon FSx file system.
Type: [FsxUpdateProtocol](API_FsxUpdateProtocol.md) object
Required: No

 ** [Subdirectory](#API_UpdateLocationFsxOntap_RequestSyntax) **   <a name="DataSync-UpdateLocationFsxOntap-request-Subdirectory"></a>
Specifies a path to the file share in the storage virtual machine (SVM) where you want to transfer data to or from.
You can specify a junction path (also known as a mount point), qtree path (for NFS file shares), or share name (for SMB file shares). For example, your mount path might be `/vol1`, `/vol1/tree1`, or `/share1`.
Don't specify a junction path in the SVM's root volume. For more information, see [Managing FSx for ONTAP storage virtual machines](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html) in the *Amazon FSx for NetApp ONTAP User Guide*.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`
Required: No

## Response Elements
<a name="API_UpdateLocationFsxOntap_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateLocationFsxOntap_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateLocationFsxOntap_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/UpdateLocationFsxOntap)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/UpdateLocationFsxOntap)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/UpdateLocationFsxOntap)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationFsxOntap)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationFsxOntap)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationFsxOntap)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationFsxOntap)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationFsxOntap)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/UpdateLocationFsxOntap)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationFsxOntap)
