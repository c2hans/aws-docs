---
source_url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_DeploymentSpecificationsField.html
---

# DeploymentSpecificationsField
<a name="API_DeploymentSpecificationsField"></a>

A field that details a specification of a deployment pattern.

## Contents
<a name="API_DeploymentSpecificationsField_Contents"></a>

 ** allowedValues **   <a name="launchwizard-Type-DeploymentSpecificationsField-allowedValues"></a>
The allowed values of the deployment specification.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1500.
Required: No

 ** conditionals **   <a name="launchwizard-Type-DeploymentSpecificationsField-conditionals"></a>
The conditionals used for the deployment specification.
Type: Array of [DeploymentConditionalField](API_DeploymentConditionalField.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** description **   <a name="launchwizard-Type-DeploymentSpecificationsField-description"></a>
The description of the deployment specification.
Type: String
Required: No

 ** name **   <a name="launchwizard-Type-DeploymentSpecificationsField-name"></a>
The name of the deployment specification.
Type: String
Required: No

 ** required **   <a name="launchwizard-Type-DeploymentSpecificationsField-required"></a>
Indicates if the deployment specification is required.
Type: String
Required: No

## See Also
<a name="API_DeploymentSpecificationsField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/launch-wizard-2018-05-10/DeploymentSpecificationsField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/launch-wizard-2018-05-10/DeploymentSpecificationsField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/launch-wizard-2018-05-10/DeploymentSpecificationsField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Launch Wizard. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query launchwizard` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
