---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/problem-the-link-command-was-removed-error.html
---

# Problem: "The 'link' command was removed" error
<a name="problem-the-link-command-was-removed-error"></a>

We updated this solution to the newest version of `lerna` which has deprecated the "link" command. CodePipeline stages uses the link command as part of the build process for multiple stages in the pipeline.

## Resolution
<a name="resolution-9"></a>

The latest installer template starting with v1.5.0 removed this command. Upgrades after v1.5.0 will require an update to the installer template to capture all new changes. Follow the [Update the solution](update-the-solution.md) steps to update the installer template and the pipeline will run again resolving the error.
