---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_HostConfiguration.html
---

# HostConfiguration
<a name="API_HostConfiguration"></a>

Provides a script that runs as a worker is starting up that you can use to provide additional configuration for workers in your fleet.

To remove a script from a fleet, use the [UpdateFleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateFleet.html) operation with the `hostConfiguration` `scriptBody` parameter set to an empty string ("").

## Contents
<a name="API_HostConfiguration_Contents"></a>

 ** scriptBody **   <a name="deadlinecloud-Type-HostConfiguration-scriptBody"></a>
The text of the script that runs as a worker is starting up that you can use to provide additional configuration for workers in your fleet. The script runs after a worker enters the `STARTING` state and before the worker processes tasks.
For more information about using the script, see [Run scripts as an administrator to configure workers](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/smf-admin.html) in the * Deadline Cloud Developer Guide*.
The script runs as an administrative user (`sudo root` on Linux, as an Administrator on Windows).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 15000.
Required: Yes

 ** scriptTimeoutSeconds **   <a name="deadlinecloud-Type-HostConfiguration-scriptTimeoutSeconds"></a>
The maximum time that the host configuration can run. If the timeout expires, the worker enters the `NOT RESPONDING` state and shuts down. You are charged for the time that the worker is running the host configuration script.
You should configure your fleet for a maximum of one worker while testing your host configuration script to avoid starting additional workers.
The default is 300 seconds (5 minutes).
Type: Integer
Valid Range: Minimum value of 300. Maximum value of 3600.
Required: No

## See Also
<a name="API_HostConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/HostConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/HostConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/HostConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
