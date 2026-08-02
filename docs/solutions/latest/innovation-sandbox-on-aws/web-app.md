---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/web-app.html
---

# Web application
<a name="web-app"></a>

![web app.drawio](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/web-app.drawio.png)

**Web UI and storage management components**
The web app infrastructure consists of an [Amazon CloudFront](https://aws.amazon.com/cloudfront/) distribution with an [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) bucket origin for hosting the static assets for the web UI, and an API origin.

The API uses an [AWS WAF](https://aws.amazon.com/waf/) protected [Amazon API Gateway REST API](https://aws.amazon.com/api-gateway/), with proxy [AWS Lambda](https://aws.amazon.com/lambda/) function integrations for each of the API resources (leases, lease-templates, accounts, configurations, users, auth, blueprints) and an AWS Lambda authorizer function for authorizing API requests. Each of the Lambda function integrations is responsible for interacting with one or more of the underlying data stores in the Data stack.
