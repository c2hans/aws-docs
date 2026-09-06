---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/lts-run-tests-from-ui.html
---

# Run qualification tests
<a name="lts-run-tests-from-ui"></a>

After you create a configuration for the IDT for FreeRTOS UI you can run your qualification tests.

**To run qualification tests**

1. In the navigation menu, choose **Run tests**.

1. Choose **Start tests** to start the test run. By default, all applicable tests are run for your device configuration. IDT for FreeRTOS generates a qualification report when all tests finish.
![Device Tester for FreeRTOS interface showing no tests run yet, with options to create new configuration, edit existing configuration, and run tests.](http://docs.aws.amazon.com/freertos/latest/userguide/images/idt-run-tests.png)

IDT for FreeRTOS runs the qualification tests. It then displays the test run summary and any errors in the **Test runner** console. After the test run is complete, you can view the test results and logs from the following locations:
+ Test results are located in the `{{devicetester-extract-location}}/results/{{execution-id}}` directory.
+ Test logs are located in the `{{devicetester-extract-location}}/results/{{execution-id}}/logs` directory.

For more information about test results and logs, see [View the IDT for FreeRTOSresults](view-results-lts.md) and [View the IDT for FreeRTOSlogs](view-logs-lts.md).

![Device Tester for FreeRTOS execution log showing tests passed, test groups, and file paths for logs and reports.](http://docs.aws.amazon.com/freertos/latest/userguide/images/idt-results.png)
