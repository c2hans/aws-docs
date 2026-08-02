---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/tutorial-troubleshooting.html
---

# Troubleshoot errors
<a name="tutorial-troubleshooting"></a>

Use the following information to help resolve any issues with completing the tutorial.

**Test case does not run successfully**

If the test does not run successfully, IDT streams the error logs to the console that can help you troubleshoot the test run. Before you check the error logs, verify the following:
+ The IDT client SDK is in the correct folder as described in [Get the IDT client SDK](add-idt-sdk.md).
+ You meet all the prerequisites for this tutorial. For more information, see [Set up the prerequisites for a simple IDT test suite](prereqs-tutorial-custom.md).

**Cannot connect to the device under test**

Verify the following:
+ Your `device.json` file contains the correct IP address, port, and authentication information.
+ You can connect to your device over SSH from your host computer.
