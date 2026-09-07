---
source_url: https://docs.aws.amazon.com/whitepapers/latest/development-and-test-on-aws/build-phase.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Build phase
<a name="build-phase"></a>

 The process of building an application involves many steps, including compilation, resource generation, and packaging. For large applications, each step involves multiple dependencies such as building internal libraries, using helper applications, generating resources in different formats, generating the documentation, and so on.

 Some projects might require building the deliverables for multiple CPU architectures, platforms, or operating systems. The complete build process can take many hours, which has a direct impact on the agility of the software development team. This impact is even stronger on teams adopting approaches like [continuous integration](https://aws.amazon.com/devops/continuous-integration/) where every commit to the source repository triggers an automated build, followed by test suites.

## Schedule builds
<a name="schedule-builds"></a>

 To mitigate this problem, teams working on projects with lengthy build times often adopt the “nightly build” (or neutral build) approach, or break the project into smaller sub- projects (or a combination of both). Doing nightly builds involves a build machine checking out the latest source code from the repository and building the project deliverables overnight. Development teams may not build as many versions as they would like, and the build should be completed in time for testing to begin the next day. Breaking down a project into smaller, more manageable parts might be a solution if each sub-project builds faster independently. However, an integration step combining all the different sub-projects is still often necessary for the team to keep an eye on the overall project, and to ensure the different parts still work well together.

## On-demand builds
<a name="on-demand-builds"></a>

 A more practical solution is to use more computational power for the build process. On traditional environments where the build server runs on hardware acquired by the organization, this option might not be viable due to economic constraints or provisioning delays. A build server running on an Amazon EC2 instance can be scaled up vertically in a matter of minutes, reducing build time by providing more CPU or memory capacity when needed.

 For teams with multiple builds triggered within the same day, a single Amazon EC2 instance might not be able to produce the builds quickly enough. A solution would be to take advantage of the on-demand and pay-as-you-go nature of [AWS CodeBuild](https://aws.amazon.com/codebuild/) to run multiple builds in parallel. Every time a new build is requested by the development team or triggered by a new commit to the source code repository, AWS CodeBuild creates a temporary compute container of the class defined in the build project and immediately processes each build as submitted. You can run separate builds concurrently without waiting in a queue. This also enables you to [schedule automated builds](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-codebuild-tutorial.html) at a specific time window.

 If you use a build tool on EC2 instances running as a fleet of worker nodes, the task distribution to the worker nodes can be done using a queue holding all the builds to process. Worker nodes pick the next build to process as they are free. To implement this system, [Amazon Simple Queue Service](https://aws.amazon.com/sqs/) (Amazon SQS) offers a reliable, highly scalable, hosted queue service. Amazon SQS makes it easy to create an automated build workflow, working in close conjunction with Amazon EC2 and other AWS infrastructure services. In this setup, developers commit code to the source code repository, which in turn pushes a build message into an Amazon SQS queue. The worker nodes poll this queue to pull a message and run the build locally according to the parameters contained in the message (for example, the branch or source version to use).

 You can further enhance this setup by dynamically adjusting the pool of worker nodes consuming the queue. [Auto Scaling](https://aws.amazon.com/autoscaling/) is a service that makes it easy to scale the number of worker nodes up or down automatically according to predefined conditions. With Auto Scaling, worker nodes’ capacity can increase seamlessly during demand spikes to maintain quick build generation, and decrease automatically during demand lulls to minimize costs.

 You can define scaling conditions using [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), a monitoring service for AWS Cloud resources. For example, Amazon CloudWatch can monitor the number of messages in the build queue and notify Auto Scaling that more or less capacity is needed depending on the number of messages in the queue. The following diagram summarizes this scenario:

![A diagram that shows how Amazon CloudWatch can monitor the number of messages in the build queue and notify Auto Scaling that more or less capacity is needed .](https://docs.aws.amazon.com/whitepapers/latest/development-and-test-on-aws/images/cloudwatch.png)

## Storing build artifacts
<a name="storing-build-artifacts"></a>

 Every time you produce a build, you need to store the output somewhere. Amazon S3 is an appropriate service for this. Initially, the amount of data to be stored for a given project is small, but it grows over time as you produce more builds. Here the pay-as- you-go and capacity characteristics of S3 are particularly attractive. When you no longer need the build output, you can delete it, or use the S3 [lifecycle policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to delete or archive the objects to [Amazon Glacier](https://aws.amazon.com/glacier) storage class. AWS CodeBuild by default uses S3 buckets to store the build outputs.

 To distribute the build output (for example, to be deployed in test, staging, or production, or to be downloaded to clients), AWS offers several options. You can distribute build output packages directly out of S3 by configuring bucket policies and/or ACLs to restrict the distribution. You can also share the output object using an [S3 presigned URL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html).

 Another option is to use [Amazon CloudFront](https://aws.amazon.com/cloudfront/), a web service for content delivery, which makes it easy to distribute packages to end users with low latency and high data transfer speeds, thereby improving the end user experience. This can be helpful, for example, when a large number of clients are downloading install packages or updates. Amazon CloudFront offers several options; for example, to authorize and/or restrict access, though a full discussion of this is out of scope for this document.
