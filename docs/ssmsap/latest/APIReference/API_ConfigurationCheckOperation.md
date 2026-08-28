---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ConfigurationCheckOperation.html
---

# ConfigurationCheckOperation
<a name="API_ConfigurationCheckOperation"></a>

Represents a configuration check operation that has been executed against an application.

## Contents
<a name="API_ConfigurationCheckOperation_Contents"></a>

 ** ApplicationId **   <a name="ssmsap-Type-ConfigurationCheckOperation-ApplicationId"></a>
The ID of the application against which the configuration check was performed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w\d\.-]+`
Required: No

 ** ConfigurationCheckDescription **   <a name="ssmsap-Type-ConfigurationCheckOperation-ConfigurationCheckDescription"></a>
A description of the configuration check that was performed.
Type: String
Required: No

 ** ConfigurationCheckId **   <a name="ssmsap-Type-ConfigurationCheckOperation-ConfigurationCheckId"></a>
The unique identifier of the configuration check that was performed.
Type: String
Valid Values: `SAP_CHECK_01 | SAP_CHECK_02 | SAP_CHECK_03`
Required: No

 ** ConfigurationCheckName **   <a name="ssmsap-Type-ConfigurationCheckOperation-ConfigurationCheckName"></a>
The name of the configuration check that was performed.
Type: String
Required: No

 ** EndTime **   <a name="ssmsap-Type-ConfigurationCheckOperation-EndTime"></a>
The time at which the configuration check operation completed.
Type: Timestamp
Required: No

 ** Id **   <a name="ssmsap-Type-ConfigurationCheckOperation-Id"></a>
The unique identifier of the configuration check operation.
Type: String
Pattern: `[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?`
Required: No

 ** RuleStatusCounts **   <a name="ssmsap-Type-ConfigurationCheckOperation-RuleStatusCounts"></a>
A summary of all the rule results, showing counts for each status type.
Type: [RuleStatusCounts](API_RuleStatusCounts.md) object
Required: No

 ** StartTime **   <a name="ssmsap-Type-ConfigurationCheckOperation-StartTime"></a>
The time at which the configuration check operation started.
Type: Timestamp
Required: No

 ** Status **   <a name="ssmsap-Type-ConfigurationCheckOperation-Status"></a>
The current status of the configuration check operation.
Type: String
Valid Values: `INPROGRESS | SUCCESS | ERROR`
Required: No

 ** StatusMessage **   <a name="ssmsap-Type-ConfigurationCheckOperation-StatusMessage"></a>
A message providing additional details about the status of the configuration check operation.
Type: String
Required: No

## See Also
<a name="API_ConfigurationCheckOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/ConfigurationCheckOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/ConfigurationCheckOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/ConfigurationCheckOperation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
