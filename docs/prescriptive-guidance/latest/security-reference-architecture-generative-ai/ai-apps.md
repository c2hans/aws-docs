---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/ai-apps.html
---

# Capability 6. Providing secure access, usage, and implementation for AI applications
<a name="ai-apps"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

The scope of this capability is to secure user-facing AI applications that provide direct access to AI capabilities. The following diagram illustrates the AWS services recommended for the Generative AI account for this capability.

![Services recommended for user-facing AI applications.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/images/guide-img/a349f18f-a9fd-43a3-9a48-27534bf6412a/images/902df093-a7fa-41b1-b1dc-676237165932.png)

## Rationale
<a name="ai-apps-rationale"></a>

User-facing AI applications enable organizations to deliver generative AI capabilities directly to end users through web interfaces, mobile applications, and integrated workflows. These applications include [Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html) for AI-assisted software development, [Amazon Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/what-is.html) for enterprise productivity and business intelligence, and [Kiro](https://kiro.dev/docs/) for agentic development environments. Each application provides distinct capabilities while requiring consistent security controls to protect user data, prevent misuse, and maintain organizational governance.

This use case refers to Scope 3 of the [Generative AI Security Scoping Matrix](https://aws.amazon.com/blogs/security/securing-generative-ai-an-introduction-to-the-generative-ai-security-scoping-matrix/), where your organization deploys user-facing AI applications using pre-trained foundation models. In this scope, you control the application interface, user authentication, data access permissions, and usage policies, whereas the AI service provider controls the underlying models and infrastructure.

**Note**
Although this guidance focuses on AI applications managed by AWS, similar principles apply to custom-built AI applications and third-party AI services integrated into your environment.

## Security considerations
<a name="ai-apps-security"></a>

When you provide users with direct access to AI applications, you should address these key security considerations:
+ User authentication and authorization across multiple AI application types with varying sensitivity levels
+ Data protection for user inputs, conversation history, and AI-generated outputs that might contain sensitive organizational information
+ Content filtering and guardrails to prevent inappropriate use, prompt injection attacks, and generation of harmful content
+ Usage monitoring and governance to track AI application adoption, detect anomalous behavior, and maintain compliance with organizational policies and controls

## Remediations
<a name="ai-apps-remediations"></a>

This section reviews the AWS services and features that address the risks that are specific to this capability.

### Data protection
<a name="data-protection.bd63ff77-6957-5c08-90bf-1f31dedfa50b"></a>

Encrypt user inputs, conversation history, and AI-generated outputs in transit and at rest using [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) customer managed keys and TLS 1.2. [Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/data-encryption.html), [Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/data-encryption.html), and [Kiro](https://kiro.dev/docs/privacy-and-security/data-protection/#data-encryption) provide comprehensive encryption by default, with options for customer managed keys to maintain enhanced control over encryption.

Implement session isolation to prevent data leakage between user sessions and maintain separation of user contexts across different AI applications. Configure data retention and memory policies that align with organizational requirements and regulatory obligations for AI-generated content and user interaction history. For more information about user-level context separation and conversation history isolation, see [Enabling identity-enhanced console sessions](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-enhanced-sessions.html) in the AWS IAM Identity Center documentation.

Store application credentials and API keys in [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) with customer managed key encryption. Configure automatic credential rotation where supported and implement fine-grained access controls to limit which users and applications can retrieve specific credentials.

Apply content filtering and validation for user inputs and AI-generated outputs across all application types.

### Identity and access management
<a name="identity-and-access-management.a2b3b6bd-b8dd-5637-8da1-de9ecce18345"></a>

Use AWS IAM Identity Center for centralized identity management across all AI applications. Integrate with enterprise identity providers including Amazon Cognito, Okta, and Microsoft Entra ID to provide consistent authentication and single sign-on capabilities. For information about Amazon Q Developer integration, see [Getting started with IAM Identity Center](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/getting-started-idc.html) in the Amazon Q Developer documentation. For information about integrating Quick with IAM Identity Center, see [Granting Quick access through IAM Identity Center integration](https://docs.aws.amazon.com/prescriptive-guidance/latest/quick-suite-access-approach/iam-identity-center-integration.html) in the *Choosing the right access approach for Amazon Quick* AWS Prescriptive Guidance guide. For information about Kiro, see its [onboarding quickstart](https://kiro.dev/docs/enterprise/getting-started/) documentation. For more information, see [Configure access to your applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-applications.html) in the IAM Identity Center documentation.

Create custom IAM policies that implement least-privilege access for AI application usage. Define granular permissions that control which users can access specific AI features, applications, and data sources based on their organizational roles and responsibilities. Implement permission data boundaries and service control policies to prevent privilege escalation through AI application features.

Configure access controls that limit AI applications to accessing only the data sources and AWS services necessary for their intended functionality. For more information, see [How Amazon Q Developer works with IAM](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.html) in the Amazon Q Developer documentation. For information about Quick, see [Using IAM](https://docs.aws.amazon.com/quicksuite/latest/userguide/iam.html) in the Quick documentation. For information relevant to Kiro, see [How Kiro works with IAM](https://kiro.dev/docs/enterprise/iam/) in the Kiro documentation. For more information about implementing least-privilege access with IAM for both human and workload users, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.

Apply rate limiting and usage quotas at the user and application level to prevent resource exhaustion and control costs. Monitor usage patterns to detect anomalous behavior that might indicate compromised credentials or policy violations. For information about monitoring of API quota usage against service limits for Quick, see [Monitoring and maintenance](https://docs.aws.amazon.com/quicksuite/latest/userguide/int-actions-monitoring.html) in the Quick documentation.

### Network security
<a name="network-security.88cf19f7-4817-5388-95cc-55f8f0c293e8"></a>

Deploy AI applications within private subnets using [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) for private connectivity to AWS services. Create VPC endpoints for Amazon Bedrock, Amazon Q Developer, and other AI services to help ensure that all traffic remains within the AWS network. For more information about VPC endpoints, see the following resources:
+ [Amazon Q Developer and interface endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/vpc-interface-endpoints.html) in the Amazon Q Developer documentation
+ [Quick and interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/quicksight/latest/developerguide/vpc-interface-endpoints.html) in the Quick documentation
+ [Kiro and interface endpoints (AWS PrivateLink)](https://kiro.dev/docs/privacy-and-security/vpc-endpoints/) in the Kiro documentation
+ [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the Amazon Virtual Private Cloud documentation

Configure security groups and network access control lists that restrict traffic to only necessary communication paths. Implement network segmentation to isolate AI application infrastructure from other organizational workloads, based on data sensitivity and compliance requirements.

Use [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) to protect web-based AI application interfaces from common attacks including SQL injection, cross-site scripting, and bot traffic. Configure custom rules to detect and block potential prompt injection patterns and implement rate limiting at the network edge. For information about an example pattern that integrates AWS WAF with a web-based AI application, see [Securing Amazon Q Business Web Experiences with AWS Amplify and AWS WAF](https://aws.amazon.com/blogs/publicsector/securing-amazon-q-business-web-experiences-with-aws-amplify-and-aws-waf/) (AWS Blog post).

Enforce TLS 1.2 or higher for all user connections to AI applications. Use [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) for certificate issuance and automatic rotation to maintain secure encrypted communications between users and AI services.

### Logging and monitoring
<a name="logging-and-monitoring.9922c625-b626-5c0f-9d3e-b3a91969038d"></a>

Enable [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) to log all AI application access and usage activities with user context attribution. Configure organization trails to capture cross-account access and maintain comprehensive audit trails for compliance and security investigations.

Configure [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) to monitor AI application usage patterns, error rates, and performance metrics. Create custom metrics for tracking user adoption, feature usage, and potential security events across different AI applications.

Implement application-specific observability features including [Amazon Q Developer usage analytics](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/dashboard.html), [Quick audit logging](https://docs.aws.amazon.com/quicksuite/latest/userguide/incident-response-logging-and-monitoring.html), and the [telemetry collection available in Kiro](https://kiro.dev/docs/enterprise/monitor-and-track/user-activity/). Use these specialized monitoring capabilities to gain visibility into AI-specific behaviors and usage patterns.

Configure [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) to automate responses to security events including unauthorized access attempts, policy violations, and anomalous usage patterns. Forward all logs to the Security Tooling account for centralized analysis and long-term retention. For more information, see [AWS service events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html).

## Recommended AWS services
<a name="ai-apps-services"></a>

This section reviews the AWS services and features that address the security risks that are specific to this capability:

### Amazon Q Developer
<a name="9999999999999999qdevlong-.b5edcdf2-6d8f-5da2-bc71-62792aa3c295"></a>

[Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html) is an AI-powered productivity tool for software development teams that integrates directly into integrated development environments (IDEs) and command line interfaces (CLIs). It provides context-aware code suggestions, automated code reviews, security scanning, and documentation generation while maintaining enterprise security controls.

Configure Amazon Q Developer with IAM Identity Center for centralized authentication and access control. Enable customer managed [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) for conversation history encryption and code analysis data. Implement resource-based policies to control which code repositories Amazon Q Developer can access. Configure code scanning sensitivity levels and customize security scanning policies to align with organizational security requirements.

### Amazon Quick
<a name="9999999999999999qslong-.f310d20a-232d-531d-ac96-f2fad8d444c3"></a>

[Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/what-is.html) combines conversational business intelligence with generative AI capabilities to transform enterprise data into actionable insights. The suite includes [Amazon Quick Sight](https://docs.aws.amazon.com/quicksuite/latest/userguide/quick-bi.html) for data analysis and visualization, enabling users to interact with business data using plain language questions while maintaining comprehensive security controls.

Implement [row-level security](https://docs.aws.amazon.com/quicksuite/latest/userguide/row-level-security.html) (RLS) in Quick Sight to ensure users can only access authorized data based on their role and permissions. Configure column-level security to mask sensitive fields from unauthorized users. Use private virtual private cloud (VPC) connectivity to establish secure connections to data sources. Enable embedded analytics with identity federation to maintain consistent access controls when integrating Quick capabilities into custom applications.

### Kiro
<a name="9999999999999999kiro-.92c04b67-7823-58a1-a5e5-86bcf72be896"></a>

[Kiro](https://kiro.dev/docs/) provides an agentic development environment that accelerates software delivery through AI-assisted workflows and automated implementation planning. Kiro transforms high-level specifications into detailed implementation plans with automated code generation while maintaining security through comprehensive isolation and encryption.

Configure Kiro with customer managed AWS KMS keys for session data encryption and persistent storage. Implement fine-grained access controls to limit which users can initiate agentic workflows and access generated code. Enable VPC connectivity to establish private network paths between Kiro and internal code repositories. Configure audit logging to track all code generation activities and link them to originating user requests for comprehensive traceability.

### AWS IAM Identity Center
<a name="9999999999999999ssolong-.799bda48-53a0-56d4-ac06-c0fa315f60f2"></a>

[IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) provides centralized identity management for all AI applications with consistent authentication and authorization. It enables single sign-on across multiple AWS accounts and business applications including Amazon Q Developer, Quick, and Kiro.

Configure IAM Identity Center with your enterprise identity provider to maintain consistent user access controls. Create permission sets that define specific access levels for different user roles. Implement attribute-based access control (ABAC) to dynamically adjust permissions based on user attributes. Enable multi-factor authentication (MFA) for all AI application access to enhance security posture and protect against credential theft.

### AWS Secrets Manager
<a name="9999999999999999asmlong-.cf6d8cfe-51d0-5bf4-bcc3-1ef2b5b8bf9c"></a>

[Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) securely stores and manages API keys, database credentials, and service tokens that are required by AI applications. It automatically rotates credentials according to configured schedules and provides a centralized service for secure credential distribution.

Store all AI application credentials in Secrets Manager with encryption by using customer managed KMS keys. Configure automatic rotation for database credentials, API keys, and OAuth tokens where supported. Implement fine-grained access policies to control which AI services can retrieve specific secrets. Enable CloudTrail logging for all secret access operations to maintain a comprehensive audit trail.

### AWS WAF
<a name="9999999999999999waflong-.71e4ebb8-5eed-5aee-b469-d51cf3835847"></a>

[AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) protects AI application interfaces from common web vulnerabilities and specialized attacks against generative AI systems. It provides customizable security rules to filter malicious traffic and protect against distributed denial-of-service (DDoS) attacks.

Configure AWS WAF with managed rule groups to protect against common vulnerabilities including SQL injection and cross-site scripting. Create custom rules to detect and block prompt injection patterns targeting AI applications. Implement rate-based rules to prevent abuse and resource exhaustion from automated or excessive queries. Enable logging to Amazon Simple Storage Service (Amazon S3) for comprehensive traffic analysis and security investigation.

### Amazon CloudWatch
<a name="9999999999999999cwlong-.e080bff8-f8e9-5a78-9bea-b2e0537cd42c"></a>

[CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) provides comprehensive monitoring and observability for all AI applications through metrics collection, log aggregation, and automated alerting. It enables detection of anomalous usage patterns and security events across your AI application portfolio.

Create custom dashboards to monitor key AI application metrics including usage rates, error frequencies, and performance indicators. Configure metric filters to extract actionable data from application logs. Implement [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) to detect potential security incidents including unusual access patterns or policy violations. Set up composite alarms that correlate multiple metrics to identify complex security scenarios with higher confidence. For more information, see the following resources:
+ [Monitoring Amazon Q Developer with Amazon CloudWatch](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/monitoring-cloudwatch.html) in the Amazon Q Developer documentation
+ [Monitoring Amazon Quick usage using CloudWatch Logs](https://docs.aws.amazon.com/quicksuite/latest/userguide/monitoring-quicksuite-chat-feedback-cloudwatch.html) in the Quick documentation
+ [Monitoring and tracking](https://kiro.dev/docs/enterprise/monitor-and-track/) on the Kiro website

### AWS CloudTrail
<a name="9999999999999999ctlong-.bf38c3a1-b1e3-58d4-b45d-b48ad9110087"></a>

[CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) provides comprehensive audit logging for all API calls and user activities across your AI application environment. It captures detailed information about each action including the identity, IP address, timestamp, and parameters used.

Enable organization trails to capture activities across all AWS accounts and forward them to centralized storage in the [Log Archive account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html). Configure log file validation to ensure integrity of audit trails. Implement event selection to capture both management and data events related to AI application usage. Use [CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) to create SQL-based queries for security investigations and compliance reporting on AI application activities. For more information, see the AWS CloudTrail section of [Security OU - Security Tooling account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html#tool-cloudtrail) in the *AWS SRA – core architecture* guide.
