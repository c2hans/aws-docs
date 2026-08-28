---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateRuleSet.html
---

# CreateRuleSet
<a name="API_CreateRuleSet"></a>

Provision a new rule set.

## Request Syntax
<a name="API_CreateRuleSet_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
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
   "RuleSetName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateRuleSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateRuleSet_RequestSyntax) **   <a name="sesmailmanager-CreateRuleSet-request-ClientToken"></a>
A unique token that Amazon SES uses to recognize subsequent retries of the same request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Rules](#API_CreateRuleSet_RequestSyntax) **   <a name="sesmailmanager-CreateRuleSet-request-Rules"></a>
Conditional rules that are evaluated for determining actions on email.
Type: Array of [Rule](API_Rule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 40 items.
Required: Yes

 ** [RuleSetName](#API_CreateRuleSet_RequestSyntax) **   <a name="sesmailmanager-CreateRuleSet-request-RuleSetName"></a>
A user-friendly name for the rule set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [Tags](#API_CreateRuleSet_RequestSyntax) **   <a name="sesmailmanager-CreateRuleSet-request-Tags"></a>
The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateRuleSet_ResponseSyntax"></a>

```
{
   "RuleSetId": "string"
}
```

## Response Elements
<a name="API_CreateRuleSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RuleSetId](#API_CreateRuleSet_ResponseSyntax) **   <a name="sesmailmanager-CreateRuleSet-response-RuleSetId"></a>
The identifier of the created rule set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

## Errors
<a name="API_CreateRuleSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
Occurs when an operation exceeds a predefined service quota or limit.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_CreateRuleSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/CreateRuleSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/CreateRuleSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/CreateRuleSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/CreateRuleSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/CreateRuleSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/CreateRuleSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/CreateRuleSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/CreateRuleSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/CreateRuleSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/CreateRuleSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
