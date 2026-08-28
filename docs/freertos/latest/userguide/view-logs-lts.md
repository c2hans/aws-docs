---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/view-logs-lts.html
---

# View the IDT for FreeRTOSlogs
<a name="view-logs-lts"></a>

You can find logs that IDT for FreeRTOS generates from test execution in `{{devicetester-extract-location}}/results/{{execution-id}}/logs`. Two sets of logs are generated:
+ `test_manager.log`

   Contains logs generated from IDT for FreeRTOS (for example, logs related configuration and report generation).
+  `{{test_group_id}}/{{test_case_id}}/{{test_case_id}}.log`

  The log file for a test case, including output from the device under test. The log file is named according to the test group and test case that was run.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
