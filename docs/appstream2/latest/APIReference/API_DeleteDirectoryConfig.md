---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteDirectoryConfig.html
---

# DeleteDirectoryConfig
<a name="API_DeleteDirectoryConfig"></a>

Deletes the specified Directory Config object from WorkSpaces Applications. This object includes the information required to join streaming instances to an Active Directory domain.

## Request Syntax
<a name="API_DeleteDirectoryConfig_RequestSyntax"></a>

```
{
   "DirectoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDirectoryConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DirectoryName](#API_DeleteDirectoryConfig_RequestSyntax) **   <a name="WorkSpacesApplications-DeleteDirectoryConfig-request-DirectoryName"></a>
The name of the directory configuration.
Type: String
Required: Yes

## Response Elements
<a name="API_DeleteDirectoryConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteDirectoryConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUseException **
The specified resource is in use.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDirectoryConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DeleteDirectoryConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DeleteDirectoryConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DeleteDirectoryConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DeleteDirectoryConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DeleteDirectoryConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DeleteDirectoryConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DeleteDirectoryConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DeleteDirectoryConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DeleteDirectoryConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DeleteDirectoryConfig)
