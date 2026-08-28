---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/customizing-the-solution.html
---

# Customizing the solution
<a name="customizing-the-solution"></a>

This solution deploys an S3 bucket with six customizable YAML configuration files contained in a single ZIP archive.. The YAML files are pre-populated with a minimal configuration for the solution. You can create an optional seventh configuration file (`customizations-config.yaml`) to define customizations to the core solution. You can customize the YAML configuration files to deploy additional resources and infrastructure to the solution environment. Refer to [Using configuration files](using-configuration-files.md) for more information, and our [sample configuration](https://github.com/awslabs/landing-zone-accelerator-on-aws/tree/main/reference/sample-configurations/lza-sample-config) for an example of sample implementation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
