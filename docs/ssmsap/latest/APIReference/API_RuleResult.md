---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_RuleResult.html
---

# RuleResult
<a name="API_RuleResult"></a>

Represents the result of a single rule within a configuration check.

## Contents
<a name="API_RuleResult_Contents"></a>

 ** Description **   <a name="ssmsap-Type-RuleResult-Description"></a>
A description of what the rule validates.
Type: String
Required: No

 ** Id **   <a name="ssmsap-Type-RuleResult-Id"></a>
The unique identifier of the rule result.
Type: String
Pattern: `[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?`
Required: No

 ** Message **   <a name="ssmsap-Type-RuleResult-Message"></a>
A message providing details about the rule result.
Type: String
Required: No

 ** Metadata **   <a name="ssmsap-Type-RuleResult-Metadata"></a>
Additional metadata associated with the rule result.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Value Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** Status **   <a name="ssmsap-Type-RuleResult-Status"></a>
The status of the rule result.
Type: String
Valid Values: `PASSED | FAILED | WARNING | INFO | UNKNOWN`
Required: No

## See Also
<a name="API_RuleResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/RuleResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/RuleResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/RuleResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
