---
source_url: https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ConfigurationSummary.html
---

# ConfigurationSummary
<a name="API_ConfigurationSummary"></a>

Details for a Quick Setup configuration.

## Contents
<a name="API_ConfigurationSummary_Contents"></a>

 ** Account **   <a name="quicksetup-Type-ConfigurationSummary-Account"></a>
The ID of the AWS account where the configuration was deployed.
Type: String
Required: No

 ** ConfigurationDefinitionId **   <a name="quicksetup-Type-ConfigurationSummary-ConfigurationDefinitionId"></a>
The ID of the configuration definition.
Type: String
Required: No

 ** CreatedAt **   <a name="quicksetup-Type-ConfigurationSummary-CreatedAt"></a>
The datetime stamp when the configuration was created.
Type: Timestamp
Required: No

 ** FirstClassParameters **   <a name="quicksetup-Type-ConfigurationSummary-FirstClassParameters"></a>
The common parameters and values for the configuration definition.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[A-Za-z0-9+=@_\/\s-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 40960.
Required: No

 ** Id **   <a name="quicksetup-Type-ConfigurationSummary-Id"></a>
A service generated identifier for the configuration.
Type: String
Required: No

 ** ManagerArn **   <a name="quicksetup-Type-ConfigurationSummary-ManagerArn"></a>
The ARN of the configuration manager.
Type: String
Required: No

 ** Region **   <a name="quicksetup-Type-ConfigurationSummary-Region"></a>
The AWS Region where the configuration was deployed.
Type: String
Required: No

 ** StatusSummaries **   <a name="quicksetup-Type-ConfigurationSummary-StatusSummaries"></a>
A summary of the state of the configuration manager. This includes deployment statuses, association statuses, drift statuses, health checks, and more.
Type: Array of [StatusSummary](API_StatusSummary.md) objects
Required: No

 ** Type **   <a name="quicksetup-Type-ConfigurationSummary-Type"></a>
The type of the Quick Setup configuration.
Type: String
Required: No

 ** TypeVersion **   <a name="quicksetup-Type-ConfigurationSummary-TypeVersion"></a>
The version of the Quick Setup type used.
Type: String
Required: No

## See Also
<a name="API_ConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-quicksetup-2018-05-10/ConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-quicksetup-2018-05-10/ConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-quicksetup-2018-05-10/ConfigurationSummary)
