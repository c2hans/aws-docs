---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ConflictException.html
---

# ConflictException
<a name="API_ConflictException"></a>

Amazon Keyspaces couldn't complete the requested action. This error may occur if you try to perform an action and the same or a different action is already in progress, or if you try to create a resource that already exists.

HTTP Status Code returned: 400

## Contents
<a name="API_ConflictException_Contents"></a>

 ** message **   <a name="keyspaces-Type-ConflictException-message"></a>
The requested operation conflicts with the current state of the resource or another concurrent operation.
Type: String
Required: No

## See Also
<a name="API_ConflictException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/ConflictException)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces (for Apache Cassandra). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
