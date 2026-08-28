---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ComplianceByResource.html
---

# ComplianceByResource
<a name="API_ComplianceByResource"></a>

Indicates whether an AWS resource that is evaluated according to one or more AWS Config rules is compliant. A resource is compliant if it complies with all of the rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules.

## Contents
<a name="API_ComplianceByResource_Contents"></a>

 ** Compliance **   <a name="config-Type-ComplianceByResource-Compliance"></a>
Indicates whether the AWS resource complies with all of the AWS Config rules that evaluated it.
Type: [Compliance](API_Compliance.md) object
Required: No

 ** ResourceId **   <a name="config-Type-ComplianceByResource-ResourceId"></a>
The ID of the AWS resource that was evaluated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 768.
Required: No

 ** ResourceType **   <a name="config-Type-ComplianceByResource-ResourceType"></a>
The type of the AWS resource that was evaluated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_ComplianceByResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ComplianceByResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ComplianceByResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ComplianceByResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
