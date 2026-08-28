---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_Identity.html
---

# Identity
<a name="API_streams_Identity"></a>

Contains details about the type of identity that made the request.

## Contents
<a name="API_streams_Identity_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** PrincipalId **   <a name="DDB-Type-streams_Identity-PrincipalId"></a>
A unique identifier for the entity that made the call. For Time To Live, the principalId is "dynamodb.amazonaws.com".
Type: String
Required: No

 ** Type **   <a name="DDB-Type-streams_Identity-Type"></a>
The type of the identity. For Time To Live, the type is "Service".
Type: String
Required: No

## See Also
<a name="API_streams_Identity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/streams-dynamodb-2012-08-10/Identity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/streams-dynamodb-2012-08-10/Identity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/streams-dynamodb-2012-08-10/Identity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
