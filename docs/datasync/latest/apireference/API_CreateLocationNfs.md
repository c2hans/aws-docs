---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_CreateLocationNfs.html
---

# CreateLocationNfs
<a name="API_CreateLocationNfs"></a>

Creates a transfer *location* for a Network File System (NFS) file server. AWS DataSync can use this location as a source or destination for transferring data.

Before you begin, make sure that you understand how DataSync [accesses NFS file servers](https://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html#accessing-nfs).

## Request Syntax
<a name="API_CreateLocationNfs_RequestSyntax"></a>

```
{
   "MountOptions": {
      "Version": "{{string}}"
   },
   "OnPremConfig": {
      "AgentArns": [ "{{string}}" ]
   },
   "ServerHostname": "{{string}}",
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
<a name="API_CreateLocationNfs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MountOptions](#API_CreateLocationNfs_RequestSyntax) **   <a name="DataSync-CreateLocationNfs-request-MountOptions"></a>
Specifies the options that DataSync can use to mount your NFS file server.
Type: [NfsMountOptions](API_NfsMountOptions.md) object
Required: No

 ** [OnPremConfig](#API_CreateLocationNfs_RequestSyntax) **   <a name="DataSync-CreateLocationNfs-request-OnPremConfig"></a>
Specifies the Amazon Resource Name (ARN) of the DataSync agent that can connect to your NFS file server.
You can specify more than one agent. For more information, see [Using multiple DataSync agents](https://docs.aws.amazon.com/datasync/latest/userguide/do-i-need-datasync-agent.html#multiple-agents).
Type: [OnPremConfig](API_OnPremConfig.md) object
Required: Yes

 ** [ServerHostname](#API_CreateLocationNfs_RequestSyntax) **   <a name="DataSync-CreateLocationNfs-request-ServerHostname"></a>
Specifies the DNS name or IP address (IPv4 or IPv6) of the NFS file server that your DataSync agent connects to.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-:]*[A-Za-z0-9])$`
Required: Yes

 ** [Subdirectory](#API_CreateLocationNfs_RequestSyntax) **   <a name="DataSync-CreateLocationNfs-request-Subdirectory"></a>
Specifies the export path in your NFS file server that you want DataSync to mount.
This path (or a subdirectory of the path) is where DataSync transfers data to or from. For information on configuring an export for DataSync, see [Accessing NFS file servers](https://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html#accessing-nfs).
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]+$`
Required: Yes

 ** [Tags](#API_CreateLocationNfs_RequestSyntax) **   <a name="DataSync-CreateLocationNfs-request-Tags"></a>
Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your location.
Type: Array of [TagListEntry](API_TagListEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateLocationNfs_ResponseSyntax"></a>

```
{
   "LocationArn": "string"
}
```

## Response Elements
<a name="API_CreateLocationNfs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LocationArn](#API_CreateLocationNfs_ResponseSyntax) **   <a name="DataSync-CreateLocationNfs-response-LocationArn"></a>
The ARN of the transfer location that you created for your NFS file server.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

## Errors
<a name="API_CreateLocationNfs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## Examples
<a name="API_CreateLocationNfs_Examples"></a>

### Example
<a name="API_CreateLocationNfs_Example_1"></a>

The following example creates a DataSync transfer location for an NFS file server.

#### Sample Request
<a name="API_CreateLocationNfs_Example_1_Request"></a>

```
{
  "MountOptions": {
     "Version": : "NFS4_0"
     },
  "OnPremConfig": {
    "AgentArn": [ "arn:aws:datasync:us-east-2:111222333444:agent/agent-0b0addbeef44b3nfs" ]
          },

           "ServerHostname": "MyServer@amazon.com",
           "Subdirectory": "/MyFolder",
           "Tags": [
              {
                "Key": "Name",
                "Value": "FileSystem-1"
              }
           ]
}
```

### Example
<a name="API_CreateLocationNfs_Example_2"></a>

The response returns the ARN of the NFS location.

#### Sample Response
<a name="API_CreateLocationNfs_Example_2_Response"></a>

```
{
  "LocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-07db7abfc326c50aa"
}
```

## See Also
<a name="API_CreateLocationNfs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/CreateLocationNfs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/CreateLocationNfs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/CreateLocationNfs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/CreateLocationNfs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationNfs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationNfs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/CreateLocationNfs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationNfs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/CreateLocationNfs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationNfs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
