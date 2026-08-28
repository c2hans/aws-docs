---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ResourceNotFoundException.html
---

# ResourceNotFoundException
<a name="API_ResourceNotFoundException"></a>

The requested resource was not found.

HTTP Status Code returned: 404

## Contents
<a name="API_ResourceNotFoundException_Contents"></a>

 ** message **   <a name="novaact-Type-ResourceNotFoundException-message"></a>
The specified resource was not found.
Type: String
Pattern: `[\s\S]+`
Required: Yes

 ** resourceId **   <a name="novaact-Type-ResourceNotFoundException-resourceId"></a>
The identifier of the resource that wasn't found.
Type: String
Pattern: `[\s\S]+`
Required: Yes

 ** resourceType **   <a name="novaact-Type-ResourceNotFoundException-resourceType"></a>
The type of resource that wasn't found.
Type: String
Pattern: `[\s\S]+`
Required: Yes

## See Also
<a name="API_ResourceNotFoundException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/ResourceNotFoundException)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova Act. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova-act` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
