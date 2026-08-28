---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/configuration-file-best-practices.html
---

# Configuration file best practices
<a name="configuration-file-best-practices"></a>

Landing Zone Accelerator on AWS aims to abstract away most aspects of managing its underlying infrastructure as code (IaC) templates from the user. This is facilitated through the use of its [configuration files](using-configuration-files.md) to define your landing zone environment. However, it is important to keep some common IaC best practices in mind when modifying your configuration to avoid pipeline failure scenarios.

## Manage accelerator resources strictly through configuration
<a name="manage-accelerator-resources-strictly-through-configuration"></a>

Introducing manual, out-of-band changes to accelerator-managed resources in your environment can cause unexpected pipeline failures or resource updates to occur when you release updates using your Core pipeline. CDK and CloudFormation don’t keep a record of these out-of-band changes, which leads to drift between the solution-generated template and actual resource configuration state. For this reason, we recommend managing changes to your landing zone resources strictly through the solution [configuration files](using-configuration-files.md). For features and configurations that aren’t supported by the solution, we recommend using custom stacks in the `customizations-config.yaml` file or externally-managed IaC to manage those updates.

## Understanding the name property
<a name="understanding-the-name-property"></a>

Several configuration objects throughout the solution configuration files make use of the `name` property. This property has two important uses:
+ It allows you to logically name and reference a configuration item in other configuration items. This allows you to easily build relationships between separate configuration items if there are dependencies between them.
+ It is used to generate unique [logical IDs](https://docs.aws.amazon.com/cdk/v2/guide/identifiers.html#identifiers_logical_ids) for resources in the solution CDK application when it is synthesizing the underlying CloudFormation templates.
**Important**
Use caution when modifying the `name` property of any configuration item. In doing so, any other configuration items that reference that `name` value must also be updated. Additionally, changing a `name` property value is treated as a resource replacement operation when the Core pipeline runs. Assess [downstream dependencies](#downstream-resource-dependencies) before performing this action.

## Managing resource create, update, and delete actions
<a name="managing-resource-create-update-and-delete-actions"></a>

This solution’s resource orchestration follows the same create, update, and delete workflow as standard CloudFormation templates. These actions are defined in [How does AWS CloudFormation work?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-howdoesitwork.html) in the *AWS CloudFormation User Guide*. This section provides specifics related to translating these behaviors to accelerator configuration file modifications.

Adding a net new configuration block to an accelerator configuration file causes a new resource to be created in the defined AWS Regions and target accounts or OUs. For the configuration items that use the ` [deploymentTargets](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/typedocs/latest/classes/_aws_accelerator_config.DeploymentTargets.html) ` property, your configured resources will be automatically replicated to every Region configured under the ` [enabledRegions](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/typedocs/latest/classes/_aws_accelerator_config.GlobalConfig.html#enabledRegions) ` property of the `global-config.yaml` file. You can explicitly remove target accounts and Regions for `deploymentTargets` by using the `excludedAccounts` and `excludedRegions` properties, respectively.

If you modify or remove a property value of an existing configuration item, an update of the previously deployed resource will occur. Specific update behaviors and constraints are dependent on the underlying resource that is being updated. Before you make updates, we recommend reviewing the configuration reference in the [Services, Features, and Configuration References section](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/user-guide/config/) of the solution’s [GitHub Pages website](https://awslabs.github.io/landing-zone-accelerator-on-aws/) for property updates that result in resource replacement. Making updates that cause resource replacement prior to removing a resource’s [downstream dependencies](#downstream-resource-dependencies) can result in a dependency error during resource replacement.

Removing a configuration block from your configuration results in resource deletion. Please be aware that removing a configuration block prior to removing a resource’s downstream dependencies may result in a dependency error during resource deletion.

## Downstream resource dependencies
<a name="downstream-resource-dependencies"></a>

This solution uses a stack layering strategy for building your landing zone environment. This means that resources provisioned in later stages of the Core pipeline might depend on resources created in earlier stages. When updating the solution configuration files, consider downstream resource dependencies. For additional information about strategizing your resource updates, see [Managing resource dependencies](managing-resource-dependencies.md).

## Existing resources in your environment
<a name="existing-resources-in-your-environment"></a>

If you want to migrate an existing landing zone to use Landing Zone Accelerator on AWS, you might have conflicts between your existing resources and your configured resources in the solution configuration files. See the details in [Working with existing landing zones](working-with-existing-landing-zones.md) for more information.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
