---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/run-test-suite.html
---

# Run the test suite
<a name="run-test-suite"></a>

After you create your test suite, you want to make sure that it functions as expected. Complete the following steps to run the test suite with your existing device pool to do so.

1. Copy your `MyTestSuite_1.0.0` folder into `{{<device-tester-extract-location>}}/tests`.

1. Run the following commands:

   ```
   cd {{<device-tester-extract-location>}}/bin
   ./devicetester_{{[linux | mac | win_x86-64]}} run-suite --suite-id MyTestSuite
   ```

IDT runs your test suite and streams the results to the console. When the test has finished running, you see the following information:

```
time="2020-10-19T09:24:47-07:00" level=info msg=Using pool: pool
time="2020-10-19T09:24:47-07:00" level=info msg=Using test suite "MyTestSuite_1.0.0" for execution
time="2020-10-19T09:24:47-07:00" level=info msg=b'hello world\n' suiteId=MyTestSuite groupId=myTestGroup testCaseId=myTestCase deviceId=my-device executionId=9a52f362-1227-11eb-86c9-8c8590419f30
time="2020-10-19T09:24:47-07:00" level=info msg=All tests finished. executionId=9a52f362-1227-11eb-86c9-8c8590419f30
time="2020-10-19T09:24:48-07:00" level=info msg=

========== Test Summary ==========
Execution Time:         1s
Tests Completed:        1
Tests Passed:           1
Tests Failed:           0
Tests Skipped:          0
----------------------------------
Test Groups:
    myTestGroup:        PASSED
----------------------------------
Path to AWS IoT Device Tester Report: /path/to/devicetester/results/9a52f362-1227-11eb-86c9-8c8590419f30/awsiotdevicetester_report.xml
Path to Test Execution Logs: /path/to/devicetester/results/9a52f362-1227-11eb-86c9-8c8590419f30/logs
Path to Aggregated JUnit Report: /path/to/devicetester/results/9a52f362-1227-11eb-86c9-8c8590419f30/MyTestSuite_Report.xml
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
