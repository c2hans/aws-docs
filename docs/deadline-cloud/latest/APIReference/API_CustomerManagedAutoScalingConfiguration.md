---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CustomerManagedAutoScalingConfiguration.html
---

# CustomerManagedAutoScalingConfiguration
<a name="API_CustomerManagedAutoScalingConfiguration"></a>

The auto scaling configuration settings for a customer managed fleet.

## Contents
<a name="API_CustomerManagedAutoScalingConfiguration_Contents"></a>

 ** scaleOutWorkersPerMinute **   <a name="deadlinecloud-Type-CustomerManagedAutoScalingConfiguration-scaleOutWorkersPerMinute"></a>
The number of workers that can be added per minute to the fleet. The default is 10 workers per minute.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2147483647.
Required: No

 ** standbyWorkerCount **   <a name="deadlinecloud-Type-CustomerManagedAutoScalingConfiguration-standbyWorkerCount"></a>
The number of idle workers maintained and ready to process incoming tasks. The default is 0.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** workerIdleDurationSeconds **   <a name="deadlinecloud-Type-CustomerManagedAutoScalingConfiguration-workerIdleDurationSeconds"></a>
The number of seconds that a worker can remain idle before it is shut down. The default is 300 seconds (5 minutes).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

## See Also
<a name="API_CustomerManagedAutoScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CustomerManagedAutoScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CustomerManagedAutoScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CustomerManagedAutoScalingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
