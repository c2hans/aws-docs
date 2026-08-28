---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsServicePlacementStrategiesDetails.html
---

# AwsEcsServicePlacementStrategiesDetails
<a name="API_AwsEcsServicePlacementStrategiesDetails"></a>

A placement strategy that determines how to place the tasks for the service.

## Contents
<a name="API_AwsEcsServicePlacementStrategiesDetails_Contents"></a>

 ** Field **   <a name="securityhub-Type-AwsEcsServicePlacementStrategiesDetails-Field"></a>
The field to apply the placement strategy against.
For the `spread` placement strategy, valid values are `instanceId` (or `host`, which has the same effect), or any platform or custom attribute that is applied to a container instance, such as `attribute:ecs.availability-zone`.
For the `binpack` placement strategy, valid values are `cpu` and `memory`.
For the `random` placement strategy, this attribute is not used.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-AwsEcsServicePlacementStrategiesDetails-Type"></a>
The type of placement strategy.
The `random` placement strategy randomly places tasks on available candidates.
The `spread` placement strategy spreads placement across available candidates evenly based on the value of `Field`.
The `binpack` strategy places tasks on available candidates that have the least available amount of the resource that is specified in `Field`.
Valid values: `random` \| `spread` \| `binpack`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsServicePlacementStrategiesDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsServicePlacementStrategiesDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsServicePlacementStrategiesDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsServicePlacementStrategiesDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
