---
source_url: https://docs.aws.amazon.com/fis/latest/userguide/troubleshooting.html
---

# Troubleshooting AWS FIS
<a name="troubleshooting"></a>

To troubleshoot errors, AWS FIS returns detailed errors from the `GetExperiment` API and FIS experiment logs. Errors are returned as part of the experiment state when the status of the experiment is **failed**. When multiple actions fail, the first failed action is returned as the experiment error. You can review your FIS experiment logs for any other errors. To learn how to log and monitor AWS FIS experiments, see [Monitoring AWS FIS experiments](monitoring-experiments.md).

Depending on the type of failure, you may receive one of the following errors:
+ **Reason:** Detailed description of the specific failure. Reason values should not be used for automation, as they are subject to change.
+ **Code:** The type of failure. Code values should not be used for automation, as they are subject to change, unless otherwise specified in table below.
+ **Location:** Context for the section of the experiment template that failed, such as the action or target.
+ **Account ID:** The AWS Account where the failure occurred.

## Error codes
<a name="error-codes"></a>

| **Error Code** | **Code Description** |
| --- | --- |
| `ConfigurationFailure` | The action, target, experiment, or log is not configured correctly. Check the error `location` and ensure that the parameters and configurations are correct. |
| `DependentServiceFailure` | There was a failure from another AWS service. Try running the experiment again. |
| `InternalFailure` | An internal error occurred when running the experiment. You can automate based on this error code. |
| `InvalidTarget` | A target was unable to be resolved during target resolution or at the start of an action. This may be due to one of the following reasons:[See the AWS documentation website for more details](http://docs.aws.amazon.com/fis/latest/userguide/troubleshooting.html)<br />To troubleshoot, review your logs to identify which targets are not resolved. Check that all actions are linked to targets, and that your resource ID or tags exist and have not been misspelled. |
| `AuthorizationFailure` | There are two primary causes for experiment failure due to permissions errors:[See the AWS documentation website for more details](http://docs.aws.amazon.com/fis/latest/userguide/troubleshooting.html) |
| `QuotaExceededFailure` | The quota for the resource type has been exceeded. To determine if the quota can be increased, see [Quotas and limitations for AWS Fault Injection Service](fis-quotas.md). |
