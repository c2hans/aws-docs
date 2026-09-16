---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceAssociations.html
---

# DescribeWorkspaceAssociations
<a name="API_DescribeWorkspaceAssociations"></a>

Describes the associations betweens applications and the specified WorkSpace.

## Request Syntax
<a name="API_DescribeWorkspaceAssociations_RequestSyntax"></a>

```
{
   "AssociatedResourceTypes": [ "{{string}}" ],
   "WorkspaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeWorkspaceAssociations_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AssociatedResourceTypes](#API_DescribeWorkspaceAssociations_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaceAssociations-request-AssociatedResourceTypes"></a>
The resource types of the associated resources.
Type: Array of strings
Valid Values: `APPLICATION`
Required: Yes

 ** [WorkspaceId](#API_DescribeWorkspaceAssociations_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaceAssociations-request-WorkspaceId"></a>
The identifier of the WorkSpace.
Type: String
Pattern: `^ws-[0-9a-z]{8,63}$`
Required: Yes

## Response Syntax
<a name="API_DescribeWorkspaceAssociations_ResponseSyntax"></a>

```
{
   "Associations": [
      {
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
   ]
}
```

## Response Elements
<a name="API_DescribeWorkspaceAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Associations](#API_DescribeWorkspaceAssociations_ResponseSyntax) **   <a name="WorkSpaces-DescribeWorkspaceAssociations-response-Associations"></a>
List of information about the specified associations.
Type: Array of [WorkspaceResourceAssociation](API_WorkspaceResourceAssociation.md) objects

## Errors
<a name="API_DescribeWorkspaceAssociations_Errors"></a>

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
<a name="API_DescribeWorkspaceAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeWorkspaceAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeWorkspaceAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeWorkspaceAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeWorkspaceAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeWorkspaceAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeWorkspaceAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeWorkspaceAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeWorkspaceAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeWorkspaceAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeWorkspaceAssociations)
