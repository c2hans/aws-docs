---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GeneratedQuery.html
---

# GeneratedQuery
<a name="API_agent-runtime_GeneratedQuery"></a>

Contains information about a query generated for a natural language query.

## Contents
<a name="API_agent-runtime_GeneratedQuery_Contents"></a>

 ** sql **   <a name="bedrock-Type-agent-runtime_GeneratedQuery-sql"></a>
An SQL query that corresponds to the natural language query.
Type: String
Required: No

 ** type **   <a name="bedrock-Type-agent-runtime_GeneratedQuery-type"></a>
The type of transformed query.
Type: String
Valid Values: `REDSHIFT_SQL`
Required: No

## See Also
<a name="API_agent-runtime_GeneratedQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/GeneratedQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/GeneratedQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/GeneratedQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
