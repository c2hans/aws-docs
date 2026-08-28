---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_OcsfBooleanFilter.html
---

# OcsfBooleanFilter
<a name="API_OcsfBooleanFilter"></a>

Enables filtering of security findings based on boolean field values in OCSF.

## Contents
<a name="API_OcsfBooleanFilter_Contents"></a>

 ** FieldName **   <a name="securityhub-Type-OcsfBooleanFilter-FieldName"></a>
The name of the field.
Type: String
Valid Values: `compliance.assessments.meets_criteria | vulnerabilities.is_exploit_available | vulnerabilities.is_fix_available`
Required: No

 ** Filter **   <a name="securityhub-Type-OcsfBooleanFilter-Filter"></a>
Boolean filter for querying findings.
Type: [BooleanFilter](API_BooleanFilter.md) object
Required: No

## See Also
<a name="API_OcsfBooleanFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/OcsfBooleanFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/OcsfBooleanFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/OcsfBooleanFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
