---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/idt-test-suite-versions.html
---

# Maintain test suite versions
<a name="idt-test-suite-versions"></a>

IDT for FreeRTOS organizes test resources into test suites and test groups:
+ A test suite is the set of test groups used to verify that a device works with particular versions of FreeRTOS.
+ A test group is the set of individual tests related to a particular feature, such as BLE and MQTT messaging.

Starting in IDT v3.0.0, test suites are versioned using a `major`.`minor`.`patch` format starting from 1.0.0. When you download IDT, the package includes the latest test suite version.

When you start IDT in the command line interface, IDT checks whether a newer test suite version is available. If so, it prompts you to update to the new version. You can choose to update or continue with your current tests.

**Note**
IDT supports the three latest test suite versions for qualification. For more information, see [Understand the support policy for AWS IoT Device Tester](idt-support-policy.md).

You can download test suites by using the `upgrade-test-suite` command. Or, you can use the optional parameter `-upgrade-test-suite {{flag}}` when you start IDT where {{flag}} can be '`y`' to always download the latest version, or '`n`' to use the existing version.

You can also run the `list-supported-versions` command to list the FreeRTOS and test suite versions that are supported by the current version of IDT.

New tests might introduce new IDT configuration settings. If the settings are optional, IDT notifies you and continues running the tests. If the settings are required, IDT notifies you and stops running. After you configure the settings, you can continue to run the tests.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
