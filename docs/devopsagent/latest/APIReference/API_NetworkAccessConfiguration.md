---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_NetworkAccessConfiguration.html
---

# NetworkAccessConfiguration
<a name="API_NetworkAccessConfiguration"></a>

Specifies how AWS DevOps Agent reaches your application using a Release Management Environment

## Contents
<a name="API_NetworkAccessConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** privateAccess **   <a name="devopsagent-Type-NetworkAccessConfiguration-privateAccess"></a>
Private network access to the resource inside a VPC, using a private connection.
Type: [PrivateNetworkAccess](API_PrivateNetworkAccess.md) object
Required: No

## See Also
<a name="API_NetworkAccessConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/NetworkAccessConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/NetworkAccessConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/NetworkAccessConfiguration)
