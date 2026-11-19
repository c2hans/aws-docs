---
source_url: https://docs.aws.amazon.com/devicefarm/latest/developerguide/reports.html
---

# Reports in AWS Device Farm

The following sections provide information about Device Farm test reports.

**Topics**
+ [Report retention](#reports-retention)
+ [Report components](#reports-components)
+ [Logs in reports](#reports-logs)
+ [Common tasks for reports](#reports-tasks)

## Report retention
<a name="reports-retention"></a>

Device Farm stores your reports for 400 days. These reports include metadata, logs, and screenshots.

## Report components
<a name="reports-components"></a>

Reports in Device Farm contain pass and fail information, crash reports, test and device logs, and screenshots. The report includes detailed per-device data and high-level results, such as the number of occurrences of a given problem.

### Test Insights
<a name="reports-test-insights"></a>

Device Farm generates a **Test Insights** report by default for each run in a custom test environment that uses one of the following frameworks:
+ Appium Java JUnit
+ Appium Java TestNG
+ Appium Node.js
+ Appium Python
+ Android Instrumentation
+ XCTest UI

This includes Appium web app tests. Appium Ruby tests are not supported. The report includes the following information:
+ Passed, failed, skipped, and errored test counts for each job and for each run
+ Detailed test output with timestamps and stack traces for each test, where applicable
+ Median test execution time for each job, and median and average job execution duration for each run

Test Insights helps you understand your test suite performance at both the job and run level. With Test Insights, you get the detailed test reporting of standard mode combined with the faster execution speed of custom mode. For more information about test environments, see [Test environments in AWS Device Farm](test-environments.md).

To configure your tests for Test Insights, see the test report section for your framework:
+ [Configure Appium test reports using a custom test environment](test-types-appium-integrate.md#test-types-appium-generate-reports)
+ [Configure instrumentation test reports using a custom test environment](test-types-android-instrumentation-integrate.md#test-types-android-instrumentation-generate-reports)
+ [Configure XCTest UI test reports using a custom test environment](test-types-ios-xctest-ui.md#test-types-ios-xctest-ui-generate-reports)

To turn off Test Insights for a run, see [Creating a test run in Device Farm](how-to-create-test-run.md).

## Logs in reports
<a name="reports-logs"></a>

Reports include complete logcat captures for Android tests and complete Device Console logs for iOS tests.

## Common tasks for reports
<a name="reports-tasks"></a>

For more information, see [Viewing test reports in Device Farm](how-to-use-reports.md).
