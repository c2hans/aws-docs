---
source_url: https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ConfigurationManagerSummary.html
---

# ConfigurationManagerSummary
<a name="API_ConfigurationManagerSummary"></a>

A summary of a Quick Setup configuration manager.

## Contents
<a name="API_ConfigurationManagerSummary_Contents"></a>

 ** ManagerArn **   <a name="quicksetup-Type-ConfigurationManagerSummary-ManagerArn"></a>
The ARN of the Quick Setup configuration.
Type: String
Required: Yes

 ** ConfigurationDefinitionSummaries **   <a name="quicksetup-Type-ConfigurationManagerSummary-ConfigurationDefinitionSummaries"></a>
A summary of the Quick Setup configuration definition.
Type: Array of [ConfigurationDefinitionSummary](API_ConfigurationDefinitionSummary.md) objects
Required: No

 ** Description **   <a name="quicksetup-Type-ConfigurationManagerSummary-Description"></a>
The description of the configuration.
Type: String
Required: No

 ** Name **   <a name="quicksetup-Type-ConfigurationManagerSummary-Name"></a>
The name of the configuration
Type: String
Required: No

 ** StatusSummaries **   <a name="quicksetup-Type-ConfigurationManagerSummary-StatusSummaries"></a>
Summaries of the state of the configuration manager. These summaries include an aggregate of the statuses from the configuration definition associated with the configuration manager. This includes deployment statuses, association statuses, drift statuses, health checks, and more.
Type: Array of [StatusSummary](API_StatusSummary.md) objects
Required: No

## See Also
<a name="API_ConfigurationManagerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-quicksetup-2018-05-10/ConfigurationManagerSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-quicksetup-2018-05-10/ConfigurationManagerSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-quicksetup-2018-05-10/ConfigurationManagerSummary)
