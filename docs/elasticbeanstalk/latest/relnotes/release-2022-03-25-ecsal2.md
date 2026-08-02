---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-03-25-ecsal2.html
---

# Release: Elastic Beanstalk introduces ECS running on Amazon Linux 2 to Docker platform on March 25, 2022
<a name="release-2022-03-25-ecsal2"></a>

This release introduces a new platform branch based on Amazon Linux 2 to the AWS Elastic Beanstalk Docker platform: **Amazon ECS running on 64bit Amazon Linux 2**.

**Release date:** March 25, 2022

## Changes
<a name="release-2022-03-25-ecsal2.changes"></a>

The following table lists the changes included in this release.

**Note**
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category** | **Description** |
| --- | --- |
| **Platform** | **Update** |
| --- | --- |
| **Platform-specific updates** | Made these platform-specific updates:[See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-03-25-ecsal2.html) |
| **Docker** | Added a new platform branch, **Amazon Elastic Container Service (Amazon ECS) running on Amazon Linux 2**, also known as **ECS AL2.**<br />This platform branch is the Amazon Linux 2 based version of the **Multicontainer Docker** platform branch that runs on Amazon Linux AMI. Like the previous **Multicontainer Docker AL1** version, the new **ECS AL2** platform branch uses Amazon ECS to coordinate a deployment of multiple Docker containers to an Amazon ECS cluster in an Elastic Beanstalk environment. <br />The new **ECS AL2** platform branch supports all of the features in the previous **Multicontainer Docker AL1** platform branch. You can deploy the same source code that's running on the **Multicontainer Docker AL1** platform branch to the new **ECS AL2** platform branch without making any changes.<br />For more information, see [The Docker platform family](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker.html#docker-platform) in the *AWS Elastic Beanstalk Developer Guide*. |

## New platform versions
<a name="release-2022-03-25-ecsal2.platforms"></a>

**Note**
The following tables list all supported platform branches for each platform. Only Amazon Linux 2 platform branches are updated.

**Topics**
+ [Docker](#release-2022-03-25-ecsal2.platforms.docker)

**Note**
Platform version *ECS Amazon Linux 2 version 3.0.0* is running ECS Agent 1.57.1.

### Docker
<a name="release-2022-03-25-ecsal2.platforms.docker"></a>

****

|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker  |  Docker Compose  |  Proxy Server  |
| --- | --- | --- | --- | --- |
|  ** Docker AL2 version 3.4.12** <br /> * 64bit Amazon Linux 2 v3.4.12 running Docker *  | 2.0.20220207 | 20.10.7-5 | 1.29.2 | nginx 1.20.0 |
|  ** ECS AL2 version 3.0.0** <br /> * 64bit Amazon Linux 2 v3.0.0 running ECS *  | 2.0.20220218 |  |  |  |
