---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ResourceDataSyncAwsOrganizationsSource.html
---

# ResourceDataSyncAwsOrganizationsSource
<a name="API_ResourceDataSyncAwsOrganizationsSource"></a>

Information about the `AwsOrganizationsSource` resource data sync source. A sync source of this type can synchronize data from AWS Organizations or, if an AWS organization isn't present, from multiple AWS Regions.

## Contents
<a name="API_ResourceDataSyncAwsOrganizationsSource_Contents"></a>

 ** OrganizationSourceType **   <a name="systemsmanager-Type-ResourceDataSyncAwsOrganizationsSource-OrganizationSourceType"></a>
If an AWS organization is present, this is either `OrganizationalUnits` or `EntireOrganization`. For `OrganizationalUnits`, the data is aggregated from a set of organization units. For `EntireOrganization`, the data is aggregated from the entire AWS organization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** OrganizationalUnits **   <a name="systemsmanager-Type-ResourceDataSyncAwsOrganizationsSource-OrganizationalUnits"></a>
The AWS Organizations organization units included in the sync.
Type: Array of [ResourceDataSyncOrganizationalUnit](API_ResourceDataSyncOrganizationalUnit.md) objects
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Required: No

## See Also
<a name="API_ResourceDataSyncAwsOrganizationsSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ResourceDataSyncAwsOrganizationsSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ResourceDataSyncAwsOrganizationsSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ResourceDataSyncAwsOrganizationsSource)
