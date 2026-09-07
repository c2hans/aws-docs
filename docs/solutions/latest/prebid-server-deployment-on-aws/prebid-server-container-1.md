---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/prebid-server-container-1.html
---

# Prebid Server container
<a name="prebid-server-container-1"></a>

This container hosted in Amazon ECR runs the open source Prebid Server. The solution’s default container image is a customized build of the Prebid Server implementation in Java. The Dockerfile for building this container image is located at `deployment/ecr/prebid-server/Dockerfile` and an accompanying configuration file is at `deployment/ecr/prebid-server/config.json`. This configuration file provides the version of the prebid server through the `GIT_TAG_VERSION` parameter.

The container differs from the open source project’s default container in configuration settings for areas including file output and bidding adapter configuration settings. Alternatively, you can use the [Go implementation of Prebid Server](https://docs.prebid.org/prebid-server/versions/pbs-versions-go.html), or any build hosted in a container repository, such as [Docker Hub](https://hub.docker.com/) or [ECR Public Gallery](https://gallery.ecr.aws/). You will have the option of overriding the solution’s default container.

**Note**
If using a custom image, ensure it is compatible with the logging configuration of the container supplied with the solution to make use of the Prebid Metrics ETL.
Make changes to the Dockerfile as needed.

The following diagram shows a detailed view of the container contents, and the resources the container interacts with directly. Additionally, the container image supplied with the solution is stored in the [ECR Public Gallery for AWS Solutions](https://gallery.ecr.aws/aws-solutions/).

 **Prebid Server container diagram**

![prebid server container diagram](https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/images/prebid-server-container-diagram.png)

1. Amazon ECR is a fully managed container registry for developers to store, manage, and deploy container images for public or private access.

1. Inbound auction requests come through Application Load Balancer. ALB distributes incoming application traffic across multiple ECS containers.

1. The Guidance for Deploying a Prebid Server on AWS container instances run in a defined environment.

1. The Java-based version of Prebid Server is configured to run with [Amazon Corretto](https://aws.amazon.com/corretto/).

1. NAT gateway enables instances in a private subnet to connect to the internet but prevents the internet from initiating a connection with those instances. It is the default gateway for outgoing network packets from the private subnet within Amazon VPC.

1. The internet gateway connects a VPC with the public internet, allowing instances such as NAT gateways to send and receive traffic.

1. Auction requests are sent to bidders over the internet.

1. EFS Standard is a managed file storage service that provides a scalable file system for use with AWS Cloud services and on-premises resources. The EFS filesystem is used for capturing transaction and operational log data from each container via an NFS network connection.

1. DataSync is used as the ETL mechanism for moving data captured in raw log files on EFS to a structured and normalized layout in AWS Glue Data Catalog.

1. The `DataSyncLogsBucket` S3 bucket receives the migrated log data from the EFS filesystem. The Glue ETL process uses the contents of this bucket as source data.
