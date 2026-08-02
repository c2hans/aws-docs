---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateWorkspaceTheme.html
---

# UpdateWorkspaceTheme
<a name="API_UpdateWorkspaceTheme"></a>

Updates the theme configuration for a workspace, including colors and styling.

## Request Syntax
<a name="API_UpdateWorkspaceTheme_RequestSyntax"></a>

```
POST /workspaces/{{InstanceId}}/{{WorkspaceId}}/theme HTTP/1.1
Content-type: application/json

{
   "Theme": {
      "Dark": {
         "Images": {
            "Logo": {
               "Default": "{{string}}",
               "Favicon": "{{string}}"
            }
         },
         "Palette": {
            "Canvas": {
               "ActiveBackground": "{{string}}",
               "ContainerBackground": "{{string}}",
               "PageBackground": "{{string}}"
            },
            "Header": {
               "Background": "{{string}}",
               "InvertActionsColors": {{boolean}},
               "Text": "{{string}}",
               "TextHover": "{{string}}"
            },
            "Navigation": {
               "Background": "{{string}}",
               "InvertActionsColors": {{boolean}},
               "Text": "{{string}}",
               "TextActive": "{{string}}",
               "TextBackgroundActive": "{{string}}",
               "TextBackgroundHover": "{{string}}",
               "TextHover": "{{string}}"
            },
            "Primary": {
               "Active": "{{string}}",
               "ContrastText": "{{string}}",
               "Default": "{{string}}"
            }
         },
         "Typography": {
            "FontFamily": {
               "Default": "{{string}}"
            }
         }
      },
      "Light": {
         "Images": {
            "Logo": {
               "Default": "{{string}}",
               "Favicon": "{{string}}"
            }
         },
         "Palette": {
            "Canvas": {
               "ActiveBackground": "{{string}}",
               "ContainerBackground": "{{string}}",
               "PageBackground": "{{string}}"
            },
            "Header": {
               "Background": "{{string}}",
               "InvertActionsColors": {{boolean}},
               "Text": "{{string}}",
               "TextHover": "{{string}}"
            },
            "Navigation": {
               "Background": "{{string}}",
               "InvertActionsColors": {{boolean}},
               "Text": "{{string}}",
               "TextActive": "{{string}}",
               "TextBackgroundActive": "{{string}}",
               "TextBackgroundHover": "{{string}}",
               "TextHover": "{{string}}"
            },
            "Primary": {
               "Active": "{{string}}",
               "ContrastText": "{{string}}",
               "Default": "{{string}}"
            }
         },
         "Typography": {
            "FontFamily": {
               "Default": "{{string}}"
            }
         }
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateWorkspaceTheme_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_UpdateWorkspaceTheme_RequestSyntax) **   <a name="connect-UpdateWorkspaceTheme-request-uri-InstanceId"></a>
The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [WorkspaceId](#API_UpdateWorkspaceTheme_RequestSyntax) **   <a name="connect-UpdateWorkspaceTheme-request-uri-WorkspaceId"></a>
The identifier of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_UpdateWorkspaceTheme_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Theme](#API_UpdateWorkspaceTheme_RequestSyntax) **   <a name="connect-UpdateWorkspaceTheme-request-Theme"></a>
The theme configuration, including color schemes and visual styles.
Type: [WorkspaceTheme](API_WorkspaceTheme.md) object
Required: No

## Response Syntax
<a name="API_UpdateWorkspaceTheme_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateWorkspaceTheme_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateWorkspaceTheme_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateWorkspaceTheme_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateWorkspaceTheme)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateWorkspaceTheme)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateWorkspaceTheme)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateWorkspaceTheme)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateWorkspaceTheme)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateWorkspaceTheme)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateWorkspaceTheme)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateWorkspaceTheme)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateWorkspaceTheme)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateWorkspaceTheme)
