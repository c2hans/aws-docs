---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/create-custom-preset-from-system-preset.html
---

# Creating a preset, based on a system preset
<a name="create-custom-preset-from-system-preset"></a>

MediaConvert doesn't allow you to modify system presets. If you want a preset that is like a system preset but slightly modified, you can duplicate the system preset, customize the settings, and save it as a custom preset.

**To create a custom output preset based on a system preset**

1. Open the [Output presets](https://console.aws.amazon.com/mediaconvert/home#/presets/list) page in the MediaConvert console.

1. In the **Output presets** pane, from the **Presets** dropdown list, choose **System presets**.

1. Choose the name of the system preset that is most like the custom preset that you want to create.

1. On the **Preset details** page, choose **Duplicate**.

1. On the **Create preset** page, specify a name for the new preset. Optionally, modify the description and category.

   These values help you find the custom preset later. For more information see [Listing presets](listing-presets.md).

1. Modify any output settings.

   For more information about each setting, choose the **Info** link that is located next to the setting or next to the heading for the group of settings.

1. Choose the **Create** button at the bottom of the page.
**Note**
This button looks like the **Create** button for creating a job, but in this context, choosing it creates the custom preset.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
