---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_UpdateLocationFsxLustre.html
---

# UpdateLocationFsxLustre
<a name="API_UpdateLocationFsxLustre"></a>

Modifies the following configuration parameters of the Amazon FSx for Lustre transfer location that you're using with AWS DataSync.

For more information, see [Configuring DataSync transfers with FSx for Lustre](https://docs.aws.amazon.com/datasync/latest/userguide/create-lustre-location.html).

## Request Syntax
<a name="API_UpdateLocationFsxLustre_RequestSyntax"></a>

```
{
   "LocationArn": "{{string}}",
   "Subdirectory": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateLocationFsxLustre_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LocationArn](#API_UpdateLocationFsxLustre_RequestSyntax) **   <a name="DataSync-UpdateLocationFsxLustre-request-LocationArn"></a>
Specifies the Amazon Resource Name (ARN) of the FSx for Lustre transfer location that you're updating.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`
Required: Yes

 ** [Subdirectory](#API_UpdateLocationFsxLustre_RequestSyntax) **   <a name="DataSync-UpdateLocationFsxLustre-request-Subdirectory"></a>
Specifies a mount path for your FSx for Lustre file system. The path can include subdirectories.
When the location is used as a source, DataSync reads data from the mount path. When the location is used as a destination, DataSync writes data to the mount path. If you don't include this parameter, DataSync uses the file system's root directory (`/`).
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`
Required: No

## Response Elements
<a name="API_UpdateLocationFsxLustre_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateLocationFsxLustre_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateLocationFsxLustre_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/UpdateLocationFsxLustre)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/UpdateLocationFsxLustre)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/UpdateLocationFsxLustre)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationFsxLustre)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationFsxLustre)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationFsxLustre)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationFsxLustre)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationFsxLustre)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/UpdateLocationFsxLustre)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationFsxLustre)
