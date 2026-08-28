---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_LambdaDeviceMount.html
---

# LambdaDeviceMount
<a name="API_LambdaDeviceMount"></a>

Contains information about a device that Linux processes in a container can access.

## Contents
<a name="API_LambdaDeviceMount_Contents"></a>

 ** path **   <a name="greengrassv2-Type-LambdaDeviceMount-path"></a>
The mount path for the device in the file system.
Type: String
Required: Yes

 ** addGroupOwner **   <a name="greengrassv2-Type-LambdaDeviceMount-addGroupOwner"></a>
Whether or not to add the component's system user as an owner of the device.
Default: `false`
Type: Boolean
Required: No

 ** permission **   <a name="greengrassv2-Type-LambdaDeviceMount-permission"></a>
The permission to access the device: read/only (`ro`) or read/write (`rw`).
Default: `ro`
Type: String
Valid Values: `ro | rw`
Required: No

## See Also
<a name="API_LambdaDeviceMount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/LambdaDeviceMount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/LambdaDeviceMount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/LambdaDeviceMount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
