---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ComponentRunWith.html
---

# ComponentRunWith
<a name="API_ComponentRunWith"></a>

Contains information system user and group that the AWS IoT Greengrass Core software uses to run component processes on the core device. For more information, see [Configure the user and group that run components](https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-user) in the * AWS IoT Greengrass V2 Developer Guide*.

## Contents
<a name="API_ComponentRunWith_Contents"></a>

 ** posixUser **   <a name="greengrassv2-Type-ComponentRunWith-posixUser"></a>
The POSIX system user and, optionally, group to use to run this component on Linux core devices. The user, and group if specified, must exist on each Linux core device. Specify the user and group separated by a colon (`:`) in the following format: `user:group`. The group is optional. If you don't specify a group, the AWS IoT Greengrass Core software uses the primary user for the group.
If you omit this parameter, the AWS IoT Greengrass Core software uses the default system user and group that you configure on the Greengrass nucleus component. For more information, see [Configure the user and group that run components](https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-user).
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** systemResourceLimits **   <a name="greengrassv2-Type-ComponentRunWith-systemResourceLimits"></a>
The system resource limits to apply to this component's process on the core device. AWS IoT Greengrass currently supports this feature on only Linux core devices.
If you omit this parameter, the AWS IoT Greengrass Core software uses the default system resource limits that you configure on the Greengrass nucleus component. For more information, see [Configure system resource limits for components](https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-system-resource-limits).
Type: [SystemResourceLimits](API_SystemResourceLimits.md) object
Required: No

 ** windowsUser **   <a name="greengrassv2-Type-ComponentRunWith-windowsUser"></a>
The Windows user to use to run this component on Windows core devices. The user must exist on each Windows core device, and its name and password must be in the LocalSystem account's Credentials Manager instance.
If you omit this parameter, the AWS IoT Greengrass Core software uses the default Windows user that you configure on the Greengrass nucleus component. For more information, see [Configure the user and group that run components](https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-user).
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_ComponentRunWith_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/ComponentRunWith)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/ComponentRunWith)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/ComponentRunWith)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
