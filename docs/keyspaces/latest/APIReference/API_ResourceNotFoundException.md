---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ResourceNotFoundException.html
---

# ResourceNotFoundException
<a name="API_ResourceNotFoundException"></a>

The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be `ACTIVE`.

HTTP Status Code returned: 400

## Contents
<a name="API_ResourceNotFoundException_Contents"></a>

 ** message **   <a name="keyspaces-Type-ResourceNotFoundException-message"></a>
The specified resource was not found. Verify the resource identifier and ensure the resource exists and is in an ACTIVE state.
Type: String
Required: No

 ** resourceArn **   <a name="keyspaces-Type-ResourceNotFoundException-resourceArn"></a>
The unique identifier in the format of Amazon Resource Name (ARN) for the resource couldn't be found.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1000.
Pattern: `arn:(aws[a-zA-Z0-9-]*):cassandra:.+.*`
Required: No

## See Also
<a name="API_ResourceNotFoundException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/ResourceNotFoundException)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces (for Apache Cassandra). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
