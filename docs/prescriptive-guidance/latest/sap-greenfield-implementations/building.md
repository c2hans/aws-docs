---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sap-greenfield-implementations/building.html
---

# Best practices for the build phase
<a name="building"></a>

The recommendations in this section help ensure a smoother build phase for your project. The build phase encompasses code, development, deployment, and implementation activities.  It often consists of a design review and approval session, a kick-off meeting to align on what is being built, timeline, and exit criteria. This is the phase where code is written, peer-reviewed, and deployed for all AWS services.

The following recommendations also cover testing or verification activities.

## Host daily stand-up meetings
<a name="standup"></a>

Be sure to host daily stand-up meetings, no matter which project methodology you're using. Although daily stand-ups are associated with agile methodologies, they are also extremely useful team connection mechanisms for other methodologies, including the waterfall model.  You might even use a hybrid project framework that that takes the best practices from various methodologies.

Considerations:
+ Use something lightweight like Jira boards to create stories for every task. These boards will be your guide for your daily stand-ups.   If your team has the bandwidth and expertise, you can also use the Scaled Agile Framework (SAFe) methodology and create epics.  However, most infrastructure teams do not want the administrative overhead of managing complex scrum boards, so we recommend a lightweight tool.  Having a board also enables you to generate reports on the work that your team is doing, and gives you mechanisms for controlling scope.
+ In a greenfield SAP project, it is not uncommon for many SAP or boundary applications to be added after the scope is locked.  If you don't have a good mechanism for controlling, prioritizing, and providing visibility to the scope of the project, it will be difficult to request additional resources or reprioritize work to keep the project on track.

## Use a unified build specification sheet
<a name="build-spec"></a>

Use a single build specification spreadsheet for all environments and landscapes.**  **This creates a single document that can easily be located and searched.  We recommend that you enable version management to easily recover from mishaps.    Come up with a format in cooperation with the SAP Basis team.  The Basis team keeps track of details around SAP systems, and having a single specification ensures that the in-house cloud team can quickly take ownership and see all the metadata in one place after project completion.

Here's an example of a template used to capture key server build metadata with one sample server requirement.

![Build specification for capturing server metadata for an SAP on AWS greenfield project](https://docs.aws.amazon.com/prescriptive-guidance/latest/sap-greenfield-implementations/images/guide-img/3deae530-9b57-46ef-8dd1-542c426e8365/images/61a644c7-466b-485f-9889-70db9155792f.png)

## Be aware of AWS service quotas
<a name="quotas"></a>

There are quotas on the number of virtual CPUs (vCPUs) that you can provision for Amazon Elastic Compute Cloud (Amazon EC2) instances. When you deploy an EC2 instance, it requires a certain number of vCPUs, depending on the EC2 instance type. Every AWS account has a soft limit on the number of vCPUs that can be provisioned for it. As you deploy EC2 instances, the soft limit increases automatically by about 100-150 vCPUs.  However, if you try to deploy multiple (say, 20) EC2 instances at the same time, you might exceed the soft limit. If you think you might encounter this limitation, [submit a request to increase the quota](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) before you deploy EC2 instances. This will allow you to avoid reaching service quota limits in the middle of deployment.

## Develop a key rotation strategy for security
<a name="key-rotation"></a>

AWS Key Management Service (AWS KMS) makes it easy for customers to create and manage cryptographic keys and control their use across a wide range of AWS services and in various applications. For SAP implementations, AWS KMS keys are used to encrypt data at rest that is stored in Amazon Elastic Block Store (Amazon EBS) volumes and are used for SAP binaries and SAP HANA file systems.  KMS keys are also used for data that is stored in Amazon Simple Storage Service (Amazon S3) buckets to hold software media and backups, and in Amazon Elastic File System (Amazon EFS) file systems for /usr/sap/trans and /sapmnt. AWS KMS gives you the flexibility to use either AWS managed keys or customer managed keys. We recommend that you document and share your security key management strategy and decisions at the beginning of the build phase. Security policy changes in the middle of the project, such as switching from customer managed keys to AWS managed keys, can require complete rebuilds of SAP environments, which might impact your project timelines.

Attain buy-in from all security stakeholders on key usage and rotation.  Consider your existing key rotation policies for the cloud or on-premises environments and modify these policies for use on AWS.  If you face difficulties gaining consensus on your key management strategy, provide training to decision makers, to help them understand security baselining and level-setting considerations.   Making key rotation decisions before environments are built is crucial.  For example, if you were to change from customer managed keys to AWS managed keys, you would encounter a problem with Amazon EBS, which doesn't allow changes to encryption keys online. The EBS volumes have to be rebuilt with new keys. This necessitates rebuilding your SAP instances, which is not an ideal scenario.

Similarly, if your project uses external key management solutions, such as Vormetric, and imports the key material into AWS KMS, make sure that your security decision makers are aware of key rotation differences between external KMS keys and AWS KMS keys (automatic rotation). When you use and rotate an external KMS key according to your security policy, not only the key material but also the key's Amazon Resource Name (ARN) changes, which means that EBS volumes will have to be recreated, and the entire SAP system will have to undergo a small migration. On the other hand, if you enable automatic rotation for customer managed keys or AWS managed keys in AWS KMS, the key material changes but the key ARN remains the same, which means that EBS volumes are not affected. For more information about key rotation, see [Rotating AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) in the AWS KMS documentation.

Another security approach is to use AWS Secrets Manager for database and operating system password rotation, which is available through a standard dashboard. In addition, make sure that the AWS Identity and Access Management (IAM) roles for the disaster recovery environment are isolated from the production environment to help protect the environments against malicious activity.

## Decommission unused servers
<a name="servers"></a>

We recommend that you decommission proof of concept (PoC) servers immediately after their usefulness has run out.  Running servers that are not in use can be costly.   It's important to keep track of all servers that you build for your greenfield SAP implementation, and stop and decommission the servers that you aren't actively using during the build phase.  Before you decommission a server, you can make an Amazon Machine Image (AMI) backup of the EC2 instance. You can then restore the backup if you need to spin up the exact same server in the future.

Decommissioning servers should not be an exercise you save for the end of the implementation project.  You should monitor usage, stop, and eventually destroy unused servers throughout the lifespan of your project and after you complete implementation, in the maintenance or operational phases. Make sure to set up a process at the beginning to teach SAP Basis team members to decommission these servers, because charges will accumulate quickly.
