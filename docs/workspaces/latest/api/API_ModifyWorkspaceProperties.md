---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyWorkspaceProperties.html
---

# ModifyWorkspaceProperties
<a name="API_ModifyWorkspaceProperties"></a>

Modifies the specified WorkSpace properties. For important information about how to modify the size of the root and user volumes, see [ Modify a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html).

**Note**
The `MANUAL` running mode value is only supported by Amazon WorkSpaces Core. Contact your account team to be allow-listed to use this value. For more information, see [Amazon WorkSpaces Core](http://aws.amazon.com/workspaces/core/).

## Request Syntax
<a name="API_ModifyWorkspaceProperties_RequestSyntax"></a>

```
{
   "DataReplication": "{{string}}",
   "WorkspaceId": "{{string}}",
   "WorkspaceProperties": {
      "ComputeTypeName": "{{string}}",
      "GlobalAccelerator": {
         "Mode": "{{string}}",
         "PreferredProtocol": "{{string}}"
      },
      "NestedVirtualizationEnabled": {{boolean}},
      "OperatingSystemName": "{{string}}",
      "Protocols": [ "{{string}}" ],
      "RootVolumeSizeGib": {{number}},
      "RunningMode": "{{string}}",
      "RunningModeAutoStopTimeoutInMinutes": {{number}},
      "UserVolumeSizeGib": {{number}}
   }
}
```

## Request Parameters
<a name="API_ModifyWorkspaceProperties_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DataReplication](#API_ModifyWorkspaceProperties_RequestSyntax) **   <a name="WorkSpaces-ModifyWorkspaceProperties-request-DataReplication"></a>
Indicates the data replication status.
Type: String
Valid Values: `NO_REPLICATION | PRIMARY_AS_SOURCE`
Required: No

 ** [WorkspaceId](#API_ModifyWorkspaceProperties_RequestSyntax) **   <a name="WorkSpaces-ModifyWorkspaceProperties-request-WorkspaceId"></a>
The identifier of the WorkSpace.
Type: String
Pattern: `^ws-[0-9a-z]{8,63}$`
Required: Yes

 ** [WorkspaceProperties](#API_ModifyWorkspaceProperties_RequestSyntax) **   <a name="WorkSpaces-ModifyWorkspaceProperties-request-WorkspaceProperties"></a>
The properties of the WorkSpace.
Type: [WorkspaceProperties](API_WorkspaceProperties.md) object
Required: No

## Response Elements
<a name="API_ModifyWorkspaceProperties_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ModifyWorkspaceProperties_Errors"></a>

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

 ** OperationInProgressException **
The properties of this WorkSpace are currently being modified. Try again in a moment.
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

 ** UnsupportedWorkspaceConfigurationException **
The configuration of this WorkSpace is not supported for this operation. For more information, see [Required Configuration and Service Components for WorkSpaces ](https://docs.aws.amazon.com/workspaces/latest/adminguide/required-service-components.html).
HTTP Status Code: 400

## See Also
<a name="API_ModifyWorkspaceProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/ModifyWorkspaceProperties)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/ModifyWorkspaceProperties)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ModifyWorkspaceProperties)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/ModifyWorkspaceProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ModifyWorkspaceProperties)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/ModifyWorkspaceProperties)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/ModifyWorkspaceProperties)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/ModifyWorkspaceProperties)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/ModifyWorkspaceProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ModifyWorkspaceProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
