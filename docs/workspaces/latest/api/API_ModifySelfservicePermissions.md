---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ModifySelfservicePermissions.html
---

# ModifySelfservicePermissions
<a name="API_ModifySelfservicePermissions"></a>

Modifies the self-service WorkSpace management capabilities for your users. For more information, see [Enable Self-Service WorkSpace Management Capabilities for Your Users](https://docs.aws.amazon.com/workspaces/latest/adminguide/enable-user-self-service-workspace-management.html).

## Request Syntax
<a name="API_ModifySelfservicePermissions_RequestSyntax"></a>

```
{
   "ResourceId": "{{string}}",
   "SelfservicePermissions": {
      "ChangeComputeType": "{{string}}",
      "IncreaseVolumeSize": "{{string}}",
      "RebuildWorkspace": "{{string}}",
      "RestartWorkspace": "{{string}}",
      "SwitchRunningMode": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ModifySelfservicePermissions_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ResourceId](#API_ModifySelfservicePermissions_RequestSyntax) **   <a name="WorkSpaces-ModifySelfservicePermissions-request-ResourceId"></a>
The identifier of the directory.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: Yes

 ** [SelfservicePermissions](#API_ModifySelfservicePermissions_RequestSyntax) **   <a name="WorkSpaces-ModifySelfservicePermissions-request-SelfservicePermissions"></a>
The permissions to enable or disable self-service capabilities.
Type: [SelfservicePermissions](API_SelfservicePermissions.md) object
Required: Yes

## Response Elements
<a name="API_ModifySelfservicePermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ModifySelfservicePermissions_Errors"></a>

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
<a name="API_ModifySelfservicePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/ModifySelfservicePermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/ModifySelfservicePermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ModifySelfservicePermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/ModifySelfservicePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ModifySelfservicePermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/ModifySelfservicePermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/ModifySelfservicePermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/ModifySelfservicePermissions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/ModifySelfservicePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ModifySelfservicePermissions)
