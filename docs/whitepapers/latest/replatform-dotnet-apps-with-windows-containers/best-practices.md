---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/best-practices.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Best practices
<a name="best-practices"></a>

## Choosing a Windows Server version
<a name="choosing-a-windows-server-version"></a>

 There are two primary release channels available for Windows Server 2019: the Long-Term Servicing Channel and the Semi-Annual Channel.
+  **Long-Term Servicing Channel (LTSC)** — This is the release model that most customers use in production (formerly called the *Long-Term Servicing Branch*) where a new major version is released every 2–3 years. With LTSC, there are five years of mainstream support and five years of extended support.

   This channel is appropriate for systems that require a longer servicing option and functional stability. Deployments of Windows Server 2019 and earlier versions of Windows Server are not affected by the Semi-Annual Channel releases. The LTSC receives ongoing security and non-security updates, but it does not receive new features and functionality.
+  **Semi-Annual Channel** — The Semi-Annual Channel is for customers who are innovating quickly to take advantage of new operating system capabilities at a faster pace, especially for containers and microservices. Windows Server products in the Semi-Annual Channel have new releases available twice a year, in spring and fall.

   Each release is supported for 18 months from the initial release. Most of the Semi-Annual Channel features are rolled into the next LTSC release of Windows Server. The editions, functionality, and supporting content might vary from release to release. In this model, Windows Server releases are identified by the year and month of release: for example, in 2017, a release in the ninth month (September) would be identified as version 1709.

**Note**
Microsoft has announced it is dropping Semi-Annual Channel (SAC) releases for Windows Server. Starting with Windows Server 2022 there will be only one release on the LTSC. It will get 10 years’ support (five years mainstream, and five years extended).

## Treat container instances as ephemeral servers
<a name="treat-container-instances-as-ephemeral-servers"></a>

 Windows administrator and IT professionals are responsible for several tasks that include OS patching, managing backups, restoring tests, and maintaining a healthy state for the applications they manage. These tasks change when using Windows containers and Amazon ECS because the containers should not be treated as an ordinary Windows Server instances. Rather, they should be treated as ephemeral instances that can be frequently removed, added, and replaced.

 The Amazon ECS Windows container instance’s sole purpose is to run containers, which drastically reduces management tasks compared to a Windows Server directly hosting an application. For example, when an Amazon ECS cluster is created, an [AWS Auto Scaling group](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-auto-scaling.html) for the cluster is automatically created, which can be used to scale-in and scale-out the cluster based on the application’s capacity requirements. Additionally, [EC2 Image Builder](https://aws.amazon.com/image-builder/) can be used to automate the creation and deployment of container images so that the images remain up to date, consistent, and secure across the cluster. For details, refer to [Building your own Amazon ECS–optimized Windows AMI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows-custom-ami.html).

## Use multi-stage builds for container images
<a name="use-multi-stage-builds-for-container-images"></a>

 One of the most challenging parts to building container images is constraining the image size. Each instruction in the [Dockerfile](https://docs.docker.com/engine/reference/builder/) adds a layer to the image, and you need to clean up any unneeded artifacts before moving on to the next layer. To write an efficient Dockerfile, you have traditionally needed to employ tricks and other logic to keep the layers as small as possible and to ensure that each layer has the artifacts it needs from the previous layer and nothing else.

 A common practice referred to as the *builder pattern* is to have one Dockerfile for development and a slimmed-down Dockerfile for production that only contains your application and the minimum dependencies required to run it. However, maintaining multiple Dockerfiles introduces surface area for error and adds to the maintenance overhead.

 For example, in the following Dockerfile, the first block builds the .NET application and the second block uses the resulting image to build the Windows container image. This process is referred to as multi-stage builds.

```
FROM mcr.microsoft.com/dotnet/framework/sdk:4.8 AS build
WORKDIR /app

# copy csproj and restore as distinct layers
COPY *.sln .
COPY aspnetmvcapp/*.csproj ./aspnetmvcapp/
COPY aspnetmvcapp/*.config ./aspnetmvcapp/
RUN nuget restore

# copy everything else and build app
COPY aspnetmvcapp/. ./aspnetmvcapp/
WORKDIR /app/aspnetmvcapp
RUN msbuild /p:Configuration=Release -r:False

FROM mcr.microsoft.com/dotnet/framework/aspnet:4.8 AS runtime
WORKDIR /inetpub/wwwroot
COPY --from=build /app/aspnetmvcapp/. ./
```

 For more information on Docker best practices, refer to [Docker development best practices](https://docs.docker.com/develop/dev-best-practices/) and [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/).

## Caching layer strategy
<a name="caching-layer-strategy"></a>

 Windows container images are large, ranging from 3.8 GB on disk for a Windows container image containing .NET framework based on Windows Server SAC edition to 5.1 GB on Windows Server 2019 LTSC. It’s essential to implement a Windows container image layer caching strategy when utilizing EC2 [Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html) to avoid delays during task launch.

 A common strategy is to pre-populate container images on the [Amazon Machine Image](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) (AMI) used by the Auto Scaling group to avoid two time-expensive Docker operations:
+  Downloading the image from the repository
+  Extracting the image as layers on the local operating system

 The download and extraction phase consumes sequential I/O operations per second on the disk that directly impacts the container instance’s performance until all images are downloaded and extracted. Also, it imposes a delay on the container’s readiness to receive traffic, because the process can take two to five minutes to complete, depending on the size of the image.

 The Amazon ECS container instances should be treated as [ephemeral](https://webapp.io/blog/what-is-an-ephemeral-environment/) servers. There is an option to use [EC2 Image Builder](https://aws.amazon.com/image-builder/) to build your own AMI with all of the necessary patches and security configuration. This service also enables you to include an additional step in the EC2 Image Builder pipeline to download and extract Docker images directly on the AMI, which reduces the time it takes to launch an EC2-based task on your Amazon ECS cluster.

 For more information on caching layer strategy, refer to [Speeding up Windows container launch times with EC2 Image Builder and image cache strategy](https://aws.amazon.com/blogs/containers/speeding-up-windows-container-launch-times-with-ec2-image-builder-and-image-cache-strategy/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
