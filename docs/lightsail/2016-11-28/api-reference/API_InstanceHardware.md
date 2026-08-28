---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_InstanceHardware.html
---

# InstanceHardware
<a name="API_InstanceHardware"></a>

Describes the hardware for the instance.

## Contents
<a name="API_InstanceHardware_Contents"></a>

 ** cpuCount **   <a name="Lightsail-Type-InstanceHardware-cpuCount"></a>
The number of vCPUs the instance has.
Type: Integer
Required: No

 ** disks **   <a name="Lightsail-Type-InstanceHardware-disks"></a>
The disks attached to the instance.
Type: Array of [Disk](API_Disk.md) objects
Required: No

 ** ramSizeInGb **   <a name="Lightsail-Type-InstanceHardware-ramSizeInGb"></a>
The amount of RAM in GB on the instance (`1.0`).
Type: Float
Required: No

## See Also
<a name="API_InstanceHardware_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/InstanceHardware)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/InstanceHardware)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/InstanceHardware)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
