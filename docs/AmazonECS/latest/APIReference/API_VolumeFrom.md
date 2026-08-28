---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_VolumeFrom.html
---

# VolumeFrom
<a name="API_VolumeFrom"></a>

Details on a data volume from another container in the same task definition.

## Contents
<a name="API_VolumeFrom_Contents"></a>

 ** readOnly **   <a name="ECS-Type-VolumeFrom-readOnly"></a>
If this value is `true`, the container has read-only access to the volume. If this value is `false`, then the container can write to the volume. The default value is `false`.
Type: Boolean
Required: No

 ** sourceContainer **   <a name="ECS-Type-VolumeFrom-sourceContainer"></a>
The name of another container within the same task definition to mount volumes from.
Type: String
Required: No

## See Also
<a name="API_VolumeFrom_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/VolumeFrom)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/VolumeFrom)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/VolumeFrom)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
