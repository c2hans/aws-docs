---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_UpdateImpersonationRole.html
---

# UpdateImpersonationRole
<a name="API_UpdateImpersonationRole"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Updates an impersonation role for the given WorkMail organization.

## Request Syntax
<a name="API_UpdateImpersonationRole_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "ImpersonationRoleId": "{{string}}",
   "Name": "{{string}}",
   "OrganizationId": "{{string}}",
   "Rules": [
      {
         "Description": "{{string}}",
         "Effect": "{{string}}",
         "ImpersonationRuleId": "{{string}}",
         "Name": "{{string}}",
         "NotTargetUsers": [ "{{string}}" ],
         "TargetUsers": [ "{{string}}" ]
      }
   ],
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateImpersonationRole_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateImpersonationRole_RequestSyntax) **   <a name="workmail-UpdateImpersonationRole-request-Description"></a>
The updated impersonation role description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\x00-\x09\x0B\x0C\x0E-\x1F\x7F\x3C\x3E\x5C]+`
Required: No

 ** [ImpersonationRoleId](#API_UpdateImpersonationRole_RequestSyntax) **   <a name="workmail-UpdateImpersonationRole-request-ImpersonationRoleId"></a>
The ID of the impersonation role to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [Name](#API_UpdateImpersonationRole_RequestSyntax) **   <a name="workmail-UpdateImpersonationRole-request-Name"></a>
The updated impersonation role name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^\x00-\x1F\x7F\x3C\x3E\x5C]+`
Required: Yes

 ** [OrganizationId](#API_UpdateImpersonationRole_RequestSyntax) **   <a name="workmail-UpdateImpersonationRole-request-OrganizationId"></a>
The WorkMail organization that contains the impersonation role to update.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

 ** [Rules](#API_UpdateImpersonationRole_RequestSyntax) **   <a name="workmail-UpdateImpersonationRole-request-Rules"></a>
The updated list of rules.
Type: Array of [ImpersonationRule](API_ImpersonationRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 ** [Type](#API_UpdateImpersonationRole_RequestSyntax) **   <a name="workmail-UpdateImpersonationRole-request-Type"></a>
The updated impersonation role type.
Type: String
Valid Values: `FULL_ACCESS | READ_ONLY`
Required: Yes

## Response Elements
<a name="API_UpdateImpersonationRole_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateImpersonationRole_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The identifier supplied for the user, group, or resource does not exist in your organization.
HTTP Status Code: 400

 ** EntityStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
You are performing an operation on a user, group, or resource that isn't in the expected state, such as trying to delete an active user.
HTTP Status Code: 400

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** LimitExceededException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The request exceeds the limit of the resource.
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
<a name="API_UpdateImpersonationRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/UpdateImpersonationRole)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/UpdateImpersonationRole)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/UpdateImpersonationRole)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/UpdateImpersonationRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/UpdateImpersonationRole)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/UpdateImpersonationRole)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/UpdateImpersonationRole)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/UpdateImpersonationRole)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/UpdateImpersonationRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/UpdateImpersonationRole)
