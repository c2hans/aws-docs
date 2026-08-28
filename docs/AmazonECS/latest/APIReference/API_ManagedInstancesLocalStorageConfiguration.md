---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedInstancesLocalStorageConfiguration.html
---

# ManagedInstancesLocalStorageConfiguration
<a name="API_ManagedInstancesLocalStorageConfiguration"></a>

The local storage configuration for Amazon ECS Managed Instances. This defines how ECS uses and configures instance store volumes available on container instance.

## Contents
<a name="API_ManagedInstancesLocalStorageConfiguration_Contents"></a>

 ** useLocalStorage **   <a name="ECS-Type-ManagedInstancesLocalStorageConfiguration-useLocalStorage"></a>
Use instance store volumes for data storage when available. EBS volumes are not provisioned for data storage. If the container instance has multiple instance store volumes, a single data volume is created. Consider defining instance store requirements using the `localStorage`, `localStorageTypes` and `totalLocalStorageGB` properties.
Type: Boolean
Required: No

## See Also
<a name="API_ManagedInstancesLocalStorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedInstancesLocalStorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedInstancesLocalStorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedInstancesLocalStorageConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
