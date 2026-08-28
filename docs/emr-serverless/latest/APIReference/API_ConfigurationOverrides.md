---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ConfigurationOverrides.html
---

# ConfigurationOverrides
<a name="API_ConfigurationOverrides"></a>

A configuration specification to be used to override existing configurations.

## Contents
<a name="API_ConfigurationOverrides_Contents"></a>

 ** applicationConfiguration **   <a name="emrserverless-Type-ConfigurationOverrides-applicationConfiguration"></a>
The override configurations for the application.
Type: Array of [Configuration](API_Configuration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** diskEncryptionConfiguration **   <a name="emrserverless-Type-ConfigurationOverrides-diskEncryptionConfiguration"></a>
The override configuration to encrypt local disks.
Type: [DiskEncryptionConfiguration](API_DiskEncryptionConfiguration.md) object
Required: No

 ** monitoringConfiguration **   <a name="emrserverless-Type-ConfigurationOverrides-monitoringConfiguration"></a>
The override configurations for monitoring.
Type: [MonitoringConfiguration](API_MonitoringConfiguration.md) object
Required: No

## See Also
<a name="API_ConfigurationOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/ConfigurationOverrides)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/ConfigurationOverrides)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/ConfigurationOverrides)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
