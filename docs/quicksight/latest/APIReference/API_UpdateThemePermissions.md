---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateThemePermissions.html
---

# UpdateThemePermissions
<a name="API_UpdateThemePermissions"></a>

Updates the resource permissions for a theme. Permissions apply to the action to grant or revoke permissions on, for example `"quicksight:DescribeTheme"`.

Theme permissions apply in groupings. Valid groupings include the following for the three levels of permissions, which are user, owner, or no permissions:
+ User
  +  `"quicksight:DescribeTheme"`
  +  `"quicksight:DescribeThemeAlias"`
  +  `"quicksight:ListThemeAliases"`
  +  `"quicksight:ListThemeVersions"`
+ Owner
  +  `"quicksight:DescribeTheme"`
  +  `"quicksight:DescribeThemeAlias"`
  +  `"quicksight:ListThemeAliases"`
  +  `"quicksight:ListThemeVersions"`
  +  `"quicksight:DeleteTheme"`
  +  `"quicksight:UpdateTheme"`
  +  `"quicksight:CreateThemeAlias"`
  +  `"quicksight:DeleteThemeAlias"`
  +  `"quicksight:UpdateThemeAlias"`
  +  `"quicksight:UpdateThemePermissions"`
  +  `"quicksight:DescribeThemePermissions"`
+ To specify no permissions, omit the permissions list.

## Request Syntax
<a name="API_UpdateThemePermissions_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/themes/{{ThemeId}}/permissions HTTP/1.1
Content-type: application/json

{
   "GrantPermissions": [
      {
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ],
   "RevokePermissions": [
      {
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateThemePermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateThemePermissions_RequestSyntax) **   <a name="QS-UpdateThemePermissions-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the theme.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [ThemeId](#API_UpdateThemePermissions_RequestSyntax) **   <a name="QS-UpdateThemePermissions-request-uri-ThemeId"></a>
The ID for the theme.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

## Request Body
<a name="API_UpdateThemePermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GrantPermissions](#API_UpdateThemePermissions_RequestSyntax) **   <a name="QS-UpdateThemePermissions-request-GrantPermissions"></a>
A list of resource permissions to be granted for the theme.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** [RevokePermissions](#API_UpdateThemePermissions_RequestSyntax) **   <a name="QS-UpdateThemePermissions-request-RevokePermissions"></a>
A list of resource permissions to be revoked from the theme.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Maximum number of 100 items.
Required: No

## Response Syntax
<a name="API_UpdateThemePermissions_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Permissions": [
      {
         "Actions": [ "string" ],
         "Principal": "string"
      }
   ],
   "RequestId": "string",
   "ThemeArn": "string",
   "ThemeId": "string"
}
```

## Response Elements
<a name="API_UpdateThemePermissions_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateThemePermissions_ResponseSyntax) **   <a name="QS-UpdateThemePermissions-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Permissions](#API_UpdateThemePermissions_ResponseSyntax) **   <a name="QS-UpdateThemePermissions-response-Permissions"></a>
The resulting list of resource permissions for the theme.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Maximum number of 100 items.

 ** [RequestId](#API_UpdateThemePermissions_ResponseSyntax) **   <a name="QS-UpdateThemePermissions-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [ThemeArn](#API_UpdateThemePermissions_ResponseSyntax) **   <a name="QS-UpdateThemePermissions-response-ThemeArn"></a>
The Amazon Resource Name (ARN) of the theme.
Type: String

 ** [ThemeId](#API_UpdateThemePermissions_ResponseSyntax) **   <a name="QS-UpdateThemePermissions-response-ThemeId"></a>
The ID for the theme.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`

## Errors
<a name="API_UpdateThemePermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_UpdateThemePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateThemePermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateThemePermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateThemePermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateThemePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateThemePermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateThemePermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateThemePermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateThemePermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateThemePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateThemePermissions)
