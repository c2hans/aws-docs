---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_DocumentAclUser.html
---

# DocumentAclUser
<a name="API_agent-runtime_DocumentAclUser"></a>

A user entry within a document access control list (ACL) condition.

## Contents
<a name="API_agent-runtime_DocumentAclUser_Contents"></a>

 ** id **   <a name="bedrock-Type-agent-runtime_DocumentAclUser-id"></a>
The identifier of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `\P{C}*`
Required: Yes

 ** type **   <a name="bedrock-Type-agent-runtime_DocumentAclUser-type"></a>
The membership type indicating the scope of the user entry.
Type: String
Valid Values: `KNOWLEDGE_BASE | DATA_SOURCE`
Required: Yes

## See Also
<a name="API_agent-runtime_DocumentAclUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/DocumentAclUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/DocumentAclUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/DocumentAclUser)
