---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/lts-open-idt-ui.html
---

# Open the IDT for FreeRTOS UI
<a name="lts-open-idt-ui"></a>

This topic explains how to open the IDT for FreeRTOS UI to use the FreeRTOS qualification suite.

**To open the IDT for FreeRTOS UI**

1. Download a supported IDT for FreeRTOS version. Then extract the downloaded archive to a directory that you have read and write permissions for.

1. Navigate to the IDT for FreeRTOS installation directory:

   ```
   cd {{devicetester-extract-location}}/bin
   ```

1. Run the following command to open the IDT for FreeRTOS UI:

------
#### [ Linux ]

   ```
   .devicetester_ui_linux_x86-64
   ```

------
#### [ Windows ]

   ```
   ./devicetester_ui_win_x64-64
   ```

------
#### [ macOS ]

   ```
   ./devicetester_ui_mac_x86-64
   ```

**Note**
In macOS, to allow your system to run the UI, go to **System Preferences -> Security & Privacy**. When you run the tests, you may need to do this three more times. this

------

   The IDT for FreeRTOS UI opens in your default browser. The latest three major versions of the following browsers support the UI:
   + Google Chrome
   + Mozilla Firefox
   + Microsoft Edge
   + Apple Safari for macOS
**Note**
For a better experience, we recommend Google Chrome or Mozilla Firefox to access the IDT for FreeRTOS UI. Microsoft Internet Explorer isn't supported by the UI.
**Important**
You must configure your AWS credentials before you open the UI. If you haven't configured your credentials, close the IDT for FreeRTOS UI browser window, follow the steps in [Configure AWS credentials to use the IDT UI](lts-configure-aws-credentials.md), and then reopen the IDT for FreeRTOS UI.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
