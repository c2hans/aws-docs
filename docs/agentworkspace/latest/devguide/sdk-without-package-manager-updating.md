---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/sdk-without-package-manager-updating.html
---

# Updating the bundle
<a name="sdk-without-package-manager-updating"></a>

When a new version of the SDK is released:

1. Navigate to your build project directory

1. Update the SDK packages:

   ```
   npm update @amazon-connect/core @amazon-connect/contact @amazon-connect/email
   ```

1. Rebuild the bundle:

   ```
   npm run build
   ```

1. Copy the new bundle to your website

1. Test your application to verify compatibility

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
