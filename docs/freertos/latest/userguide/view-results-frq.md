---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/view-results-frq.html
---

# View the IDT for FreeRTOS results
<a name="view-results-frq"></a>

While running, IDT writes errors to the console, log files, and test reports. After IDT completes the qualification test suite, it writes a test run summary to the console and generates two test reports. These reports can be found in `{{devicetester-extract-location}}/results/{{execution-id}}/`. Both reports capture the results from the qualification test suite execution.

The `awsiotdevicetester_report.xml` is the qualification test report that you submit to AWS to list your device in the AWS Partner Device Catalog. The report contains the following elements:
+ The IDT for FreeRTOS version.
+ The FreeRTOS version that was tested.
+ The features of FreeRTOS that are supported by the device based on the tests passed.
+ The SKU and the device name specified in the `device.json` file.
+ The features of the device specified in the `device.json` file.
+ The aggregate summary of test case results.
+ A breakdown of test case results by libraries that were tested based on the device features (for example, FullWiFi, FullMQTT, and so on).
+ Whether this qualification of FreeRTOS is for version 202012.00 that uses LTS libraries.

The `FRQ_Report.xml` is a report in standard [JUnit XML format](https://llg.cubic.org/docs/junit/). You can integrate it into CI/CD platforms like [Jenkins](https://jenkins.io/), [Bamboo](https://www.atlassian.com/software/bamboo), and so on. The report contains the following elements:
+ An aggregate summary of test case results.
+ A breakdown of test case results by libraries that were tested based on the device features.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
