---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_OcsfMapFilter.html
---

# OcsfMapFilter
<a name="API_OcsfMapFilter"></a>

Enables filtering of security findings based on map field values in OCSF.

## Contents
<a name="API_OcsfMapFilter_Contents"></a>

 ** FieldName **   <a name="securityhub-Type-OcsfMapFilter-FieldName"></a>
The name of the field.
Type: String
Valid Values: `resources.tags | compliance.control_parameters | databucket.tags | finding_info.tags`
Required: No

 ** Filter **   <a name="securityhub-Type-OcsfMapFilter-Filter"></a>
A map filter for filtering AWS Security Hub CSPM findings. Each map filter provides the field to check for, the value to check for, and the comparison operator.
Type: [MapFilter](API_MapFilter.md) object
Required: No

## See Also
<a name="API_OcsfMapFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/OcsfMapFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/OcsfMapFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/OcsfMapFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
