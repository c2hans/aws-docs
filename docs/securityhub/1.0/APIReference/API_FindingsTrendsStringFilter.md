---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_FindingsTrendsStringFilter.html
---

# FindingsTrendsStringFilter
<a name="API_FindingsTrendsStringFilter"></a>

A filter for string-based fields in findings trend data.

## Contents
<a name="API_FindingsTrendsStringFilter_Contents"></a>

 ** FieldName **   <a name="securityhub-Type-FindingsTrendsStringFilter-FieldName"></a>
The name of the findings field to filter on. You can specify one of the following fields.
+  `account_id` – The AWS account ID associated with the finding.
+  `region` – The AWS Region associated with the finding.
+  `finding_types` – The finding types associated with the finding.
+  `finding_status` – The status of the finding.
+  `finding_cve_ids` – The Common Vulnerabilities and Exposures (CVE) identifiers associated with the finding.
+  `finding_compliance_status` – The compliance status of the finding.
+  `finding_control_id` – The identifier of the security control associated with the finding.
+  `finding_class_name` – The finding class, such as `Compliance Finding`.
+  `finding_provider` – The name of the product that generated the finding.
+  `finding_activity_name` – The activity name associated with the finding.
+  `resource_cloud_providers` – The cloud providers of the resources that the finding is associated with. Valid values are `AWS` and `Azure`.
+  `resource_regions` – The Regions of the associated resources. For an AWS resource, this is the AWS Region. For an Azure resource, this is the Azure Region, such as `eastus`.
+  `resource_owner_ids` – The identifiers of the accounts that own the associated resources. For an AWS resource, this is the AWS account ID. For an Azure resource, this is the Azure subscription ID.
+  `resource_owner_organization_ids` – The identifiers of the organizations that own the associated resources. For an AWS resource, this is the AWS organization ID. For an Azure resource, this is the Azure tenant ID.
Type: String
Valid Values: `account_id | region | finding_types | finding_status | finding_cve_ids | finding_compliance_status | finding_control_id | finding_class_name | finding_provider | finding_activity_name | resource_cloud_providers | resource_regions | resource_owner_ids | resource_owner_organization_ids`
Required: No

 ** Filter **   <a name="securityhub-Type-FindingsTrendsStringFilter-Filter"></a>
A string filter for filtering AWS Security Hub CSPM findings.
Type: [StringFilter](API_StringFilter.md) object
Required: No

## See Also
<a name="API_FindingsTrendsStringFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/FindingsTrendsStringFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/FindingsTrendsStringFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/FindingsTrendsStringFilter)
