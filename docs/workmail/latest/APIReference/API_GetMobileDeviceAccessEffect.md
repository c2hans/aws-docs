---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetMobileDeviceAccessEffect.html
---

# GetMobileDeviceAccessEffect
<a name="API_GetMobileDeviceAccessEffect"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Simulates the effect of the mobile device access rules for the given attributes of a sample access event. Use this method to test the effects of the current set of mobile device access rules for the WorkMail organization for a particular user's attributes.

## Request Syntax
<a name="API_GetMobileDeviceAccessEffect_RequestSyntax"></a>

```
{
   "DeviceModel": "{{string}}",
   "DeviceOperatingSystem": "{{string}}",
   "DeviceType": "{{string}}",
   "DeviceUserAgent": "{{string}}",
   "OrganizationId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMobileDeviceAccessEffect_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeviceModel](#API_GetMobileDeviceAccessEffect_RequestSyntax) **   <a name="workmail-GetMobileDeviceAccessEffect-request-DeviceModel"></a>
Device model the simulated user will report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [DeviceOperatingSystem](#API_GetMobileDeviceAccessEffect_RequestSyntax) **   <a name="workmail-GetMobileDeviceAccessEffect-request-DeviceOperatingSystem"></a>
Device operating system the simulated user will report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [DeviceType](#API_GetMobileDeviceAccessEffect_RequestSyntax) **   <a name="workmail-GetMobileDeviceAccessEffect-request-DeviceType"></a>
Device type the simulated user will report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [DeviceUserAgent](#API_GetMobileDeviceAccessEffect_RequestSyntax) **   <a name="workmail-GetMobileDeviceAccessEffect-request-DeviceUserAgent"></a>
Device user agent the simulated user will report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [OrganizationId](#API_GetMobileDeviceAccessEffect_RequestSyntax) **   <a name="workmail-GetMobileDeviceAccessEffect-request-OrganizationId"></a>
The WorkMail organization to simulate the access effect for.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

## Response Syntax
<a name="API_GetMobileDeviceAccessEffect_ResponseSyntax"></a>

```
{
   "Effect": "string",
   "MatchedRules": [
      {
         "MobileDeviceAccessRuleId": "string",
         "Name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetMobileDeviceAccessEffect_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Effect](#API_GetMobileDeviceAccessEffect_ResponseSyntax) **   <a name="workmail-GetMobileDeviceAccessEffect-response-Effect"></a>
The effect of the simulated access, `ALLOW` or `DENY`, after evaluating mobile device access rules in the WorkMail organization for the simulated user parameters.
Type: String
Valid Values: `ALLOW | DENY`

 ** [MatchedRules](#API_GetMobileDeviceAccessEffect_ResponseSyntax) **   <a name="workmail-GetMobileDeviceAccessEffect-response-MatchedRules"></a>
A list of the rules which matched the simulated user input and produced the effect.
Type: Array of [MobileDeviceAccessMatchedRule](API_MobileDeviceAccessMatchedRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

## Errors
<a name="API_GetMobileDeviceAccessEffect_Errors"></a>

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

## See Also
<a name="API_GetMobileDeviceAccessEffect_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/GetMobileDeviceAccessEffect)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/GetMobileDeviceAccessEffect)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/GetMobileDeviceAccessEffect)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/GetMobileDeviceAccessEffect)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/GetMobileDeviceAccessEffect)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/GetMobileDeviceAccessEffect)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/GetMobileDeviceAccessEffect)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/GetMobileDeviceAccessEffect)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/GetMobileDeviceAccessEffect)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/GetMobileDeviceAccessEffect)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
