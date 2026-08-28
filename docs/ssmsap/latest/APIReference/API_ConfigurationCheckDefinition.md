---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ConfigurationCheckDefinition.html
---

# ConfigurationCheckDefinition
<a name="API_ConfigurationCheckDefinition"></a>

Represents a configuration check definition supported by AWS Systems Manager for SAP.

## Contents
<a name="API_ConfigurationCheckDefinition_Contents"></a>

 ** ApplicableApplicationTypes **   <a name="ssmsap-Type-ConfigurationCheckDefinition-ApplicableApplicationTypes"></a>
The list of SSMSAP application types that this configuration check can be evaluated against.
Type: Array of strings
Valid Values: `HANA | SAP_ABAP`
Required: No

 ** Description **   <a name="ssmsap-Type-ConfigurationCheckDefinition-Description"></a>
A description of what the configuration check validates.
Type: String
Required: No

 ** Id **   <a name="ssmsap-Type-ConfigurationCheckDefinition-Id"></a>
The unique identifier of the configuration check.
Type: String
Valid Values: `SAP_CHECK_01 | SAP_CHECK_02 | SAP_CHECK_03`
Required: No

 ** Name **   <a name="ssmsap-Type-ConfigurationCheckDefinition-Name"></a>
The name of the configuration check.
Type: String
Required: No

## See Also
<a name="API_ConfigurationCheckDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/ConfigurationCheckDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/ConfigurationCheckDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/ConfigurationCheckDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
