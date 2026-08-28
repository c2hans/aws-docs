---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_EBSTagSpecification.html
---

# EBSTagSpecification
<a name="API_EBSTagSpecification"></a>

The tag specifications of an Amazon EBS volume.

## Contents
<a name="API_EBSTagSpecification_Contents"></a>

 ** resourceType **   <a name="ECS-Type-EBSTagSpecification-resourceType"></a>
The type of volume resource.
Type: String
Valid Values: `volume`
Required: Yes

 ** propagateTags **   <a name="ECS-Type-EBSTagSpecification-propagateTags"></a>
Determines whether to propagate the tags from the task definition to the Amazon EBS volume. Tags can only propagate to a `SERVICE` specified in `ServiceVolumeConfiguration`. If no value is specified, the tags aren't propagated.
Type: String
Valid Values: `TASK_DEFINITION | SERVICE | NONE`
Required: No

 ** tags **   <a name="ECS-Type-EBSTagSpecification-tags"></a>
The tags applied to this Amazon EBS volume. `AmazonECSCreated` and `AmazonECSManaged` are reserved tags that can't be used.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_EBSTagSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/EBSTagSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/EBSTagSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/EBSTagSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
