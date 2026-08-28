---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/step-5-create-the-module-manifest.html
---

# Step 5: Create the module manifest
<a name="step-5-create-the-module-manifest"></a>

To track MCS module updates, you must list module revisions in an external [module manifest](module-manifest-schema.md) file. The module manifest must be accessible so that MCS can read it. There is only a single manifest file per module. When you publish a new revision of a module, update the manifest to reflect that a new revision is available.

The [module manifest schema](module-manifest-schema.md) must meet the following requirements:
+ Be in JSON format
+ Include the following:
  + Name of the module author/owner (company name)
  + Description text
  + Optional URL to the web page with more information about the module
  + Module name
  + Module category (Network, Identity, WorkstationManagement, Storage, PixelStreaming, or Custom)
+ Contain an array of revisions, each of which:
  + Specifies the URL(s) to the CloudFormation template:
    + Use `TemplateUrl` when the hub and spoke modules share the same template.
    + Use `TemplateUrls` when the hub and spoke modules have separate templates, or for hub-only modules.

**Note**
 **Note:** These two fields are mutually exclusive.
+ Includes the revision number.
+ Includes compatibility information specifying which revisions of MCS it is compatible with.
+ Contains details about what’s new in the revision.

When registering a new external module, the MCS admin user only requires the URL of the module manifest file. Optionally, the user can also specify a revision number to access a specific revision of the module. If the revision is not supplied, MCS assumes that the user needs the latest compatible revision of the module.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
