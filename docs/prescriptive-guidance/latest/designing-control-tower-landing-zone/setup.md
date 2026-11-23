---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/setup.html
---

# Setting up a landing zone

AWS Control Tower automates the setup of a landing zone by using templates that follow AWS guidance for identity, federated access, controls, and account structure. AWS Control Tower helps you set up and govern a secure, multi-account AWS environment. The [AWS Control Tower dashboard](https://aws.amazon.com/controltower/features/) provides visibility into your landing zone environment, an aggregated view of organizational units (OUs) and accounts in the organization, the controls that are enabled, and the compliance status of OUs and accounts with those controls. The dashboard also lists non-compliant resources so that you can identify required actions.

If your enterprise is new to AWS, we recommend that you start with AWS Control Tower as the foundation for your landing zone. However, as an alternative, you can opt for a [custom-built landing zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-aws-environment/building-landing-zones.html).

## AWS Control Tower managed resources
<a name="managed-resources"></a>

When you set up a landing zone, AWS Control Tower creates multiple managed resources in your [management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) for the accounts in the landing zone. For more information about these resources, see [How AWS Control Tower works](https://docs.aws.amazon.com/controltower/latest/userguide/how-control-tower-works.html) in the AWS Control Tower documentation.

**Important**
When you use a landing zone, don't modify or delete AWS Control Tower managed resources. Doing so might cause the landing zone to drift and enter an unknown state. For more information about drift, see [Detect and resolve drift in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/drift.html) in the AWS Control Tower documentation.

## Deployment
<a name="deployment"></a>

You deploy AWS Control Tower in a management account that you create for the new landing zone. In the management account, you provision new accounts and centrally manage or configure controls, user access, permissions, and organizational units (OUs).

When you set up the landing zone, AWS Control Tower automatically creates a Security OU that contains the Log Archive account and Audit account. These accounts enable centralized management and governance of the landing zone through monitoring and logging. For more information about OUs and accounts in the landing zone, see the [Account structure and OUs](account-structure.md) section of this guide.

## Launch parameters
<a name="launch-parameters"></a>

The following table shows the required parameters for setting up a landing zone.

|
|
| Category | Parameter | Sample values |
| --- |--- |--- |
| Regions | *Home Region*<br />This is the AWS Region where AWS Control Tower provisions shared resources. You can't change the home Region after you set up the landing zone, but you can add more Regions to govern. | Your current Region (as reflected in the AWS Region selector on the navigation bar). This field is not editable. |
| *Additional Regions for governance*<br />You can optionally choose additional Regions for AWS Control Tower to govern. | No additional Regions |
| *Region deny setting*<br />If you have data residency requirements, you can optionally choose to enable a Region deny service control policy (SCP) to deny access in Regions that aren't selected. | Not enabled |
| Configuration for the landing zone shared accounts | *Foundational organizational unit (OU)*<br />This is the OU that contains the shared accounts. | Security |
| *Additional OU*<br />This is a secondary OU for storing production or development accounts. | Sandbox |
| *Log Archive account options*<br />Either create a new account or use your existing Log Archive account. | Create new account |
| *Log Archive account details*<br />If you are creating a new account, specify a unique email address that is not yet associated with an AWS account. You can also specify the account name. The default name is Log Archive. If you are using an existing Log Archive account, specify the AWS account ID. You can't edit these details after you set up the landing zone. | aws-logarchive@example.com<br />Log Archive |
| *Audit account options*<br />Either create a new account or use your existing Audit account. | Create new account |
| *Audit account details*<br />If you are creating a new account, specify a unique email address that is not yet associated with an AWS account. Also specify the account name. The default name is Audit. If you are using an existing Audit account, specify the AWS account ID.You can't edit these details after you set up the landing zone. | audit@example.com<br />Audit |
| Additional configurationsThese are optional configurations. You can leave them at their default settings or choose your own configuration. | *AWS account access configuration*<br />You can optionally choose to manage account access yourself or accept the default IAM Identity Center setup in AWS Control Tower. | AWS Control Tower sets up AWS account access with IAM Identity Center. |
| *AWS CloudTrail configuration*<br />You can optionally choose to manage CloudTrail in your organization yourself or accept the default CloudTrail setup from AWS Control Tower. The default setting enables an organization-level trail for management events in your Log Archive account. | Enabled |
| *Log configuration for Amazon S3*<br />You can optionally configure log retention for the Log Archive S3 bucket or accept the default retention periods. | Standard account logging: 1 year <br />Access logging: 10 years  |
| *KMS encryption*<br />You can optionally enable encryption for AWS Control Tower resources by using an AWS Key Management Service (AWS KMS) customer managed key. If you enable encryption, specify the key name or Amazon Resource Name (ARN) of the customer managed key to use.If you don't enable this option, AWS Control Tower uses Amazon S3 server-side encryption (SSE-S3) with AWS managed keys as the default configuration. | Disabled |
