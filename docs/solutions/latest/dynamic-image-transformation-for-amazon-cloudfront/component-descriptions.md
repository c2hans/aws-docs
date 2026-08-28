---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/component-descriptions.html
---

# Component descriptions
<a name="component-descriptions"></a>

## Application Load Balancer (ALB)
<a name="application-load-balancer-alb"></a>

Distributes incoming image transformation requests across multiple ECS tasks, providing high availability and automatic scaling capabilities. The ALB performs health checks on ECS tasks and routes traffic only to healthy instances.

## Amazon ECS with AWS Fargate
<a name="amazon-ecs-with-aws-fargate"></a>

Runs containerized image processing applications without managing servers. ECS tasks automatically scale based on demand and maintain in-memory caches for optimal performance. Fargate provides serverless compute for containers, eliminating the need to provision and manage EC2 instances.

## Administrative Interface
<a name="administrative-interface"></a>

A web-based management console built with AWS Amplify that allows administrators to configure and manage image origins (both S3 and external sources), create and edit transformation policies, set up origin mappings using path-based and host-header routing, monitor system performance and usage metrics, and test configurations before deployment to ensure proper functionality.

## Amazon DynamoDB
<a name="amazon-dynamodb"></a>

Stores configuration data including transformation policies, origin definitions, and mapping rules. DynamoDB provides fast, predictable performance with seamless scalability for configuration lookups.

## Amazon Cognito
<a name="amazon-cognito"></a>

Provides secure authentication and authorization for the administrative interface, supporting user management, multi-factor authentication, and role-based access control.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
