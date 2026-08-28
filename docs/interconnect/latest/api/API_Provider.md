---
source_url: https://docs.aws.amazon.com/interconnect/latest/api/API_Provider.html
---

# Provider
<a name="API_Provider"></a>

Describes the respective AWS Interconnect Partner organization.

## Contents
<a name="API_Provider_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cloudServiceProvider **   <a name="interconnect-Type-Provider-cloudServiceProvider"></a>
The provider's name. Specifically, connections to/from this Cloud Service Provider will be considered Multicloud connections.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Required: No

 ** lastMileProvider **   <a name="interconnect-Type-Provider-lastMileProvider"></a>
The provider's name. Specifically, connections to/from this Last Mile Provider will be considered LastMile connections.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Required: No

## See Also
<a name="API_Provider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/interconnect-2022-07-26/Provider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/interconnect-2022-07-26/Provider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/interconnect-2022-07-26/Provider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Interconnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query interconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
