---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetImpersonationRoleEffect.html
---

# GetImpersonationRoleEffect
<a name="API_GetImpersonationRoleEffect"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Tests whether the given impersonation role can impersonate a target user.

## Request Syntax
<a name="API_GetImpersonationRoleEffect_RequestSyntax"></a>

```
{
   "ImpersonationRoleId": "{{string}}",
   "OrganizationId": "{{string}}",
   "TargetUser": "{{string}}"
}
```

## Request Parameters
<a name="API_GetImpersonationRoleEffect_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ImpersonationRoleId](#API_GetImpersonationRoleEffect_RequestSyntax) **   <a name="workmail-GetImpersonationRoleEffect-request-ImpersonationRoleId"></a>
The impersonation role ID to test.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [OrganizationId](#API_GetImpersonationRoleEffect_RequestSyntax) **   <a name="workmail-GetImpersonationRoleEffect-request-OrganizationId"></a>
The WorkMail organization where the impersonation role is defined.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

 ** [TargetUser](#API_GetImpersonationRoleEffect_RequestSyntax) **   <a name="workmail-GetImpersonationRoleEffect-request-TargetUser"></a>
The WorkMail organization user chosen to test the impersonation role. The following identity formats are available:
+ User ID: `12345678-1234-1234-1234-123456789012` or `S-1-1-12-1234567890-123456789-123456789-1234`
+ Email address: `user@domain.tld`
+ User name: `user`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9._%+@-]+`
Required: Yes

## Response Syntax
<a name="API_GetImpersonationRoleEffect_ResponseSyntax"></a>

```
{
   "Effect": "string",
   "MatchedRules": [
      {
         "ImpersonationRuleId": "string",
         "Name": "string"
      }
   ],
   "Type": "string"
}
```

## Response Elements
<a name="API_GetImpersonationRoleEffect_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Effect](#API_GetImpersonationRoleEffect_ResponseSyntax) **   <a name="workmail-GetImpersonationRoleEffect-response-Effect"></a>
 ``Effect of the impersonation role on the target user based on its rules. Available effects are `ALLOW` or `DENY`.
Type: String
Valid Values: `ALLOW | DENY`

 ** [MatchedRules](#API_GetImpersonationRoleEffect_ResponseSyntax) **   <a name="workmail-GetImpersonationRoleEffect-response-MatchedRules"></a>
A list of the rules that match the input and produce the configured effect.
Type: Array of [ImpersonationMatchedRule](API_ImpersonationMatchedRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [Type](#API_GetImpersonationRoleEffect_ResponseSyntax) **   <a name="workmail-GetImpersonationRoleEffect-response-Type"></a>
The impersonation role type.
Type: String
Valid Values: `FULL_ACCESS | READ_ONLY`

## Errors
<a name="API_GetImpersonationRoleEffect_Errors"></a>

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
<a name="API_GetImpersonationRoleEffect_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/GetImpersonationRoleEffect)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/GetImpersonationRoleEffect)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/GetImpersonationRoleEffect)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/GetImpersonationRoleEffect)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/GetImpersonationRoleEffect)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/GetImpersonationRoleEffect)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/GetImpersonationRoleEffect)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/GetImpersonationRoleEffect)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/GetImpersonationRoleEffect)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/GetImpersonationRoleEffect)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
