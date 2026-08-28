---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetAccessControlEffect.html
---

# GetAccessControlEffect
<a name="API_GetAccessControlEffect"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Gets the effects of an organization's access control rules as they apply to a specified IPv4 address, access protocol action, and user ID or impersonation role ID. You must provide either the user ID or impersonation role ID. Impersonation role ID can only be used with Action EWS.

## Request Syntax
<a name="API_GetAccessControlEffect_RequestSyntax"></a>

```
{
   "Action": "{{string}}",
   "ImpersonationRoleId": "{{string}}",
   "IpAddress": "{{string}}",
   "OrganizationId": "{{string}}",
   "UserId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAccessControlEffect_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Action](#API_GetAccessControlEffect_RequestSyntax) **   <a name="workmail-GetAccessControlEffect-request-Action"></a>
The access protocol action. Valid values include `ActiveSync`, `AutoDiscover`, `EWS`, `IMAP`, `SMTP`, `WindowsOutlook`, and `WebMail`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [ImpersonationRoleId](#API_GetAccessControlEffect_RequestSyntax) **   <a name="workmail-GetAccessControlEffect-request-ImpersonationRoleId"></a>
The impersonation role ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** [IpAddress](#API_GetAccessControlEffect_RequestSyntax) **   <a name="workmail-GetAccessControlEffect-request-IpAddress"></a>
The IPv4 address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$`
Required: Yes

 ** [OrganizationId](#API_GetAccessControlEffect_RequestSyntax) **   <a name="workmail-GetAccessControlEffect-request-OrganizationId"></a>
The identifier for the organization.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

 ** [UserId](#API_GetAccessControlEffect_RequestSyntax) **   <a name="workmail-GetAccessControlEffect-request-UserId"></a>
The user ID.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_GetAccessControlEffect_ResponseSyntax"></a>

```
{
   "Effect": "string",
   "MatchedRules": [ "string" ]
}
```

## Response Elements
<a name="API_GetAccessControlEffect_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Effect](#API_GetAccessControlEffect_ResponseSyntax) **   <a name="workmail-GetAccessControlEffect-response-Effect"></a>
The rule effect.
Type: String
Valid Values: `ALLOW | DENY`

 ** [MatchedRules](#API_GetAccessControlEffect_ResponseSyntax) **   <a name="workmail-GetAccessControlEffect-response-MatchedRules"></a>
The rules that match the given parameters, resulting in an effect.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

## Errors
<a name="API_GetAccessControlEffect_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The identifier supplied for the user, group, or resource does not exist in your organization.
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
<a name="API_GetAccessControlEffect_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/GetAccessControlEffect)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/GetAccessControlEffect)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/GetAccessControlEffect)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/GetAccessControlEffect)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/GetAccessControlEffect)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/GetAccessControlEffect)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/GetAccessControlEffect)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/GetAccessControlEffect)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/GetAccessControlEffect)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/GetAccessControlEffect)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
