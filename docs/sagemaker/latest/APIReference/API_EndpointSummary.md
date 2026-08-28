---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EndpointSummary.html
---

# EndpointSummary
<a name="API_EndpointSummary"></a>

Provides summary information for an endpoint.

## Contents
<a name="API_EndpointSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-EndpointSummary-CreationTime"></a>
A timestamp that shows when the endpoint was created.
Type: Timestamp
Required: Yes

 ** EndpointArn **   <a name="sagemaker-Type-EndpointSummary-EndpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:endpoint/.*`
Required: Yes

 ** EndpointName **   <a name="sagemaker-Type-EndpointSummary-EndpointName"></a>
The name of the endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** EndpointStatus **   <a name="sagemaker-Type-EndpointSummary-EndpointStatus"></a>
The status of the endpoint.
+  `OutOfService`: Endpoint is not available to take incoming requests.
+  `Creating`: [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) is executing.
+  `Updating`: [UpdateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html) or [UpdateEndpointWeightsAndCapacities](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpointWeightsAndCapacities.html) is executing.
+  `SystemUpdating`: Endpoint is undergoing maintenance and cannot be updated or deleted or re-scaled until it has completed. This maintenance operation does not change any customer-specified values such as VPC config, KMS encryption, model, instance type, or instance count.
+  `RollingBack`: Endpoint fails to scale up or down or change its variant weight and is in the process of rolling back to its previous configuration. Once the rollback completes, endpoint returns to an `InService` status. This transitional status only applies to an endpoint that has autoscaling enabled and is undergoing variant weight or capacity changes as part of an [UpdateEndpointWeightsAndCapacities](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpointWeightsAndCapacities.html) call or when the [UpdateEndpointWeightsAndCapacities](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpointWeightsAndCapacities.html) operation is called explicitly.
+  `InService`: Endpoint is available to process incoming requests.
+  `Deleting`: [DeleteEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteEndpoint.html) is executing.
+  `Failed`: Endpoint could not be created, updated, or re-scaled. Use `DescribeEndpointOutput$FailureReason` for information about the failure. [DeleteEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteEndpoint.html) is the only operation that can be performed on a failed endpoint.
To get a list of endpoints with a specified status, use the `StatusEquals` filter with a call to [ListEndpoints](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListEndpoints.html).
Type: String
Valid Values: `OutOfService | Creating | Updating | SystemUpdating | RollingBack | InService | Deleting | Failed | UpdateRollbackFailed`
Required: Yes

 ** LastModifiedTime **   <a name="sagemaker-Type-EndpointSummary-LastModifiedTime"></a>
A timestamp that shows when the endpoint was last modified.
Type: Timestamp
Required: Yes

## See Also
<a name="API_EndpointSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EndpointSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EndpointSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EndpointSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
