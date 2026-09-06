---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ResourceInventory.html
---

# ResourceInventory
<a name="API_ResourceInventory"></a>

Details about a resource.

## Contents
<a name="API_ResourceInventory_Contents"></a>

 ** AmiId **   <a name="licensemanager-Type-ResourceInventory-AmiId"></a>
Amazon Machine Image (AMI) ID associated with the resource.
Type: String
Required: No

 ** HostId **   <a name="licensemanager-Type-ResourceInventory-HostId"></a>
Dedicated Host ID where the resource is running.
Type: String
Required: No

 ** InstanceType **   <a name="licensemanager-Type-ResourceInventory-InstanceType"></a>
EC2 instance type of the resource.
Type: String
Required: No

 ** MarketplaceProductCodes **   <a name="licensemanager-Type-ResourceInventory-MarketplaceProductCodes"></a>
List of Marketplace product codes associated with the resource.
Type: Array of strings
Required: No

 ** Platform **   <a name="licensemanager-Type-ResourceInventory-Platform"></a>
Platform of the resource.
Type: String
Required: No

 ** PlatformVersion **   <a name="licensemanager-Type-ResourceInventory-PlatformVersion"></a>
Platform version of the resource in the inventory.
Type: String
Required: No

 ** Region **   <a name="licensemanager-Type-ResourceInventory-Region"></a>
Region where the resource is located.
Type: String
Required: No

 ** ResourceArn **   <a name="licensemanager-Type-ResourceInventory-ResourceArn"></a>
Amazon Resource Name (ARN) of the resource.
Type: String
Required: No

 ** ResourceId **   <a name="licensemanager-Type-ResourceInventory-ResourceId"></a>
ID of the resource.
Type: String
Required: No

 ** ResourceOwningAccountId **   <a name="licensemanager-Type-ResourceInventory-ResourceOwningAccountId"></a>
ID of the account that owns the resource.
Type: String
Required: No

 ** ResourceType **   <a name="licensemanager-Type-ResourceInventory-ResourceType"></a>
Type of resource.
Type: String
Valid Values: `EC2_INSTANCE | EC2_HOST | EC2_AMI | RDS | SYSTEMS_MANAGER_MANAGED_INSTANCE`
Required: No

 ** UsageOperation **   <a name="licensemanager-Type-ResourceInventory-UsageOperation"></a>
Usage operation value that corresponds to the license type for billing purposes.
Type: String
Required: No

## See Also
<a name="API_ResourceInventory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ResourceInventory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ResourceInventory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ResourceInventory)
