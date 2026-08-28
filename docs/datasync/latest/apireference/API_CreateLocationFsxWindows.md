---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_CreateLocationFsxWindows.html
---

# CreateLocationFsxWindows
<a name="API_CreateLocationFsxWindows"></a>

Creates a transfer *location* for an Amazon FSx for Windows File Server file system. AWS DataSync can use this location as a source or destination for transferring data.

Before you begin, make sure that you understand how DataSync [accesses FSx for Windows File Server file systems](https://docs.aws.amazon.com/datasync/latest/userguide/create-fsx-location.html#create-fsx-location-access).

## Request Syntax
<a name="API_CreateLocationFsxWindows_RequestSyntax"></a>

```
{
   "CmkSecretConfig": {
      "KmsKeyArn": "{{string}}",
      "SecretArn": "{{string}}"
   },
   "CustomSecretConfig": {
      "SecretAccessRoleArn": "{{string}}",
      "SecretArn": "{{string}}"
   },
   "Domain": "{{string}}",
   "FsxFilesystemArn": "{{string}}",
   "Password": "{{string}}",
   "SecurityGroupArns": [ "{{string}}" ],
   "Subdirectory": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "User": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateLocationFsxWindows_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CmkSecretConfig](#API_CreateLocationFsxWindows_RequestSyntax) **   <a name="DataSync-CreateLocationFsxWindows-request-CmkSecretConfig"></a>
Specifies configuration information for a DataSync-managed secret, which includes the password that DataSync uses to access a specific FSx Windows storage location, with a customer-managed AWS KMS key.
When you include this parameter as part of a `CreateLocationFsxWindows` request, you provide only the KMS key ARN. DataSync uses this KMS key together with the `Password` you specify for to create a DataSync-managed secret to store the location access credentials.
Make sure that DataSync has permission to access the KMS key that you specify. For more information, see [ Using a service-managed secret encrypted with a custom AWS KMS key](https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#service-secret-custom-key).
You can use either `CmkSecretConfig` (with `Password`) or `CustomSecretConfig` (without `Password`) to provide credentials for a `CreateLocationFsxWindows` request. Do not provide both parameters for the same request.
Type: [CmkSecretConfig](API_CmkSecretConfig.md) object
Required: No

 ** [CustomSecretConfig](#API_CreateLocationFsxWindows_RequestSyntax) **   <a name="DataSync-CreateLocationFsxWindows-request-CustomSecretConfig"></a>
Specifies configuration information for a customer-managed Secrets Manager secret where the password for an FSx for Windows File Server storage location is stored in plain text, in Secrets Manager. This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret. For more information, see [ Using a secret that you manage](https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#custom-secret-custom-key).
You can use either `CmkSecretConfig` (with `Password`) or `CustomSecretConfig` (without `Password`) to provide credentials for a `CreateLocationFsxWindows` request. Do not provide both parameters for the same request.
Type: [CustomSecretConfig](API_CustomSecretConfig.md) object
Required: No

 ** [Domain](#API_CreateLocationFsxWindows_RequestSyntax) **   <a name="DataSync-CreateLocationFsxWindows-request-Domain"></a>
Specifies the name of the Windows domain that the FSx for Windows File Server file system belongs to.
If you have multiple Active Directory domains in your environment, configuring this parameter makes sure that DataSync connects to the right file system.
Type: String
Length Constraints: Maximum length of 253.
Pattern: `^[A-Za-z0-9]((\.|-+)?[A-Za-z0-9]){0,252}$`
Required: No

 ** [FsxFilesystemArn](#API_CreateLocationFsxWindows_RequestSyntax) **   <a name="DataSync-CreateLocationFsxWindows-request-FsxFilesystemArn"></a>
Specifies the Amazon Resource Name (ARN) for the FSx for Windows File Server file system.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):fsx:[a-z\-0-9]+:[0-9]{12}:file-system/fs-[0-9a-f]+$`
Required: Yes

 ** [Password](#API_CreateLocationFsxWindows_RequestSyntax) **   <a name="DataSync-CreateLocationFsxWindows-request-Password"></a>
Specifies the password of the user with the permissions to mount and access the files, folders, and file metadata in your FSx for Windows File Server file system.
Type: String
Length Constraints: Maximum length of 104.
Pattern: `^.{0,104}$`
Required: No

 ** [SecurityGroupArns](#API_CreateLocationFsxWindows_RequestSyntax) **   <a name="DataSync-CreateLocationFsxWindows-request-SecurityGroupArns"></a>
Specifies the ARNs of the Amazon EC2 security groups that provide access to your file system's preferred subnet.
The security groups that you specify must be able to communicate with your file system's security groups. For information about configuring security groups for file system access, see the [*Amazon FSx for Windows File Server User Guide*](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/limit-access-security-groups.html).
If you choose a security group that doesn't allow connections from within itself, do one of the following:
+ Configure the security group to allow it to communicate within itself.
+ Choose a different security group that can communicate with the mount target's security group.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:security-group/sg-[a-f0-9]+$`
Required: Yes

 ** [Subdirectory](#API_CreateLocationFsxWindows_RequestSyntax) **   <a name="DataSync-CreateLocationFsxWindows-request-Subdirectory"></a>
Specifies a mount path for your file system using forward slashes. This is where DataSync reads or writes data (depending on if this is a source or destination location).
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`
Required: No

 ** [Tags](#API_CreateLocationFsxWindows_RequestSyntax) **   <a name="DataSync-CreateLocationFsxWindows-request-Tags"></a>
Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your location.
Type: Array of [TagListEntry](API_TagListEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [User](#API_CreateLocationFsxWindows_RequestSyntax) **   <a name="DataSync-CreateLocationFsxWindows-request-User"></a>
Specifies the user with the permissions to mount and access the files, folders, and file metadata in your FSx for Windows File Server file system.
For information about choosing a user with the right level of access for your transfer, see [required permissions](https://docs.aws.amazon.com/datasync/latest/userguide/create-fsx-location.html#create-fsx-windows-location-permissions) for FSx for Windows File Server locations.
Type: String
Length Constraints: Maximum length of 104.
Pattern: `^[^\x22\x5B\x5D/\\:;|=,+*?\x3C\x3E]{1,104}$`
Required: Yes

## Response Syntax
<a name="API_CreateLocationFsxWindows_ResponseSyntax"></a>

```
{
   "LocationArn": "string"
}
```

## Response Elements
<a name="API_CreateLocationFsxWindows_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LocationArn](#API_CreateLocationFsxWindows_ResponseSyntax) **   <a name="DataSync-CreateLocationFsxWindows-response-LocationArn"></a>
The ARN of the FSx for Windows File Server file system location you created.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

## Errors
<a name="API_CreateLocationFsxWindows_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_CreateLocationFsxWindows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/CreateLocationFsxWindows)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/CreateLocationFsxWindows)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/CreateLocationFsxWindows)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/CreateLocationFsxWindows)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationFsxWindows)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationFsxWindows)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/CreateLocationFsxWindows)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationFsxWindows)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/CreateLocationFsxWindows)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationFsxWindows)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
