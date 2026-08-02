---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/aws-cloudformation-template.html
---

# AWS CloudFormation templates
<a name="aws-cloudformation-template"></a>

This solution provides two CloudFormation templates, each designed for a specific deployment architecture:

 **Lambda Architecture Template** [https://solutions-reference.s3.amazonaws.com/dynamic-image-transformation-for-amazon-cloudfront/latest/dynamic-image-transformation-for-amazon-cloudfront-lambda.template](https://solutions-reference.s3.amazonaws.com/dynamic-image-transformation-for-amazon-cloudfront/latest/dynamic-image-transformation-for-amazon-cloudfront-lambda.template) - Use this template for cost-optimized deployments with images up to 6 MB. The configuration deploys CloudFront, API Gateway, Lambda, CloudWatch, and EventBridge.

 **ECS Architecture Template** [https://solutions-reference.s3.amazonaws.com/dynamic-image-transformation-for-amazon-cloudfront/latest/dynamic-image-transformation-for-amazon-cloudfront-ecs.template](https://solutions-reference.s3.amazonaws.com/dynamic-image-transformation-for-amazon-cloudfront/latest/dynamic-image-transformation-for-amazon-cloudfront-ecs.template) - Use this template for high-performance deployments with images up to 100 MB. The configuration deploys CloudFront, Application Load Balancer, ECS with Fargate, DynamoDB, Amplify Admin UI, Cognito, CloudWatch, and EventBridge.

**Note**
CloudFormation resources are created from AWS CDK constructs.

 **Template selection guidance:** - Choose the **Lambda template** for cost-optimized deployments with basic transformation needs - Choose the **ECS template** for advanced features including transformation policies, non-S3 origins, and administrative interface - Refer to the [deployment architecture guide](choosing-deployment-architecture.md) for detailed comparison

Before you launch the solution’s AWS CloudFormation template, you must specify an S3 bucket in the **Source Buckets** template parameter. Use this S3 bucket to store the images that you want to manipulate. If you have multiple image source S3 buckets, you can specify them as comma-separated values. For lower latency, use an S3 bucket in the same AWS Region where you launch your CloudFormation template. Additional cross-region data transfer costs may apply if the solution is not deployed in the same AWS Region as the S3 bucket(s) provided in the Source Buckets template parameter.

**Note**
If you are launching from a [supported opt-in Region](opt-in-regions.md), the source S3 bucket you created and provided as the **Source Buckets** template parameter must be in the same Region where you’re launching the CloudFormation template.

We recommend deploying the optional demo UI when you first deploy the solution to test the solution’s functionality. For more information, refer to [Use the demo UI](use-the-demo-ui.md).

**Note**
If you have previously deployed this solution, see [Update the solution](update-the-solution.md) for update instructions.
Dynamic Image Transformation for Amazon CloudFront version 6.0 and newer include significant changes, and you can’t update the solution from versions before 6.0 to version 6.0 or later. To use version 6.0 or later, launch a new stack using version 6.x of the CloudFormation template and [uninstall](uninstall-the-solution.md) your previous version of this solution.
