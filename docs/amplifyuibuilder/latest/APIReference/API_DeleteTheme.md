---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_DeleteTheme.html
---

# DeleteTheme
<a name="API_DeleteTheme"></a>

Deletes a theme from an Amplify app.

## Request Syntax
<a name="API_DeleteTheme_RequestSyntax"></a>

```
DELETE /app/{{appId}}/environment/{{environmentName}}/themes/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteTheme_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_DeleteTheme_RequestSyntax) **   <a name="amplifyuibuilder-DeleteTheme-request-uri-appId"></a>
The unique ID of the Amplify app associated with the theme to delete.
Required: Yes

 ** [environmentName](#API_DeleteTheme_RequestSyntax) **   <a name="amplifyuibuilder-DeleteTheme-request-uri-environmentName"></a>
The name of the backend environment that is a part of the Amplify app.
Required: Yes

 ** [id](#API_DeleteTheme_RequestSyntax) **   <a name="amplifyuibuilder-DeleteTheme-request-uri-id"></a>
The unique ID of the theme to delete.
Required: Yes

## Request Body
<a name="API_DeleteTheme_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteTheme_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteTheme_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteTheme_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred. Please retry your request.
HTTP Status Code: 500

 ** InvalidParameterException **
An invalid or out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

## See Also
<a name="API_DeleteTheme_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplifyuibuilder-2021-08-11/DeleteTheme)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplifyuibuilder-2021-08-11/DeleteTheme)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/DeleteTheme)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplifyuibuilder-2021-08-11/DeleteTheme)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/DeleteTheme)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplifyuibuilder-2021-08-11/DeleteTheme)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplifyuibuilder-2021-08-11/DeleteTheme)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplifyuibuilder-2021-08-11/DeleteTheme)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/amplifyuibuilder-2021-08-11/DeleteTheme)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/DeleteTheme)
