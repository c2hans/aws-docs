---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceVolumeConfiguration.html
---

# ServiceVolumeConfiguration
<a name="API_ServiceVolumeConfiguration"></a>

The configuration for a volume specified in the task definition as a volume that is configured at launch time. Currently, the only supported volume type is an Amazon EBS volume.

## Contents
<a name="API_ServiceVolumeConfiguration_Contents"></a>

 ** name **   <a name="ECS-Type-ServiceVolumeConfiguration-name"></a>
The name of the volume. This value must match the volume name from the `Volume` object in the task definition.
Type: String
Required: Yes

 ** managedEBSVolume **   <a name="ECS-Type-ServiceVolumeConfiguration-managedEBSVolume"></a>
The configuration for the Amazon EBS volume that Amazon ECS creates and manages on your behalf. These settings are used to create each Amazon EBS volume, with one volume created for each task in the service. The Amazon EBS volumes are visible in your account in the Amazon EC2 console once they are created.
Type: [ServiceManagedEBSVolumeConfiguration](API_ServiceManagedEBSVolumeConfiguration.md) object
Required: No

## See Also
<a name="API_ServiceVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ServiceVolumeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ServiceVolumeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ServiceVolumeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
