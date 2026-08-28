---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteOrganizationConfigRule.html
---

# DeleteOrganizationConfigRule
<a name="API_DeleteOrganizationConfigRule"></a>

Deletes the specified organization AWS Config rule and all of its evaluation results from all member accounts in that organization.

Only a management account and a delegated administrator account can delete an organization AWS Config rule. When calling this API with a delegated administrator, you must ensure AWS Organizations `ListDelegatedAdministrator` permissions are added.

 AWS Config sets the state of a rule to DELETE\_IN\_PROGRESS until the deletion is complete. You cannot update a rule while it is in this state.

**Note**
 **Recommendation: Consider excluding the `AWS::Config::ResourceCompliance` resource type from recording before deleting rules**
Deleting rules creates configuration items (CIs) for `AWS::Config::ResourceCompliance` that can affect your costs for the configuration recorder. If you are deleting rules which evaluate a large number of resource types, this can lead to a spike in the number of CIs recorded.
To avoid the associated costs, you can opt to disable recording for the `AWS::Config::ResourceCompliance` resource type before deleting rules, and re-enable recording after the rules have been deleted.
However, since deleting rules is an asynchronous process, it might take an hour or more to complete. During the time when recording is disabled for `AWS::Config::ResourceCompliance`, rule evaluations will not be recorded in the associated resource’s history.

## Request Syntax
<a name="API_DeleteOrganizationConfigRule_RequestSyntax"></a>

```
{
   "OrganizationConfigRuleName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteOrganizationConfigRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OrganizationConfigRuleName](#API_DeleteOrganizationConfigRule_RequestSyntax) **   <a name="config-DeleteOrganizationConfigRule-request-OrganizationConfigRuleName"></a>
The name of organization AWS Config rule that you want to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: Yes

## Response Elements
<a name="API_DeleteOrganizationConfigRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteOrganizationConfigRule_Errors"></a>

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

 ** ResourceInUseException **
You see this exception in the following cases:
+ For DeleteConfigRule, AWS Config is deleting this rule. Try your request again later.
+ For DeleteConfigRule, the rule is deleting your evaluation results. Try your request again later.
+ For DeleteConfigRule, a remediation action is associated with the rule and AWS Config cannot delete this rule. Delete the remediation action associated with the rule before deleting the rule and try your request again later.
+ For PutConfigOrganizationRule, organization AWS Config rule deletion is in progress. Try your request again later.
+ For DeleteOrganizationConfigRule, organization AWS Config rule creation is in progress. Try your request again later.
+ For PutConformancePack and PutOrganizationConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.
+ For DeleteConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.
HTTP Status Code: 400

## See Also
<a name="API_DeleteOrganizationConfigRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DeleteOrganizationConfigRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DeleteOrganizationConfigRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DeleteOrganizationConfigRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DeleteOrganizationConfigRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DeleteOrganizationConfigRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DeleteOrganizationConfigRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DeleteOrganizationConfigRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DeleteOrganizationConfigRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DeleteOrganizationConfigRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DeleteOrganizationConfigRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
