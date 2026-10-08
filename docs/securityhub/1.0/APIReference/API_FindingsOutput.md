---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_FindingsOutput.html
---

# FindingsOutput
<a name="API_FindingsOutput"></a>

The configuration for a findings export: the output format, an optional set of filters, and the fields to include.

## Contents
<a name="API_FindingsOutput_Contents"></a>

 ** Format **   <a name="securityhub-Type-FindingsOutput-Format"></a>
The output format of the export. `CSV` produces comma-separated rows that are suitable for spreadsheets and analysis tools. `OCSF_JSON` produces newline-delimited JSON records in the Open Cybersecurity Schema Framework (OCSF) format used elsewhere in Security Hub.
Type: String
Valid Values: `CSV | OCSF_JSON`
Required: Yes

 ** Filters **   <a name="securityhub-Type-FindingsOutput-Filters"></a>
An optional set of OCSF finding filters that restrict which findings are exported. The filter structure is the same as the one used by `GetFindingsV2`. If you omit this member, Security Hub exports all findings available to the caller. When echoed by `GetExportJobV2`, relative date ranges are returned unresolved.
Type: [OcsfFindingFilters](API_OcsfFindingFilters.md) object
Required: No

 ** SelectedFields **   <a name="securityhub-Type-FindingsOutput-SelectedFields"></a>
The OCSF finding fields to include in the export, specified as OCSF field paths (for example, `finding_info.title` or `severity`). You can specify from 1 to 50 fields.
Whether this parameter is required depends on the value of `Format`:
+  `CSV` – Required. The field paths that you specify become the columns of the output, in the order that you provide them. If you omit this parameter, the request returns a `ValidationException`.
+  `OCSF_JSON` – Not supported. This format includes each finding in full, so field selection doesn't apply. If you specify this parameter, the request returns a `ValidationException`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Valid Values: `metadata.uid | activity_name | cloud.account.name | cloud.account.uid | cloud.provider | cloud.region | compliance.assessments.category | compliance.assessments.name | compliance.control | compliance.status | compliance.standards | finding_info.desc | finding_info.src_url | finding_info.title | finding_info.types | finding_info.uid | finding_info.related_events.traits.category | finding_info.related_events.uid | finding_info.related_events.product.uid | finding_info.related_events.title | metadata.product.feature.uid | metadata.product.name | metadata.product.uid | metadata.product.vendor_name | remediation.desc | remediation.references | resources.cloud_partition | resources.name | resources.owner.account.uid | resources.owner.org.uid | resources.owner.account.name | resources.provider | resources.region | resources.type | resources.uid | severity | status | comment | vulnerabilities.fix_coverage | class_name | databucket.encryption_details.algorithm | databucket.encryption_details.key_uid | databucket.file.data_classifications.classifier_details.type | evidences.actor.user.account.uid | evidences.api.operation | evidences.api.response.error_message | evidences.api.service.name | evidences.connection_info.direction | evidences.connection_info.protocol_name | evidences.dst_endpoint.autonomous_system.name | evidences.dst_endpoint.location.city | evidences.dst_endpoint.location.country | evidences.src_endpoint.autonomous_system.name | evidences.src_endpoint.hostname | evidences.src_endpoint.location.city | evidences.src_endpoint.location.country | finding_info.analytic.name | malware.name | malware_scan_info.uid | malware.severity | resources.cloud_function.layers.uid_alt | resources.cloud_function.runtime | resources.cloud_function.user.uid | resources.device.encryption_details.key_uid | resources.device.image.uid | resources.image.architecture | resources.image.registry_uid | resources.image.repository_name | resources.image.uid | resources.subnet_info.uid | resources.vpc_uid | vulnerabilities.affected_code.file.path | vulnerabilities.affected_packages.name | vulnerabilities.cve.cvss.vendor_name | vulnerabilities.cve.cvss.version | vulnerabilities.cve.epss.score | vulnerabilities.cve.uid | vulnerabilities.related_vulnerabilities | vendor_attributes.severity | activity_id | compliance.status_id | confidence_score | severity_id | status_id | finding_info.related_events_count | evidences.api.response.code | evidences.dst_endpoint.autonomous_system.number | evidences.dst_endpoint.port | evidences.src_endpoint.autonomous_system.number | evidences.src_endpoint.port | resources.image.in_use_count | vulnerabilities.cve.cvss.base_score | vendor_attributes.severity_id | finding_info.created_time_dt | finding_info.first_seen_time_dt | finding_info.last_seen_time_dt | finding_info.modified_time_dt | resources.image.created_time_dt | resources.image.last_used_time_dt | resources.modified_time_dt | compliance.assessments.meets_criteria | vulnerabilities.is_exploit_available | vulnerabilities.is_fix_available | resources.tags | compliance.control_parameters | databucket.tags | finding_info.tags | evidences.dst_endpoint.ip | evidences.src_endpoint.ip`
Required: No

## See Also
<a name="API_FindingsOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/FindingsOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/FindingsOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/FindingsOutput)
