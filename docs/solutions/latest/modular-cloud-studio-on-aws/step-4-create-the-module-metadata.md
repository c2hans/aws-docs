---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/step-4-create-the-module-metadata.html
---

# Step 4: Create the module metadata
<a name="step-4-create-the-module-metadata"></a>

MCS needs additional metadata about a module that isn’t part of the native CloudFormation template. The module metadata is stored in the CloudFormation template in the [Metadata](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html) section. The metadata is stored with the template and no linkage is necessary with an external file.

The [module metadata schema](module-metadata-schema.md) requires the following additional information specific to MCS:
+ Module type
+ Module name
+ Dependencies on other modules
+ Module revision number

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
