---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ApiRequestBody.html
---

# ApiRequestBody
<a name="API_agent-runtime_ApiRequestBody"></a>

The request body to provide for the API request, as the agent elicited from the user.

This data type is used in the following API operations:
+  [InvokeAgent response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html#API_agent-runtime_InvokeAgent_ResponseSyntax)

## Contents
<a name="API_agent-runtime_ApiRequestBody_Contents"></a>

 ** content **   <a name="bedrock-Type-agent-runtime_ApiRequestBody-content"></a>
The content of the request body. The key of the object in this field is a media type defining the format of the request body.
Type: String to [PropertyParameters](API_agent-runtime_PropertyParameters.md) object map
Required: No

## See Also
<a name="API_agent-runtime_ApiRequestBody_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ApiRequestBody)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ApiRequestBody)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ApiRequestBody)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
