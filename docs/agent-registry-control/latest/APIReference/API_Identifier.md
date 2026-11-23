---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_Identifier.html
---

# Identifier

Identifies a publisher by one of the supported identifier types. A domain name is the only supported type.

## Contents
<a name="API_Identifier_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** domain **   <a name="agentregistrycontrol-Type-Identifier-domain"></a>
The fully qualified domain name of the publisher, such as `example.com`. The name must have at least two labels and can be up to 253 characters long. Domain names aren't case sensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(?=.{1,253}$)([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63}`
Required: No

## See Also
<a name="API_Identifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/Identifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/Identifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/Identifier)
