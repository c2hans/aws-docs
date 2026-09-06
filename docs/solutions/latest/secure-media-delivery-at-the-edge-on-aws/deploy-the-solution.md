---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

 This solution uses [AWS CloudFormation templates and stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) to automate its deployment. The CloudFormation template specifies the AWS resources included in this solution and their properties. The CloudFormation stack provisions the resources that are described in the template.

## Prerequisites
<a name="prerequisites"></a>

 This solution is designed to work with Amazon CloudFront distributions used for video streaming. If you do not have one configured already, complete the applicable task before you launch this solution. For testing purposes, you can create video delivery pipeline including CloudFront distribution using the [Live Streaming on AWS](https://aws.amazon.com/solutions/implementations/live-streaming-on-aws/) solution.

 Refer to [CloudFront prerequisites](cloudfront-prerequisites.md), which outlines which CloudFront configuration settings should be revised prior to launching the solution.

 Inspect the body of video manifests published by the video origin service in use. If your video origin service references other objects using absolute URL paths, configure it to switch to relative paths instead.

## Deployment process overview
<a name="deployment-process-overview"></a>

 Before you launch the solution, review the [cost](cost.md), [architecture](architecture-overview.md), [security](security.md), and other considerations discussed earlier in this guide.

 **Time to deploy:** Approximately 5-10 minutes

 [Step 1. Launch the stack](step-1-launch-the-stack.md)

 [Step 2. Define video assets and token policies](step-2.-define-video-assets-and-token-policies.md)

 [Step 3. Prepare your CloudFront distributions](step-3.-prepare-your-cloudfront-distributions.md)

 [Step 4. Test the solution](step-4.-test-the-solution.md)

**Important**
 This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).
 To opt out of this feature, download the template, modify the AWS CloudFormation mapping section, and then use the AWS CloudFormation console to upload your updated template and deploy the solution. For more information, see the [Anonymized data collection](anonymized-data-collection.md) section of this guide.
