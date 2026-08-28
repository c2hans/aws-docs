---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-create.html
---

# Create an application inference profile
<a name="inference-profiles-create"></a>

You can create an application inference profile with one or more Regions to track usage and costs when invoking a model.
+ To create an application inference profile for one Region, specify a foundation model. Usage and costs for requests made to that Region with that model will be tracked.
+ To create an application inference profile for multiple Regions, specify a cross Region (system-defined) inference profile. The inference profile will route requests to the Regions defined in the cross Region (system-defined) inference profile that you choose. Usage and costs for requests made to the Regions in the inference profile will be tracked.

You can create an application inference profile using the Amazon Bedrock console or the Amazon Bedrock API.

To create an inference profile using the API, send a [CreateInferenceProfile](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateInferenceProfile.html) request with an [Amazon Bedrock control plane endpoint](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#br-cp).

The following fields are required:

| Field | Use case |
| --- | --- |
| inferenceProfileName | To specify a name for the inference profile. |
| modelSource | To specify the foundation model or cross Region (system-defined) inference profile that defines the model and Regions for which you want to track costs and usage. |

The following fields are optional:

| Field | Use case |
| --- | --- |
| description | To provide a description for the inference profile. |
| tags | To attach tags to the inference profile. For more information, see [Tagging Amazon Bedrock resources](tagging.md) and [Organizing and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html). |
| clientRequestToken | To ensure the API request completes only once. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html). |

The response returns an `inferenceProfileArn` that can be used in other inference profile-related actions and that can be used with model invocation and Amazon Bedrock resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
