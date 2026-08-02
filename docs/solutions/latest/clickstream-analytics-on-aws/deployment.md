---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/deployment.html
---

# Deployment
<a name="deployment"></a>

 Before you launch the guidance, review the architecture, supported Regions, and other considerations discussed in this guide. Follow the step-by-step instructions in this section to configure and deploy the guidance into your account.

## Prerequisites
<a name="prerequisites"></a>

 Review all the [considerations](cost.md) and make sure you have the following in the target Region you want to deploy the solution:
+  At least two vacant S3 buckets.

## Deployment in AWS Regions
<a name="deployment-in-aws-regions"></a>
+ Clone the repository:

  ```
            git clone https://github.com/aws-solutions-library-samples/guidance-for-clickstream-analytics-on-aws.git
            cd guidance-for-clickstream-analytics-on-aws
  ```
+ Install pnpm and dependencies:

  ```
              npm install -g pnpm@9.15.3
              pnpm install && pnpm projen && pnpm nx build @aws/clickstream-base-lib
  ```
+ Bootstrap CDK (if not done before):

  ```
            npx cdk bootstrap
  ```
+ Deploy the stack:

  ```
            cd deployment
            sh solution-deploy.sh --region <aws_region> --profile <profile_name> --email <user_email> --template-deploy
  ```
+ Note the CloudFront URL from the outputs to access the web console.
