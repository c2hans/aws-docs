---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ApplicationSummary.html
---

# ApplicationSummary
<a name="API_ApplicationSummary"></a>

Contains summary information about an application.

## Contents
<a name="API_ApplicationSummary_Contents"></a>

 ** applicationId **   <a name="securityagent-Type-ApplicationSummary-applicationId"></a>
The unique identifier of the application.
Type: String
Required: Yes

 ** applicationName **   <a name="securityagent-Type-ApplicationSummary-applicationName"></a>
The name of the application.
Type: String
Required: Yes

 ** domain **   <a name="securityagent-Type-ApplicationSummary-domain"></a>
The domain associated with the application.
Type: String
Required: Yes

 ** defaultKmsKeyId **   <a name="securityagent-Type-ApplicationSummary-defaultKmsKeyId"></a>
The identifier of the default AWS KMS key used to encrypt data for the application.
Type: String
Required: No

## See Also
<a name="API_ApplicationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ApplicationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ApplicationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ApplicationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
