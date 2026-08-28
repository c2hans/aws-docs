---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_HttpVerification.html
---

# HttpVerification
<a name="API_HttpVerification"></a>

Contains HTTP route verification details for a target domain, including the route path and token to serve for domain ownership verification.

## Contents
<a name="API_HttpVerification_Contents"></a>

 ** routePath **   <a name="securityagent-Type-HttpVerification-routePath"></a>
The HTTP route path where the verification token must be served.
Type: String
Required: No

 ** token **   <a name="securityagent-Type-HttpVerification-token"></a>
The verification token to serve at the specified route path.
Type: String
Required: No

## See Also
<a name="API_HttpVerification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/HttpVerification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/HttpVerification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/HttpVerification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
