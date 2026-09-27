---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/container-image.html
---

# Container image customization
<a name="container-image"></a>

## Load tester image
<a name="load-tester-image"></a>

This solution uses a public Amazon Elastic Container Registry (Amazon ECR) image repository managed by AWS to store the image that is used to run the configured tests. You can rebuild and push the container image into an ECR image repository in your own AWS account.

You can edit the default container image to fit your needs. Set these environment variables before building a customized image.

```
#!/bin/bash
export REGION=aws-region-code # the AWS region to launch the solution (e.g. us-east-1)
export BUCKET_PREFIX=my-bucket-name # prefix of the bucket name without the region code
export BUCKET_NAME=$BUCKET_PREFIX-$REGION # full bucket name where the code will reside
export SOLUTION_NAME=my-solution-name
export VERSION=my-version # version number for the customized code
export PUBLIC_ECR_REGISTRY=public.ecr.aws/awssolutions/distributed-load-testing-on-aws-load-tester # replace with the container registry and image if you want to use a different container image export PUBLIC_ECR_TAG=v3.1.0 # replace with the container image tag if you want to use a different container image
```

You can host a customized container image in either a private or public image repository in your AWS account. The image resources are in the `deployment/ecr/distributed-load-testing-on-aws-load-tester` directory in the code base.

You can then build and push the image to the host destination.
+ For private Amazon ECR repositories and images, refer to [Amazon ECR private repositories](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html) and [private images](https://docs.aws.amazon.com/AmazonECR/latest/userguide/images.html) in the *Amazon ECR User Guide*.
+ For public Amazon ECR repositories and images, refer to [Amazon ECR public repositories](https://docs.aws.amazon.com/AmazonECR/latest/public/public-repositories.html) and [public images](https://docs.aws.amazon.com/AmazonECR/latest/public/public-images.html) in the *Amazon ECR Public User Guide*.

After you create the custom image, declare the following environment variables before building the customized solution.

```
#!/bin/bash
export PUBLIC_ECR_REGISTRY=YOUR_ECR_REGISTRY_URI # e.g. YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/YOUR_IMAGE_NAME
export PUBLIC_ECR_TAG=YOUR_ECR_TAG # e.g. latest, v3.4.0
```

The Dockerfile defines the load testing image. It builds on an Amazon Linux base image, installs the language runtimes, system packages, and testing tools required to run load tests, adds the framework version metadata files and the `load-test.sh` entrypoint script, and runs as a non-root user. To view the Dockerfile, refer to [Dockerfile](https://github.com/aws-solutions/distributed-load-testing-on-aws/blob/main/deployment/ecr/distributed-load-testing-on-aws-load-tester/Dockerfile) in the GitHub repository.

The `load-test.sh` entrypoint script runs inside the container each time a task starts. It reads the test configuration and container metadata. It then downloads the test definition from Amazon S3 and provisions the selected testing framework for the run. The script waits for a start signal so that all tasks in a test begin at the same time. It then runs the test for the configured duration while producing metrics and logs. When the test finishes, the script collects the results and enriches them with details about the container that produced them. It uploads the results, logs, and other artifacts to Amazon S3. The script also handles termination signals, so it preserves partial results and logs if you cancel a test before it completes. To view the full script, refer to [load-test.sh](https://github.com/aws-solutions/distributed-load-testing-on-aws/blob/main/deployment/ecr/distributed-load-testing-on-aws-load-tester/load-test.sh) in the GitHub repository.

## Web console image (ALB \+ ECS Fargate template only)
<a name="web-console-image"></a>

The ALB \+ ECS Fargate template runs the web console as a container on ECS Fargate. By default, the solution pulls the web console image from a public Amazon ECR repository managed by AWS.

In environments where access to public container registries is restricted (for example, VPCs with no internet access or accounts with ECR public access policies), you must mirror the public image to a private Amazon ECR repository and provide the private image URI in the **Web Console Image URI** CloudFormation parameter. You can also use the following steps to customize the web console image.

### Mirror the public image to a private ECR repository
<a name="mirror-the-public-image-to-a-private-ecr-repository"></a>

To mirror the web console image to a private ECR repository:

1. Authenticate to the public ECR registry:

   ```
   $ aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
   ```

1. Pull the public web console image:

   ```
   $ docker pull public.ecr.aws/aws-solutions/distributed-load-testing-on-aws-web-console:<version>
   ```

1. Create a private ECR repository in your account (if one does not already exist):

   ```
   $ aws ecr create-repository --repository-name <your-repo-name> --region <region> 2>/dev/null || true
   ```

1. Authenticate to your private ECR registry:

   ```
   $ aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
   ```

1. Tag and push the image to your private repository:

   ```
   $ docker tag public.ecr.aws/aws-solutions/distributed-load-testing-on-aws-web-console:<version> \
     <account-id>.dkr.ecr.<region>.amazonaws.com/<your-repo-name>:<version>
   $ docker push <account-id>.dkr.ecr.<region>.amazonaws.com/<your-repo-name>:<version>
   ```

1. When launching the ALB \+ ECS Fargate stack, enter the private image URI in the **Web Console Image URI** parameter:

   ```
   <account-id>.dkr.ecr.<region>.amazonaws.com/<your-repo-name>:<version>
   ```

### Customize the web console image
<a name="customize-the-web-console-image"></a>

You can also customize the web console image. The image resources are in the `deployment/ecr/distributed-load-testing-on-aws-web-console` directory, located in the [GitHub repository](https://github.com/aws-solutions/distributed-load-testing-on-aws/tree/main/deployment/ecr/distributed-load-testing-on-aws-web-console). You can edit the container files, build a local image, push it to a private ECR repository, and provide the resulting image URI in the **Web Console Image URI** parameter.

The web console container image builds on an Nginx base image and installs the AWS CLI. Its [Dockerfile](https://github.com/aws-solutions/distributed-load-testing-on-aws/blob/main/deployment/ecr/distributed-load-testing-on-aws-web-console/Dockerfile) copies in the Nginx configuration and an entrypoint script. The Dockerfile exposes the HTTP port and sets the entrypoint script to run when the container starts. When the container starts, the [entrypoint.sh](https://github.com/aws-solutions/distributed-load-testing-on-aws/blob/main/deployment/ecr/distributed-load-testing-on-aws-web-console/entrypoint.sh) uses the AWS CLI to download the web console assets from Amazon S3. It extracts them into the Nginx document root and then starts Nginx in the foreground. The [nginx.conf](https://github.com/aws-solutions/distributed-load-testing-on-aws/blob/main/deployment/ecr/distributed-load-testing-on-aws-web-console/nginx.conf) serves the single-page application (SPA) and routes unmatched paths back to the application entry point. It also adds a health check endpoint for the Application Load Balancer, enables gzip compression, sets long-lived caching for static assets (while disabling caching for the entry point and runtime configuration), and adds common security response headers.

For more information, see [Pushing a Docker image to an Amazon ECR private repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html) in the *Amazon ECR User Guide*.

## Load tester image URI
<a name="load-tester-image-uri"></a>

All three deployment templates (Amazon CloudFront \+ S3, Application Load Balancer (ALB) \+ ECS on AWS Fargate, and headless) pull a load tester container image from the Amazon Elastic Container Registry (Amazon ECR) public registry (`public.ecr.aws`) at deploy time.

In environments where access to public container registries is restricted, mirror the load tester image to a private Amazon ECR repository and provide the private image URI in the **Load Tester Image URI** (`LoadTesterImageUri`) AWS CloudFormation parameter. Common examples include VPCs with no internet access, accounts with ECR public access policies, and AWS GovCloud (US) Regions, where ECS tasks cannot access the public ECR registry. Mirroring to a private repository in your deployment Region is required for AWS GovCloud (US) deployments and optional elsewhere.

### Mirror the load tester image to a private ECR repository
<a name="mirror-the-load-tester-image-to-a-private-ecr-repository"></a>

**Note**
When you provide `LoadTesterImageUri`, the **Auto-update Container Image** (`UseStableTagging`) parameter no longer manages the load tester image. To pick up security patches, you must re-mirror updated image tags.

To mirror the load tester image to a private ECR repository, complete the following steps. In the following commands, replace `<version>` with the image tag (for example, `v4.0.0`), `<region>` with your deployment Region (for example, `us-gov-west-1`), `<profile>` with your AWS Command Line Interface (AWS CLI) profile name, and `<account-id>` with your 12-digit AWS account ID.

1. Authenticate to the public ECR registry from a machine with internet access.

   ```
   aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
   ```

1. Pull the public load tester image.

   ```
   docker pull public.ecr.aws/aws-solutions/distributed-load-testing-on-aws-load-tester:<version>
   ```

1. Create a private ECR repository in your account (if one does not already exist).

   ```
   aws ecr create-repository --repository-name dlt-load-tester --region <region> --profile <profile> 2>/dev/null || true
   ```

1. Authenticate to your private ECR registry.

   ```
   aws ecr get-login-password --region <region> --profile <profile> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
   ```

1. Tag and push the image to your private repository.

   ```
   docker tag public.ecr.aws/aws-solutions/distributed-load-testing-on-aws-load-tester:<version> \
     <account-id>.dkr.ecr.<region>.amazonaws.com/dlt-load-tester:<version>
   docker push <account-id>.dkr.ecr.<region>.amazonaws.com/dlt-load-tester:<version>
   ```

1. Enter the private image URI in the **Load Tester Image URI** parameter when you launch the stack.

   ```
   <account-id>.dkr.ecr.<region>.amazonaws.com/dlt-load-tester:<version>
   ```

### AWS GovCloud (US) deployment examples
<a name="aws-govcloud-us-deployment-examples"></a>

The following examples show the parameters required for each stack variant in AWS GovCloud (US).

For the headless stack, only `LoadTesterImageUri` is required:

```
aws cloudformation create-stack \
  --stack-name dlt-govcloud \
  --template-url https://solutions-reference-us-gov.s3.us-gov-west-1.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws-headless.template \
  --parameters \
    ParameterKey=AdminName,ParameterValue=admin \
    ParameterKey=AdminEmail,ParameterValue=admin@example.com \
    ParameterKey=LoadTesterImageUri,ParameterValue=<account-id>.dkr.ecr.us-gov-west-1.amazonaws.com/dlt-load-tester:<version> \
  --capabilities CAPABILITY_IAM \
  --region us-gov-west-1
```

For the Application Load Balancer (ALB) \+ ECS on AWS Fargate stack, provide both `LoadTesterImageUri` and `WebConsoleImageUri`. ECS tasks in AWS GovCloud (US) cannot access the public ECR registry (`public.ecr.aws`), so you must mirror both container images.

```
aws cloudformation create-stack \
  --stack-name dlt-govcloud \
  --template-url https://solutions-reference-us-gov.s3.us-gov-west-1.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws-alb-ecs.template \
  --parameters \
    ParameterKey=AdminName,ParameterValue=admin \
    ParameterKey=AdminEmail,ParameterValue=admin@example.com \
    ParameterKey=ConsoleDomainName,ParameterValue=dlt.example.gov \
    ParameterKey=ACMCertificateArn,ParameterValue=arn:aws-us-gov:acm:us-gov-west-1:123456789012:certificate/abcd1234-ef56-gh78-ij90-klmnopqrstuv \
    ParameterKey=LoadTesterImageUri,ParameterValue=<account-id>.dkr.ecr.us-gov-west-1.amazonaws.com/dlt-load-tester:<version> \
    ParameterKey=WebConsoleImageUri,ParameterValue=<account-id>.dkr.ecr.us-gov-west-1.amazonaws.com/dlt-web-console:<version> \
  --capabilities CAPABILITY_IAM \
  --region us-gov-west-1
```

For instructions on mirroring the web console image, see [Web console image](#web-console-image).
