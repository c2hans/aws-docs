---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateImagePermissions.html
---

# UpdateImagePermissions
<a name="API_UpdateImagePermissions"></a>

Adds or updates permissions for the specified private image.

## Request Syntax
<a name="API_UpdateImagePermissions_RequestSyntax"></a>

```
{
   "ImagePermissions": {
      "allowFleet": {{boolean}},
      "allowImageBuilder": {{boolean}}
   },
   "Name": "{{string}}",
   "SharedAccountId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateImagePermissions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ImagePermissions](#API_UpdateImagePermissions_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateImagePermissions-request-ImagePermissions"></a>
The permissions for the image.
Type: [ImagePermissions](API_ImagePermissions.md) object
Required: Yes

 ** [Name](#API_UpdateImagePermissions_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateImagePermissions-request-Name"></a>
The name of the private image.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [SharedAccountId](#API_UpdateImagePermissions_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateImagePermissions-request-SharedAccountId"></a>
The 12-digit identifier of the AWS account for which you want add or update image permissions.
Type: String
Pattern: `^\d+$`
Required: Yes

## Response Elements
<a name="API_UpdateImagePermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateImagePermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededException **
The requested limit exceeds the permitted limit for an account.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotAvailableException **
The specified resource exists and is not in use, but isn't available.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateImagePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/UpdateImagePermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/UpdateImagePermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/UpdateImagePermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/UpdateImagePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/UpdateImagePermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/UpdateImagePermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/UpdateImagePermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/UpdateImagePermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/UpdateImagePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/UpdateImagePermissions)
