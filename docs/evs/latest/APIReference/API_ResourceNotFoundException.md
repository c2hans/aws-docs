---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_ResourceNotFoundException.html
---

# ResourceNotFoundException
<a name="API_ResourceNotFoundException"></a>

A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a `state` of `DELETED`.

HTTP Status Code returned: 400

## Contents
<a name="API_ResourceNotFoundException_Contents"></a>

 ** message **   <a name="evs-Type-ResourceNotFoundException-message"></a>
Describes the error encountered.
Type: String
Required: Yes

 ** resourceId **   <a name="evs-Type-ResourceNotFoundException-resourceId"></a>
The ID of the resource that could not be found.
Type: String
Required: Yes

 ** resourceType **   <a name="evs-Type-ResourceNotFoundException-resourceType"></a>
The type of the resource that is associated with the error.
Type: String
Required: Yes

## See Also
<a name="API_ResourceNotFoundException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/ResourceNotFoundException)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic VMware Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query evs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
