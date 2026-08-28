---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeGroup.html
---

# DescribeGroup
<a name="API_DescribeGroup"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Returns the data available for the group.

## Request Syntax
<a name="API_DescribeGroup_RequestSyntax"></a>

```
{
   "GroupId": "{{string}}",
   "OrganizationId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GroupId](#API_DescribeGroup_RequestSyntax) **   <a name="workmail-DescribeGroup-request-GroupId"></a>
The identifier for the group to be described.
The identifier can accept *GroupId*, *Groupname*, or *email*. The following identity formats are available:
+ Group ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234
+ Email address: group@domain.tld
+ Group name: group
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9._%+@-]+`
Required: Yes

 ** [OrganizationId](#API_DescribeGroup_RequestSyntax) **   <a name="workmail-DescribeGroup-request-OrganizationId"></a>
The identifier for the organization under which the group exists.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

## Response Syntax
<a name="API_DescribeGroup_ResponseSyntax"></a>

```
{
   "DisabledDate": number,
   "Email": "string",
   "EnabledDate": number,
   "GroupId": "string",
   "HiddenFromGlobalAddressList": boolean,
   "Name": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_DescribeGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DisabledDate](#API_DescribeGroup_ResponseSyntax) **   <a name="workmail-DescribeGroup-response-DisabledDate"></a>
The date and time when a user was deregistered from WorkMail, in UNIX epoch time format.
Type: Timestamp

 ** [Email](#API_DescribeGroup_ResponseSyntax) **   <a name="workmail-DescribeGroup-response-Email"></a>
The email of the described group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Pattern: `[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]+\.[a-zA-Z-]{2,}`

 ** [EnabledDate](#API_DescribeGroup_ResponseSyntax) **   <a name="workmail-DescribeGroup-response-EnabledDate"></a>
The date and time when a user was registered to WorkMail, in UNIX epoch time format.
Type: Timestamp

 ** [GroupId](#API_DescribeGroup_ResponseSyntax) **   <a name="workmail-DescribeGroup-response-GroupId"></a>
The identifier of the described group.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 256.

 ** [HiddenFromGlobalAddressList](#API_DescribeGroup_ResponseSyntax) **   <a name="workmail-DescribeGroup-response-HiddenFromGlobalAddressList"></a>
If the value is set to *true*, the group is hidden from the address book.
Type: Boolean

 ** [Name](#API_DescribeGroup_ResponseSyntax) **   <a name="workmail-DescribeGroup-response-Name"></a>
The name of the described group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`

 ** [State](#API_DescribeGroup_ResponseSyntax) **   <a name="workmail-DescribeGroup-response-State"></a>
The state of the user: enabled (registered to WorkMail) or disabled (deregistered or never registered to WorkMail).
Type: String
Valid Values: `ENABLED | DISABLED | DELETED`

## Errors
<a name="API_DescribeGroup_Errors"></a>

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
<a name="API_DescribeGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/DescribeGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/DescribeGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/DescribeGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/DescribeGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/DescribeGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/DescribeGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/DescribeGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/DescribeGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/DescribeGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/DescribeGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
