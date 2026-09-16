---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_CreateWorkspaceBundle.html
---

# CreateWorkspaceBundle
<a name="API_CreateWorkspaceBundle"></a>

Creates the specified WorkSpace bundle. For more information about creating WorkSpace bundles, see [ Create a Custom WorkSpaces Image and Bundle](https://docs.aws.amazon.com/workspaces/latest/adminguide/create-custom-bundle.html).

## Request Syntax
<a name="API_CreateWorkspaceBundle_RequestSyntax"></a>

```
{
   "BundleDescription": "{{string}}",
   "BundleName": "{{string}}",
   "ComputeType": {
      "Name": "{{string}}"
   },
   "ImageId": "{{string}}",
   "RootStorage": {
      "Capacity": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "UserStorage": {
      "Capacity": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateWorkspaceBundle_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [BundleDescription](#API_CreateWorkspaceBundle_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspaceBundle-request-BundleDescription"></a>
The description of the bundle.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_./() -]+$`
Required: Yes

 ** [BundleName](#API_CreateWorkspaceBundle_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspaceBundle-request-BundleName"></a>
The name of the bundle.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_./()\\-]+$`
Required: Yes

 ** [ComputeType](#API_CreateWorkspaceBundle_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspaceBundle-request-ComputeType"></a>
Describes the compute type of the bundle.
Type: [ComputeType](API_ComputeType.md) object
Required: Yes

 ** [ImageId](#API_CreateWorkspaceBundle_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspaceBundle-request-ImageId"></a>
The identifier of the image that is used to create the bundle.
Type: String
Pattern: `wsi-[0-9a-z]{9,63}$`
Required: Yes

 ** [RootStorage](#API_CreateWorkspaceBundle_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspaceBundle-request-RootStorage"></a>
Describes the root volume for a WorkSpace bundle.
Type: [RootStorage](API_RootStorage.md) object
Required: No

 ** [Tags](#API_CreateWorkspaceBundle_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspaceBundle-request-Tags"></a>
The tags associated with the bundle.
To add tags at the same time when you're creating the bundle, you must create an IAM policy that grants your IAM user permissions to use `workspaces:CreateTags`.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [UserStorage](#API_CreateWorkspaceBundle_RequestSyntax) **   <a name="WorkSpaces-CreateWorkspaceBundle-request-UserStorage"></a>
Describes the user volume for a WorkSpace bundle.
Type: [UserStorage](API_UserStorage.md) object
Required: Yes

## Response Syntax
<a name="API_CreateWorkspaceBundle_ResponseSyntax"></a>

```
{
   "WorkspaceBundle": {
      "BundleId": "string",
      "BundleType": "string",
      "ComputeType": {
         "Name": "string"
      },
      "CreationTime": number,
      "Description": "string",
      "ImageId": "string",
      "LastUpdatedTime": number,
      "Name": "string",
      "Owner": "string",
      "RootStorage": {
         "Capacity": "string"
      },
      "State": "string",
      "UserStorage": {
         "Capacity": "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateWorkspaceBundle_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WorkspaceBundle](#API_CreateWorkspaceBundle_ResponseSyntax) **   <a name="WorkSpaces-CreateWorkspaceBundle-response-WorkspaceBundle"></a>
Describes a WorkSpace bundle.
Type: [WorkspaceBundle](API_WorkspaceBundle.md) object

## Errors
<a name="API_CreateWorkspaceBundle_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
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

 ** ResourceUnavailableException **
The specified resource is not available.
 ** message **
The exception error message.
 ** ResourceId **
The identifier of the resource that is not available.
HTTP Status Code: 400

## See Also
<a name="API_CreateWorkspaceBundle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/CreateWorkspaceBundle)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/CreateWorkspaceBundle)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/CreateWorkspaceBundle)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/CreateWorkspaceBundle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/CreateWorkspaceBundle)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/CreateWorkspaceBundle)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/CreateWorkspaceBundle)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/CreateWorkspaceBundle)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/CreateWorkspaceBundle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/CreateWorkspaceBundle)
