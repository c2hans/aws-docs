---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateWorkspace.html
---

# CreateWorkspace
<a name="API_CreateWorkspace"></a>

Creates a workspace that defines the user experience by mapping views to pages. Workspaces can be assigned to users or routing profiles.

## Request Syntax
<a name="API_CreateWorkspace_RequestSyntax"></a>

```
PUT /workspaces/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
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
   },
   "Title": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateWorkspace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateWorkspace_RequestSyntax) **   <a name="connect-CreateWorkspace-request-uri-InstanceId"></a>
The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateWorkspace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateWorkspace_RequestSyntax) **   <a name="connect-CreateWorkspace-request-Description"></a>
The description of the workspace. Maximum length is 250 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `^[\\P{C}\r\n\t]*$`
Required: No

 ** [Name](#API_CreateWorkspace_RequestSyntax) **   <a name="connect-CreateWorkspace-request-Name"></a>
The name of the workspace. Must be unique within the instance and can contain 1-127 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\\S.*`
Required: Yes

 ** [Tags](#API_CreateWorkspace_RequestSyntax) **   <a name="connect-CreateWorkspace-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, `{ "Tags": {"key1":"value1", "key2":"value2"} }`.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [Theme](#API_CreateWorkspace_RequestSyntax) **   <a name="connect-CreateWorkspace-request-Theme"></a>
The theme configuration for the workspace, including colors and styling.
Type: [WorkspaceTheme](API_WorkspaceTheme.md) object
Required: No

 ** [Title](#API_CreateWorkspace_RequestSyntax) **   <a name="connect-CreateWorkspace-request-Title"></a>
The title displayed for the workspace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 127.
Pattern: `^[\\P{C}]*$`
Required: No

## Response Syntax
<a name="API_CreateWorkspace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "WorkspaceArn": "string",
   "WorkspaceId": "string"
}
```

## Response Elements
<a name="API_CreateWorkspace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WorkspaceArn](#API_CreateWorkspace_ResponseSyntax) **   <a name="connect-CreateWorkspace-response-WorkspaceArn"></a>
The Amazon Resource Name (ARN) of the workspace.
Type: String

 ** [WorkspaceId](#API_CreateWorkspace_ResponseSyntax) **   <a name="connect-CreateWorkspace-response-WorkspaceId"></a>
The identifier of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_CreateWorkspace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

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

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateWorkspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateWorkspace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateWorkspace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateWorkspace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateWorkspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateWorkspace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateWorkspace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateWorkspace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateWorkspace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateWorkspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateWorkspace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
