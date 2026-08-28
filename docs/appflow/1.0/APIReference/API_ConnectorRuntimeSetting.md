---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ConnectorRuntimeSetting.html
---

# ConnectorRuntimeSetting
<a name="API_ConnectorRuntimeSetting"></a>

Contains information about the connector runtime settings that are required for flow execution.

## Contents
<a name="API_ConnectorRuntimeSetting_Contents"></a>

 ** connectorSuppliedValueOptions **   <a name="appflow-Type-ConnectorRuntimeSetting-connectorSuppliedValueOptions"></a>
Contains default values for the connector runtime setting that are supplied by the connector.
Type: Array of strings
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

 ** dataType **   <a name="appflow-Type-ConnectorRuntimeSetting-dataType"></a>
Data type of the connector runtime setting.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

 ** description **   <a name="appflow-Type-ConnectorRuntimeSetting-description"></a>
A description about the connector runtime setting.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[\s\w/!@#+=.-]*`
Required: No

 ** isRequired **   <a name="appflow-Type-ConnectorRuntimeSetting-isRequired"></a>
Indicates whether this connector runtime setting is required.
Type: Boolean
Required: No

 ** key **   <a name="appflow-Type-ConnectorRuntimeSetting-key"></a>
Contains value information about the connector runtime setting.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: No

 ** label **   <a name="appflow-Type-ConnectorRuntimeSetting-label"></a>
A label used for connector runtime setting.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `.*`
Required: No

 ** scope **   <a name="appflow-Type-ConnectorRuntimeSetting-scope"></a>
Indicates the scope of the connector runtime setting.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

## See Also
<a name="API_ConnectorRuntimeSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ConnectorRuntimeSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ConnectorRuntimeSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ConnectorRuntimeSetting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
