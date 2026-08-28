---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateError.html
---

# UpdateError
<a name="API_UpdateError"></a>

A structure containing information about one error encountered while performing an [UpdatePermissions](https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdatePermissions.html) operation.

## Contents
<a name="API_UpdateError_Contents"></a>

 ** causedBy **   <a name="ManagedGrafana-Type-UpdateError-causedBy"></a>
Specifies which permission update caused the error.
Type: [UpdateInstruction](API_UpdateInstruction.md) object
Required: Yes

 ** code **   <a name="ManagedGrafana-Type-UpdateError-code"></a>
The error code.
Type: Integer
Valid Range: Minimum value of 100. Maximum value of 999.
Required: Yes

 ** message **   <a name="ManagedGrafana-Type-UpdateError-message"></a>
The message for this error.
Type: String
Required: Yes

## See Also
<a name="API_UpdateError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/UpdateError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/UpdateError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/UpdateError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
