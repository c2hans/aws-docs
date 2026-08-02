---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_GetOrganizationCustomRulePolicy.html
---

# GetOrganizationCustomRulePolicy
<a name="API_GetOrganizationCustomRulePolicy"></a>

Returns the policy definition containing the logic for your organization AWS Config Custom Policy rule.

## Request Syntax
<a name="API_GetOrganizationCustomRulePolicy_RequestSyntax"></a>

```
{
   "OrganizationConfigRuleName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetOrganizationCustomRulePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OrganizationConfigRuleName](#API_GetOrganizationCustomRulePolicy_RequestSyntax) **   <a name="config-GetOrganizationCustomRulePolicy-request-OrganizationConfigRuleName"></a>
The name of your organization AWS Config Custom Policy rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: Yes

## Response Syntax
<a name="API_GetOrganizationCustomRulePolicy_ResponseSyntax"></a>

```
{
   "PolicyText": "string"
}
```

## Response Elements
<a name="API_GetOrganizationCustomRulePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PolicyText](#API_GetOrganizationCustomRulePolicy_ResponseSyntax) **   <a name="config-GetOrganizationCustomRulePolicy-response-PolicyText"></a>
The policy definition containing the logic for your organization AWS Config Custom Policy rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.

## Errors
<a name="API_GetOrganizationCustomRulePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchOrganizationConfigRuleException **
The AWS Config rule in the request is not valid. Verify that the rule is an organization AWS Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.
HTTP Status Code: 400

 ** OrganizationAccessDeniedException **
For `PutConfigurationAggregator` API, you can see this exception for the following reasons:
+ No permission to call `EnableAWSServiceAccess` API
+ The configuration aggregator cannot be updated because your AWS Organization management account or the delegated administrator role changed. Delete this aggregator and create a new one with the current AWS Organization.
+ The configuration aggregator is associated with a previous AWS Organization and AWS Config cannot aggregate data with current AWS Organization. Delete this aggregator and create a new one with the current AWS Organization.
+ You are not a registered delegated administrator for AWS Config with permissions to call `ListDelegatedAdministrators` API. Ensure that the management account registers delagated administrator for AWS Config service principal name before the delegated administrator creates an aggregator.
For all `OrganizationConfigRule` and `OrganizationConformancePack` APIs, AWS Config throws an exception if APIs are called from member accounts. All APIs must be called from organization management account.
HTTP Status Code: 400

## See Also
<a name="API_GetOrganizationCustomRulePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/GetOrganizationCustomRulePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/GetOrganizationCustomRulePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/GetOrganizationCustomRulePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/GetOrganizationCustomRulePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/GetOrganizationCustomRulePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/GetOrganizationCustomRulePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/GetOrganizationCustomRulePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/GetOrganizationCustomRulePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/GetOrganizationCustomRulePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/GetOrganizationCustomRulePolicy)
