---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ResourcesMapFilter.html
---

# ResourcesMapFilter
<a name="API_ResourcesMapFilter"></a>

Enables filtering of AWS resources based on key-value map attributes.

## Contents
<a name="API_ResourcesMapFilter_Contents"></a>

 ** FieldName **   <a name="securityhub-Type-ResourcesMapFilter-FieldName"></a>
The name of the field.
Type: String
Valid Values: `ResourceTags`
Required: No

 ** Filter **   <a name="securityhub-Type-ResourcesMapFilter-Filter"></a>
A map filter for filtering AWS Security Hub CSPM findings. Each map filter provides the field to check for, the value to check for, and the comparison operator.
Type: [MapFilter](API_MapFilter.md) object
Required: No

## See Also
<a name="API_ResourcesMapFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ResourcesMapFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ResourcesMapFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ResourcesMapFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
