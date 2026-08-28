---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_ExperienceEndpoint.html
---

# ExperienceEndpoint
<a name="API_ExperienceEndpoint"></a>

Provides the configuration information for the endpoint for your Amazon Kendra experience.

## Contents
<a name="API_ExperienceEndpoint_Contents"></a>

 ** Endpoint **   <a name="kendra-Type-ExperienceEndpoint-Endpoint"></a>
The endpoint of your Amazon Kendra experience.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^\P{C}*$`
Required: No

 ** EndpointType **   <a name="kendra-Type-ExperienceEndpoint-EndpointType"></a>
The type of endpoint for your Amazon Kendra experience. The type currently available is `HOME`, which is a unique and fully hosted URL to the home page of your Amazon Kendra experience.
Type: String
Valid Values: `HOME`
Required: No

## See Also
<a name="API_ExperienceEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/ExperienceEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/ExperienceEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/ExperienceEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
