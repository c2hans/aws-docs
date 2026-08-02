---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ResourcesTrendsStringFilter.html
---

# ResourcesTrendsStringFilter
<a name="API_ResourcesTrendsStringFilter"></a>

A filter for string-based fields in resources trend data, such as resource type or account ID.

## Contents
<a name="API_ResourcesTrendsStringFilter_Contents"></a>

 ** FieldName **   <a name="securityhub-Type-ResourcesTrendsStringFilter-FieldName"></a>
The name of the resources field to filter on. You can specify one of the following fields.
+  `account_id` – The AWS account ID that owns the resource.
+  `region` – The AWS Region of the resource.
+  `resource_type` – The type of the resource.
+  `resource_category` – The category of the resource.
+  `resource_cloud_provider` – The cloud provider of the resource. Valid values are `AWS` and `Azure`.
+  `resource_region` – The Region of the resource. For an AWS resource, this is the AWS Region. For an Azure resource, this is the Azure Region, such as `eastus`.
+  `resource_owner_id` – The identifier of the account that owns the resource. For an AWS resource, this is the AWS account ID. For an Azure resource, this is the Azure subscription ID.
+  `resource_owner_organization_id` – The identifier of the organization that owns the resource. For an AWS resource, this is the AWS organization ID. For an Azure resource, this is the Azure tenant ID.
Type: String
Valid Values: `account_id | region | resource_type | resource_category | resource_cloud_provider | resource_region | resource_owner_id | resource_owner_organization_id`
Required: No

 ** Filter **   <a name="securityhub-Type-ResourcesTrendsStringFilter-Filter"></a>
A string filter for filtering AWS Security Hub CSPM findings.
Type: [StringFilter](API_StringFilter.md) object
Required: No

## See Also
<a name="API_ResourcesTrendsStringFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ResourcesTrendsStringFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ResourcesTrendsStringFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ResourcesTrendsStringFilter)
