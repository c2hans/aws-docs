---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeWorkspace.html
---

# DescribeWorkspace
<a name="API_DescribeWorkspace"></a>

Retrieves details about a workspace, including its configuration and metadata.

## Request Syntax
<a name="API_DescribeWorkspace_RequestSyntax"></a>

```
GET /workspaces/{{InstanceId}}/{{WorkspaceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeWorkspace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DescribeWorkspace_RequestSyntax) **   <a name="connect-DescribeWorkspace-request-uri-InstanceId"></a>
The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [WorkspaceId](#API_DescribeWorkspace_RequestSyntax) **   <a name="connect-DescribeWorkspace-request-uri-WorkspaceId"></a>
The identifier of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_DescribeWorkspace_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeWorkspace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Workspace": {
      "Arn": "string",
      "Description": "string",
      "Id": "string",
      "LastModifiedRegion": "string",
      "LastModifiedTime": number,
      "Name": "string",
      "Tags": {
         "string" : "string"
      },
      "Theme": {
         "Dark": {
            "Images": {
               "Logo": {
                  "Default": "string",
                  "Favicon": "string"
               }
            },
            "Palette": {
               "Canvas": {
                  "ActiveBackground": "string",
                  "ContainerBackground": "string",
                  "PageBackground": "string"
               },
               "Header": {
                  "Background": "string",
                  "InvertActionsColors": boolean,
                  "Text": "string",
                  "TextHover": "string"
               },
               "Navigation": {
                  "Background": "string",
                  "InvertActionsColors": boolean,
                  "Text": "string",
                  "TextActive": "string",
                  "TextBackgroundActive": "string",
                  "TextBackgroundHover": "string",
                  "TextHover": "string"
               },
               "Primary": {
                  "Active": "string",
                  "ContrastText": "string",
                  "Default": "string"
               }
            },
            "Typography": {
               "FontFamily": {
                  "Default": "string"
               }
            }
         },
         "Light": {
            "Images": {
               "Logo": {
                  "Default": "string",
                  "Favicon": "string"
               }
            },
            "Palette": {
               "Canvas": {
                  "ActiveBackground": "string",
                  "ContainerBackground": "string",
                  "PageBackground": "string"
               },
               "Header": {
                  "Background": "string",
                  "InvertActionsColors": boolean,
                  "Text": "string",
                  "TextHover": "string"
               },
               "Navigation": {
                  "Background": "string",
                  "InvertActionsColors": boolean,
                  "Text": "string",
                  "TextActive": "string",
                  "TextBackgroundActive": "string",
                  "TextBackgroundHover": "string",
                  "TextHover": "string"
               },
               "Primary": {
                  "Active": "string",
                  "ContrastText": "string",
                  "Default": "string"
               }
            },
            "Typography": {
               "FontFamily": {
                  "Default": "string"
               }
            }
         }
      },
      "Title": "string",
      "Visibility": "string"
   }
}
```

## Response Elements
<a name="API_DescribeWorkspace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Workspace](#API_DescribeWorkspace_ResponseSyntax) **   <a name="connect-DescribeWorkspace-response-Workspace"></a>
Information about the workspace.
Type: [Workspace](API_Workspace.md) object

## Errors
<a name="API_DescribeWorkspace_Errors"></a>

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
<a name="API_DescribeWorkspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeWorkspace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeWorkspace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeWorkspace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeWorkspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeWorkspace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeWorkspace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeWorkspace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeWorkspace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeWorkspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeWorkspace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
