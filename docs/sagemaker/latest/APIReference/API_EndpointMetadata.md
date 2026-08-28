---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EndpointMetadata.html
---

# EndpointMetadata
<a name="API_EndpointMetadata"></a>

The metadata of the endpoint.

## Contents
<a name="API_EndpointMetadata_Contents"></a>

 ** EndpointName **   <a name="sagemaker-Type-EndpointMetadata-EndpointName"></a>
The name of the endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** EndpointConfigName **   <a name="sagemaker-Type-EndpointMetadata-EndpointConfigName"></a>
The name of the endpoint configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** EndpointStatus **   <a name="sagemaker-Type-EndpointMetadata-EndpointStatus"></a>
 The status of the endpoint. For possible values of the status of an endpoint, see [EndpointSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EndpointSummary.html).
Type: String
Valid Values: `OutOfService | Creating | Updating | SystemUpdating | RollingBack | InService | Deleting | Failed | UpdateRollbackFailed`
Required: No

 ** FailureReason **   <a name="sagemaker-Type-EndpointMetadata-FailureReason"></a>
 If the status of the endpoint is `Failed`, or the status is `InService` but update operation fails, this provides the reason why it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_EndpointMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EndpointMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EndpointMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EndpointMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
