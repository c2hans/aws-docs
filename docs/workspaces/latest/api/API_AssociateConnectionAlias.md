---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_AssociateConnectionAlias.html
---

# AssociateConnectionAlias
<a name="API_AssociateConnectionAlias"></a>

Associates the specified connection alias with the specified directory to enable cross-Region redirection. For more information, see [ Cross-Region Redirection for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html).

**Note**
Before performing this operation, call [ DescribeConnectionAliases](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeConnectionAliases.html) to make sure that the current state of the connection alias is `CREATED`.

## Request Syntax
<a name="API_AssociateConnectionAlias_RequestSyntax"></a>

```
{
   "AliasId": "{{string}}",
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateConnectionAlias_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AliasId](#API_AssociateConnectionAlias_RequestSyntax) **   <a name="WorkSpaces-AssociateConnectionAlias-request-AliasId"></a>
The identifier of the connection alias.
Type: String
Length Constraints: Minimum length of 13. Maximum length of 68.
Pattern: `^wsca-[0-9a-z]{8,63}$`
Required: Yes

 ** [ResourceId](#API_AssociateConnectionAlias_RequestSyntax) **   <a name="WorkSpaces-AssociateConnectionAlias-request-ResourceId"></a>
The identifier of the directory to associate the connection alias with.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## Response Syntax
<a name="API_AssociateConnectionAlias_ResponseSyntax"></a>

```
{
   "ConnectionIdentifier": "string"
}
```

## Response Elements
<a name="API_AssociateConnectionAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionIdentifier](#API_AssociateConnectionAlias_ResponseSyntax) **   <a name="WorkSpaces-AssociateConnectionAlias-response-ConnectionIdentifier"></a>
The identifier of the connection alias association. You use the connection identifier in the DNS TXT record when you're configuring your DNS routing policies.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^[a-zA-Z0-9]+$`

## Errors
<a name="API_AssociateConnectionAlias_Errors"></a>

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

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_AssociateConnectionAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/AssociateConnectionAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/AssociateConnectionAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/AssociateConnectionAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/AssociateConnectionAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/AssociateConnectionAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/AssociateConnectionAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/AssociateConnectionAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/AssociateConnectionAlias)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/AssociateConnectionAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/AssociateConnectionAlias)
