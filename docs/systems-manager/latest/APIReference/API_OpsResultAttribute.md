---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_OpsResultAttribute.html
---

# OpsResultAttribute
<a name="API_OpsResultAttribute"></a>

The OpsItem data type to return.

## Contents
<a name="API_OpsResultAttribute_Contents"></a>

 ** TypeName **   <a name="systemsmanager-Type-OpsResultAttribute-TypeName"></a>
Name of the data type. Valid value: `AWS:OpsItem`, `AWS:EC2InstanceInformation`, `AWS:OpsItemTrendline`, or `AWS:ComplianceSummary`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(AWS|Custom):.*$`
Required: Yes

## See Also
<a name="API_OpsResultAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/OpsResultAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/OpsResultAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/OpsResultAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
