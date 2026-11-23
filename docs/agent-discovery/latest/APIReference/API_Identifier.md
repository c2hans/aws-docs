---
source_url: https://docs.aws.amazon.com/agent-discovery/latest/APIReference/API_Identifier.html
---

# Identifier

The identifier of a record. Exactly one member is set.

## Contents
<a name="API_Identifier_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** domain **   <a name="agentdiscovery-Type-Identifier-domain"></a>
The verified domain of the publisher, such as `example.com`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(?=.{1,253}$)([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63}`
Required: No

 ** uri **   <a name="agentdiscovery-Type-Identifier-uri"></a>
A resolvable URI, such as a URN, URL, or DID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_Identifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-discovery-2022-07-26/Identifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-discovery-2022-07-26/Identifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-discovery-2022-07-26/Identifier)
