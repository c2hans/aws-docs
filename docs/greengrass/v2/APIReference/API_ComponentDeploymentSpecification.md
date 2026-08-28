---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ComponentDeploymentSpecification.html
---

# ComponentDeploymentSpecification
<a name="API_ComponentDeploymentSpecification"></a>

Contains information about a component to deploy.

## Contents
<a name="API_ComponentDeploymentSpecification_Contents"></a>

 ** componentVersion **   <a name="greengrassv2-Type-ComponentDeploymentSpecification-componentVersion"></a>
The version of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** configurationUpdate **   <a name="greengrassv2-Type-ComponentDeploymentSpecification-configurationUpdate"></a>
The configuration updates to deploy for the component. You can define *reset* updates and *merge* updates. A reset updates the keys that you specify to the default configuration for the component. A merge updates the core device's component configuration with the keys and values that you specify. The AWS IoT Greengrass Core software applies reset updates before it applies merge updates. For more information, see [Update component configurations](https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html) in the * AWS IoT Greengrass V2 Developer Guide*.
Type: [ComponentConfigurationUpdate](API_ComponentConfigurationUpdate.md) object
Required: No

 ** runWith **   <a name="greengrassv2-Type-ComponentDeploymentSpecification-runWith"></a>
The system user and group that the AWS IoT Greengrass Core software uses to run component processes on the core device. If you omit this parameter, the AWS IoT Greengrass Core software uses the system user and group that you configure for the core device. For more information, see [Configure the user and group that run components](https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-user) in the * AWS IoT Greengrass V2 Developer Guide*.
Type: [ComponentRunWith](API_ComponentRunWith.md) object
Required: No

## See Also
<a name="API_ComponentDeploymentSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/ComponentDeploymentSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/ComponentDeploymentSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/ComponentDeploymentSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
