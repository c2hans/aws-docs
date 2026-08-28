---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_DocumentAcl.html
---

# DocumentAcl
<a name="API_agent-runtime_DocumentAcl"></a>

The access control list for a document, containing allow and deny membership lists. Each list specifies conditions that determine which users and groups are granted or denied access.

## Contents
<a name="API_agent-runtime_DocumentAcl_Contents"></a>

 ** allowList **   <a name="bedrock-Type-agent-runtime_DocumentAcl-allowList"></a>
The list of principals allowed access to the document.
Type: [DocumentAclMembership](API_agent-runtime_DocumentAclMembership.md) object
Required: No

 ** denyList **   <a name="bedrock-Type-agent-runtime_DocumentAcl-denyList"></a>
The list of principals denied access to the document.
Type: [DocumentAclMembership](API_agent-runtime_DocumentAclMembership.md) object
Required: No

## See Also
<a name="API_agent-runtime_DocumentAcl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/DocumentAcl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/DocumentAcl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/DocumentAcl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
