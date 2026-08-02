---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/deploy-govcloud.html
---

# Deploy in AWS GovCloud (US) Regions
<a name="deploy-govcloud"></a>

The solution supports deployment in the AWS GovCloud (US-West) and AWS GovCloud (US-East) Regions. However, you must use the launch buttons in this section rather than the launch buttons provided in other sections of this guide. The launch buttons in other sections reference templates staged for the standard AWS partition, which are not accessible from AWS GovCloud (US) Regions.

**Note**
The default CloudFront \+ S3 web console hosting option is not available in AWS GovCloud (US) Regions because Amazon CloudFront is not available in the AWS GovCloud (US) partition. Use the ALB \+ ECS Fargate template or the headless template instead.

Before you deploy, you must mirror the solution’s container images to a private Amazon ECR repository in your AWS GovCloud (US) Region, because ECS tasks in AWS GovCloud (US) cannot access the public ECR registry (`public.ecr.aws`). For instructions on mirroring the container images, refer to the [Load tester image URI](container-image.md#load-tester-image-uri) section of this guide.

 [https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/new?templateURL=https:%2F%2Fs3.us-gov-west-1.amazonaws.com%2Fsolutions-reference-us-gov%2Fdistributed-load-testing-on-aws%2Flatest%2Fdistributed-load-testing-on-aws-alb-ecs.template&redirectId=ImplementationGuide](https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/new?templateURL=https:%2F%2Fs3.us-gov-west-1.amazonaws.com%2Fsolutions-reference-us-gov%2Fdistributed-load-testing-on-aws%2Flatest%2Fdistributed-load-testing-on-aws-alb-ecs.template&redirectId=ImplementationGuide) **distributed-load-testing-on-aws-alb-ecs.template** - Launches the solution with the web console hosted on ECS Fargate behind an ALB. Follow the instructions in [Launch the stack (ALB \+ ECS Fargate hosted web console)](deploy-alb-ecs-fargate.md), and additionally provide the **Load Tester Image URI** and **Web Console Image URI** parameters.

 [https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/new?templateURL=https:%2F%2Fs3.us-gov-west-1.amazonaws.com%2Fsolutions-reference-us-gov%2Fdistributed-load-testing-on-aws%2Flatest%2Fdistributed-load-testing-on-aws-headless.template&redirectId=ImplementationGuide](https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/new?templateURL=https:%2F%2Fs3.us-gov-west-1.amazonaws.com%2Fsolutions-reference-us-gov%2Fdistributed-load-testing-on-aws%2Flatest%2Fdistributed-load-testing-on-aws-headless.template&redirectId=ImplementationGuide) **distributed-load-testing-on-aws-headless.template** - Launches the solution backend only. Follow the instructions in [Launch the stack (Headless)](deploy-self-hosted.md), and additionally provide the **Load Tester Image URI** parameter.

Alternatively, you can download the templates as a starting point for your own implementation. Choose a launch button above, then copy the template URL from the **Amazon S3 URL** field on the **Create stack** page.
