---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/problem-the-link-command-was-removed-error.html
---

# Problem: "The 'link' command was removed" error
<a name="problem-the-link-command-was-removed-error"></a>

We updated this solution to the newest version of `lerna` which has deprecated the "link" command. CodePipeline stages uses the link command as part of the build process for multiple stages in the pipeline.

## Resolution
<a name="resolution-9"></a>

The latest installer template starting with v1.5.0 removed this command. Upgrades after v1.5.0 will require an update to the installer template to capture all new changes. Follow the [Update the solution](update-the-solution.md) steps to update the installer template and the pipeline will run again resolving the error.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
