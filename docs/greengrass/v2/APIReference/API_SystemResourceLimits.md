---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_SystemResourceLimits.html
---

# SystemResourceLimits
<a name="API_SystemResourceLimits"></a>

Contains information about system resource limits that the AWS IoT Greengrass Core software applies to a component's processes. For more information, see [Configure system resource limits for components](https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-system-resource-limits).

## Contents
<a name="API_SystemResourceLimits_Contents"></a>

 ** cpus **   <a name="greengrassv2-Type-SystemResourceLimits-cpus"></a>
The maximum amount of CPU time that a component's processes can use on the core device. A core device's total CPU time is equivalent to the device's number of CPU cores. For example, on a core device with 4 CPU cores, you can set this value to `2` to limit the component's processes to 50 percent usage of each CPU core. On a device with 1 CPU core, you can set this value to `0.25` to limit the component's processes to 25 percent usage of the CPU. If you set this value to a number greater than the number of CPU cores, the AWS IoT Greengrass Core software doesn't limit the component's CPU usage.
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** memory **   <a name="greengrassv2-Type-SystemResourceLimits-memory"></a>
The maximum amount of RAM, expressed in kilobytes, that a component's processes can use on the core device.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 9223372036854771712.
Required: No

## See Also
<a name="API_SystemResourceLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/SystemResourceLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/SystemResourceLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/SystemResourceLimits)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
