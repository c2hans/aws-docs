---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_DescribeLocationNfs.html
---

# DescribeLocationNfs
<a name="API_DescribeLocationNfs"></a>

Provides details about how an AWS DataSync transfer location for a Network File System (NFS) file server is configured.

## Request Syntax
<a name="API_DescribeLocationNfs_RequestSyntax"></a>

```
{
   "LocationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeLocationNfs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LocationArn](#API_DescribeLocationNfs_RequestSyntax) **   <a name="DataSync-DescribeLocationNfs-request-LocationArn"></a>
Specifies the Amazon Resource Name (ARN) of the NFS location that you want information about.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`
Required: Yes

## Response Syntax
<a name="API_DescribeLocationNfs_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "LocationArn": "string",
   "LocationUri": "string",
   "MountOptions": {
      "Version": "string"
   },
   "OnPremConfig": {
      "AgentArns": [ "string" ]
   }
}
```

## Response Elements
<a name="API_DescribeLocationNfs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeLocationNfs_ResponseSyntax) **   <a name="DataSync-DescribeLocationNfs-response-CreationTime"></a>
The time when the NFS location was created.
Type: Timestamp

 ** [LocationArn](#API_DescribeLocationNfs_ResponseSyntax) **   <a name="DataSync-DescribeLocationNfs-response-LocationArn"></a>
The ARN of the NFS location.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

 ** [LocationUri](#API_DescribeLocationNfs_ResponseSyntax) **   <a name="DataSync-DescribeLocationNfs-response-LocationUri"></a>
The URI of the NFS location.
Type: String
Length Constraints: Maximum length of 4360.
Pattern: `^(efs|nfs|s3|smb|hdfs|fsx[a-z0-9-]+)://[a-zA-Z0-9.:/\-]+$`

 ** [MountOptions](#API_DescribeLocationNfs_ResponseSyntax) **   <a name="DataSync-DescribeLocationNfs-response-MountOptions"></a>
The mount options that DataSync uses to mount your NFS file server.
Type: [NfsMountOptions](API_NfsMountOptions.md) object

 ** [OnPremConfig](#API_DescribeLocationNfs_ResponseSyntax) **   <a name="DataSync-DescribeLocationNfs-response-OnPremConfig"></a>
The AWS DataSync agents that can connect to your Network File System (NFS) file server.
Type: [OnPremConfig](API_OnPremConfig.md) object

## Errors
<a name="API_DescribeLocationNfs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## Examples
<a name="API_DescribeLocationNfs_Examples"></a>

### Example
<a name="API_DescribeLocationNfs_Example_1"></a>

The following example returns information about the NFS location specified in the sample request.

#### Sample Request
<a name="API_DescribeLocationNfs_Example_1_Request"></a>

```
{
  "LocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-07db7abfc326c50aa"
}
```

### Example
<a name="API_DescribeLocationNfs_Example_2"></a>

This example illustrates one usage of DescribeLocationNfs.

#### Sample Response
<a name="API_DescribeLocationNfs_Example_2_Response"></a>

```
{
   "CreationTime": 1532660733.39,
   "LocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-07db7abfc326c50aa",
   "LocationUri": "hostname.amazon.com",
   "OnPremConfig": {
      "AgentArns": [ "arn:aws:datasync:us-east-2:111222333444:agent/agent-0b0addbeef44b3nfs" ]
   }
}
```

## See Also
<a name="API_DescribeLocationNfs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/DescribeLocationNfs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/DescribeLocationNfs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/DescribeLocationNfs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationNfs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationNfs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationNfs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationNfs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationNfs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/DescribeLocationNfs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationNfs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
