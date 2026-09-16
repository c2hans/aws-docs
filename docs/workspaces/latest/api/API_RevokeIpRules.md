---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_RevokeIpRules.html
---

# RevokeIpRules
<a name="API_RevokeIpRules"></a>

Removes one or more rules from the specified IP access control group.

## Request Syntax
<a name="API_RevokeIpRules_RequestSyntax"></a>

```
{
   "GroupId": "{{string}}",
   "UserRules": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_RevokeIpRules_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [GroupId](#API_RevokeIpRules_RequestSyntax) **   <a name="WorkSpaces-RevokeIpRules-request-GroupId"></a>
The identifier of the group.
Type: String
Pattern: `wsipg-[0-9a-z]{8,63}$`
Required: Yes

 ** [UserRules](#API_RevokeIpRules_RequestSyntax) **   <a name="WorkSpaces-RevokeIpRules-request-UserRules"></a>
The rules to remove from the group.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_RevokeIpRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RevokeIpRules_Errors"></a>

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

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_RevokeIpRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/RevokeIpRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/RevokeIpRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/RevokeIpRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/RevokeIpRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/RevokeIpRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/RevokeIpRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/RevokeIpRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/RevokeIpRules)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/RevokeIpRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/RevokeIpRules)
