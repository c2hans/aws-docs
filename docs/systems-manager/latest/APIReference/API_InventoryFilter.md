---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InventoryFilter.html
---

# InventoryFilter
<a name="API_InventoryFilter"></a>

One or more filters. Use a filter to return a more specific list of results.

 **Example formats for the `aws ssm get-inventory` command:**

 `--filters Key=AWS:InstanceInformation.AgentType,Values=amazon-ssm-agent,Type=Equal`

 `--filters Key=AWS:InstanceInformation.AgentVersion,Values=3.3.2299.0,Type=Equal`

 `--filters Key=AWS:InstanceInformation.ComputerName,Values=ip-192.0.2.0.us-east-2.compute.internal,Type=Equal`

 `--filters Key=AWS:InstanceInformation.InstanceId,Values=i-0a4cd6ceffEXAMPLE,i-1a2b3c4d5e6EXAMPLE,Type=Equal`

 `--filters Key=AWS:InstanceInformation.InstanceStatus,Values=Active,Type=Equal`

 `--filters Key=AWS:InstanceInformation.IpAddress,Values=198.51.100.0,Type=Equal`

 `--filters Key=AWS:InstanceInformation.PlatformName,Values="Amazon Linux",Type=Equal`

 `--filters Key=AWS:InstanceInformation.PlatformType,Values=Linux,Type=Equal`

 `--filters Key=AWS:InstanceInformation.PlatformVersion,Values=2023,Type=BeginWith`

 `--filters Key=AWS:InstanceInformation.ResourceType,Values=EC2Instance,Type=Equal`

## Contents
<a name="API_InventoryFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-InventoryFilter-Key"></a>
The name of the filter key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** Values **   <a name="systemsmanager-Type-InventoryFilter-Values"></a>
Inventory filter values.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 40 items.
Required: Yes

 ** Type **   <a name="systemsmanager-Type-InventoryFilter-Type"></a>
The type of filter.
The `Exists` filter must be used with aggregators. For more information, see [Aggregating inventory data](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-aggregate.html) in the * AWS Systems Manager User Guide*.
Type: String
Valid Values: `Equal | NotEqual | BeginWith | LessThan | GreaterThan | Exists`
Required: No

## See Also
<a name="API_InventoryFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InventoryFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InventoryFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InventoryFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
