---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/solution-overview.html
---

# Deploy a solution to protect your premium video content from unauthorized access when delivered through Amazon CloudFront
<a name="solution-overview"></a>

Publication date: *August 2022 ([last update](revisions.md): November 2024*)

 Premium video content is one of the most valuable assets for media and entertainment companies. Video delivery teams must continue to raise the security bar to ensure that only authorized viewers consume the content over approved delivery channels. For a video streaming distribution of any scale, customers seek a complete, incremental solution that works universally on a variety of video clients without requiring a re-architecture of their workloads.

 The Secure Media Delivery at the Edge on AWS solution integrates with Amazon CloudFront to offer a ready-to-use content protection mechanism that allows you to meet licensing obligations from the right holders by improving anti-piracy controls. Video Streaming Engineers and Content Delivery Network (CDN) operators can easily deploy the solution into their environment and incorporate it with a minimal number of steps without needing to rearchitect their video services.

 This solution leverages [CloudFront Functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html) to introduce a cookie-less approach that simplifies and automates the process of access token management for media streaming services. By using serverless resources based on a new edge serverless environment, customers can generate an encrypted token, inject it into the media delivery path, and validate the token for every request, without needing to produce and attach the token for the same playback session. The token authorization function at the edge can be associated with specific CloudFront path behavior, pointing to the media origin with original content. Shifting this functionality to the edge simplifies customers’ secure video streaming workflows by making it transparent for existing video origins, removing the complexity of manipulating media manifest files.

 This implementation guide provides an overview of the Secure Media Delivery at the Edge on AWS solution, its reference architecture and components, considerations for planning the deployment, configuration steps for deploying the solution to the Amazon Web Services (AWS) Cloud.

 The intended audience for using this solution’s features and capabilities in their environment includes solution architects, DevOps engineers, data scientists, and cloud professionals.

 Use this navigation table to quickly find answers to these questions:

|  If you want to . . .  |  Read . . .  |
| --- | --- |
|  Know the cost for running this solution. <br /> The estimated cost for running this solution in the US East (N. Virginia) Region is **USD $25.65** for the base module **per month** for AWS resources.  |  [Cost](cost.md)  |
|  Understand the security considerations for this solution.  |  [Security](security.md)  |
|  Know how to plan for quotas for this solution.  |  [Quotas](quotas.md)  |
|  Know which AWS Regions support this solution.  |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
|  Know which video streaming formats the solution supports.  |  [Supported formats](supported-formats.md)  |
|  Know the requirements for using an existing CloudFront distribution.  |  [CloudFront prerequisites](cloudfront-prerequisites.md)  |
|  View or download the AWS CloudFormation template included in this solution to automatically deploy the infrastructure resources (the “stack”) for this solution.  |  [AWS CloudFormation template](aws-cloudformation-template.md)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the solution. |  [GitHub repository](https://github.com/aws-solutions/secure-media-delivery-at-the-edge-on-aws/)  |
