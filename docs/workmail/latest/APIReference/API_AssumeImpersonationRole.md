---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_AssumeImpersonationRole.html
---

# AssumeImpersonationRole
<a name="API_AssumeImpersonationRole"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Assumes an impersonation role for the given WorkMail organization. This method returns an authentication token you can use to make impersonated calls.

## Request Syntax
<a name="API_AssumeImpersonationRole_RequestSyntax"></a>

```
{
   "ImpersonationRoleId": "{{string}}",
   "OrganizationId": "{{string}}"
}
```

## Request Parameters
<a name="API_AssumeImpersonationRole_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ImpersonationRoleId](#API_AssumeImpersonationRole_RequestSyntax) **   <a name="workmail-AssumeImpersonationRole-request-ImpersonationRoleId"></a>
The impersonation role ID to assume.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [OrganizationId](#API_AssumeImpersonationRole_RequestSyntax) **   <a name="workmail-AssumeImpersonationRole-request-OrganizationId"></a>
The WorkMail organization under which the impersonation role will be assumed.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

## Response Syntax
<a name="API_AssumeImpersonationRole_ResponseSyntax"></a>

```
{
   "ExpiresIn": number,
   "Token": "string"
}
```

## Response Elements
<a name="API_AssumeImpersonationRole_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExpiresIn](#API_AssumeImpersonationRole_ResponseSyntax) **   <a name="workmail-AssumeImpersonationRole-response-ExpiresIn"></a>
The authentication token's validity, in seconds.
Type: Long

 ** [Token](#API_AssumeImpersonationRole_ResponseSyntax) **   <a name="workmail-AssumeImpersonationRole-response-Token"></a>
The authentication token for the impersonation role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\x21-\x7e]+`

## Errors
<a name="API_AssumeImpersonationRole_Errors"></a>

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
<a name="API_AssumeImpersonationRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/AssumeImpersonationRole)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/AssumeImpersonationRole)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/AssumeImpersonationRole)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/AssumeImpersonationRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/AssumeImpersonationRole)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/AssumeImpersonationRole)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/AssumeImpersonationRole)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/AssumeImpersonationRole)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/AssumeImpersonationRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/AssumeImpersonationRole)
