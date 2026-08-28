---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListMobileDeviceAccessOverrides.html
---

# ListMobileDeviceAccessOverrides
<a name="API_ListMobileDeviceAccessOverrides"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Lists all the mobile device access overrides for any given combination of WorkMail organization, user, or device.

## Request Syntax
<a name="API_ListMobileDeviceAccessOverrides_RequestSyntax"></a>

```
{
   "DeviceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OrganizationId": "{{string}}",
   "UserId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListMobileDeviceAccessOverrides_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeviceId](#API_ListMobileDeviceAccessOverrides_RequestSyntax) **   <a name="workmail-ListMobileDeviceAccessOverrides-request-DeviceId"></a>
The mobile device to which the access override applies.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[A-Za-z0-9]+`
Required: No

 ** [MaxResults](#API_ListMobileDeviceAccessOverrides_RequestSyntax) **   <a name="workmail-ListMobileDeviceAccessOverrides-request-MaxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListMobileDeviceAccessOverrides_RequestSyntax) **   <a name="workmail-ListMobileDeviceAccessOverrides-request-NextToken"></a>
The token to use to retrieve the next page of results. The first call does not require a token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S\s]*|[a-zA-Z0-9/+=]{1,1024}`
Required: No

 ** [OrganizationId](#API_ListMobileDeviceAccessOverrides_RequestSyntax) **   <a name="workmail-ListMobileDeviceAccessOverrides-request-OrganizationId"></a>
The WorkMail organization under which to list mobile device access overrides.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

 ** [UserId](#API_ListMobileDeviceAccessOverrides_RequestSyntax) **   <a name="workmail-ListMobileDeviceAccessOverrides-request-UserId"></a>
The WorkMail user under which you list the mobile device access overrides. Accepts the following types of user identities:
+ User ID: `12345678-1234-1234-1234-123456789012` or `S-1-1-12-1234567890-123456789-123456789-1234`
+ Email address: `user@domain.tld`
+ User name: `user`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9._%+@-]+`
Required: No

## Response Syntax
<a name="API_ListMobileDeviceAccessOverrides_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Overrides": [
      {
         "DateCreated": number,
         "DateModified": number,
         "Description": "string",
         "DeviceId": "string",
         "Effect": "string",
         "UserId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListMobileDeviceAccessOverrides_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListMobileDeviceAccessOverrides_ResponseSyntax) **   <a name="workmail-ListMobileDeviceAccessOverrides-response-NextToken"></a>
The token to use to retrieve the next page of results. The value is “null” when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S\s]*|[a-zA-Z0-9/+=]{1,1024}`

 ** [Overrides](#API_ListMobileDeviceAccessOverrides_ResponseSyntax) **   <a name="workmail-ListMobileDeviceAccessOverrides-response-Overrides"></a>
The list of mobile device access overrides that exist for the specified WorkMail organization and user.
Type: Array of [MobileDeviceAccessOverride](API_MobileDeviceAccessOverride.md) objects

## Errors
<a name="API_ListMobileDeviceAccessOverrides_Errors"></a>

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
<a name="API_ListMobileDeviceAccessOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/ListMobileDeviceAccessOverrides)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/ListMobileDeviceAccessOverrides)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/ListMobileDeviceAccessOverrides)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/ListMobileDeviceAccessOverrides)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/ListMobileDeviceAccessOverrides)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/ListMobileDeviceAccessOverrides)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/ListMobileDeviceAccessOverrides)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/ListMobileDeviceAccessOverrides)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/ListMobileDeviceAccessOverrides)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/ListMobileDeviceAccessOverrides)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
