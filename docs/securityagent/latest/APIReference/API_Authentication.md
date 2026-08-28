---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_Authentication.html
---

# Authentication
<a name="API_Authentication"></a>

The authentication configuration for an actor, specifying the provider type and credentials.

## Contents
<a name="API_Authentication_Contents"></a>

 ** providerType **   <a name="securityagent-Type-Authentication-providerType"></a>
The type of authentication provider. Valid values include SECRETS\_MANAGER, AWS\_LAMBDA, AWS\_IAM\_ROLE, and AWS\_INTERNAL.
Type: String
Valid Values: `SECRETS_MANAGER | AWS_LAMBDA | AWS_IAM_ROLE | AWS_INTERNAL`
Required: No

 ** value **   <a name="securityagent-Type-Authentication-value"></a>
The authentication value, such as a secret ARN, Lambda function ARN, or IAM role ARN, depending on the provider type.
Type: String
Required: No

## See Also
<a name="API_Authentication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/Authentication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/Authentication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/Authentication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
