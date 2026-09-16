---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetImpersonationRole.html
---

# GetImpersonationRole
<a name="API_GetImpersonationRole"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Gets the impersonation role details for the given WorkMail organization.

## Request Syntax
<a name="API_GetImpersonationRole_RequestSyntax"></a>

```
{
   "ImpersonationRoleId": "{{string}}",
   "OrganizationId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetImpersonationRole_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ImpersonationRoleId](#API_GetImpersonationRole_RequestSyntax) **   <a name="workmail-GetImpersonationRole-request-ImpersonationRoleId"></a>
The impersonation role ID to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [OrganizationId](#API_GetImpersonationRole_RequestSyntax) **   <a name="workmail-GetImpersonationRole-request-OrganizationId"></a>
The WorkMail organization from which to retrieve the impersonation role.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

## Response Syntax
<a name="API_GetImpersonationRole_ResponseSyntax"></a>

```
{
   "DateCreated": number,
   "DateModified": number,
   "Description": "string",
   "ImpersonationRoleId": "string",
   "Name": "string",
   "Rules": [
      {
         "Description": "string",
         "Effect": "string",
         "ImpersonationRuleId": "string",
         "Name": "string",
         "NotTargetUsers": [ "string" ],
         "TargetUsers": [ "string" ]
      }
   ],
   "Type": "string"
}
```

## Response Elements
<a name="API_GetImpersonationRole_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DateCreated](#API_GetImpersonationRole_ResponseSyntax) **   <a name="workmail-GetImpersonationRole-response-DateCreated"></a>
The date when the impersonation role was created.
Type: Timestamp

 ** [DateModified](#API_GetImpersonationRole_ResponseSyntax) **   <a name="workmail-GetImpersonationRole-response-DateModified"></a>
The date when the impersonation role was last modified.
Type: Timestamp

 ** [Description](#API_GetImpersonationRole_ResponseSyntax) **   <a name="workmail-GetImpersonationRole-response-Description"></a>
The impersonation role description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\x00-\x09\x0B\x0C\x0E-\x1F\x7F\x3C\x3E\x5C]+`

 ** [ImpersonationRoleId](#API_GetImpersonationRole_ResponseSyntax) **   <a name="workmail-GetImpersonationRole-response-ImpersonationRoleId"></a>
The impersonation role ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [Name](#API_GetImpersonationRole_ResponseSyntax) **   <a name="workmail-GetImpersonationRole-response-Name"></a>
The impersonation role name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^\x00-\x1F\x7F\x3C\x3E\x5C]+`

 ** [Rules](#API_GetImpersonationRole_ResponseSyntax) **   <a name="workmail-GetImpersonationRole-response-Rules"></a>
The list of rules for the given impersonation role.
Type: Array of [ImpersonationRule](API_ImpersonationRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [Type](#API_GetImpersonationRole_ResponseSyntax) **   <a name="workmail-GetImpersonationRole-response-Type"></a>
The impersonation role type.
Type: String
Valid Values: `FULL_ACCESS | READ_ONLY`

## Errors
<a name="API_GetImpersonationRole_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** OrganizationNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
An operation received a valid organization identifier that either doesn't belong or exist in the system.
HTTP Status Code: 400

 ** OrganizationStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The organization must have a valid state to perform certain operations on the organization or its members.
HTTP Status Code: 400

 ** ResourceNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_GetImpersonationRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/GetImpersonationRole)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/GetImpersonationRole)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/GetImpersonationRole)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/GetImpersonationRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/GetImpersonationRole)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/GetImpersonationRole)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/GetImpersonationRole)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/GetImpersonationRole)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/GetImpersonationRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/GetImpersonationRole)
