---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/embed-quick-sight-visual-components-into-web-apps-cognito-iac.html
---

# Embed Amazon Quick Sight visual components into web applications by using Amazon Cognito and IaC automation
<a name="embed-quick-sight-visual-components-into-web-apps-cognito-iac"></a>

*Ishita Gupta, Saurabh Singh, and Srishti Wadhwa, Amazon Web Services*

## Summary
<a name="embed-quick-sight-visual-components-into-web-apps-cognito-iac-summary"></a>

This pattern delivers a specialized approach for embedding Amazon Quick Sight visual components into React applications by using registered user embedding with streamlined Amazon Cognito authentication. These resources are then deployed through an infrastructure as code (IaC) template. Unlike traditional dashboard embedding, this solution isolates specific charts and graphs for direct integration into React applications, which dramatically improves both performance and the user experience.

The architecture establishes an efficient authentication flow between Amazon Cognito user management and Quick Sight permissions: Users authenticate through Amazon Cognito and access their authorized visualizations based on the dashboard sharing rules in Quick Sight. This streamlined approach eliminates the need for direct Quick Sight console access while maintaining robust security controls.

The complete environment is deployed through a single AWS CloudFormation template that provisions all the necessary infrastructure components, including:
+ A serverless backend that uses AWS Lambda and Amazon API Gateway
+ Secure frontend hosting through Amazon CloudFront, Amazon Simple Storage Service (Amazon S3), and AWS WAF
+ Identity management by using Amazon Cognito

All components are configured by following security best practices with least-privilege AWS Identity and Access Management (IAM) policies, AWS WAF protection, and end-to-end encryption.

This solution is ideal for development teams and organizations that want to integrate secure, interactive analytics into their applications while maintaining fine-grained control over user access. The solution uses AWS managed services and automation to simplify the embedding process, enhance security, and ensure scalability to meet evolving business needs.

Target audience and use cases:
+ **Frontend developers** who want to embed analytics into React apps
+ **Software as a service (SaaS) product teams** that want to offer per-user or role-based data visualizations
+ **Solutions architects** who are interested in integrating AWS analytics into custom portals
+ **Business intelligence (BI) developers** who want to expose visuals to authenticated users without requiring full dashboard access
+ **Enterprise teams** that want to embed interactive Quick Sight charts within internal tools

## Prerequisites and limitations
<a name="embed-quick-sight-visual-components-into-web-apps-cognito-iac-prereqs"></a>

**Prerequisites**

To successfully implement this pattern, make sure that the following are in place:
+ **Active AWS account** – An AWS account with permissions to deploy CloudFormation stacks and create Lambda, API Gateway, Amazon Cognito, CloudFront, and Amazon S3 resources.
+ **Amazon Quick Sight account** – An active Quick Sight account with at least one dashboard that contains visuals. For setup instructions, see [Tutorial: Create an Amazon Quick Sight dashboard using sample data](https://docs.aws.amazon.com/quicksuite/latest/userguide/example-analysis.html) in the Amazon Quick documentation.
+ **A development environment** that consists of:
  + Node.js (version 16 or later)
  + npm or yarn installed
  + Vite as the React build tool
  + React (version 19.1.1)
+ **Dashboard sharing** – Dashboards must be shared in Quick Sight and the implementer must log in to access the embedded visuals or dashboards.

**Limitations**
+ This pattern uses the registered user embedding method, which requires implementers to have an active Quick Sight account.
+ Access is restricted to the dashboards and visuals that are explicitly shared with the authenticated Quick Sight user who is implementing this pattern. If the implementer doesn’t have the correct access rights, the embed URL generation will fail and visuals won’t load.
+ The CloudFormation stack must be deployed in an AWS Region where Quick Sight, API Gateway, and Amazon Cognito are supported. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

**Product versions**
+ [Quick Sight Embedding SDK](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk) version 2.10.1
+ [React](https://www.npmjs.com/package/react) version 19.1.1
+ [Node.js](https://nodejs.org/en/download) version 16 or later to ensure compatibility with the latest React and Vite versions used in this solution

## Architecture
<a name="embed-quick-sight-visual-components-into-web-apps-cognito-iac-architecture"></a>

**Target architecture**

The following diagram shows the architecture and workflow for this pattern.

![Architecture and workflow for embedding Quick Sight visuals into a React application.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/75ad12b1-caaa-4532-b709-8f3eaf3f9cc0/images/d0905f61-9055-49cf-887d-f46f5ca6c871.png)

In this workflow:

1. **The user accesses the application**. The user opens the React web application by using a browser. The request is routed to a CloudFront distribution, which acts as a content delivery network for the application.

1. **AWS WAF filters malicious requests**.** **Before the request reaches CloudFront, it passes through AWS WAF. AWS WAF inspects the traffic and blocks any malicious or suspicious requests based on security rules.

1. **Amazon S3 serves static files**. If the request is clean, CloudFront retrieves the static frontend assets (HTML, JS, CSS) from a private S3 bucket by using origin access control (OAC) and delivers them to the browser.

1. **The user signs in**. After the application is loaded, the user signs in through Amazon Cognito, which authenticates the user and returns a secure JSON web token (JWT) for authorized API access.

1. **The application makes an API request**. After login, the React application makes a secure call to the `/get-embed-url` endpoint on API Gateway, and passes the JWT token in the request header for authentication.

1. **The token is validated**. API Gateway validates the token by using an Amazon Cognito authorizer. If the token is valid, the request proceeds; otherwise, it is denied with a 401 (unauthorized) response.

1. **The request is directed to Lambda for processing**. The validated request is then forwarded to a backend Lambda function. This function is responsible for generating the embed URL for the requested Quick Sight visual.

1. **Lambda generates the embed URL from Quick Sight**. IAM uses an IAM role with appropriate permissions to call the Quick Sight `GenerateEmbedUrlForRegisteredUser` API to generate a secure, user-scoped visual URL.

1. **Lambda returns the embed URL to API Gateway**. Lambda sends the generated embed URL back to API Gateway as part of a JSON response. This response is then prepared for delivery to the frontend.

1. **The embed URL is sent to the browser**. The embed URL is returned to the browser as the API response.

1. **The visual is displayed to the user**.** **The React application receives the response and uses the Quick Sight Embedding SDK to render the specific visual to the user.

**Automation and scale**

Backend and frontend deployments are fully automated by using CloudFormation, which provisions all required AWS resources, including Amazon Cognito, Lambda, API Gateway, Amazon S3, CloudFront, AWS WAF, IAM roles, and Amazon CloudWatch in a single deployment.

This automation ensures consistent and repeatable infrastructure across all environments. All components scale automatically: Lambda adjusts to function invocations, CloudFront serves cached content globally, and API Gateway scales with incoming requests.

## Tools
<a name="embed-quick-sight-visual-components-into-web-apps-cognito-iac-tools"></a>

**AWS services**
+ [Amazon Quick Sight](https://aws.amazon.com/quicksuite/quicksight/) is a cloud-native business intelligence service that helps you create, manage, and embed interactive dashboards and visuals.
+ [Amazon API Gateway](https://aws.amazon.com/api-gateway/) manages APIs that act as the bridge between the React application and backend services.
+ [AWS Lambda](https://aws.amazon.com/lambda/)is a serverless compute service that this pattern uses to generate secure Quick Sight embed URLs dynamically, and scales automatically based on requests.
+ [Amazon Cognito](https://aws.amazon.com/cognito/)provides authentication and authorization for users, and issues secure tokens for API access.
+ [Amazon S3](https://aws.amazon.com/s3/) hosts static frontend assets for this pattern, and serves them securely through CloudFront.
+ [Amazon CloudFront ](https://aws.amazon.com/cloudfront/getting-started/)delivers frontend content globally with low latency and integrates with AWS WAF for traffic filtering.
+ [AWS WAF](https://aws.amazon.com/waf/) protects the web application from malicious traffic by applying security rules and rate limiting.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)automates the provisioning and configuration of all application resources in a single deployment.
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) collects logs and metrics from Lambda, API Gateway, and AWS WAF for monitoring and troubleshooting.

**Development tools**
+ [React JS](https://react.dev/) is a frontend framework that this pattern uses to build the web application and integrate embedded Quick Sight visuals.
+ [Vite](https://vite.dev/) is a build tool used for fast development and optimized production builds of the React application.
+ [Quick Sight Embedding SDK](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk/v/2.10.1) facilitates embedding Quick Sight visuals into the React application and enables seamless interaction between the application and visuals.

**Code repository**

The code for this pattern is available in the GitHub [Amazon Quick Sight Visual Embedding in React](https://github.com/aws-samples/sample-quicksight-visual-embedding) repository.

## Best practices
<a name="embed-quick-sight-visual-components-into-web-apps-cognito-iac-best-practices"></a>

This pattern automatically implements the following security best practices:
+ Uses Amazon Cognito user pools for JWT-based authentication, with optional multi-factor authentication (MFA).
+ Secures APIs with Amazon Cognito authorizers and enforces least-privilege IAM policies across all services.
+ Implements Quick Sight registered user embedding and auto-provisions users with the reader role.
+ Enforces encryption in transit that supports TLS 1.2 and later versions through CloudFront and HTTPS.
+ Encrypts data at rest by using AES-256 for Amazon S3 with versioning and OAC.
+ Configures API Gateway usage plans with throttling and quotas.
+ Secures Lambda with reserved concurrency and environment variable protection.
+ Enables logging for Amazon S3, CloudFront, Lambda, and API Gateway; monitors services by using CloudWatch.
+ Encrypts logs, applies access controls, and enforces deny policies for non-HTTPS or unencrypted uploads.

In addition, we recommend the following:
+ Use CloudFormation to automate deployments and maintain consistent configurations across environments.
+ Make sure that each user has the correct Quick Sight permissions to access embedded visuals.
+ Protect API Gateway endpoints with Amazon Cognito authorizers and enforce the principle of least privilege for all IAM roles.
+ Store sensitive information such as Amazon Resource Names (ARNs) and IDs in environment variables instead of hardcoding them.
+ Optimize Lambda functions by reducing dependencies and improving cold-start performance. For more information, see the AWS blog post [Optimizing cold start performance of AWS Lambda using advanced priming strategies with SnapStart](https://aws.amazon.com/blogs/compute/optimizing-cold-start-performance-of-aws-lambda-using-advanced-priming-strategies-with-snapstart/).
+ Add your CloudFront domain to the Quick Sight allowlist to enable secure visual embedding.
+ Monitor performance and security by using CloudWatch and AWS WAF for logging, alerts, and traffic protection.

**Other recommended best practices**
+ Use custom domains with SSL certificates from AWS Certificate Manager to provide a secure and branded user experience.
+ Encrypt Amazon S3 data and CloudWatch logs by using customer managed AWS Key Management Service (AWS KMS) keys for greater control over encryption.
+ Extend AWS WAF rules with geo-blocking, SQL injection (SQLi), cross-site scripting (XSS) protection, and custom filters for enhanced threat prevention.
+ Enable CloudWatch alarms, AWS Config, and AWS CloudTrail for real-time monitoring, auditing, and configuration compliance.
+ Apply granular IAM policies, enforce API key rotation, and allow cross-account access only when absolutely necessary.
+ Perform regular security assessments to ensure alignment with compliance frameworks such as System and Organization Controls 2 (SOC 2), General Data Protection Regulation (GDPR), and Health Insurance Portability and Accountability Act (HIPAA).

## Epics
<a name="embed-quick-sight-visual-components-into-web-apps-cognito-iac-epics"></a>

### Prepare the environment
<a name="prepare-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | Clone the GitHub repository for this solution to your local system and navigate to the project directory:<pre>git clone https://github.com/aws-samples/sample-quicksight-visual-embedding.git<br /><br />cd sample-quicksight-visual-embedding</pre><br />This repository contains the CloudFormation template and React source code required to deploy the solution. | App developer |

### Deploy the CloudFormation stack
<a name="deploy-the-cfn-stack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the template. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/embed-quick-sight-visual-components-into-web-apps-cognito-iac.html) For more information, see [Creating and managing stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html) in the CloudFormation documentation. | AWS administrator |
| Monitor stack creation. | Monitor the stack in the **Events** tab until its status is **CREATE\_COMPLETE**. | AWS administrator |
| Retrieve stack outputs. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/embed-quick-sight-visual-components-into-web-apps-cognito-iac.html) | AWS administrator |

### Configure the frontend environment
<a name="configure-the-frontend-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Retrieve Quick Sight visual identifiers. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/embed-quick-sight-visual-components-into-web-apps-cognito-iac.html) | Quick Sight administrator |
| Configure your local React environment. | To set up your local React environment and link it to AWS resources, create an `.env` file in the `my-app/` folder of your local GitHub repository. Populate the file with:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/embed-quick-sight-visual-components-into-web-apps-cognito-iac.html)<br />Here’s an example `.env` file:<pre>VITE_AWS_REGION=us-east-1<br /><br /># Cognito Configuration (from CloudFormation outputs)<br />VITE_USER_POOL_ID=us-east-1_xxxxxxxxx VITE_USER_POOL_WEB_CLIENT_ID=xxxxxxxxxxxxxxxxxxxxxxxxxx<br /><br /># API Configuration (from CloudFormation outputs)<br />VITE_API_URL=https:/your-api-id.execute-api.us-east-1.amazonaws.com/prod<br /><br /># QuickSight Visual Configuration<br />VITE_DASHBOARD_ID=your-dashboard-id <br />VITE_SHEET_ID=your-sheet-id <br />VITE_VISUAL_ID=your-visual-id</pre> | App developer |

### Set up user authentication
<a name="set-up-user-authentication"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create or Manage Users in Cognito | To enable authenticated user access to embedded Quick Sight visuals, you first create users in Amazon Cognito:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/embed-quick-sight-visual-components-into-web-apps-cognito-iac.html) | AWS administrator |
| Provide Quick Sight dashboard access | To provide access to Quick Sight visuals, provide Viewer permission access to authenticated users:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/embed-quick-sight-visual-components-into-web-apps-cognito-iac.html)<br />Each user will receive an email with a link to the dashboard. You can modify permissions at any time through the **Share** menu.<br />For more information, see [Granting individual Amazon Quick Sight users and groups access to a dashboard in Amazon Quick Sight](https://docs.aws.amazon.com/quicksuite/latest/userguide/share-a-dashboard-grant-access-users.html) in the Amazon Quick documentation. | Quick Sight administrator |

### Build and deploy the React frontend
<a name="build-and-deploy-the-react-frontend"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install dependencies and build the project. | In the React application directory, run the following commands to generate optimized production files:<pre>cd my-app<br />npm install<br />npm run build</pre> | App developer |
| Upload the build files to Amazon S3. | Upload all the files from the `my-app/dist/` directory to the S3 bucket provisioned by CloudFormation (do not upload the folder itself). | App developer |
| Create a CloudFront invalidation. | On the [CloudFront console](https://console.aws.amazon.com/cloudfront/v4/home), create an invalidation for path `/*` to refresh cached content after deployment. For instructions, see [Invalidate files](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation_Requests.html) in the CloudFront documentation. | AWS administrator |

### Configure the Quick Sight allowlist
<a name="configure-the-qsight-allowlist"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add the CloudFront domain to the Quick Sight allowlist. | To enable your CloudFront domain to securely embed Quick Sight visuals:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/embed-quick-sight-visual-components-into-web-apps-cognito-iac.html) | Quick Sight administrator |

### Access the application and verify functionality
<a name="access-the-application-and-verify-functionality"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Open the React application. | Use the **CloudFront domain** (from CloudFormation outputs) to open the deployed React web application in a browser. | App owner |
| Verify authentication. | Sign in to the application by using Amazon Cognito credentials to verify the authentication flow and JWT validation through API Gateway. | App owner |
| Verify embedded visuals. | Confirm that Quick Sight visuals load properly within the application based on user-specific access permissions. | App owner |
| Validate API and Lambda connectivity. | Confirm that the application can successfully call the `/get-embed-url` API and retrieve valid Quick Sight embed URLs without errors. | App owner |

### Monitor and maintain the application
<a name="monitor-and-maintain-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Monitor by using CloudWatch. | You can use AWS observability tools to monitor the application and to maintain secure, scalable performance in production.<br />Review Lambda logs, API Gateway metrics and Amazon Cognito authentication events in CloudWatch to ensure application health and to detect anomalies. | AWS administrator |
| Track AWS WAF and CloudFront logs. | Inspect AWS WAF logs for blocked or suspicious requests and CloudFront access logs for performance and caching metrics. | AWS administrator |

## Troubleshooting
<a name="embed-quick-sight-visual-components-into-web-apps-cognito-iac-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| "Domain not allowed" error | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/embed-quick-sight-visual-components-into-web-apps-cognito-iac.html) |
| Authentication errors | Possible causes:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/embed-quick-sight-visual-components-into-web-apps-cognito-iac.html)<br />Solutions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/embed-quick-sight-visual-components-into-web-apps-cognito-iac.html) |
| API Gateway errors | Possible causes:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/embed-quick-sight-visual-components-into-web-apps-cognito-iac.html)<br />Solutions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/embed-quick-sight-visual-components-into-web-apps-cognito-iac.html) |
| Quick Sight visuals don’t load | Possible causes:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/embed-quick-sight-visual-components-into-web-apps-cognito-iac.html)<br />Solutions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/embed-quick-sight-visual-components-into-web-apps-cognito-iac.html) |
| "User does not have access" error | Possible causes:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/embed-quick-sight-visual-components-into-web-apps-cognito-iac.html)<br />Solution:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/embed-quick-sight-visual-components-into-web-apps-cognito-iac.html) |

## Related resources
<a name="embed-quick-sight-visual-components-into-web-apps-cognito-iac-resources"></a>

** AWS documentation**
+ [Signing up for an Amazon Quick subscription](https://docs.aws.amazon.com/quicksight/latest/user/signing-up.html)
+ [Embedded analytics for Amazon Quick Sight](https://docs.aws.amazon.com/quicksuite/latest/userguide/embedded-analytics.html)
+ [Quick Sight API reference – GenerateEmbedUrlForRegisteredUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForRegisteredUser.html)
+ [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html)
+ [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
+ [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
+ [Basic monitoring and detailed monitoring in CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-basic-detailed.html)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [Amazon CloudFront Developer Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
+ [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html)

**Tutorials and videos**
+ [Embedded analytics for Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics.html)
+ [Amazon Quick Sight YouTube tutorials](https://www.youtube.com/results?search_query=amazon+quicksight+embedding)
