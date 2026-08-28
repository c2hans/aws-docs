---
source_url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ExecutionConfiguration.html
---

# ExecutionConfiguration
<a name="API_connect-app-integrations_ExecutionConfiguration"></a>

The configuration for how the files should be pulled from the source.

## Contents
<a name="API_connect-app-integrations_ExecutionConfiguration_Contents"></a>

 ** ExecutionMode **   <a name="connect-Type-connect-app-integrations_ExecutionConfiguration-ExecutionMode"></a>
The mode for data import/export execution.
Type: String
Valid Values: `ON_DEMAND | SCHEDULED`
Required: Yes

 ** OnDemandConfiguration **   <a name="connect-Type-connect-app-integrations_ExecutionConfiguration-OnDemandConfiguration"></a>
The start and end time for data pull from the source.
Type: [OnDemandConfiguration](API_connect-app-integrations_OnDemandConfiguration.md) object
Required: No

 ** ScheduleConfiguration **   <a name="connect-Type-connect-app-integrations_ExecutionConfiguration-ScheduleConfiguration"></a>
The name of the data and how often it should be pulled from the source.
Type: [ScheduleConfiguration](API_connect-app-integrations_ScheduleConfiguration.md) object
Required: No

## See Also
<a name="API_connect-app-integrations_ExecutionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/ExecutionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/ExecutionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/ExecutionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
