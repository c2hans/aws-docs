---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_OcsfNumberFilter.html
---

# OcsfNumberFilter
<a name="API_OcsfNumberFilter"></a>

Enables filtering of security findings based on numerical field values in OCSF.

## Contents
<a name="API_OcsfNumberFilter_Contents"></a>

 ** FieldName **   <a name="securityhub-Type-OcsfNumberFilter-FieldName"></a>
The name of the field.
Type: String
Valid Values: `activity_id | compliance.status_id | confidence_score | severity_id | status_id | finding_info.related_events_count | evidences.api.response.code | evidences.dst_endpoint.autonomous_system.number | evidences.dst_endpoint.port | evidences.src_endpoint.autonomous_system.number | evidences.src_endpoint.port | resources.image.in_use_count | vulnerabilities.cve.cvss.base_score | vendor_attributes.severity_id`
Required: No

 ** Filter **   <a name="securityhub-Type-OcsfNumberFilter-Filter"></a>
A number filter for querying findings.
Type: [NumberFilter](API_NumberFilter.md) object
Required: No

## See Also
<a name="API_OcsfNumberFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/OcsfNumberFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/OcsfNumberFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/OcsfNumberFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
