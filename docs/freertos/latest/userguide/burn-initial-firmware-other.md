---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/burn-initial-firmware-other.html
---

# Install the initial version of firmware on a custom board
<a name="burn-initial-firmware-other"></a>

Using your IDE, build the `aws_demos` project, making sure to include the OTA library. For more information about the structure of the FreeRTOS source code, see [FreeRTOS demos](freertos-next-steps.md).

Make sure to include your code-signing certificate, private key, and certificate trust chain either in the FreeRTOS project or on your device.

Using the appropriate tool, burn the application onto your board and make sure it is running correctly.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
