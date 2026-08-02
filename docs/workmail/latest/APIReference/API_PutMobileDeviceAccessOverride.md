---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_PutMobileDeviceAccessOverride.html
---

# PutMobileDeviceAccessOverride
<a name="API_PutMobileDeviceAccessOverride"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Creates or updates a mobile device access override for the given WorkMail organization, user, and device.

## Request Syntax
<a name="API_PutMobileDeviceAccessOverride_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "DeviceId": "{{string}}",
   "Effect": "{{string}}",
   "OrganizationId": "{{string}}",
   "UserId": "{{string}}"
}
```

## Request Parameters
<a name="API_PutMobileDeviceAccessOverride_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_PutMobileDeviceAccessOverride_RequestSyntax) **   <a name="workmail-PutMobileDeviceAccessOverride-request-Description"></a>
A description of the override.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S\s]+`
Required: No

 ** [DeviceId](#API_PutMobileDeviceAccessOverride_RequestSyntax) **   <a name="workmail-PutMobileDeviceAccessOverride-request-DeviceId"></a>
The mobile device for which you create the override. `DeviceId` is case insensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[A-Za-z0-9]+`
Required: Yes

 ** [Effect](#API_PutMobileDeviceAccessOverride_RequestSyntax) **   <a name="workmail-PutMobileDeviceAccessOverride-request-Effect"></a>
The effect of the override, `ALLOW` or `DENY`.
Type: String
Valid Values: `ALLOW | DENY`
Required: Yes

 ** [OrganizationId](#API_PutMobileDeviceAccessOverride_RequestSyntax) **   <a name="workmail-PutMobileDeviceAccessOverride-request-OrganizationId"></a>
Identifies the WorkMail organization for which you create the override.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

 ** [UserId](#API_PutMobileDeviceAccessOverride_RequestSyntax) **   <a name="workmail-PutMobileDeviceAccessOverride-request-UserId"></a>
The WorkMail user for which you create the override. Accepts the following types of user identities:
+ User ID: `12345678-1234-1234-1234-123456789012` or `S-1-1-12-1234567890-123456789-123456789-1234`
+ Email address: `user@domain.tld`
+ User name: `user`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9._%+@-]+`
Required: Yes

## Response Elements
<a name="API_PutMobileDeviceAccessOverride_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutMobileDeviceAccessOverride_Errors"></a>

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

## See Also
<a name="API_PutMobileDeviceAccessOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/PutMobileDeviceAccessOverride)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/PutMobileDeviceAccessOverride)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/PutMobileDeviceAccessOverride)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/PutMobileDeviceAccessOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/PutMobileDeviceAccessOverride)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/PutMobileDeviceAccessOverride)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/PutMobileDeviceAccessOverride)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/PutMobileDeviceAccessOverride)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/PutMobileDeviceAccessOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/PutMobileDeviceAccessOverride)
