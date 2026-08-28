---
source_url: https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_ResourceNotFoundException.html
---

# ResourceNotFoundException
<a name="API_ResourceNotFoundException"></a>

The requested resource doesn't exist or could not be found.

This exception occurs when you attempt to access a keyspace, table, stream, or other Amazon Keyspaces resource that doesn't exist or that has been deleted. Verify that the resource identifier is correct and that the resource exists in your account.

HTTP Status Code returned: 400

## Contents
<a name="API_ResourceNotFoundException_Contents"></a>

 ** message **   <a name="keyspaces-Type-ResourceNotFoundException-message"></a>
The requested resource wasn't found. Verify that the resource exists and try again.
Type: String
Required: No

## See Also
<a name="API_ResourceNotFoundException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspacesstreams-2024-09-09/ResourceNotFoundException)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
