---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AssociateSoftwareToImageBuilder.html
---

# AssociateSoftwareToImageBuilder
<a name="API_AssociateSoftwareToImageBuilder"></a>

Associates license included application(s) with an existing image builder instance.

## Request Syntax
<a name="API_AssociateSoftwareToImageBuilder_RequestSyntax"></a>

```
{
   "ImageBuilderName": "{{string}}",
   "SoftwareNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_AssociateSoftwareToImageBuilder_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ImageBuilderName](#API_AssociateSoftwareToImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-AssociateSoftwareToImageBuilder-request-ImageBuilderName"></a>
The name of the target image builder instance.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [SoftwareNames](#API_AssociateSoftwareToImageBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-AssociateSoftwareToImageBuilder-request-SoftwareNames"></a>
The list of license included applications to associate with the image builder.
Possible values include the following:
+ Microsoft\_Office\_2021\_LTSC\_Professional\_Plus\_32Bit
+ Microsoft\_Office\_2021\_LTSC\_Professional\_Plus\_64Bit
+ Microsoft\_Office\_2024\_LTSC\_Professional\_Plus\_32Bit
+ Microsoft\_Office\_2024\_LTSC\_Professional\_Plus\_64Bit
+ Microsoft\_Visio\_2021\_LTSC\_Professional\_32Bit
+ Microsoft\_Visio\_2021\_LTSC\_Professional\_64Bit
+ Microsoft\_Visio\_2024\_LTSC\_Professional\_32Bit
+ Microsoft\_Visio\_2024\_LTSC\_Professional\_64Bit
+ Microsoft\_Project\_2021\_Professional\_32Bit
+ Microsoft\_Project\_2021\_Professional\_64Bit
+ Microsoft\_Project\_2024\_Professional\_32Bit
+ Microsoft\_Project\_2024\_Professional\_64Bit
+ Microsoft\_Office\_2021\_LTSC\_Standard\_32Bit
+ Microsoft\_Office\_2021\_LTSC\_Standard\_64Bit
+ Microsoft\_Office\_2024\_LTSC\_Standard\_32Bit
+ Microsoft\_Office\_2024\_LTSC\_Standard\_64Bit
+ Microsoft\_Visio\_2021\_LTSC\_Standard\_32Bit
+ Microsoft\_Visio\_2021\_LTSC\_Standard\_64Bit
+ Microsoft\_Visio\_2024\_LTSC\_Standard\_32Bit
+ Microsoft\_Visio\_2024\_LTSC\_Standard\_64Bit
+ Microsoft\_Project\_2021\_Standard\_32Bit
+ Microsoft\_Project\_2021\_Standard\_64Bit
+ Microsoft\_Project\_2024\_Standard\_32Bit
+ Microsoft\_Project\_2024\_Standard\_64Bit
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: Yes

## Response Elements
<a name="API_AssociateSoftwareToImageBuilder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateSoftwareToImageBuilder_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** IncompatibleImageException **
The image can't be updated because it's not compatible for updates.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidParameterCombinationException **
Indicates an incorrect combination of parameters, or a missing parameter.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_AssociateSoftwareToImageBuilder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/AssociateSoftwareToImageBuilder)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/AssociateSoftwareToImageBuilder)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/AssociateSoftwareToImageBuilder)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/AssociateSoftwareToImageBuilder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/AssociateSoftwareToImageBuilder)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/AssociateSoftwareToImageBuilder)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/AssociateSoftwareToImageBuilder)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/AssociateSoftwareToImageBuilder)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/AssociateSoftwareToImageBuilder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/AssociateSoftwareToImageBuilder)
