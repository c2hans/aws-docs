---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_CreateConnectionAlias.html
---

# CreateConnectionAlias
<a name="API_CreateConnectionAlias"></a>

Creates the specified connection alias for use with cross-Region redirection. For more information, see [ Cross-Region Redirection for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html).

## Request Syntax
<a name="API_CreateConnectionAlias_RequestSyntax"></a>

```
{
   "ConnectionString": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateConnectionAlias_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ConnectionString](#API_CreateConnectionAlias_RequestSyntax) **   <a name="WorkSpaces-CreateConnectionAlias-request-ConnectionString"></a>
A connection string in the form of a fully qualified domain name (FQDN), such as `www.example.com`.
After you create a connection string, it is always associated to your AWS account. You cannot recreate the same connection string with a different account, even if you delete all instances of it from the original account. The connection string is globally reserved for your account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[.0-9a-zA-Z\-]{1,255}$`
Required: Yes

 ** [Tags](#API_CreateConnectionAlias_RequestSyntax) **   <a name="WorkSpaces-CreateConnectionAlias-request-Tags"></a>
The tags to associate with the connection alias.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateConnectionAlias_ResponseSyntax"></a>

```
{
   "AliasId": "string"
}
```

## Response Elements
<a name="API_CreateConnectionAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AliasId](#API_CreateConnectionAlias_ResponseSyntax) **   <a name="WorkSpaces-CreateConnectionAlias-response-AliasId"></a>
The identifier of the connection alias.
Type: String
Length Constraints: Minimum length of 13. Maximum length of 68.
Pattern: `^wsca-[0-9a-z]{8,63}$`

## Errors
<a name="API_CreateConnectionAlias_Errors"></a>

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

## See Also
<a name="API_CreateConnectionAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/CreateConnectionAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/CreateConnectionAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/CreateConnectionAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/CreateConnectionAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/CreateConnectionAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/CreateConnectionAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/CreateConnectionAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/CreateConnectionAlias)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/CreateConnectionAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/CreateConnectionAlias)
