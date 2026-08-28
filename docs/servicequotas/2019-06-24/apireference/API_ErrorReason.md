---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ErrorReason.html
---

# ErrorReason
<a name="API_ErrorReason"></a>

An error that explains why an action did not succeed.

## Contents
<a name="API_ErrorReason_Contents"></a>

 ** ErrorCode **   <a name="servicequotas-Type-ErrorReason-ErrorCode"></a>
Service Quotas returns the following error values:
+  `DEPENDENCY_ACCESS_DENIED_ERROR` - The caller does not have the required permissions to complete the action. To resolve the error, you must have permission to access the AWS service or quota.
+  `DEPENDENCY_THROTTLING_ERROR` - The AWS service is throttling Service Quotas.
+  `DEPENDENCY_SERVICE_ERROR` - The AWS service is not available.
+  `SERVICE_QUOTA_NOT_AVAILABLE_ERROR` - There was an error in Service Quotas.
Type: String
Valid Values: `DEPENDENCY_ACCESS_DENIED_ERROR | DEPENDENCY_THROTTLING_ERROR | DEPENDENCY_SERVICE_ERROR | SERVICE_QUOTA_NOT_AVAILABLE_ERROR`
Required: No

 ** ErrorMessage **   <a name="servicequotas-Type-ErrorReason-ErrorMessage"></a>
The error message.
Type: String
Required: No

## See Also
<a name="API_ErrorReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/ErrorReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/ErrorReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/ErrorReason)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Service Quotas. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicequotas` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
