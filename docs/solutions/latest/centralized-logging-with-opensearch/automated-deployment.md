---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/automated-deployment.html
---

# Automated deployment
<a name="automated-deployment"></a>

Before you launch the solution, review the architecture, supported Regions, and other considerations discussed in this guide. Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Prerequisites**

Review all the [considerations](plan-your-deployment.md) and make sure you have the following in the target Region you want to deploy the solution:
+ At least one vacancy to create new VPCs, if you choose to launch with a new VPC.
+ At least two vacant Elastic IP addresses, if you choose to launch with a new VPC.
+ At least five vacant S3 buckets.

**Important**
The solution provisions an Amazon CloudFront distribution to serve its web console, with TLS 1.0 and 1.1 enabled by default. We recommend associating a custom domain and upgrading the TLS certificate to version 1.2 or higher after deployment.

 **Deployment in AWS Regions**

Centralized Logging with OpenSearch provides two ways to authenticate and log into the Centralized Logging with OpenSearch console. For some AWS Regions where Amazon Cognito User Pool is not available (for example, Hong Kong), you must launch the solution with OpenID Connect provider.
+  [Launch with Amazon Cognito User Pool](launch-with-amazon-cognito-user-pool.md)
+  [Launch with OpenID Connect](launch-with-openid-connect-oidc.md)

For more information about supported Regions, see [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions).

 **Deployment in AWS China Regions**

AWS China Regions do not have a Amazon Cognito User Pool. Launch the solution with OpenID Connect.
+  [Launch with OpenID Connect](launch-with-openid-connect-oidc.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Logging with OpenSearch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
