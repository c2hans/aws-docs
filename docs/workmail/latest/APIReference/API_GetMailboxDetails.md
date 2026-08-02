---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetMailboxDetails.html
---

# GetMailboxDetails
<a name="API_GetMailboxDetails"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Requests a user's mailbox details for a specified organization and user.

## Request Syntax
<a name="API_GetMailboxDetails_RequestSyntax"></a>

```
{
   "OrganizationId": "{{string}}",
   "UserId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMailboxDetails_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OrganizationId](#API_GetMailboxDetails_RequestSyntax) **   <a name="workmail-GetMailboxDetails-request-OrganizationId"></a>
The identifier for the organization that contains the user whose mailbox details are being requested.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

 ** [UserId](#API_GetMailboxDetails_RequestSyntax) **   <a name="workmail-GetMailboxDetails-request-UserId"></a>
The identifier for the user whose mailbox details are being requested.
The identifier can be the *UserId*, *Username*, or *email*. The following identity formats are available:
+ User ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234
+ Email address: user@domain.tld
+ User name: user
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9._%+@-]+`
Required: Yes

## Response Syntax
<a name="API_GetMailboxDetails_ResponseSyntax"></a>

```
{
   "MailboxQuota": number,
   "MailboxSize": number
}
```

## Response Elements
<a name="API_GetMailboxDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MailboxQuota](#API_GetMailboxDetails_ResponseSyntax) **   <a name="workmail-GetMailboxDetails-response-MailboxQuota"></a>
The maximum allowed mailbox size, in MB, for the specified user.
Type: Integer
Valid Range: Minimum value of 1.

 ** [MailboxSize](#API_GetMailboxDetails_ResponseSyntax) **   <a name="workmail-GetMailboxDetails-response-MailboxSize"></a>
The current mailbox size, in MB, for the specified user.
Type: Double
Valid Range: Minimum value of 0.

## Errors
<a name="API_GetMailboxDetails_Errors"></a>

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

## See Also
<a name="API_GetMailboxDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/GetMailboxDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/GetMailboxDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/GetMailboxDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/GetMailboxDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/GetMailboxDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/GetMailboxDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/GetMailboxDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/GetMailboxDetails)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/GetMailboxDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/GetMailboxDetails)
