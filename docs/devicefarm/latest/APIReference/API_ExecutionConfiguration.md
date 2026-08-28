---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ExecutionConfiguration.html
---

# ExecutionConfiguration
<a name="API_ExecutionConfiguration"></a>

Represents configuration information about a test run, such as the execution timeout (in minutes).

## Contents
<a name="API_ExecutionConfiguration_Contents"></a>

 ** accountsCleanup **   <a name="devicefarm-Type-ExecutionConfiguration-accountsCleanup"></a>
True if account cleanup is enabled at the beginning of the test. Otherwise, false.
Type: Boolean
Required: No

 ** appPackagesCleanup **   <a name="devicefarm-Type-ExecutionConfiguration-appPackagesCleanup"></a>
True if app package cleanup is enabled at the beginning of the test. Otherwise, false.
Type: Boolean
Required: No

 ** jobTimeoutMinutes **   <a name="devicefarm-Type-ExecutionConfiguration-jobTimeoutMinutes"></a>
The number of minutes a test run executes before it times out.
Type: Integer
Required: No

 ** skipAppResign **   <a name="devicefarm-Type-ExecutionConfiguration-skipAppResign"></a>
When set to `true`, for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.
For more information about how Device Farm re-signs your apps, see [Do you modify my app?](http://aws.amazon.com/device-farm/faqs/) in the *AWS Device Farm FAQs*.
Type: Boolean
Required: No

 ** videoCapture **   <a name="devicefarm-Type-ExecutionConfiguration-videoCapture"></a>
Set to true to enable video capture. Otherwise, set to false. The default is true.
Type: Boolean
Required: No

## See Also
<a name="API_ExecutionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ExecutionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ExecutionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ExecutionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
