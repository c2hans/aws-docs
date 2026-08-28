---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/api-gateway-existing-distribution.html
---

# Lambda architecture
<a name="api-gateway-existing-distribution"></a>

If you’ve deployed the Lambda architecture stack and have set the Use Existing CloudFront Distribution template parameter to Yes, use the following instructions to complete your setup.

## Setting the Origin
<a name="setting-the-origin"></a>

1. In the CloudFront console, navigate to the distribution you indicated in the Existing CloudFront Distribution ID template parameter.

1. Select the Origins tab and click **Create origin**.

1. Set the Origin domain as the API Gateway execution link. This value can be found by placing the Physical ID of the stack’s AWS::ApiGateway::RestApi in the search field and selecting LambdaRestApi under API Gateway.

1. Set the Origin path to `/image`.

1. Select **Create origin**.

## Setting the behavior
<a name="setting-the-behavior"></a>

1. In the CloudFront console, navigate to the distribution you indicated in the Existing CloudFront Distribution ID template parameter.

1. Select the Behaviors tab and choose **Create behavior**

1. Set the Path pattern you’d like to point to your solution instance, in a Solution created distribution, this is Default (\*)

1. Set the Origin to the Origin created in the previous section.

1. Set the Viewer Protocol policy to `Redirect HTTP to HTTPS`

1. Set the Cache Policy to the one named `ServerlessImageHandler-${UUID}`.

1. Set the Origin request policy to the one named `ServerlessImageHandler-${UUID}`.

1. Set the Viewer request Function type to CloudFront Functions, and the Function ARN to the one named `sih-apig-request-modifier-${UUID}`.

1. Select **Create behavior**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
