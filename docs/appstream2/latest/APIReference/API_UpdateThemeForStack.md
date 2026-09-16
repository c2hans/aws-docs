---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateThemeForStack.html
---

# UpdateThemeForStack
<a name="API_UpdateThemeForStack"></a>

Updates custom branding that customizes the appearance of the streaming application catalog page.

## Request Syntax
<a name="API_UpdateThemeForStack_RequestSyntax"></a>

```
{
   "AttributesToDelete": [ "{{string}}" ],
   "FaviconS3Location": {
      "S3Bucket": "{{string}}",
      "S3Key": "{{string}}"
   },
   "FooterLinks": [
      {
         "DisplayName": "{{string}}",
         "FooterLinkURL": "{{string}}"
      }
   ],
   "OrganizationLogoS3Location": {
      "S3Bucket": "{{string}}",
      "S3Key": "{{string}}"
   },
   "StackName": "{{string}}",
   "State": "{{string}}",
   "ThemeStyling": "{{string}}",
   "TitleText": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateThemeForStack_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttributesToDelete](#API_UpdateThemeForStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateThemeForStack-request-AttributesToDelete"></a>
The attributes to delete.
Type: Array of strings
Valid Values: `FOOTER_LINKS`
Required: No

 ** [FaviconS3Location](#API_UpdateThemeForStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateThemeForStack-request-FaviconS3Location"></a>
The S3 location of the favicon. The favicon enables users to recognize their application streaming site in a browser full of tabs or bookmarks. It is displayed at the top of the browser tab for the application streaming site during users' streaming sessions.
Type: [S3Location](API_S3Location.md) object
Required: No

 ** [FooterLinks](#API_UpdateThemeForStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateThemeForStack-request-FooterLinks"></a>
The links that are displayed in the footer of the streaming application catalog page. These links are helpful resources for users, such as the organization's IT support and product marketing sites.
Type: Array of [ThemeFooterLink](API_ThemeFooterLink.md) objects
Required: No

 ** [OrganizationLogoS3Location](#API_UpdateThemeForStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateThemeForStack-request-OrganizationLogoS3Location"></a>
The organization logo that appears on the streaming application catalog page.
Type: [S3Location](API_S3Location.md) object
Required: No

 ** [StackName](#API_UpdateThemeForStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateThemeForStack-request-StackName"></a>
The name of the stack for the theme.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [State](#API_UpdateThemeForStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateThemeForStack-request-State"></a>
Specifies whether custom branding should be applied to catalog page or not.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [ThemeStyling](#API_UpdateThemeForStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateThemeForStack-request-ThemeStyling"></a>
The color theme that is applied to website links, text, and buttons. These colors are also applied as accents in the background for the streaming application catalog page.
Type: String
Valid Values: `LIGHT_BLUE | BLUE | PINK | RED`
Required: No

 ** [TitleText](#API_UpdateThemeForStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateThemeForStack-request-TitleText"></a>
The title that is displayed at the top of the browser tab during users' application streaming sessions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[-@./#&+\w\s]*$`
Required: No

## Response Syntax
<a name="API_UpdateThemeForStack_ResponseSyntax"></a>

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
<a name="API_UpdateThemeForStack_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Theme](#API_UpdateThemeForStack_ResponseSyntax) **   <a name="WorkSpacesApplications-UpdateThemeForStack-response-Theme"></a>
 The theme object that contains the metadata of the custom branding.
Type: [Theme](API_Theme.md) object

## Errors
<a name="API_UpdateThemeForStack_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidAccountStatusException **
The resource cannot be created because your AWS account is suspended. For assistance, contact AWS Support.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidParameterCombinationException **
Indicates an incorrect combination of parameters, or a missing parameter.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** LimitExceededException **
The requested limit exceeds the permitted limit for an account.
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
<a name="API_UpdateThemeForStack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/UpdateThemeForStack)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/UpdateThemeForStack)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/UpdateThemeForStack)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/UpdateThemeForStack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/UpdateThemeForStack)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/UpdateThemeForStack)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/UpdateThemeForStack)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/UpdateThemeForStack)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/UpdateThemeForStack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/UpdateThemeForStack)
