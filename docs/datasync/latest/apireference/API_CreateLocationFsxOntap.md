---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_CreateLocationFsxOntap.html
---

# CreateLocationFsxOntap
<a name="API_CreateLocationFsxOntap"></a>

Creates a transfer *location* for an Amazon FSx for NetApp ONTAP file system. AWS DataSync can use this location as a source or destination for transferring data.

Before you begin, make sure that you understand how DataSync [accesses FSx for ONTAP file systems](https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html#create-ontap-location-access).

## Request Syntax
<a name="API_CreateLocationFsxOntap_RequestSyntax"></a>

```
{
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
   "SecurityGroupArns": [ "{{string}}" ],
   "StorageVirtualMachineArn": "{{string}}",
   "Subdirectory": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateLocationFsxOntap_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Protocol](#API_CreateLocationFsxOntap_RequestSyntax) **   <a name="DataSync-CreateLocationFsxOntap-request-Protocol"></a>
Specifies the data transfer protocol that AWS DataSync uses to access your Amazon FSx file system.
Type: [FsxProtocol](API_FsxProtocol.md) object
Required: Yes

 ** [SecurityGroupArns](#API_CreateLocationFsxOntap_RequestSyntax) **   <a name="DataSync-CreateLocationFsxOntap-request-SecurityGroupArns"></a>
Specifies the Amazon EC2 security groups that provide access to your file system's preferred subnet.
The security groups must allow outbound traffic on the following ports (depending on the protocol you use):
+  **Network File System (NFS)**: TCP ports 111, 635, and 2049
+  **Server Message Block (SMB)**: TCP port 445
Your file system's security groups must also allow inbound traffic on the same ports.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:security-group/sg-[a-f0-9]+$`
Required: Yes

 ** [StorageVirtualMachineArn](#API_CreateLocationFsxOntap_RequestSyntax) **   <a name="DataSync-CreateLocationFsxOntap-request-StorageVirtualMachineArn"></a>
Specifies the ARN of the storage virtual machine (SVM) in your file system where you want to copy data to or from.
Type: String
Length Constraints: Maximum length of 162.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):fsx:[a-z\-0-9]+:[0-9]{12}:storage-virtual-machine/fs-[0-9a-f]+/svm-[0-9a-f]{17,}$`
Required: Yes

 ** [Subdirectory](#API_CreateLocationFsxOntap_RequestSyntax) **   <a name="DataSync-CreateLocationFsxOntap-request-Subdirectory"></a>
Specifies a path to the file share in the SVM where you want to transfer data to or from.
You can specify a junction path (also known as a mount point), qtree path (for NFS file shares), or share name (for SMB file shares). For example, your mount path might be `/vol1`, `/vol1/tree1`, or `/share1`.
Don't specify a junction path in the SVM's root volume. For more information, see [Managing FSx for ONTAP storage virtual machines](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html) in the *Amazon FSx for NetApp ONTAP User Guide*.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`
Required: No

 ** [Tags](#API_CreateLocationFsxOntap_RequestSyntax) **   <a name="DataSync-CreateLocationFsxOntap-request-Tags"></a>
Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your location.
Type: Array of [TagListEntry](API_TagListEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateLocationFsxOntap_ResponseSyntax"></a>

```
{
   "LocationArn": "string"
}
```

## Response Elements
<a name="API_CreateLocationFsxOntap_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LocationArn](#API_CreateLocationFsxOntap_ResponseSyntax) **   <a name="DataSync-CreateLocationFsxOntap-response-LocationArn"></a>
Specifies the ARN of the FSx for ONTAP file system location that you create.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

## Errors
<a name="API_CreateLocationFsxOntap_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_CreateLocationFsxOntap_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/CreateLocationFsxOntap)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/CreateLocationFsxOntap)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/CreateLocationFsxOntap)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/CreateLocationFsxOntap)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationFsxOntap)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationFsxOntap)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/CreateLocationFsxOntap)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationFsxOntap)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/CreateLocationFsxOntap)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationFsxOntap)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
