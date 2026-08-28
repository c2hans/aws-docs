---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetRuleSet.html
---

# GetRuleSet
<a name="API_GetRuleSet"></a>

Fetch attributes of a rule set.

## Request Syntax
<a name="API_GetRuleSet_RequestSyntax"></a>

```
{
   "RuleSetId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetRuleSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RuleSetId](#API_GetRuleSet_RequestSyntax) **   <a name="sesmailmanager-GetRuleSet-request-RuleSetId"></a>
The identifier of an existing rule set to be retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_GetRuleSet_ResponseSyntax"></a>

```
{
   "CreatedDate": number,
   "LastModificationDate": number,
   "Rules": [
      {
         "Actions": [
            { ... }
         ],
         "Conditions": [
            { ... }
         ],
         "Name": "string",
         "Unless": [
            { ... }
         ]
      }
   ],
   "RuleSetArn": "string",
   "RuleSetId": "string",
   "RuleSetName": "string"
}
```

## Response Elements
<a name="API_GetRuleSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedDate](#API_GetRuleSet_ResponseSyntax) **   <a name="sesmailmanager-GetRuleSet-response-CreatedDate"></a>
The date of when then rule set was created.
Type: Timestamp

 ** [LastModificationDate](#API_GetRuleSet_ResponseSyntax) **   <a name="sesmailmanager-GetRuleSet-response-LastModificationDate"></a>
The date of when the rule set was last modified.
Type: Timestamp

 ** [Rules](#API_GetRuleSet_ResponseSyntax) **   <a name="sesmailmanager-GetRuleSet-response-Rules"></a>
The rules contained in the rule set.
Type: Array of [Rule](API_Rule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 40 items.

 ** [RuleSetArn](#API_GetRuleSet_ResponseSyntax) **   <a name="sesmailmanager-GetRuleSet-response-RuleSetArn"></a>
The Amazon Resource Name (ARN) of the rule set resource.
Type: String

 ** [RuleSetId](#API_GetRuleSet_ResponseSyntax) **   <a name="sesmailmanager-GetRuleSet-response-RuleSetId"></a>
The identifier of the rule set resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [RuleSetName](#API_GetRuleSet_ResponseSyntax) **   <a name="sesmailmanager-GetRuleSet-response-RuleSetName"></a>
A user-friendly name for the rule set resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.-]+`

## Errors
<a name="API_GetRuleSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Occurs when a requested resource is not found.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_GetRuleSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/GetRuleSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/GetRuleSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/GetRuleSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/GetRuleSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/GetRuleSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/GetRuleSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/GetRuleSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/GetRuleSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/GetRuleSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/GetRuleSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
