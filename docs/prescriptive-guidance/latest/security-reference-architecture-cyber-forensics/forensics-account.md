---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-cyber-forensics/forensics-account.html
---

# Forensics account
<a name="forensics-account"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

**Disclaimer**: The following description of an AWS Forensics account should only be used by organizations as a starting point for organizations to develop their own forensic capabilities in conjunction with guidance from their legal advisors.

We make no claim as to the suitability of this guidance in the detection or investigation of crime, nor the ability of data or forensics evidence captured through the application of this guidance to be used in a court of law. You should independently evaluate the suitability of best practices described here for your use case.

The following diagram illustrates the AWS security services that can be configured in a dedicated Forensics account. For context, the diagram shows the [Security Tooling account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html) in the AWS SRA core architecture to depict the AWS services that are used to provide detection or notifications in the Forensics account.

![Forensics account on AWS.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-cyber-forensics/images/guide-img/4107c52b-4ef3-48bd-b4b6-a184f0f0df58/images/a3ff2913-539d-44e4-8270-27cf95e6029d.png)

The Forensics account is a separate and dedicated type of Security Tooling account that is within the Security OU. The purpose of the Forensics account is to provide a standard, preconfigured, and repeatable clean room to allow an organization's forensics team to implement all phases of the forensics process: collection, examination, analysis, and reporting. In addition, the quarantine and isolation process for in-scope resources are also included in this account.

Containing the entire forensics process in a separate account allows you to apply additional access controls to the forensic data that's collected and stored. We recommend that you separate the Forensics and Security Tooling accounts for the following reasons:
+ Forensics and security resources might be on different teams or have different permissions.
+ The Security Tooling account might have automation that's focused on responding to security events at the AWS control plane, such as enabling [Amazon S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) for Amazon Simple Storage Service (Amazon S3) buckets, whereas the Forensics account also includes AWS data plane artifacts that the customer might be responsible for, such as operating system (OS) or application-specific data within an Amazon Elastic Compute Cloud (Amazon EC2) instance.
+ You might need to implement additional access restrictions or legal holds depending on your organizational or regulatory requirements.
+ The forensic analysis process might require analysis of malicious code such as malware in a secured environment in alignment with the AWS terms of service.

The Forensics account should include automation to expedite evidence collection at scale while minimizing human interaction in the forensic collection process. The automation to respond and quarantine resources would also be included in this account to simplify tracking and reporting mechanisms.

The forensic capabilities described in this section should be deployed into every available AWS Region, even if your organization isn't actively using the capabilities. If you don't plan to use specific AWS Regions, you should apply a service control policy (SCP) to restrict provisioning AWS resources. Additionally, maintaining investigations and storage of forensic artifacts within the same Region helps avoid issues with the changing regulatory landscape of data residency and ownership.

This guidance uses the [Log Archive account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html) as outlined in the *AWS SRA – core architecture* guide to record actions taken in the environment through AWS APIs, including the APIs that you run in the Forensics account. Having such logs can help avoid allegations of mishandling or tampering of artifacts. Depending on the level of detail that you enable (see [Logging management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html) and [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the AWS CloudTrail documentation), the logs can include information about the account used to collect the artifacts, the time the artifacts were collected, and the steps taken to collect the data. By storing artifacts in Amazon S3, you can also use advanced access controls and log information about who had access to the objects. A detailed log of actions allows others to repeat the process later if needed (assuming that the resources in scope are still available).

**Design considerations:**
+ Automation is helpful when you have many concurrent incidents, because it helps speed up and scale the collection of vital evidence. However, you should consider these benefits carefully. For example, in case of a false positive incident, a fully automated forensic response might negatively impact a business process that's supported by an AWS workload in scope. For more information, see the design considerations for Amazon GuardDuty, AWS Security Hub CSPM, and AWS Step Functions in the following sections.
+ We recommend separate Security Tooling and Forensics accounts, even if your organization's forensics and security resources are on the same team and all functions can be performed by any member of the team. Splitting the functions into separate accounts further supports least privilege, helps avoid contamination from an ongoing security event analysis, and helps enforce the integrity of artifacts that are gathered.
+ You can create a separate Forensics OU to host this account if you want to further emphasize the separation of duties, least privilege, and restrictive guardrails.
+ If your organization uses immutable infrastructure resources, information that is forensically valuable might get lost if a resource is automatically deleted (for example, during a scaling down event) and before a security incident is detected. To avoid this, consider running a forensic collection process for each such resource. To reduce the volume of data collected, you can consider factors such as environments, business criticality of the workload, type of data processed, and so on.
+ Consider using Amazon WorkSpaces to spin up clean workstations. This can help separate actions of stakeholders during an investigation.

## Amazon GuardDuty
<a name="forensics-guardduty"></a>

[Amazon GuardDuty](https://aws.amazon.com/guardduty/) is a detection service that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts and workloads. For general AWS SRA guidance, see [Amazon GuardDuty](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html#tool-guardduty) in the *Security Tooling account* section of the *AWS SRA – core architecture* guide.

You can use GuardDuty findings to initiate the forensic workflow that captures disk and memory images of potentially compromised EC2 instances. This reduces human interaction and can significantly increase the speed of forensic data collection. You can integrate GuardDuty with Amazon EventBridge to [automate responses to new GuardDuty findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_cloudwatch.html).

The list of [GuardDuty finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-active.html) is growing. You should consider which finding types—for example, Amazon EC2, Amazon Elastic Kubernetes Service (Amazon EKS), malware protection, and so on—should initiate the forensic workflow.

You can fully automate the integration of the containment and forensic data collection process with GuardDuty findings to capture the investigation of disk and memory artifacts and quarantine EC2 instances. For example, if all ingress and egress rules are removed from a  security group, you can apply a network access control list (network ACL) to interrupt the existing connection and attach an AWS Identity and Access Management (IAM) policy to deny all requests.

**Design considerations:**
+ Depending on the AWS service, the customer's shared responsibility can vary. For example, capturing volatile data on EC2 instances is possible only on the instance itself, and might include valuable data that can be used as forensic evidence. Conversely, responding and investigating a finding for Amazon S3 primarily involves CloudTrail data or Amazon S3 access logs. Response automation should be organized across both the Security Tooling and Forensics accounts depending on the customer's shared responsibility, the general process flow, and the captured artifacts that need to be secured.
+ Before you quarantine an EC2 instance, weigh its overall business impact and criticality. Consider establishing a process where appropriate stakeholders are consulted before you use automation to contain the EC2 instance.

## AWS Security Hub CSPM
<a name="forensics-security-hub"></a>

[AWS Security Hub CSPM](https://aws.amazon.com/security-hub/cspm/) provides you with a comprehensive view of your security posture on AWS and helps you check your environment against security industry standards and best practices. Security Hub CSPM collects security data from AWS integrated services, supported third-party products, and other custom security products that you might use. It helps you continuously monitor and analyze your security trends and identify the highest priority security issues. For general AWS SRA guidance, see [AWS Security Hub CSPM](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html#tool-security-hub) in the *Security Tooling account* section of the *AWS SRA – core architecture* guide.

In addition to monitoring your security posture, Security Hub CSPM supports integration with EventBridge to automate the remediation of specific findings. For example, you can define custom actions that can be programmed to run an AWS Lambda function or a Step Functions workflow to implement a forensic process.

Security Hub CSPM custom actions provide a standardized mechanism for authorized security analysts or resources to implement containment and forensic automation. This reduces human interactions in the containment and capture of forensic evidence. You can add a manual checkpoint in the automated process to confirm that a forensic collection is actually required.

**Design consideration:**

Security Hub CSPM can be integrated with many services, including AWS Partner solutions. If your organization uses detective security controls that aren't fully fine-tuned and sometimes result in false positive alerts, fully automating the forensic collection process would result in running that process unnecessarily.

## Amazon EventBridge
<a name="forensics-eventbridge"></a>

[Amazon EventBridge](https://aws.amazon.com/eventbridge/) is a serverless event bus service that makes it straightforward to connect your applications with data from a variety of sources. It is frequently used in security automation. For general AWS SRA guidance, see [Amazon EventBridge](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html#tool-ev) in the *Security Tooling account* section of the *AWS SRA – core architecture* guide.

For example, you can use EventBridge as a mechanism to initiate a forensic workflow in Step Functions to capture disk and memory images based on detections from security monitoring tools such as GuardDuty. Or you could use it in a more manual way: EventBridge could detect tag change events in CloudTrail, which could initiate the forensic workflow in Step Functions.

## AWS Step Functions
<a name="forensics-step-functions"></a>

[AWS Step Functions](https://aws.amazon.com/step-functions/) is a serverless orchestration service that you can integrate with AWS Lambda functions and other AWS services to build business-critical applications. On the Step Functions graphical console, you see your application's workflow as a series of event-driven steps. Step Functions is based on state machines and tasks. In Step Functions, a workflow is called a *state machine*, which is a series of event-driven steps. Each step in a workflow is called a *state*. A [Task](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-task-state.html) state represents a unit of work that another AWS service, such as Lambda, performs. A Task state can call any AWS service or API. You can use the built-in controls in Step Functions to examine the state of each step in your workflow to make sure that each step runs in the correct order and as expected. Depending on your use case, you can have Step Functions call AWS services, such as Lambda, to perform tasks. You also can create long-running, automated workflows for applications that require human interaction.

Step Functions is ideal for use with a forensic process because it supports a repeatable, automated set of predefined steps that can be verified through AWS logs. This helps you exclude any human involvement and avoid mistakes in your forensic process.

**Design considerations:**
+ You can initiate a Step Functions workflow manually or automatically to capture and analyze security data when GuardDuty or Security Hub CSPM indicates a compromise. Automation with minimal or no human interaction enables your team to quickly scale in case of a significant security event that affects many resources.
+ To limit fully automated workflows, you can include steps in the automation flow for some manual intervention. For example, you might require an authorized security analyst or team member to review the generated security findings and determine whether to initiate a collection of forensic evidence, or quarantine and contain affected resources, or both.
+ If you want to initiate a forensic investigation without an active finding created from security tooling (such as GuardDuty or Security Hub CSPM), you should implement additional integrations to invoke a forensic Step Functions workflow. This can be done by creating an EventBridge rule that looks for a specific CloudTrail event (such as a tag change event) or by allowing a security analyst or team member to start a forensic Step Functions workflow directly from the console. You can also use Step Functions to create actionable tickets by integrating it with your organization's ticketing system.

## AWS Lambda
<a name="forensics-lambda"></a>

With [AWS Lambda](https://aws.amazon.com/lambda/) you can run code without provisioning or managing servers. You pay only for the compute time that you consume. There's no charge when your code isn't running. Lambda runs your code on a high-availability compute infrastructure and administers all compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, and logging. You supply your code in one of the language runtimes that Lambda supports, and then organize your code into Lambda functions. The Lambda service runs your function only when needed and scales automatically.

In the context of a forensic investigation, using Lambda functions helps you achieve constant results through repeatable, automated, and predefined steps that are defined in the Lambda code. When a Lambda function runs, it creates a log that helps you verify that the proper process was implemented. **Design considerations:**
+ Lambda functions have a timeout of 15 minutes, whereas a comprehensive forensic process to collect relevant evidence might take longer. For this reason, we recommend that you orchestrate your forensic process by using Lambda functions that are integrated in a Step Functions workflow. The workflow lets you create Lambda functions in the correct order, and each Lambda function implements an individual collection step.
+ By organizing your forensic Lambda functions into a Step Functions workflow, you can run parts of the forensic collection procedure in parallel to speed up the collection. For example, you can collect information about the creation of disk images faster when multiple volumes are in scope.

## AWS KMS
<a name="forensics-kms"></a>

AWS Key Management Service (AWS KMS) helps you create and manage cryptographic keys and control their use across a wide range of AWS services and in your applications. For general AWS SRA guidance, see [AWS KMS](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html#tool-kms) in the *Security Tooling account* section of the *AWS SRA – core architecture* guide.

As part of the forensics process, data collection and investigation should be done in an isolated environment to minimize business impact. Data security and integrity cannot be compromised during this process, and a process will need to be put in place to allow sharing of encrypted resources, such as snapshots and disk volumes, between the potentially compromised account and the Forensics account. In order to accomplish this, your organization will have to make sure that the associated AWS KMS resource policy supports reading the encrypted data as well as securing the data by re-encrypting it with an AWS KMS key in the Forensics account.

**Design consideration:**
+ An organization's AWS KMS key policies should allow authorized IAM principals for forensics to use the key to decrypt data in the source account and re-encrypt it in the Forensics account. Use infrastructure as code (IaC) to centrally manage all your organization's keys in AWS KMS to help ensure that only authorized IAM principals have the appropriate and least privilege access. These permissions should exist on all KMS keys that can be used to encrypt resources on AWS that could be collected during a forensics investigation. If you update the KMS key policy after a security event, the subsequent resource policy update for a KMS key that's in use might impact your business. Additionally, permission issues can increase the overall mean time to respond (MTTR) for a security event.
