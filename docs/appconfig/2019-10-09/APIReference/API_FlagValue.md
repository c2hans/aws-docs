---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_FlagValue.html
---

# FlagValue
<a name="API_FlagValue"></a>

The feature flag value configuration for a treatment, including the enabled state and attribute values.

## Contents
<a name="API_FlagValue_Contents"></a>

 ** Enabled **   <a name="appconfig-Type-FlagValue-Enabled"></a>
Specifies whether the feature flag is enabled for this treatment.
Type: Boolean
Required: Yes

 ** AttributeValues **   <a name="appconfig-Type-FlagValue-AttributeValues"></a>
The attribute values associated with this flag value.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 25 items.
Key Pattern: `(?!enabled$)[a-z][a-zA-Z0-9_-]{0,63}`
Required: No

## See Also
<a name="API_FlagValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/FlagValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/FlagValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/FlagValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
