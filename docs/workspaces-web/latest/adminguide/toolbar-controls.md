---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/toolbar-controls.html
---

# Managing toolbar controls in Amazon WorkSpaces Secure Browser
<a name="toolbar-controls"></a>

With **Toolbar controls**, you can configure the toolbar presentation for end user sessions, including the following options:
+ **Features**
  + **Clipboard**: When enabled, allows copy/paste with granular controls (copy only, paste only, or both). When disabled, hides icon and prevents usage from the toolbar.
  + **File transfer**: When enabled, allows file operations with granular controls (upload only, download only, or both). When disabled, hides icon and prevents transfers.
  + **Microphone**: When enabled, allows microphone usage. When disabled, hides icon.
  + **Webcam**: When enabled, allows camera usage. When disabled, hides icon.
  + **Dual monitor**: When enabled, allows dual monitor usage. When disabled, hides icon.
  + **Full screen**: When enabled, allows full screen mode. When disabled, hides icon.
  + **Windows**: When enabled, allows moving between windows. When disabled, hides icon.
+ **Settings**
  + **Toolbar theme**: Controls light or dark mode display. Configuration removes end user theme control.
  + **Toolbar state**: Sets docked or detached state of the toolbar. Configuration removes end user control over the toolbar state.
  + **Max resolution**: Defines the highest allowed display resolution. Users can only select resolutions up to this defined limit.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
