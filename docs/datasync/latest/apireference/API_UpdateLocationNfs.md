---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_UpdateLocationNfs.html
---

# UpdateLocationNfs
<a name="API_UpdateLocationNfs"></a>

Modifies the following configuration parameters of the Network File System (NFS) transfer location that you're using with AWS DataSync.

For more information, see [Configuring transfers with an NFS file server](https://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html).

## Request Syntax
<a name="API_UpdateLocationNfs_RequestSyntax"></a>

```
{
   "LocationArn": "{{string}}",
   "MountOptions": {
      "Version": "{{string}}"
   },
   "OnPremConfig": {
      "AgentArns": [ "{{string}}" ]
   },
   "ServerHostname": "{{string}}",
   "Subdirectory": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateLocationNfs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LocationArn](#API_UpdateLocationNfs_RequestSyntax) **   <a name="DataSync-UpdateLocationNfs-request-LocationArn"></a>
Specifies the Amazon Resource Name (ARN) of the NFS transfer location that you want to update.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`
Required: Yes

 ** [MountOptions](#API_UpdateLocationNfs_RequestSyntax) **   <a name="DataSync-UpdateLocationNfs-request-MountOptions"></a>
Specifies how DataSync can access a location using the NFS protocol.
Type: [NfsMountOptions](API_NfsMountOptions.md) object
Required: No

 ** [OnPremConfig](#API_UpdateLocationNfs_RequestSyntax) **   <a name="DataSync-UpdateLocationNfs-request-OnPremConfig"></a>
The AWS DataSync agents that can connect to your Network File System (NFS) file server.
Type: [OnPremConfig](API_OnPremConfig.md) object
Required: No

 ** [ServerHostname](#API_UpdateLocationNfs_RequestSyntax) **   <a name="DataSync-UpdateLocationNfs-request-ServerHostname"></a>
Specifies the DNS name or IP address (IPv4 or IPv6) of the NFS file server that your DataSync agent connects to.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-:]*[A-Za-z0-9])$`
Required: No

 ** [Subdirectory](#API_UpdateLocationNfs_RequestSyntax) **   <a name="DataSync-UpdateLocationNfs-request-Subdirectory"></a>
Specifies the export path in your NFS file server that you want DataSync to mount.
This path (or a subdirectory of the path) is where DataSync transfers data to or from. For information on configuring an export for DataSync, see [Accessing NFS file servers](https://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html#accessing-nfs).
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]+$`
Required: No

## Response Elements
<a name="API_UpdateLocationNfs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateLocationNfs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateLocationNfs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/UpdateLocationNfs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/UpdateLocationNfs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/UpdateLocationNfs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationNfs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationNfs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationNfs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationNfs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationNfs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/UpdateLocationNfs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationNfs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
