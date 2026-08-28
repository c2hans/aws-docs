---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-app-integrations_ScheduleConfiguration.html
---

# ScheduleConfiguration
<a name="API_connect-app-integrations_ScheduleConfiguration"></a>

The name of the data and how often it should be pulled from the source.

## Contents
<a name="API_connect-app-integrations_ScheduleConfiguration_Contents"></a>

 ** ScheduleExpression **   <a name="connect-Type-connect-app-integrations_ScheduleConfiguration-ScheduleExpression"></a>
How often the data should be pulled from data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*\S.*`
Required: Yes

 ** FirstExecutionFrom **   <a name="connect-Type-connect-app-integrations_ScheduleConfiguration-FirstExecutionFrom"></a>
The start date for objects to import in the first flow run as an Unix/epoch timestamp in milliseconds or in ISO-8601 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*\S.*`
Required: No

 ** Object **   <a name="connect-Type-connect-app-integrations_ScheduleConfiguration-Object"></a>
The name of the object to pull from the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: No

## See Also
<a name="API_connect-app-integrations_ScheduleConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/ScheduleConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/ScheduleConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/ScheduleConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
