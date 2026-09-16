---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeThemeForStack.html
---

# DescribeThemeForStack
<a name="API_DescribeThemeForStack"></a>

Retrieves a list that describes the theme for a specified stack. A theme is custom branding that customizes the appearance of the streaming application catalog page.

## Request Syntax
<a name="API_DescribeThemeForStack_RequestSyntax"></a>

```
{
   "StackName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeThemeForStack_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [StackName](#API_DescribeThemeForStack_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeThemeForStack-request-StackName"></a>
The name of the stack for the theme.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

## Response Syntax
<a name="API_DescribeThemeForStack_ResponseSyntax"></a>

```
{
   "Theme": {
      "CreatedTime": number,
      "StackName": "string",
      "State": "string",
      "ThemeFaviconURL": "string",
      "ThemeFooterLinks": [
         {
            "DisplayName": "string",
            "FooterLinkURL": "string"
         }
      ],
      "ThemeOrganizationLogoURL": "string",
      "ThemeStyling": "string",
      "ThemeTitleText": "string"
   }
}
```

## Response Elements
<a name="API_DescribeThemeForStack_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Theme](#API_DescribeThemeForStack_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeThemeForStack-response-Theme"></a>
 The theme object that contains the metadata of the custom branding.
Type: [Theme](API_Theme.md) object

## Errors
<a name="API_DescribeThemeForStack_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_DescribeThemeForStack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DescribeThemeForStack)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DescribeThemeForStack)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DescribeThemeForStack)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DescribeThemeForStack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DescribeThemeForStack)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DescribeThemeForStack)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DescribeThemeForStack)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DescribeThemeForStack)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DescribeThemeForStack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DescribeThemeForStack)
