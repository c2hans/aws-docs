---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/tutorial-troubleshooting-custom.html
---

# Troubleshoot errors
<a name="tutorial-troubleshooting-custom"></a>

Use the following information to help resolve any issues with completing the tutorial.

**Test case does not run successfully**
+ If the test does not run successfully, IDT streams the error logs to the console that can help you troubleshoot the test run. Make sure that you meet all the [prerequisites](prereqs-tutorial-sample.md) for this tutorial.

**Cannot connect to the device under test**

Verify the following:
+ Your `device.json` file contains the correct IP address, port, and authentication information.
+ You can connect to your device over SSH from your host computer.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
