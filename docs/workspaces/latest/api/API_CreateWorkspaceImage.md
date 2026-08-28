---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_CreateWorkspaceImage.html
---

# CreateWorkspaceImage
<a name="API_CreateWorkspaceImage"></a>

Creates a new WorkSpace image from an existing WorkSpace.

## Request Syntax
<a name="API_CreateWorkspaceImage_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "WorkspaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateWorkspaceImage_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspaceImage-request-Description"></a>
The description of the new WorkSpace image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_./() -]+$`
Required: Yes

 ** [Name](#API_CreateWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspaceImage-request-Name"></a>
The name of the new WorkSpace image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_./()\\-]+$`
Required: Yes

 ** [Tags](#API_CreateWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspaceImage-request-Tags"></a>
The tags that you want to add to the new WorkSpace image. To add tags when you're creating the image, you must create an IAM policy that grants your IAM user permission to use `workspaces:CreateTags`.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [WorkspaceId](#API_CreateWorkspaceImage_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspaceImage-request-WorkspaceId"></a>
The identifier of the source WorkSpace
Type: String
Pattern: `^ws-[0-9a-z]{8,63}$`
Required: Yes

## Response Syntax
<a name="API_CreateWorkspaceImage_ResponseSyntax"></a>

```
{
   "Created": number,
   "Description": "string",
   "ImageId": "string",
   "Name": "string",
   "OperatingSystem": {
      "Type": "string"
   },
   "OwnerAccountId": "string",
   "RequiredTenancy": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_CreateWorkspaceImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Created](#API_CreateWorkspaceImage_ResponseSyntax) **   <a name="WorkSpaces-CreateWorkspaceImage-response-Created"></a>
The date when the image was created.
Type: Timestamp

 ** [Description](#API_CreateWorkspaceImage_ResponseSyntax) **   <a name="WorkSpaces-CreateWorkspaceImage-response-Description"></a>
The description of the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_./() -]+$`

 ** [ImageId](#API_CreateWorkspaceImage_ResponseSyntax) **   <a name="WorkSpaces-CreateWorkspaceImage-response-ImageId"></a>
The identifier of the new WorkSpace image.
Type: String
Pattern: `wsi-[0-9a-z]{9,63}$`

 ** [Name](#API_CreateWorkspaceImage_ResponseSyntax) **   <a name="WorkSpaces-CreateWorkspaceImage-response-Name"></a>
The name of the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_./()\\-]+$`

 ** [OperatingSystem](#API_CreateWorkspaceImage_ResponseSyntax) **   <a name="WorkSpaces-CreateWorkspaceImage-response-OperatingSystem"></a>
The operating system that the image is running.
Type: [OperatingSystem](API_OperatingSystem.md) object

 ** [OwnerAccountId](#API_CreateWorkspaceImage_ResponseSyntax) **   <a name="WorkSpaces-CreateWorkspaceImage-response-OwnerAccountId"></a>
The identifier of the AWS account that owns the image.
Type: String
Pattern: `^\d{12}$`

 ** [RequiredTenancy](#API_CreateWorkspaceImage_ResponseSyntax) **   <a name="WorkSpaces-CreateWorkspaceImage-response-RequiredTenancy"></a>
Specifies whether the image is running on dedicated hardware. When Bring Your Own License (BYOL) is enabled, this value is set to DEDICATED. For more information, see [ Bring Your Own Windows Desktop Images.](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.htm).
Type: String
Valid Values: `DEFAULT | DEDICATED`

 ** [State](#API_CreateWorkspaceImage_ResponseSyntax) **   <a name="WorkSpaces-CreateWorkspaceImage-response-State"></a>
The availability status of the image.
Type: String
Valid Values: `AVAILABLE | PENDING | ERROR`

## Errors
<a name="API_CreateWorkspaceImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** InvalidResourceStateException **
The state of the resource is not valid for this operation.
HTTP Status Code: 400

 ** OperationNotSupportedException **
This operation is not supported.
 ** message **
The exception error message.
 ** reason **
The exception error reason.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The specified resource already exists.
HTTP Status Code: 400

 ** ResourceLimitExceededException **
Your resource limits have been exceeded.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_CreateWorkspaceImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/CreateWorkspaceImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/CreateWorkspaceImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/CreateWorkspaceImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/CreateWorkspaceImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/CreateWorkspaceImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/CreateWorkspaceImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/CreateWorkspaceImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/CreateWorkspaceImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/CreateWorkspaceImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/CreateWorkspaceImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
