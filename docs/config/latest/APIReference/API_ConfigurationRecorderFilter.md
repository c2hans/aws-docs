---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationRecorderFilter.html
---

# ConfigurationRecorderFilter
<a name="API_ConfigurationRecorderFilter"></a>

Filters configuration recorders by recording scope.

## Contents
<a name="API_ConfigurationRecorderFilter_Contents"></a>

 ** filterName **   <a name="config-Type-ConfigurationRecorderFilter-filterName"></a>
The name of the type of filter. Currently, only `recordingScope` is supported.
Type: String
Valid Values: `recordingScope`
Required: No

 ** filterValue **   <a name="config-Type-ConfigurationRecorderFilter-filterValue"></a>
The value of the filter. For `recordingScope`, valid values include: `INTERNAL` and `PAID`.
 `INTERNAL` indicates that the [ConfigurationItems](https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationItem.html) in scope for the configuration recorder are recorded for free.
 `PAID` indicates that the [ConfigurationItems](https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationItem.html) in scope for the configuration recorder impact the costs to your bill.
Type: Array of strings
Pattern: `^[0-9a-zA-Z\\*\\.\\\/\\?-]*$`
Required: No

## See Also
<a name="API_ConfigurationRecorderFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConfigurationRecorderFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConfigurationRecorderFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConfigurationRecorderFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
