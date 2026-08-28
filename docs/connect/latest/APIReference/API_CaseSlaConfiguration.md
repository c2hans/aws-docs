---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CaseSlaConfiguration.html
---

# CaseSlaConfiguration
<a name="API_CaseSlaConfiguration"></a>

The SLA configuration for Case SlaAssignmentType.

## Contents
<a name="API_CaseSlaConfiguration_Contents"></a>

 ** Name **   <a name="connect-Type-CaseSlaConfiguration-Name"></a>
Name of an SLA.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `^.*[\S]$`
Required: Yes

 ** TargetSlaMinutes **   <a name="connect-Type-CaseSlaConfiguration-TargetSlaMinutes"></a>
Target duration in minutes within which an SLA should be completed.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 1051200.
Required: Yes

 ** Type **   <a name="connect-Type-CaseSlaConfiguration-Type"></a>
Type of SLA for Case SlaAssignmentType.
Type: String
Valid Values: `CaseField`
Required: Yes

 ** FieldId **   <a name="connect-Type-CaseSlaConfiguration-FieldId"></a>
Unique identifier of a Case field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** TargetFieldValues **   <a name="connect-Type-CaseSlaConfiguration-TargetFieldValues"></a>
Represents a list of target field values for the fieldId specified in CaseSlaConfiguration. The SLA is considered met if any one of these target field values matches the actual field value.
Type: Array of [FieldValueUnion](API_FieldValueUnion.md) objects
Array Members: Maximum number of 1 item.
Required: No

## See Also
<a name="API_CaseSlaConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CaseSlaConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CaseSlaConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CaseSlaConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
