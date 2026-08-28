---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ErrorInformation.html
---

# ErrorInformation
<a name="API_ErrorInformation"></a>

Contains error information for a pentest job that encountered an error.

## Contents
<a name="API_ErrorInformation_Contents"></a>

 ** code **   <a name="securityagent-Type-ErrorInformation-code"></a>
The error code. Valid values include CLIENT\_ERROR, INTERNAL\_ERROR, and STOPPED\_BY\_USER.
Type: String
Valid Values: `CLIENT_ERROR | INTERNAL_ERROR | STOPPED_BY_USER`
Required: No

 ** message **   <a name="securityagent-Type-ErrorInformation-message"></a>
A message describing the error.
Type: String
Required: No

## See Also
<a name="API_ErrorInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ErrorInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ErrorInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ErrorInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
