---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_ForbiddenError.html
---

# ForbiddenError
<a name="API_ForbiddenError"></a>

Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.

HTTP Status Code returned: 403

## Contents
<a name="API_ForbiddenError_Contents"></a>

 ** message **   <a name="wickr-Type-ForbiddenError-message"></a>
A message explaining why access was denied and what permissions are required.
Type: String
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_ForbiddenError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/ForbiddenError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
