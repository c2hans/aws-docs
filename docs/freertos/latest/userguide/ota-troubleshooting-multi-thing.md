---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/ota-troubleshooting-multi-thing.html
---

# Troubleshoot OTA updates of multiple devices
<a name="ota-troubleshooting-multi-thing"></a>

To perform OTAs on multiple devices (things) using the same firmware image, implement a function (for example `getThingName()`) that retrieves `clientcredentialIOT_THING_NAME` from non-volatile memory. Make sure that this function reads the thing name from a part of non-volatile memory that is not overwritten by the OTA, and that the thing name is provisioned before running the first job. If you are using the JITP flow, you can read the thing name out of your device certificate's common name.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
