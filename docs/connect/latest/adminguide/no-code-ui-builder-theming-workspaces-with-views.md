---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/no-code-ui-builder-theming-workspaces-with-views.html
---

# Theming Workspaces with Views
<a name="no-code-ui-builder-theming-workspaces-with-views"></a>

When Views are used in the Workspace or agent workspace with custom theming, UI components can inherit workspace themes or use custom styling. Keep in mind a few principles:
+ When a workspace theme is set, a View's global primary color, secondary color, default color and components will inherit workspace-level styling by default when users don't make custom edits.
+ When a view has custom global styles such as primary, secondary, and default colors defined in the UI builder, the custom styling will take precedence over workspace theming.
+ When components have custom styles defined in the UI builder, the component styling will take precedence over workspace theming.
+ Custom component colors are preserved across different workspaces.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
