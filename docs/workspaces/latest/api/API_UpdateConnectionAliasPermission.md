---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateConnectionAliasPermission.html
---

# UpdateConnectionAliasPermission
<a name="API_UpdateConnectionAliasPermission"></a>

Shares or unshares a connection alias with one account by specifying whether that account has permission to associate the connection alias with a directory. If the association permission is granted, the connection alias is shared with that account. If the association permission is revoked, the connection alias is unshared with the account. For more information, see [ Cross-Region Redirection for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html).

**Note**
Before performing this operation, call [ DescribeConnectionAliases](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeConnectionAliases.html) to make sure that the current state of the connection alias is `CREATED`.
To delete a connection alias that has been shared, the shared account must first disassociate the connection alias from any directories it has been associated with. Then you must unshare the connection alias from the account it has been shared with. You can delete a connection alias only after it is no longer shared with any accounts or associated with any directories.

## Request Syntax
<a name="API_UpdateConnectionAliasPermission_RequestSyntax"></a>

```
{
   "AliasId": "{{string}}",
   "ConnectionAliasPermission": {
      "AllowAssociation": {{boolean}},
      "SharedAccountId": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateConnectionAliasPermission_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AliasId](#API_UpdateConnectionAliasPermission_RequestSyntax) **   <a name="WorkSpaces-UpdateConnectionAliasPermission-request-AliasId"></a>
The identifier of the connection alias that you want to update permissions for.
Type: String
Length Constraints: Minimum length of 13. Maximum length of 68.
Pattern: `^wsca-[0-9a-z]{8,63}$`
Required: Yes

 ** [ConnectionAliasPermission](#API_UpdateConnectionAliasPermission_RequestSyntax) **   <a name="WorkSpaces-UpdateConnectionAliasPermission-request-ConnectionAliasPermission"></a>
Indicates whether to share or unshare the connection alias with the specified AWS account.
Type: [ConnectionAliasPermission](API_ConnectionAliasPermission.md) object
Required: Yes

## Response Elements
<a name="API_UpdateConnectionAliasPermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateConnectionAliasPermission_Errors"></a>

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

 ** ResourceAssociatedException **
The resource is associated with a directory.
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
<a name="API_UpdateConnectionAliasPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/UpdateConnectionAliasPermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/UpdateConnectionAliasPermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/UpdateConnectionAliasPermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/UpdateConnectionAliasPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/UpdateConnectionAliasPermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/UpdateConnectionAliasPermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/UpdateConnectionAliasPermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/UpdateConnectionAliasPermission)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/UpdateConnectionAliasPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/UpdateConnectionAliasPermission)
