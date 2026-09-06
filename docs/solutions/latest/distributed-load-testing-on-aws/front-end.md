---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/front-end.html
---

# Front end
<a name="front-end"></a>

The front end provides the interfaces for interacting with the solution and includes:
+ A load testing API for programmatic access
+ A web console for creating, scheduling, and running performance tests
+ An optional MCP Server for AI-assisted analysis of test results and errors

## Load testing API
<a name="load-testing-api"></a>

Distributed Load Testing on AWS configures Amazon API Gateway to host the solution’s RESTful API. Users can interact with the load testing system securely through the included web console, RESTful API, and optional MCP Server. The API acts as a "front door" for access to testing data stored in Amazon DynamoDB. You can also use the APIs to access any extended functionality you build into the solution.

This solution takes advantage of the user authentication features of Amazon Cognito user pools. After successfully authenticating a user, Amazon Cognito issues a JSON web token that is used to allow the console to submit requests to the solution’s APIs (Amazon API Gateway endpoints). HTTPS requests are sent by the console to the APIs with the authorization header that includes the token.

Based on the request, API Gateway invokes the appropriate AWS Lambda function to perform the necessary tasks on the data stored in the DynamoDB tables, store test scenarios as JSON objects in Amazon S3, retrieve Amazon CloudWatch metrics images, and submit test scenarios to the AWS Step Functions state machine.

For more information about the solution’s API, refer to the [Distributed load testing API](distributed-load-testing-api.md) section of this guide.

## Web console
<a name="web-console"></a>

This solution includes a web console that you can use to configure and run tests, monitor running tests, and view detailed test results. The console is a ReactJS application built with [Cloudscape](https://cloudscape.design/), an open-source design system for building intuitive web applications. The application leverages AWS Amplify to integrate with Amazon Cognito to authenticate users. The web console also contains an option to view live data for a running test, in which it subscribes to the corresponding topic in AWS IoT Core.

The solution supports three web console hosting options. The backend architecture and Cognito authentication are identical across all options:
+  **CloudFront \+ S3 (default)** — The console is hosted in Amazon S3 and accessed through Amazon CloudFront. The web console URL is the CloudFront distribution domain name which can be found in the CloudFormation outputs as **ConsoleURL**. After you launch the CloudFormation template, you also receive an email that contains the web console URL and the one-time password to log into it.
+  **ALB \+ ECS Fargate** — The console runs on an ECS Fargate service behind an Application Load Balancer with a customer-provided ACM certificate and custom domain. An AWS WAF web ACL is deployed in front of the ALB to filter common web-based attacks. This option is suitable for environments where VPC Block Public Access (BPA) policies prevent traffic from public CloudFront distributions, or organizations with zero public internet exposure requirements. For deployment instructions, refer to [Deploy using ALB \+ ECS Fargate](deploy-alb-ecs-fargate.md).
+  **Headless (bring your own web server)** — The solution deploys the backend only and provides a downloadable zip archive of the web console static assets. You host the console on your own web server. This option is suitable for organizations that require complete network isolation with no public-facing AWS endpoints, or that need to host the console on existing on-premises or corporate-managed infrastructure. For deployment instructions, refer to [Deploy using headless template (bring your own web server)](deploy-self-hosted.md).

## MCP Server (Optional)
<a name="mcp-server-front-end"></a>

The optional Model Context Protocol (MCP) Server provides an additional interface for AI development tools to access and analyze load testing data through natural language interactions. This component is only deployed if you select the MCP Server option during solution deployment.

The MCP Server enables AI agents to query test results, analyze performance metrics, and gain insights into your load testing data using tools like Amazon Q, Claude, and other MCP-compatible AI assistants. For detailed information about the MCP Server architecture and configuration, refer to [MCP Server](MCP-Server.md) in this section.
