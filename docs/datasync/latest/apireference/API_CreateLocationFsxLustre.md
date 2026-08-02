---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_CreateLocationFsxLustre.html
---

# CreateLocationFsxLustre
<a name="API_CreateLocationFsxLustre"></a>

Creates a transfer *location* for an Amazon FSx for Lustre file system. AWS DataSync can use this location as a source or destination for transferring data.

Before you begin, make sure that you understand how DataSync [accesses FSx for Lustre file systems](https://docs.aws.amazon.com/datasync/latest/userguide/create-lustre-location.html#create-lustre-location-access).

## Request Syntax
<a name="API_CreateLocationFsxLustre_RequestSyntax"></a>

```
{
   "FsxFilesystemArn": "{{string}}",
   "SecurityGroupArns": [ "{{string}}" ],
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
<a name="API_CreateLocationFsxLustre_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FsxFilesystemArn](#API_CreateLocationFsxLustre_RequestSyntax) **   <a name="DataSync-CreateLocationFsxLustre-request-FsxFilesystemArn"></a>
Specifies the Amazon Resource Name (ARN) of the FSx for Lustre file system.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):fsx:[a-z\-0-9]+:[0-9]{12}:file-system/fs-[0-9a-f]+$`
Required: Yes

 ** [SecurityGroupArns](#API_CreateLocationFsxLustre_RequestSyntax) **   <a name="DataSync-CreateLocationFsxLustre-request-SecurityGroupArns"></a>
Specifies the Amazon Resource Names (ARNs) of up to five security groups that provide access to your FSx for Lustre file system.
The security groups must be able to access the file system's ports. The file system must also allow access from the security groups. For information about file system access, see the [https://docs.aws.amazon.com/fsx/latest/LustreGuide/limit-access-security-groups.html](https://docs.aws.amazon.com/fsx/latest/LustreGuide/limit-access-security-groups.html).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:security-group/sg-[a-f0-9]+$`
Required: Yes

 ** [Subdirectory](#API_CreateLocationFsxLustre_RequestSyntax) **   <a name="DataSync-CreateLocationFsxLustre-request-Subdirectory"></a>
Specifies a mount path for your FSx for Lustre file system. The path can include subdirectories.
When the location is used as a source, DataSync reads data from the mount path. When the location is used as a destination, DataSync writes data to the mount path. If you don't include this parameter, DataSync uses the file system's root directory (`/`).
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`
Required: No

 ** [Tags](#API_CreateLocationFsxLustre_RequestSyntax) **   <a name="DataSync-CreateLocationFsxLustre-request-Tags"></a>
Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your location.
Type: Array of [TagListEntry](API_TagListEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateLocationFsxLustre_ResponseSyntax"></a>

```
{
   "LocationArn": "string"
}
```

## Response Elements
<a name="API_CreateLocationFsxLustre_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LocationArn](#API_CreateLocationFsxLustre_ResponseSyntax) **   <a name="DataSync-CreateLocationFsxLustre-response-LocationArn"></a>
The Amazon Resource Name (ARN) of the FSx for Lustre file system location that you created.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

## Errors
<a name="API_CreateLocationFsxLustre_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_CreateLocationFsxLustre_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/CreateLocationFsxLustre)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/CreateLocationFsxLustre)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/CreateLocationFsxLustre)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/CreateLocationFsxLustre)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationFsxLustre)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationFsxLustre)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/CreateLocationFsxLustre)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationFsxLustre)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/CreateLocationFsxLustre)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationFsxLustre)
