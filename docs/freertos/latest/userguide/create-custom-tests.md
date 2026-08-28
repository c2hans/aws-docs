---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/create-custom-tests.html
---

# Tutorial: Develop a simple IDT test suite
<a name="create-custom-tests"></a>

A test suite combines the following:
+ Test executable that contain the test logic
+ Configuration files that describe the test suite

This tutorial shows you how to use IDT for FreeRTOS to develop a Python test suite that contains a single test case. Although this tutorial uses SSH, it is useful to learn how to use AWS IoT Device Tester with FreeRTOS devices.

In this tutorial, you will complete the following steps:

1. [Create a test suite directory](test-suite-dir.md)

1. [Create configuration files](test-suite-json.md)

1. [Create the test case executable](test-suite-exe.md)

1. [Run the test suite](run-test-suite.md)

Follow the steps below to complete a tutorial for developing a simple IDT test suite.

**Topics**
+ [Set up the prerequisites for a simple IDT test suite](prereqs-tutorial-custom.md)
+ [Create a test suite directory](test-suite-dir.md)
+ [Create configuration files](test-suite-json.md)
+ [Get the IDT client SDK](add-idt-sdk.md)
+ [Create the test case executable](test-suite-exe.md)
+ [Configure device information for IDT](configure-idt-sample2.md)
+ [Run the test suite](run-test-suite.md)
+ [Troubleshoot errors](tutorial-troubleshooting.md)
+ [Create IDT test suite configuration files](idt-json-config.md)
+ [Configure the IDT test orchestrator](idt-test-orchestrator.md)
+ [Configure the IDT state machine](idt-state-machine.md)
+ [Create IDT test case executable](test-executables.md)
+ [Use the IDT context](idt-context.md)
+ [Configure settings for test runners](set-config-custom.md)
+ [Debug and run custom test suites](run-tests-custom.md)
+ [Review IDT test results and logs](idt-review-results-logs.md)
+ [Submit IDT usage metrics](idt-usage-metrics.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
