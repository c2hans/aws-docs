---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DisassociateConnectionAlias.html
---

# DisassociateConnectionAlias
<a name="API_DisassociateConnectionAlias"></a>

Disassociates a connection alias from a directory. Disassociating a connection alias disables cross-Region redirection between two directories in different Regions. For more information, see [ Cross-Region Redirection for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html).

**Note**
Before performing this operation, call [ DescribeConnectionAliases](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeConnectionAliases.html) to make sure that the current state of the connection alias is `CREATED`.

## Request Syntax
<a name="API_DisassociateConnectionAlias_RequestSyntax"></a>

```
{
   "AliasId": "{{string}}"
}
```

## Request Parameters
<a name="API_DisassociateConnectionAlias_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AliasId](#API_DisassociateConnectionAlias_RequestSyntax) **   <a name="WorkSpaces-DisassociateConnectionAlias-request-AliasId"></a>
The identifier of the connection alias to disassociate.
Type: String
Length Constraints: Minimum length of 13. Maximum length of 68.
Pattern: `^wsca-[0-9a-z]{8,63}$`
Required: Yes

## Response Elements
<a name="API_DisassociateConnectionAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateConnectionAlias_Errors"></a>

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

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateConnectionAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DisassociateConnectionAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DisassociateConnectionAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DisassociateConnectionAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DisassociateConnectionAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DisassociateConnectionAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DisassociateConnectionAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DisassociateConnectionAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DisassociateConnectionAlias)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DisassociateConnectionAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DisassociateConnectionAlias)
