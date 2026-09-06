---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/appstream-well-architected-framework/security.html
---

# Security pillar
<a name="security"></a>

The [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/security.html) of the AWS Well-Architected Framework focuses on taking advantage of cloud capabilities to help establish robust protection mechanisms for your information, infrastructure, and resources. These principles help enhance your overall security posture while enabling innovation.

Key focus areas for applying this pillar to your WorkSpaces Applications streaming environment:
+ Data integrity and confidentiality
+ Managing user permissions
+ Establishing controls to detect security events

## Implement a strong identity foundation
<a name="security-foundation"></a>

Use minimum required permissions to access AWS resources while centralizing identity management and avoiding long-term credentials.
+ Grant least privileged permissions for WorkSpaces Applications resources:
  + Create specific IAM roles for WorkSpaces Applications fleets with minimal required permissions.
  + Configure limited IAM permissions for image builders.
  + Restrict administrative access to WorkSpaces Applications management functions.
  + Define granular permissions for stack and fleet management.
+ Implement proper user authentication mechanisms:
  + Configure SAML 2.0 federation for enterprise identity provider integration.
  + Set up [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) for user management.
  + Use custom identity brokers only when required for specific authentication scenarios.
  + Implement multi-factor authentication (MFA) where supported.
+ Control user access to applications:
  + Configure application entitlements to restrict access to specific applications.
  + Create application assignment groups based on user roles.
  + Manage application access through stack permissions.
  + Implement session policies to control application behavior.
+ Secure user sessions with appropriate controls:
  + Configure session timeout policies.
  + Set disconnect timeout actions.
  + Implement session persistence requirements.
  + Control file system redirection permissions.
+ Configure certificate-based authentication for WorkSpaces Applications. For more information, see the AWS blog post [Simplify certificate-based authentication for WorkSpaces Applications and WorkSpaces with AWS Private CA Connector for Active Directory](https://aws.amazon.com/blogs/desktop-and-application-streaming/simplify-certificate-based-authentication-for-appstream-2-0-and-workspaces-with-aws-private-ca-connector-for-active-directory/).
+ Use session tags to implement fine-grained access control. For more information, see the AWS blog post [Use session tags to simplify WorkSpaces Applications permissions](https://aws.amazon.com/blogs/desktop-and-application-streaming/use-session-tags-to-simplify-appstream-2-0-permissions/).

## Maintain traceability
<a name="security-traceability"></a>

Implement real-time monitoring and automated response systems for all environment changes and activities.
+ Configure [CloudWatch logging](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/welcome.html) for application logs to monitor application-specific events, including application launches, crashes, and errors. Configure session logs to track streaming session information, including session starts, stops, and user connection events.
+ [Activate CloudTrail to log all WorkSpaces Applications API calls](https://docs.aws.amazon.com/appstream2/latest/developerguide/logging-using-cloudtrail.html) and to track management events such as fleet creation and modifications, image builder operations, stack configurations, and user management activities.
+ Monitor WorkSpaces Applications instance activity:
  + Configure instance logging to capture system-level events.
  + Track application launches and failures.
  + Monitor system resource usage and performance.
+ Track user activity:
  + Monitor user authentication attempts and failures. Use CloudWatch metrics and CloudWatch Logs to track user login attempts, session start and end times, and session disconnect events.
  + Track application usage patterns. [Enable WorkSpaces Applications usage reports](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-usage-reports.html) to retrieve information such as session duration, start and end times, instance types used, and applications accessed.
  + Record file system activities through enabled home folders.
  + Configure clipboard settings and printing operations to achieve your data loss prevention goals.
+ Configure [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) for security-related metrics such as failed user authentications, unusual session patterns, and resource access violations.
+ Use the EUC toolkit to track active sessions and states, monitor IP addresses for in-use active sessions, and export session data for auditing. For more information, see the AWS blog post [Use the EUC toolkit to manage Amazon WorkSpaces Applications and Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/euc-toolkit/).

## Apply security at all layers
<a name="security-layers"></a>

Implement multiple layers of security controls across all components of your infrastructure, from network edge to application code.
+ Configure network layer security:
  + Implement strict security group rules.
  + Place WorkSpaces Applications fleet instances in private subnets that have no direct internet access. Control internet access through NAT devices.
  + Use virtual private cloud (VPC) endpoints to access supported AWS services (such as Amazon S3).
  + Implement network access control lists (ACLs) as an additional network security layer.
  + Restrict streaming port (TCP 8443 for HTTPS and WebSocket Secure) access to specific IP ranges.
+ Configure access layer security:
  + Implement session timeout policies to automatically disconnect inactive users.
  + Implement attribute-based access control by using session tags. For more information, see the AWS blog post [Use session tags to simplify WorkSpaces Applications permissions](https://aws.amazon.com/blogs/desktop-and-application-streaming/use-session-tags-to-simplify-appstream-2-0-permissions/).
+ Configure application layer security:
  + Configure application entitlements to control which users can access specific applications.
  + Enable file system redirection controls to restrict access to local drives.
  + Configure clipboard, file transfer, and printing permissions based on security requirements.
  + Set up USB device access controls according to security policies.
+ Configure image layer security:
  + Create and maintain hardened base images that meet security requirements.
  + Keep base images updated with the latest security patches.
  + Configure Windows security settings in base images.
  + Disable unnecessary Windows services and features in base images.

## Automate security best practices
<a name="security-automation"></a>

Use automated, code-defined security controls in version-controlled templates to enable secure and scalable infrastructure deployment.
+ Use infrastructure as code by using services such as AWS CloudFormation to implement consistent security configurations across all fleet deployments. For more information, see the AWS blog post [Automatically attach additional security groups to Amazon WorkSpaces Applications and Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/automatically-attach-additional-security-groups-to-amazon-appstream-2-0-and-amazon-workspaces/).
+ Automate image creation security processes by using the Image Assistant CLI.
+ Configure automated responses for capacity utilization thresholds exceeded, unauthorized access attempts, and security group changes by using Amazon CloudWatch alarms, Amazon EventBridge rules, and AWS Lambda functions for automated responses.

## Keep people away from data
<a name="security-data"></a>

Automate data handling processes to minimize direct human access and reduce the risk of errors or mishandling.
+ Configure application entitlements to control which users can access specific applications.
+ Use the [dynamic application framework](https://docs.aws.amazon.com/appstream2/latest/developerguide/build-dynamic-app-provider.html) to build a dynamic app provider to make applications available dynamically based on user attributes.
+ Configure file system redirection to control which local drives users can access, to restrict access to specific folders, and to manage file transfer permissions between local and streaming sessions.
+ Implement clipboard restrictions to disable clipboard sharing between local and streaming sessions, enable one-way clipboard flow where needed, and prevent unauthorized data copying.
+ Configure application settings persistence to automatically save and restore application configurations, eliminate manual configuration needs, and maintain consistent user experiences.

## Prepare for security events
<a name="security-events"></a>

Develop and practice incident response plans by using automated tools to enable swift detection, investigation, and recovery from security events.
+ Set up CloudWatch alarms for failed authentication attempts, changes to fleet security groups, modifications to image configurations, and unusual streaming session patterns.
+ Document response procedures for common WorkSpaces Applications security scenarios such as:
  + Unauthorized access attempts
    + Detection: Monitor authentication failures.
    + Response: Revoke user entitlements, review session logs, and update access policies.
  + Compromised streaming instances
    + Detection: Monitor instance behavior.
    + Response: Terminate affected sessions, replace fleet instances, and review security group configurations.
  + Data exfiltration attempts
    + Detection: Monitor file transfer activities.
    + Response: Review clipboard and file transfer logs, adjust file transfer permissions, and update data protection policies.
+ Implement automated recovery processes for fleet instance replacement, security group restoration, user access reconfiguration, and application settings recovery.
+ Use AWS services for security management, such as AWS Security Hub CSPM for security findings and Amazon GuardDuty for threat detection.
