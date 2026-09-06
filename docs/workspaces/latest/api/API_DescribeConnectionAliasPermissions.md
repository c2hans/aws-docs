---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeConnectionAliasPermissions.html
---

# DescribeConnectionAliasPermissions
<a name="API_DescribeConnectionAliasPermissions"></a>

Describes the permissions that the owner of a connection alias has granted to another AWS account for the specified connection alias. For more information, see [ Cross-Region Redirection for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html).

## Request Syntax
<a name="API_DescribeConnectionAliasPermissions_RequestSyntax"></a>

```
{
   "AliasId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeConnectionAliasPermissions_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AliasId](#API_DescribeConnectionAliasPermissions_RequestSyntax) **   <a name="WorkSpaces-DescribeConnectionAliasPermissions-request-AliasId"></a>
The identifier of the connection alias.
Type: String
Length Constraints: Minimum length of 13. Maximum length of 68.
Pattern: `^wsca-[0-9a-z]{8,63}$`
Required: Yes

 ** [MaxResults](#API_DescribeConnectionAliasPermissions_RequestSyntax) **   <a name="WorkSpaces-DescribeConnectionAliasPermissions-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [NextToken](#API_DescribeConnectionAliasPermissions_RequestSyntax) **   <a name="WorkSpaces-DescribeConnectionAliasPermissions-request-NextToken"></a>
If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_DescribeConnectionAliasPermissions_ResponseSyntax"></a>

```
{
   "AliasId": "string",
   "ConnectionAliasPermissions": [
      {
         "AllowAssociation": boolean,
         "SharedAccountId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeConnectionAliasPermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AliasId](#API_DescribeConnectionAliasPermissions_ResponseSyntax) **   <a name="WorkSpaces-DescribeConnectionAliasPermissions-response-AliasId"></a>
The identifier of the connection alias.
Type: String
Length Constraints: Minimum length of 13. Maximum length of 68.
Pattern: `^wsca-[0-9a-z]{8,63}$`

 ** [ConnectionAliasPermissions](#API_DescribeConnectionAliasPermissions_ResponseSyntax) **   <a name="WorkSpaces-DescribeConnectionAliasPermissions-response-ConnectionAliasPermissions"></a>
The permissions associated with a connection alias.
Type: Array of [ConnectionAliasPermission](API_ConnectionAliasPermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.

 ** [NextToken](#API_DescribeConnectionAliasPermissions_ResponseSyntax) **   <a name="WorkSpaces-DescribeConnectionAliasPermissions-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_DescribeConnectionAliasPermissions_Errors"></a>

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
<a name="API_DescribeConnectionAliasPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeConnectionAliasPermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeConnectionAliasPermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeConnectionAliasPermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeConnectionAliasPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeConnectionAliasPermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeConnectionAliasPermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeConnectionAliasPermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeConnectionAliasPermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeConnectionAliasPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeConnectionAliasPermissions)
