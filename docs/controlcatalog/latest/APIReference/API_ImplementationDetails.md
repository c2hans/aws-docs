---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ImplementationDetails.html
---

# ImplementationDetails
<a name="API_ImplementationDetails"></a>

An object that describes the implementation type for a control.

Our `ImplementationDetails` `Type` format has three required segments:
+  `SERVICE-PROVIDER::SERVICE-NAME::RESOURCE-NAME`

For example, `AWS::Config::ConfigRule` **or** `AWS::SecurityHub::SecurityControl` resources have the format with three required segments.

Our `ImplementationDetails` `Type` format has an optional fourth segment, which is present for applicable implementation types. The format is as follows:
+  `SERVICE-PROVIDER::SERVICE-NAME::RESOURCE-NAME::RESOURCE-TYPE-DESCRIPTION`

For example, `AWS::Organizations::Policy::SERVICE_CONTROL_POLICY` **or** `AWS::CloudFormation::Type::HOOK` have the format with four segments.

Although the format is similar, the values for the `Type` field do not match any AWS CloudFormation values.

## Contents
<a name="API_ImplementationDetails_Contents"></a>

 ** Type **   <a name="controlcatalog-Type-ImplementationDetails-Type"></a>
A string that describes a control's implementation type.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 2048.
Pattern: `[A-Za-z0-9]+(::[A-Za-z0-9_]+){2,3}`
Required: Yes

 ** Identifier **   <a name="controlcatalog-Type-ImplementationDetails-Identifier"></a>
A service-specific identifier for the control, assigned by the service that implemented the control. For example, this identifier could be an AWS Config Rule ID or a Security Hub Control ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_\.-]+`
Required: No

## See Also
<a name="API_ImplementationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/ImplementationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/ImplementationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/ImplementationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controlcatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
