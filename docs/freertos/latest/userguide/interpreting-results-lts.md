---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/interpreting-results-lts.html
---

# Interpret the IDT for FreeRTOS results
<a name="interpreting-results-lts"></a>

The report section in `awsiotdevicetester_report.xml` or `FRQ_Report.xml` lists the results of the tests that are executed.

The first XML tag `<testsuites>` contains the overall summary of the test execution. For example:

 `<testsuites name="FRQ results" time="5633" tests="184" failures="0" errors="0" disabled="0">`

**Attributes used in the `<testsuites>` tag**

** `name` **
The name of the test suite.

** `time` **
The time, in seconds, it took to run the qualification suite.

** `tests` **
The number of test cases executed.

** `failures` **
The number of test cases that were run, but did not pass.

** `errors` **
The number of test cases that IDT for FreeRTOS couldn't execute.

** `disabled` **
This attribute is not used and can be ignored.

If there are no test case failures or errors, your device meets the technical requirements to run FreeRTOS and can interoperate with AWS IoT services. If you choose to list your device in the AWS Partner Device Catalog, you can use this report as qualification evidence.

In the event of test case failures or errors, you can identify the test case that failed by reviewing the `<testsuites>` XML tags. The `<testsuite>` XML tags inside the `<testsuites>` tag shows the test case result summary for a test group.

 `<testsuite name="FreeRTOSVersion" package="" tests="1" failures="0" time="2" disabled="0" errors="0" skipped="0">`

The format is similar to the `<testsuites>` tag, but with an attribute called `skipped` that is not used and can be ignored. Inside each `<testsuite>` XML tag, there are `<testcase>` tags for each of the test cases that were executed for a test group. For example:

 `<testcase classname="FRQ FreeRTOSVersion" name="FreeRTOSVersion" attempts="1"></testcase>`

**Attributes used in the `<awsproduct>` tag**

** `name` **
The name of the product being tested.

** `version` **
The version of the product being tested.

** `features` **
The features validated. Features marked as `required` are required to submit your board for qualification. The following snippet shows how this appears in the `awsiotdevicetester_report.xml` file.

```
<feature name="core-freertos" value="not-supported" type="required"></feature>
```
Features marked as `optional` are not required for qualification. The following snippets show optional features.

```
<feature name="ota-dataplane-mqtt" value="not-supported" type="optional"></feature>
  <feature name="ota-dataplane-http" value="not-supported" type="optional"></feature>
```
If there are no test failures or errors for the required features, your device meets the technical requirements to run FreeRTOS and can interoperate with AWS IoT services. If you want to list your device in the [AWS Partner Device Catalog](https://partners.amazonaws.com/qualified-devices), you can use this report as qualification evidence.
In the event of test failures or errors, you can identify the test that failed by reviewing the `<testsuites>` XML tags. The `<testsuite>` XML tags inside the `<testsuites>` tag show the test result summary for a test group. For example:

```
<testsuite name="FreeRTOSVersion" package="" tests="1" failures="1" time="2" disabled="0" errors="0" skipped="0">
```
The format is similar to the `<testsuites>` tag, but has a `skipped` attribute that is not used and can be ignored. Inside each `<testsuite>` XML tag, there are `<testcase>` tags for each executed test for a test group. For example:

```
<testcase classname="FreeRTOSVersion" name="FreeRTOSVersion"></testcase>
```

**Attributes used in the `<testcase>` tag**

** `name` **
The name of the test case.

** `attempts` **
The number of times IDT for FreeRTOS executed the test case.

When a test fails or an error occurs, `<failure>` or `<error>` tags are added to the `<testcase>` tag with information for troubleshooting. For example:

```
<testcase classname="FRQ FreeRTOSVersion" name="FreeRTOSVersion">
      <failure type="Failure">{{Reason for the test case failure}}</failure>
      <error>{{Reason for the test case execution error}}</error>
  </testcase>
```

For more information, see [Troubleshoot errors](dt-afr-troubleshooting.md).
