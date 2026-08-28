---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_UpdateRuleSet.html
---

# UpdateRuleSet
<a name="API_UpdateRuleSet"></a>

Update attributes of an already provisioned rule set.

## Request Syntax
<a name="API_UpdateRuleSet_RequestSyntax"></a>

```
{
   "Rules": [
      {
         "Actions": [
            { ... }
         ],
         "Conditions": [
            { ... }
         ],
         "Name": "{{string}}",
         "Unless": [
            { ... }
         ]
      }
   ],
   "RuleSetId": "{{string}}",
   "RuleSetName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateRuleSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Rules](#API_UpdateRuleSet_RequestSyntax) **   <a name="sesmailmanager-UpdateRuleSet-request-Rules"></a>
A new set of rules to replace the current rules of the rule set—these rules will override all the rules of the rule set.
Type: Array of [Rule](API_Rule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 40 items.
Required: No

 ** [RuleSetId](#API_UpdateRuleSet_RequestSyntax) **   <a name="sesmailmanager-UpdateRuleSet-request-RuleSetId"></a>
The identifier of a rule set you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [RuleSetName](#API_UpdateRuleSet_RequestSyntax) **   <a name="sesmailmanager-UpdateRuleSet-request-RuleSetName"></a>
A user-friendly name for the rule set resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Elements
<a name="API_UpdateRuleSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateRuleSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Occurs when a requested resource is not found.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_UpdateRuleSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/UpdateRuleSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/UpdateRuleSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/UpdateRuleSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/UpdateRuleSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/UpdateRuleSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/UpdateRuleSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/UpdateRuleSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/UpdateRuleSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/UpdateRuleSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/UpdateRuleSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
