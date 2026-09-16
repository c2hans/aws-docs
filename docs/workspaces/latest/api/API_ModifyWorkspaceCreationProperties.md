---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyWorkspaceCreationProperties.html
---

# ModifyWorkspaceCreationProperties
<a name="API_ModifyWorkspaceCreationProperties"></a>

Modify the default properties used to create WorkSpaces.

## Request Syntax
<a name="API_ModifyWorkspaceCreationProperties_RequestSyntax"></a>

```
{
   "ResourceId": "{{string}}",
   "WorkspaceCreationProperties": {
      "CustomSecurityGroupId": "{{string}}",
      "DefaultOu": "{{string}}",
      "EnableInternetAccess": {{boolean}},
      "EnableMaintenanceMode": {{boolean}},
      "InstanceIamRoleArn": "{{string}}",
      "UserEnabledAsLocalAdministrator": {{boolean}}
   }
}
```

## Request Parameters
<a name="API_ModifyWorkspaceCreationProperties_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ResourceId](#API_ModifyWorkspaceCreationProperties_RequestSyntax) **   <a name="WorkSpaces-ModifyWorkspaceCreationProperties-request-ResourceId"></a>
The identifier of the directory.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: Yes

 ** [WorkspaceCreationProperties](#API_ModifyWorkspaceCreationProperties_RequestSyntax) **   <a name="WorkSpaces-ModifyWorkspaceCreationProperties-request-WorkspaceCreationProperties"></a>
The default properties for creating WorkSpaces.
Type: [WorkspaceCreationProperties](API_WorkspaceCreationProperties.md) object
Required: Yes

## Response Elements
<a name="API_ModifyWorkspaceCreationProperties_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ModifyWorkspaceCreationProperties_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** OperationNotSupportedException **
This operation is not supported.
 ** message **
The exception error message.
 ** reason **
The exception error reason.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_ModifyWorkspaceCreationProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/ModifyWorkspaceCreationProperties)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/ModifyWorkspaceCreationProperties)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ModifyWorkspaceCreationProperties)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/ModifyWorkspaceCreationProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ModifyWorkspaceCreationProperties)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/ModifyWorkspaceCreationProperties)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/ModifyWorkspaceCreationProperties)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/ModifyWorkspaceCreationProperties)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/ModifyWorkspaceCreationProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ModifyWorkspaceCreationProperties)
