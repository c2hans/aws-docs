---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ComponentConfigurationUpdate.html
---

# ComponentConfigurationUpdate
<a name="API_ComponentConfigurationUpdate"></a>

Contains information about a deployment's update to a component's configuration on Greengrass core devices. For more information, see [Update component configurations](https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html) in the * AWS IoT Greengrass V2 Developer Guide*.

## Contents
<a name="API_ComponentConfigurationUpdate_Contents"></a>

 ** merge **   <a name="greengrassv2-Type-ComponentConfigurationUpdate-merge"></a>
A serialized JSON string that contains the configuration object to merge to target devices. The core device merges this configuration with the component's existing configuration. If this is the first time a component deploys on a device, the core device merges this configuration with the component's default configuration. This means that the core device keeps it's existing configuration for keys and values that you don't specify in this object. For more information, see [Merge configuration updates](https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html#merge-configuration-update) in the * AWS IoT Greengrass V2 Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10485760.
Required: No

 ** reset **   <a name="greengrassv2-Type-ComponentConfigurationUpdate-reset"></a>
The list of configuration nodes to reset to default values on target devices. Use JSON pointers to specify each node to reset. JSON pointers start with a forward slash (`/`) and use forward slashes to separate the key for each level in the object. For more information, see the [JSON pointer specification](https://tools.ietf.org/html/rfc6901) and [Reset configuration updates](https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html#reset-configuration-update) in the * AWS IoT Greengrass V2 Developer Guide*.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_ComponentConfigurationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/ComponentConfigurationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/ComponentConfigurationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/ComponentConfigurationUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
