---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ams-accelerate-governance-best-practices/ams-accelerate-governance.html
---

# AMS Accelerate operations plan governance
<a name="ams-accelerate-governance"></a>

## Roles and responsibilities (RACI matrix)
<a name="roles-and-responsibilities--raci-matrix-.9dc4440b-71e0-5ab7-af2c-0fd8cbd99a9b"></a>

The following table is a responsible, accountable, consulted, and informed (RACI) matrix for the AMS Accelerate operations plan. The chart assigns primary responsibility either to AMS or you, as the customer, for a variety of activities—from application lifecycle to configuration and onboarding.

For more information, see [Roles and responsibilities](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sd.html#acc-sd-responsibilities) in the *AMS Accelerate User Guide*.

**RACI matrix key**
+ **R** is the responsible party
+ **A** is the accountable party
+ **C** is the consulted party
+ **I** is the informed party (informed on completion of the task)

|
|
|  Activity | You | AMS Accelerate |
| --- |--- |--- |
| **Application lifecycle ** |
| Application development | R | I |
| Application infrastructure requirements analysis and design | R | I |
| Application deployment | R | I |
| AWS resource deployment | R | I |
| Application monitoring | R | I |
| Application testing and optimization | R | I |
| Troubleshooting and resolving application issues | R | I |
| Troubleshooting and resolving AWS network issues (outside of AWS firewalls) | R | I |
| AWS infrastructure monitoring | C | R |
| Incident response for AWS network issues | C | R |
| Incident response for AWS resource issues | C | R |
| **Account configuration and onboarding** |
| Managing the lifecycle of users and their permissions for local directory services that are used to access AWS accounts and instances | R | I |
| Creating cross-account AWS Identity and Access Management (IAM) admin roles within each managed account for AMS to use during onboarding | R | C |
| Recommending reserved instances optimization | I | R |
| Managing access credentials for AMS engineers | I | R |
| Installing and configuring AWS Systems Manager Agent (SSM Agent) and Amazon CloudWatch agents and scripts for patching, configuration management, monitoring, and log aggregation | R | C |
| Activating and configuring supported AWS services for security management | C | R |
| Configuring default alert thresholds for monitoring | I | R |
| Configuring default alert thresholds for Amazon Elastic Compute Cloud (Amazon EC2) patching | I | R |
| Configuring default alert thresholds for monitoring backups | I | R |
| Configuring default alert thresholds for AWS CloudTrail and Amazon CloudWatch logging | I | R |
| Configuring default alert thresholds for security management | I | R |

### Account teams
<a name="account-teams"></a>

Your AMS Accelerate account team can help you launch new projects and give best practice recommendations throughout the software development and operations lifecycles.

**Account team roles**

**Cloud services delivery managers (CSDMs)** provide advisory assistance across AMS and have a detailed understanding of the use case and technology architecture of the managed environment.

**AMS cloud architects (CAs) and solutions architects (SAs)** help launch new projects and give best-practices recommendations throughout the software development and operations processes.

For more information, including the specific responsibilities of your CSDM, see [Account governance](https://docs.aws.amazon.com/managedservices/latest/userguide/apx-gov.html) in the *AMS Advanced User Guide*.

### SLAs
<a name="sl-as"></a>

AMS Accelerate has two Service Level Agreement (SLA) tiers: **Plus **and **Premium**. You can apply different SLA tiers to each AWS account.

The following tables show the SLA targets for each tier's response and resolution time, based on the priority of the incident or request.

**Plus tier SLAs**

|
|
| Priority level | Response time | Resolution time |
| --- |--- |--- |
| 1—Major outages with major business impact | 95% within 4 hours | 95% within 12 hours |
| 2—Impaired services with significant business impact | 95% within 8 hours | 95% within 24 hours |
| 3—Impaired services with limited business impact | 90% within 24 hours | 90% within 48 hours |

**Premium tier SLAs**

|
|
| Priority level | Response time | Resolution time |
| --- |--- |--- |
| 1—Major outages with major business impact | 95% within 15 minutes | 95% within 4 hours |
| 2—Impaired services with significant business impact | 95% within 4 hours | 95% within 8 hours |
| 3—Impaired services with limited business impact | 90% within 12 hours | 90% within 24 hours |

### Contact hours
<a name="contact-hours"></a>

AMS Accelerate provides different contact hours based on the SLA tier level assigned to each AWS account. For more information, see [Contact hours](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-contact-hours.html) in the *AMS Accelerate User Guide.*

### Notifications
<a name="notifications"></a>

**When notifications occur**

AMS sends notifications to you for the following reasons only:
+ Events created by monitoring alerts
+ Patching service notifications (if you've activated the patch add-on)
+ Service requests and incident reports
+ Important AWS announcements

**Configuring notifications**

There are two ways to set up AMS Accelerate notifications:
+ [Tag-based alert notifications](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/how-monitoring-works.html#how-mon-works-alert-notes-tags) send an alert for a specific AWS resource to an email address that's configured in the resource's tag. For more information, see [Tagging in AMS Accelerate](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-tagging.html) in the *AMS Accelerate User Guide*.
+ [Alert notifications](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/how-monitoring-works.html#how-monitoring-works-alert-notes) send an alert to the email address associated with your account.

**Note**
It's a best practice to use tag-based alert notifications. Alert notifications sent to a single email address can cause confusion when multiple teams use the same AWS account. Tag-based alert notifications are available for most Amazon CloudWatch alarms.

**Tag-based alert notification examples**

|
|
| Notification type | Example alert scenarios | Relevant tags |
| --- |--- |--- |
| Security | Escalations of privileges, uses of exposed credentials, or communication with malicious IP addresses or domains<br />Access behavior that points to signs of account compromise, such as unauthorized infrastructure deployments | **ams:rt:ams-managed** |
| Operations: Service-level events | A change to an underlying AWS service that affects your infrastructure<br />Amazon EC2 hardware issues that require you to reboot an instance before a certain date | **ams:rt:ams-managed**<br />**ams:rt:ams-monitoring-policy** |
| Operations: Resource-level events | Any resource-level change in your AWS environment | **ownerteamemail** |
| Operations: Patching | An advance notice of each upcoming maintenance window<br />Patching statuses | **ams:rt:ams-managed**<br />**AmsDefaultPatchKey ** |
| Operations: Incidents | Logging the occurrence of incidents<br />Incident updates<br />Incident resolution notices | **ams:rt:ams-managed** |
| Operations: Backups | AWS Backup job failures<br />AWS Backup job expirations<br />Amazon Relational Database Service (Amazon RDS) backup job failures | **ams:rt:ams-managed**<br />**ams:rt:backup-orchestrator **<br />**ams-onboarding-backup-plan ** |
