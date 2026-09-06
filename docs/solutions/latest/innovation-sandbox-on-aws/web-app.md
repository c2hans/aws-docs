---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/web-app.html
---

# Web application
<a name="web-app"></a>

![Diagram showing the web UI and storage management components including CloudFront S3 WAF API Gateway and Lambda functions](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/diagrams/web-app.drawio.png)

**Web UI and storage management components**
The web app infrastructure consists of an [Amazon CloudFront](https://aws.amazon.com/cloudfront/) distribution with an [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) bucket origin for hosting the static assets for the web UI, and an API origin.

The API uses an [AWS WAF](https://aws.amazon.com/waf/) protected [Amazon API Gateway REST API](https://aws.amazon.com/api-gateway/), with proxy [AWS Lambda](https://aws.amazon.com/lambda/) function integrations for each API resource (leases, lease-templates, accounts, configurations, users, blueprints). API Gateway authorizes requests natively using IAM authorization (SigV4) and does not require a custom Lambda authorizer. Each integration function then verifies the caller’s identity token and enforces role-based access control through shared middleware before interacting with the underlying data stores in the Data stack.
