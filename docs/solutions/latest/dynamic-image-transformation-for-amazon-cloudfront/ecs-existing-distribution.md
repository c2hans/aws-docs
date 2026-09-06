---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/ecs-existing-distribution.html
---

# ECS architecture
<a name="ecs-existing-distribution"></a>

For the ECS architecture, deploy the solution as-is to provision all necessary resources. Then manually configure your existing CloudFront distribution to use the solution’s resources.

## Deploy the solution
<a name="deploy-the-solution-2"></a>

1. Deploy the ECS architecture CloudFormation template without specifying an existing CloudFront distribution.

1. The solution will create its own CloudFront distribution along with all required resources including the Application Load Balancer and CloudFront function.

## Configure your existing distribution
<a name="configure-your-existing-distribution"></a>

After the solution deployment is complete:

1. In the CloudFront console, navigate to your existing CloudFront distribution.

1. Select the Origins tab and choose **Create origin**.

1. Set the Origin domain as the Application Load Balancer DNS name. This value can be found in the CloudFormation stack outputs under the key `LoadBalancerDNS`.

1. Leave the Origin path empty (default).

1. Select **Create origin**.

## Create behavior for image processing
<a name="create-behavior-for-image-processing"></a>

1. In your existing CloudFront distribution, select the Behaviors tab and choose **Create behavior**.

1. Set the Path pattern for image requests (for example, `/images/*` or your preferred pattern).

1. Set the Origin to the ALB origin created in the previous step.

1. Set the Viewer Protocol policy to `Redirect HTTP to HTTPS`.

1. Set the Cache Policy to the one named `dit-cache-policy` (created by the solution).

1. Set the Response headers policy to the one named `SecurityHeadersPolicy` (created by the solution).

1. Set the Viewer request Function type to CloudFront Functions, and the Function ARN to the one named `dit-header-normalization` (created by the solution).

1. Select **Create behavior**.

This approach allows you to leverage the solution’s provisioned resources while maintaining control over your existing CloudFront distribution configuration.
