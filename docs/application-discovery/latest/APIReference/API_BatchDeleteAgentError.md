---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_BatchDeleteAgentError.html
---

# BatchDeleteAgentError
<a name="API_BatchDeleteAgentError"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

 An object representing the agent or data collector that failed to delete, each containing agentId, errorMessage, and errorCode.

## Contents
<a name="API_BatchDeleteAgentError_Contents"></a>

 ** agentId **   <a name="DiscServ-Type-BatchDeleteAgentError-agentId"></a>
 The ID of the agent or data collector to delete.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 20.
Pattern: `\S+`
Required: Yes

 ** errorCode **   <a name="DiscServ-Type-BatchDeleteAgentError-errorCode"></a>
 The type of error that occurred for the delete failed agent. Valid status are: AGENT\_IN\_USE \| NOT\_FOUND \| INTERNAL\_SERVER\_ERROR.
Type: String
Valid Values: `NOT_FOUND | INTERNAL_SERVER_ERROR | AGENT_IN_USE`
Required: Yes

 ** errorMessage **   <a name="DiscServ-Type-BatchDeleteAgentError-errorMessage"></a>
 The description of the error that occurred for the delete failed agent.
Type: String
Length Constraints: Maximum length of 10000.
Pattern: `[\s\S]*`
Required: Yes

## See Also
<a name="API_BatchDeleteAgentError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/BatchDeleteAgentError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/BatchDeleteAgentError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/BatchDeleteAgentError)
