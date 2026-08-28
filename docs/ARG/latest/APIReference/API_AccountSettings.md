---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_AccountSettings.html
---

# AccountSettings
<a name="API_AccountSettings"></a>

The Resource Groups settings for this AWS account.

## Contents
<a name="API_AccountSettings_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** GroupLifecycleEventsDesiredStatus **   <a name="ARG-Type-AccountSettings-GroupLifecycleEventsDesiredStatus"></a>
The desired target status of the group lifecycle events feature. If
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

 ** GroupLifecycleEventsStatus **   <a name="ARG-Type-AccountSettings-GroupLifecycleEventsStatus"></a>
The current status of the group lifecycle events feature.
Type: String
Valid Values: `ACTIVE | INACTIVE | IN_PROGRESS | ERROR`
Required: No

 ** GroupLifecycleEventsStatusMessage **   <a name="ARG-Type-AccountSettings-GroupLifecycleEventsStatusMessage"></a>
The text of any error message occurs during an attempt to turn group lifecycle events on or off.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_AccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/AccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/AccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/AccountSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups & Tagging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
