---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_AssociateWorkspaceApplication.html
---

# AssociateWorkspaceApplication
<a name="API_AssociateWorkspaceApplication"></a>

Associates the specified application to the specified WorkSpace.

## Request Syntax
<a name="API_AssociateWorkspaceApplication_RequestSyntax"></a>

```
{
   "ApplicationId": "{{string}}",
   "WorkspaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateWorkspaceApplication_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationId](#API_AssociateWorkspaceApplication_RequestSyntax) **   <a name="WorkSpaces-AssociateWorkspaceApplication-request-ApplicationId"></a>
The identifier of the application.
Type: String
Pattern: `^wsa-[0-9a-z]{8,63}$`
Required: Yes

 ** [WorkspaceId](#API_AssociateWorkspaceApplication_RequestSyntax) **   <a name="WorkSpaces-AssociateWorkspaceApplication-request-WorkspaceId"></a>
The identifier of the WorkSpace.
Type: String
Pattern: `^ws-[0-9a-z]{8,63}$`
Required: Yes

## Response Syntax
<a name="API_AssociateWorkspaceApplication_ResponseSyntax"></a>

```
{
   "Association": {
      "AssociatedResourceId": "string",
      "AssociatedResourceType": "string",
      "Created": number,
      "LastUpdatedTime": number,
      "State": "string",
      "StateReason": {
         "ErrorCode": "string",
         "ErrorMessage": "string"
      },
      "WorkspaceId": "string"
   }
}
```

## Response Elements
<a name="API_AssociateWorkspaceApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Association](#API_AssociateWorkspaceApplication_ResponseSyntax) **   <a name="WorkSpaces-AssociateWorkspaceApplication-response-Association"></a>
Information about the association between the specified WorkSpace and the specified application.
Type: [WorkspaceResourceAssociation](API_WorkspaceResourceAssociation.md) object

## Errors
<a name="API_AssociateWorkspaceApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** ApplicationNotSupportedException **
The specified application is not supported.
HTTP Status Code: 400

 ** ComputeNotCompatibleException **
The compute type of the WorkSpace is not compatible with the application.
HTTP Status Code: 400

 ** IncompatibleApplicationsException **
The specified application is not compatible with the resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** OperatingSystemNotCompatibleException **
The operating system of the WorkSpace is not compatible with the application.
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

 ** ResourceInUseException **
The specified resource is currently in use.
 ** ResourceId **
The ID of the resource that is in use.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_AssociateWorkspaceApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/AssociateWorkspaceApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/AssociateWorkspaceApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/AssociateWorkspaceApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/AssociateWorkspaceApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/AssociateWorkspaceApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/AssociateWorkspaceApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/AssociateWorkspaceApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/AssociateWorkspaceApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/AssociateWorkspaceApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/AssociateWorkspaceApplication)
