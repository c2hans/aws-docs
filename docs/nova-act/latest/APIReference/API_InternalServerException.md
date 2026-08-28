---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_InternalServerException.html
---

# InternalServerException
<a name="API_InternalServerException"></a>

An internal server error occurred. Please try again later.

HTTP Status Code returned: 500

## Contents
<a name="API_InternalServerException_Contents"></a>

 ** message **   <a name="novaact-Type-InternalServerException-message"></a>
The service encountered an internal error. Try again later.
Type: String
Pattern: `[\s\S]+`
Required: Yes

 ** reason **   <a name="novaact-Type-InternalServerException-reason"></a>
The reason for the internal server error.
Type: String
Valid Values: `InvalidModelGeneration | RequestTokenLimitExceeded`
Required: No

 ** Retry-After **   <a name="novaact-Type-InternalServerException-retryAfterSeconds"></a>
The number of seconds to wait before retrying the request.
Type: Integer
Required: No

## See Also
<a name="API_InternalServerException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/InternalServerException)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova Act. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova-act` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
