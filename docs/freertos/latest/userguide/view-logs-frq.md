---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/view-logs-frq.html
---

# View the IDT for FreeRTOS logs
<a name="view-logs-frq"></a>

You can find logs that IDT for FreeRTOS generates from test execution in `{{devicetester-extract-location}}/results/{{execution-id}}/logs`. Two sets of logs are generated:

**`test_manager.log`**
Contains logs generated from IDT for FreeRTOS (for example, logs related configuration and report generation).

**`{{test_group_id}}__{{test_case_id}}.log` (for example, `FullMQTT__Full_MQTT.log`)**
The log file for a test case, including output from the device under test. The log file is named according to the test group and test case that was run.
