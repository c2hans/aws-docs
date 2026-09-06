---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-with-aws/core-services.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Core services
<a name="core-services"></a>

 We have identified three core services for a hybrid cloud implementation:

## Device and Fleet Management Service
<a name="device-and-fleet-management-service"></a>

 Device and [fleet management](https://en.wikipedia.org/wiki/Fleet_management) service provides two main functions in a hybrid cloud:
+  Host management of on-premises physical devices such as compute, networking, and storage devices. This includes device, configuration, software, metrics, and inventory management of the physical infrastructure.
+  Device and fleet management service also provides the functionality and management interfaces to provision, manage and monitor infrastructure for the host devices. This includes management interfaces (such as create, delete, update, and read) for physical or virtual compute, storage and networking resources.

 For the AWS physical infrastructure, all fleet management functions are managed by AWS on behalf of customers, including host management. [AWS APIs](https://docs.aws.amazon.com/general/latest/gr/aws-apis.html) provide capability for management and monitoring of AWS resources. [VMware vSphere](https://docs.vmware.com/en/VMware-vSphere/index.html) and [OpenStack](https://www.openstack.org/) are examples of software that provide fleet management functions of host management, and interfaces for managing virtual infrastructure for on-premises compute environments.

 For host management of on-premises infrastructure, you can manage servers in on-premises data center with [AWS Systems Manager](https://aws.amazon.com/systems-manager/). Systems Manager provides several [features](https://aws.amazon.com/systems-manager/features/) like remote command execution, patch management, inventory management, state management, and automation to help with host management functions. [AWS OpsWorks](https://aws.amazon.com/opsworks/) provides a configuration management system using [Chef](https://www.chef.io/) and [Puppet](https://puppet.com/) to automate how servers are configured, deployed, and managed in on-premises environments.

## Metrics and logging
<a name="metrics-and-logging"></a>

 Unified monitoring capability across the hybrid cloud simplifies operations and provides consistent health monitoring, alerting, logging, and auditing capabilities. A few major components for this service include:
+  **Metrics and alerting**: Continuous monitoring of infrastructure, service, and application metrics provides the basis for secure, performant, reliable and cost-optimized operational practices. As a best practice, capturing of metrics from all sources in the hybrid environment must be at a unified repository.

   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) provides a central repository for metrics collection, monitoring, alerting, and dashboarding. CloudWatch agents are deployed on EC2 instances, on-premises servers, and virtual machines, which export metrics on CPU, processes, memory, storage, and networking. [CloudWatch custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) allow collection, storage, and monitoring of metrics from applications and infrastructure.
+  **Auditing, logging and traceability**: Continuous collection, monitoring, and retaining logs related to management/control, application, and data-plane activities provides detective controls and auditing capabilities to identify security threats, to troubleshoot incidents, and for event correlation. As a best practice, all logs must be stored in a central repository for troubleshooting and further analytics processing.

   [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) is a service that enables governance, compliance, operational auditing, and risk auditing of AWS accounts. With CloudTrail, customers can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) enables you to centralize logs from all systems, applications, and AWS services. Use CloudWatch Logs to monitor, store, and access log files from EC2 instances, CloudTrail, Route 53, and custom sources.

## Identity, security, and access management
<a name="identity-security-and-access-management"></a>

 Establishing a unified identity and access management solution is key to providing secure and consistent access to services in a hybrid cloud environment. As a best practice, a single Identity Provider (IdP), which manages identity information for principals while providing authentication services to resources on the hybrid cloud, must be instituted.

 [AWS Directory Services](https://docs.aws.amazon.com/directory-service/) provide multiple ways to set up and run directories like [Amazon Cloud Directory](https://aws.amazon.com/cloud-directory/), [Amazon Cognito](https://aws.amazon.com/cognito/), and [Microsoft AD](https://aws.amazon.com/directoryservice/) to serve as the IdP for the hybrid cloud.

 [AWS Identity and Access Management](https://aws.amazon.com/iam/) (AWS IAM) and [Amazon Cognito Identity Pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html) enable identity federation through integration with IdPs supporting Security Assertion Markup Language (SAML) or Open-ID Connect (OIDC) to obtain temporary, limited-privilege AWS credentials to manage and access resources on AWS and in a hybrid cloud deployment with AWS Outposts.

 Finally, [AWS Single Sign-On (SSO](https://aws.amazon.com/single-sign-on/)) enables you to integrate services in the Unified hybrid cloud management layer to the same IdPs as used to manage access to AWS resources and services.
