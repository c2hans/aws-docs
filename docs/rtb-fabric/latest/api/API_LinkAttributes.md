---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_LinkAttributes.html
---

# LinkAttributes
<a name="API_LinkAttributes"></a>

Describes the attributes of a link.

## Contents
<a name="API_LinkAttributes_Contents"></a>

 ** customerProvidedId **   <a name="rtbfabric-Type-LinkAttributes-customerProvidedId"></a>
The customer-provided unique identifier of the link.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** responderErrorMasking **   <a name="rtbfabric-Type-LinkAttributes-responderErrorMasking"></a>
Describes the masking for HTTP error codes.
Type: Array of [ResponderErrorMaskingForHttpCode](API_ResponderErrorMaskingForHttpCode.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## See Also
<a name="API_LinkAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/LinkAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/LinkAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/LinkAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RTB Fabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rtb-fabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
