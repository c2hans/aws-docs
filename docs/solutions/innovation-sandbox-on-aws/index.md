---
source_url: https://docs.aws.amazon.com//solutions/innovation-sandbox-on-aws//index.html
---

# Innovation Sandbox on AWS

Accelerate cloud innovation with automated, secure, and cost-controlled sandbox environments

- **Version**: 1.2.17
- **Release**: 08/2026
- **Author**: AWS
- **Est. deployment time**: 60 mins
- **Estimated cost**: [See details](/solutions/latest/innovation-sandbox-on-aws/cost.html)

## Overview

Innovation Sandbox on AWS empowers organizations to accelerate cloud innovation by automating the complete lifecycle of temporary sandbox environments. Cloud administrators can provision secure, governed AWS accounts in minutes, not days, with built-in spend controls, automated policy enforcement, and intelligent account lifecycle management. By eliminating weeks of manual administration and reducing operational overhead, Innovation Sandbox frees your teams to focus on what matters most: learning, experimenting, and building on AWS.

## Benefits

### Manage and monitor temporary sandbox environments

Streamline your development workflow with fully automated sandbox lifecycle management that provisions, monitors, and manages short-lived environments from creation through decommissioning. Through an intuitive web interface, users can easily request account leases and track usage and costs, while administrators maintain visibility and control across the entire sandbox ecosystem, eliminating manual overhead and ensuring consistent governance throughout the account lifecycle.

### Enhance operational efficiency

Reduce administrative overhead and accelerate cloud adoption by automatically applying standardized governance policies across all sandbox accounts. Eliminate weeks of manual configuration work while ensuring consistent security and compliance controls, freeing your team to focus on innovation rather than administration.

### Accelerate experimentation with Blueprints

Deploy pre-configured environments instantly using Blueprints: reusable CloudFormation StackSets that automatically provision common resources in new sandbox accounts. Whether setting up training labs, deploying standard networking stacks, configuring data access patterns, or preparing AI/ML experimentation environments, Blueprints eliminate repetitive setup work and get users productive from the start.

### Establish cost governance controls

Gain visibility into sandbox spending with cost tracking and automated budget enforcement. Configure budget limits and alerts to proactively manage costs. Notifications and spend-limiting mechanisms activate when usage approaches your defined thresholds, preventing budget overruns before they happen.

### Flexible account lifecycle management

Automatically freeze accounts when they reach time or budget limits, preserving work while preventing additional spend. Frozen accounts can be easily reinstated to continue development, or ejected from the sandbox ecosystem to transition workloads into non-sandbox environments, providing a clear path from prototype to production-ready solutions.

## How it works

You can automatically deploy this architecture using the implementation guide and the accompanying AWS CloudFormation template for AWS Regions. [View implementation guide](/solutions/latest/innovation-sandbox-on-aws/solution-overview.html)

![Innovation Sandbox on AWS](/images/solutions/innovation-sandbox-on-aws/images/innovation-sandbox-architecture.png)

1. **Step 1**: Users access the solution (SAML2.0 application) using AWS IAM Identity Center authentication. You can configure IAM Identity Center to use its own internal user store, or integrate it with an external identity provider such as Okta or Microsoft Entra ID.
1. **Step 2**: The web User Interface (UI) is hosted in an Amazon CloudFront distribution. It uses an Amazon Simple Storage Service (Amazon S3) bucket to host and serve the web frontend, including the HTML pages, CSS stylesheets, and the JavaScript code.
1. **Step 3**: The web UI calls Amazon API Gateway REST API resources (resource, method, model) to fetch and mutate the solution data. AWS Lambda functions authorize the requests using role-based access, based on identities assigned by solution administrators to user groups in IAM Identity Center. AWS WAF protects the API Gateway from common exploits and bots that can affect availability, compromise security, or consume excessive resources.
1. **Step 4**: AWS Lambda functions handle the API requests by reading, and writing status and configuration data to an Amazon DynamoDB table. These Lambda functions also fetch global configurations from AWS AppConfig to manage solution parameters including lease preferences, account cleanup setting, customer worded "terms of service", and auth configurations.
1. **Step 5**: AWS Lambda functions manage the lifecycle of accounts using the AWS Organizations API, and move them between organizational units (OUs) based on the account status. Service control policies (SCPs) attached to OUs prevent sensitive, expensive, or difficult to clean up services and resources from being used by sandbox users.
1. **Step 6**: The solution's backend includes an event-based architecture built on Amazon EventBridge for routing events. The solution monitors sandbox account leases using AWS Lambda for breaches in configured lease budget and duration thresholds and creates events that produce email notifications via Amazon Simple Email Service and invoke Lambda functions that are responsible for the management of lease and account lifecycle.
1. **Step 7**: Accounts going through the onboarding process or leases being terminated will invoke the account cleanup AWS Step Functions, which is responsible for recycling the accounts back into the account pool, ready for reuse.
1. **Step 8**: AWS Step Functions run an AWS CodeBuild project responsible for deleting resources in the account. AWS Lambda functions monitor active account leases and issues actions such as moving an AWS account between Organizational Units (OUs), attaching/detaching an IAM Identity Center permission set to the account giving user access, or initiating the cleanup of an AWS account which deletes all user-created resources using [AWS Nuke](https://aws-nuke.ekristen.dev/). If the clean up process is successful, the account is moved to the available account pool, or if some resources cannot be deleted, the account is moved to a quarantine state, for manual investigation and remediation.
1. **Step 9**: Users access assigned sandbox accounts via IAM Identity Center access portal console, or programmatically using credentials. The solution provides a link in the web UI to directly access the AWS account with Single Sign-On (SSO).
## Deploy with confidence

Everything you need to launch this AWS Solution in your account is right here.

- **We'll walk you through it**: Get started fast. Read the implementation guide for deployment steps, architecture details, cost information, and customization options.

[Open guide](/solutions/latest/innovation-sandbox-on-aws/solution-overview.html)

- **Let's make it happen**: Ready to deploy? Open the CloudFormation template in the AWS Console to begin setting up the infrastructure you need. You'll be prompted to access your AWS account if you haven't yet logged in.

[Launch in the AWS Console](/solutions/latest/innovation-sandbox-on-aws/deploy-the-solution)

## Deployment tools

Follow these links for direct access to the artifacts for this AWS Solution.

- **CloudFormation template**: View or modify the CloudFormation template to customize your deployment.

[Learn more](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/aws-cloudformation-templates.html)

- **Source code**: The source code for this AWS Solution is available in GitHub.

[Go to GitHub](https://github.com/aws-solutions/innovation-sandbox-on-aws)

- **Implementation guide**: Follow the implementation guide for step-by-step actions to deploy this AWS Solution.

[Download guide](https://docs.aws.amazon.com/pdfs/solutions/latest/innovation-sandbox-on-aws/innovation-sandbox-on-aws.pdf)

## Customer stories

### University of Sheffield

*"We built a new course module to teach GenAI and get our students familiarized with Amazon Bedrock. We were able to get this rolling quite quickly with Innovation Sandbox on AWS and managed to make Amazon Bedrock available to students in a controlled way, with security and cost controls in place. The module we introduced now enables a set of law students to build their own GenAI Law agent for their Law Advice clinique. Our vision is for the GenAI Law agent to be improved each semester by new students and eventually become an innovative agentic AI product that can be used by all law students within the university - or even better, in the broader legal industry."*

**Ben Orza, Former Lead Technology Architect - IT Services, University of Sheffield**

### RMIT University

*"Innovation Sandbox has allowed us to focus on delivering quality education rather than managing the complexities of cloud infrastructure. It's been valuable in supporting our students working on cloud security assignments. In a sandbox environment, the ability to configure different roles and permissions has helped us to support our students' learning effectively, while maintaining a secure and flexible learning environment."*

**Iqbal Gondal, Associate Dean Cyber Security & Software Systems, School of Computing Technologies, RMIT University**

### University of East London

*"Innovation Sandbox on AWS has reduced operational burden for our AWS admins by streamlining the management of sandbox environments for students and staff to experiment with. We manage 330+ sandbox accounts through this product and it has simplified our lifecycle management, which enables me to spend more time on the academic objectives - to create various environments that students need for their learning requirements."*

**Jordan Richards, Solutions Architect - IT Services, University of East London**

### Hanoi University of Science and Technology

*"The Innovation Sandbox on AWS was instrumental in enabling us to host HACK TOGETHER 2025 at scale and onboard 24 hackathon teams in just a few days. By providing secure and isolated environments, the solution empowered our hackathon teams to experiment freely, while giving us the peace of mind through built-in governance and cost controls. This solution aligned perfectly with our digital transformation strategy and helped us create a truly innovative and hands-on experience for all participants."*

**Nguyen Binh Minh, Associate Professor and Dean, Institute for Digital Technology and Economy, Hanoi University of Science and Technology**

## Related content

- **Accelerate Cloud Innovation with Innovation Sandbox on AWS**: See how easy it is to rapidly experiment, test, and innovate on the cloud.

[Watch the video](https://www.youtube.com/watch?v=FFFVSvMHaBg)

- **AWS and University of East London innovate in Higher Education**: Law students build Generative AI agents with Amazon Bedrock using Innovation Sandbox on AWS.

[Watch the video](https://www.youtube.com/watch?v=GdooYpBuvgw)

---

## AWS Support

- [Get support for this AWS Solution](/solutions/latest/innovation-sandbox-on-aws/contact-aws-support.html)

## RSS Feed

- [Subscribe now to get updates on the latest release.](https://solutions-reference.s3.us-east-1.amazonaws.com/innovation-sandbox-on-aws/latest/rss.xml)
