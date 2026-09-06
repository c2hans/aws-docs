---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iap-on-aws/dev-sec-ops-lifecycle-support.html
---

# DevSecOps lifecycle support
<a name="dev-sec-ops-lifecycle-support"></a>

Currently, products that are provisioned with Service Catalog CloudFormation scripts don't have built-in support for CI/CD processes. We recommend that you create a CI/CD process in AWS CodePipeline or other DevOps tools to develop, test, and release a product through lifecycle environments such as development, test, stage, and production.

The AWS CDK does provide built-in CI/CD support for products, as discussed earlier in this guide.
