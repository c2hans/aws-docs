---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteThemeForStack.html
---

# DeleteThemeForStack
<a name="API_DeleteThemeForStack"></a>

Deletes custom branding that customizes the appearance of the streaming application catalog page.

## Request Syntax
<a name="API_DeleteThemeForStack_RequestSyntax"></a>

```
{
   "StackName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteThemeForStack_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [StackName](#API_DeleteThemeForStack_RequestSyntax) **   <a name="WorkSpacesApplications-DeleteThemeForStack-request-StackName"></a>
The name of the stack for the theme.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

## Response Elements
<a name="API_DeleteThemeForStack_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteThemeForStack_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
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
<a name="API_DeleteThemeForStack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DeleteThemeForStack)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DeleteThemeForStack)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DeleteThemeForStack)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DeleteThemeForStack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DeleteThemeForStack)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DeleteThemeForStack)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DeleteThemeForStack)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DeleteThemeForStack)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DeleteThemeForStack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DeleteThemeForStack)
