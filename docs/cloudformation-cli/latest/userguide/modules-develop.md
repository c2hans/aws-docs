---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/modules-develop.html
---

# Develop a module using the CFN-CLI
<a name="modules-develop"></a>

Follow these basic steps to develop and register a module project.

1. In the CFN-CLI, use the `[init](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-init.html)` command to create a new project. The `init` command creates a `fragments` folder containing a sample fragment file named `sample.json`.

   Follow the prompts. Specify that you want to create a **module(m)**, and enter the module name.

   ```
   $ cfn init
   Initializing new project
   Do you want to develop a new resource(r) a module(m) or a hook(h)?
   >> {{m}}
   What is the name of your module type?
   (<Organization>::<Service>::<Name>::MODULE)
   >> {{My::Sample::SampleBucket::MODULE}}
   ```

1. Include your template fragment in the project.

   In the `fragments` folder in the project, you should find a file named `sample.json`. This is the template fragment file. Author your template fragment in this file and save.

   You can rename this file as necessary. The folder can only contain a single file.

   For more information, see [Creating a module template fragment](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/modules-structure.html#modules-template-fragment).

1. Use `[validate](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-validate.html)` to validate your project. Fix any issues reported.

   The `validate` command regenerates the module schema, based on the template fragment you included in the `fragments` folder. The module schema is located in the root folder, and named `schema.json`.

1. Use `[submit](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html)` to register the module with CloudFormation, in the specified region. Registering a module makes it available for inclusion in CloudFormation templates.
**Note**
When you register your module using `submit`, CloudFormation regenerates your module schema based on the template fragment in your project. You can't specify a schema file directly. To specify a module schema file when registering a module, use `[RegisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html)` in the CloudFormation API.

For information about using modules in CloudFormation templates, see [Create reusable resource configurations with modules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/modules.html) in the *CloudFormation Users Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
