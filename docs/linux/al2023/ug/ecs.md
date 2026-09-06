---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/ecs.html
---

# Using AL2023 based Amazon ECS AMIs to host containerized workloads
<a name="ecs"></a>

**Note**
 For more information on how to use AL2023 inside a container, see [AL2023 in containers](container.md).

 Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service that helps you easily deploy, manage, and scale containerized applications. As a fully managed service, Amazon ECS comes with AWS configuration and operational best practices built-in. It's integrated with both AWS and third-party tools, such as Amazon Elastic Container Registry (Amazon ECR) and Docker. This integration makes it easier for teams to focus on building the applications, not the environment. You can run and scale your container workloads across AWS Regions in the cloud, without the complexity of managing a control plane.

You can host containerized workloads on AL2023 using the AL2023 based Amazon ECS‐optimized AMI. For more information, see the [Amazon ECS-optimized AMI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html)

## Changes in AL2023 for Amazon ECS compared to AL2
<a name="ecs-al2-changes"></a>

 As with AL2, AL2023 provides the base packages required to run as an Amazon ECS Linux instance. In AL2 the `containerd`, `docker`, and `ecs-init` packages were available through `amazon-linux-extras`, whereas AL2023 includes these packages in the core repositories.

 With the deterministic upgrades through versioned repositories feature, every AL2023 AMI by default is locked to a specific repository version. This is also true for the AL2023 Amazon ECS optimized AMI. All updates to your environment can be carefully managed and tested prior to deployment, as well as providing an easy way to revert to the content of a prior AMI in the event of an issue. For more information on this AL2023 feature, see [Deterministic upgrades through versioned repositories on AL2023](deterministic-upgrades.md).

 AL2023 switches to cgroup v2 over the cgroup v1 interface supported in AL2. For more information, see [Unified Control Group hierarchy (cgroup v2)](cgroupv2.md).

**Note**
 AL2023 versions prior to [2023.2.20230920](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.2.20230920.html) (the first AL2023.2 release) contained a bug in `systemd` for Out-of-Memory (OOM) handling inside a cgroup. All processes in the cgroup were always killed instead of the OOM-Killer choosing one process at a time, which is the intended behavior.
 This was a regression when compared to AL2 behavior, and is fixed as of the 2023.2.20230920 release of AL2023.

 The code to build the Amazon ECS-optimized AMI is available on the [amazon-ecs-ami GitHub project](https://github.com/aws/amazon-ecs-ami). The [release notes](https://github.com/aws/amazon-ecs-ami/releases) describe which AL2023 version maps to which Amazon ECS AMI version.

## Customizing the AL2023 based Amazon ECS-optimized AMI
<a name="custom-ecs-amis"></a>

**Important**
 We recommend that you use the Amazon ECS optimized AL2023 AMI. For more information, see [Amazon ECS-optimized AMI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html) in the *Amazon Elastic Container Service Developer Guide*.

 You can use the same build scripts that Amazon ECS uses to create custom AMIs. For more information, see [Amazon ECS-optimized Linux AMI build script](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-ami-build-scripts.html).
