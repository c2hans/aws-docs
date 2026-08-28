---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_OcsfDateFilter.html
---

# OcsfDateFilter
<a name="API_OcsfDateFilter"></a>

Enables filtering of security findings based on date and timestamp fields in OCSF.

## Contents
<a name="API_OcsfDateFilter_Contents"></a>

 ** FieldName **   <a name="securityhub-Type-OcsfDateFilter-FieldName"></a>
The name of the field.
Type: String
Valid Values: `finding_info.created_time_dt | finding_info.first_seen_time_dt | finding_info.last_seen_time_dt | finding_info.modified_time_dt | resources.image.created_time_dt | resources.image.last_used_time_dt | resources.modified_time_dt`
Required: No

 ** Filter **   <a name="securityhub-Type-OcsfDateFilter-Filter"></a>
A date filter for querying findings.
Type: [DateFilter](API_DateFilter.md) object
Required: No

## See Also
<a name="API_OcsfDateFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/OcsfDateFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/OcsfDateFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/OcsfDateFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
