---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_SlaInputConfiguration.html
---

# SlaInputConfiguration
<a name="API_connect-cases_SlaInputConfiguration"></a>

Represents the input configuration of an SLA being created.

## Contents
<a name="API_connect-cases_SlaInputConfiguration_Contents"></a>

 ** name **   <a name="connect-Type-connect-cases_SlaInputConfiguration-name"></a>
Name of an SLA.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `.*[\S]`
Required: Yes

 ** targetSlaMinutes **   <a name="connect-Type-connect-cases_SlaInputConfiguration-targetSlaMinutes"></a>
Target duration in minutes within which an SLA should be completed.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 1051200.
Required: Yes

 ** type **   <a name="connect-Type-connect-cases_SlaInputConfiguration-type"></a>
Type of SLA.
Type: String
Valid Values: `CaseField`
Required: Yes

 ** fieldId **   <a name="connect-Type-connect-cases_SlaInputConfiguration-fieldId"></a>
Unique identifier of a field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** targetFieldValues **   <a name="connect-Type-connect-cases_SlaInputConfiguration-targetFieldValues"></a>
Represents a list of target field values for the fieldId specified in SlaInputConfiguration. The SLA is considered met if any one of these target field values matches the actual field value.
Type: Array of [FieldValueUnion](API_connect-cases_FieldValueUnion.md) objects
Array Members: Fixed number of 1 item.
Required: No

## See Also
<a name="API_connect-cases_SlaInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/SlaInputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/SlaInputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/SlaInputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
