---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DeleteAgent.html
---

# DeleteAgent
<a name="API_DeleteAgent"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

 An object representing the agent or data collector to be deleted along with the optional configurations for error handling.

## Contents
<a name="API_DeleteAgent_Contents"></a>

 ** agentId **   <a name="DiscServ-Type-DeleteAgent-agentId"></a>
 The ID of the agent or data collector to delete.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 20.
Pattern: `\S+`
Required: Yes

 ** force **   <a name="DiscServ-Type-DeleteAgent-force"></a>
 Optional flag used to force delete an agent or data collector. It is needed to delete any agent in HEALTHY/UNHEALTHY/RUNNING status. Note that deleting an agent that is actively reporting health causes it to be re-registered with a different agent ID after data collector re-connects with AWS.
Type: Boolean
Required: No

## See Also
<a name="API_DeleteAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/DeleteAgent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/DeleteAgent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/DeleteAgent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
