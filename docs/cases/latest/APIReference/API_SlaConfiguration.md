---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_SlaConfiguration.html
---

# SlaConfiguration
<a name="API_connect-cases_SlaConfiguration"></a>

Represents an SLA configuration.

## Contents
<a name="API_connect-cases_SlaConfiguration_Contents"></a>

 ** name **   <a name="connect-Type-connect-cases_SlaConfiguration-name"></a>
Name of an SLA.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `.*[\S]`
Required: Yes

 ** status **   <a name="connect-Type-connect-cases_SlaConfiguration-status"></a>
Status of an SLA.
Type: String
Valid Values: `Active | Overdue | Met | NotMet`
Required: Yes

 ** targetTime **   <a name="connect-Type-connect-cases_SlaConfiguration-targetTime"></a>
Target time by which an SLA should be completed.
Type: Timestamp
Required: Yes

 ** type **   <a name="connect-Type-connect-cases_SlaConfiguration-type"></a>
Type of SLA.
Type: String
Valid Values: `CaseField`
Required: Yes

 ** completionTime **   <a name="connect-Type-connect-cases_SlaConfiguration-completionTime"></a>
Time at which an SLA was completed.
Type: Timestamp
Required: No

 ** fieldId **   <a name="connect-Type-connect-cases_SlaConfiguration-fieldId"></a>
Unique identifier of a field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** targetFieldValues **   <a name="connect-Type-connect-cases_SlaConfiguration-targetFieldValues"></a>
Represents a list of target field values for the fieldId specified in SlaConfiguration.
Type: Array of [FieldValueUnion](API_connect-cases_FieldValueUnion.md) objects
Array Members: Fixed number of 1 item.
Required: No

## See Also
<a name="API_connect-cases_SlaConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/SlaConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/SlaConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/SlaConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
