---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListMobileDeviceAccessRules.html
---

# ListMobileDeviceAccessRules
<a name="API_ListMobileDeviceAccessRules"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Lists the mobile device access rules for the specified WorkMail organization.

## Request Syntax
<a name="API_ListMobileDeviceAccessRules_RequestSyntax"></a>

```
{
   "OrganizationId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListMobileDeviceAccessRules_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OrganizationId](#API_ListMobileDeviceAccessRules_RequestSyntax) **   <a name="workmail-ListMobileDeviceAccessRules-request-OrganizationId"></a>
The WorkMail organization for which to list the rules.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

## Response Syntax
<a name="API_ListMobileDeviceAccessRules_ResponseSyntax"></a>

```
{
   "Rules": [
      {
         "DateCreated": number,
         "DateModified": number,
         "Description": "string",
         "DeviceModels": [ "string" ],
         "DeviceOperatingSystems": [ "string" ],
         "DeviceTypes": [ "string" ],
         "DeviceUserAgents": [ "string" ],
         "Effect": "string",
         "MobileDeviceAccessRuleId": "string",
         "Name": "string",
         "NotDeviceModels": [ "string" ],
         "NotDeviceOperatingSystems": [ "string" ],
         "NotDeviceTypes": [ "string" ],
         "NotDeviceUserAgents": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_ListMobileDeviceAccessRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Rules](#API_ListMobileDeviceAccessRules_ResponseSyntax) **   <a name="workmail-ListMobileDeviceAccessRules-response-Rules"></a>
The list of mobile device access rules that exist under the specified WorkMail organization.
Type: Array of [MobileDeviceAccessRule](API_MobileDeviceAccessRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

## Errors
<a name="API_ListMobileDeviceAccessRules_Errors"></a>

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
<a name="API_ListMobileDeviceAccessRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/ListMobileDeviceAccessRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/ListMobileDeviceAccessRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/ListMobileDeviceAccessRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/ListMobileDeviceAccessRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/ListMobileDeviceAccessRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/ListMobileDeviceAccessRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/ListMobileDeviceAccessRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/ListMobileDeviceAccessRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/ListMobileDeviceAccessRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/ListMobileDeviceAccessRules)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
