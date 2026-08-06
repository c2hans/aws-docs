---
source_url: https://docs.aws.amazon.com/managedservices/latest/userguide/tr-supported-recommendations-co.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Compute Optimizer recommendations supported by Trusted Remediator
<a name="tr-supported-recommendations-co"></a>

The following table lists the supported Compute Optimizer recommendations, SSM automation documents, preconfigured parameters, and the expected outcome of the automation documents. Review the expected outcome to help you understand possible risks based on your business requirements before you enable an SSM automation document for check remediation.

Make sure that the corresponding config rule for each Compute Optimizer check is present for the supported checks that you want to enable remediation for. For more information, see [Opt in AWS Compute Optimizer for Trusted Advisor checks](https://docs.aws.amazon.com/awssupport/latest/user/compute-optimizer-with-trusted-advisor.html).

<a name="cost-optimizer-recommendations"></a>
<table>
<thead>
  <tr><th>Optimization option</th><th>SSM document name and expected outcome</th><th>Supported preconfigured parameters and constraints</th></tr>
</thead>
<tbody>
  <tr><td colspan="3">Rightsizing</td></tr>
  <tr><td>[Amazon EC2 instance recommendations](https://aws.amazon.com/compute-optimizer/faqs/#topic-4)</td><td>**AWSManagedServices-TrustedRemediatorResizeInstanceByComputeOptimizerRecommendation**<br />Amazon EC2 instance type updated according Compute Optimizer recommendations. The most optimal options are chosen while maintain the same platform parameters (Architecture, Hypervisor, Network interface, Virtualization type, and so forth) if the option exists.</td><td>+ **MinimumDaysSinceLastChange**: The parameter to specify minimum number of days since the last instance type change. The default is 7 days. <br />No constraints<br />+ **CreateAMIBeforeResize**: To create the instance AMI as backup before resizing, set to 'true.' To not create a backup, set to 'false.' Default is 'true'.  <br />No constraints</td></tr>
  <tr><td>[Amazon EBS volume recommendations](https://aws.amazon.com/compute-optimizer/faqs/#topic-6)</td><td>**AWSManagedServices-ModifyEBSVolume**<br /> The Amazon EBS volume is modified according to Compute Optimizer recommendations. Modification may include volume type, size, IOPS, volume generation (gp2, gp3 etc).</td><td>+ **CreateSnapshot**: To create a snapshot before modifying the volume, set to 'true.' To not create a snapshot, set to 'false.' The default is 'true'. <br />No constraints<br />+ **VolumeType**: The desired volume type. If no type is specified, the existing type is retained. <br />No constraints<br />+ **VolumeSize**: The desired size of the volume, in GiB. The target volume size must be greater than or equal to the existing size of the volume. If no size is specified, the existing size is retained. <br />No constraints<br />+ **Iops**: The requested number of I/O operations per second (IOPS). This parameter is only valid for io1, io2 and gp3 volumes. <br />No constraints<br />+ **Throughput**: The throughput to provision for a volume, with a maximum of 1000 MiB/s. This parameter is valid only for gp3 volumes. <br />No constraints<br />+ **RemediateStackDrift**: To initiate drift remediation, if any drift is caused by volume modification, set to 'true.' To not attempt drift remediation, set to 'false.' Default is 'true'. <br />No constraints</td></tr>
  <tr><td>[Lambda function recommendations](https://aws.amazon.com/compute-optimizer/faqs/#topic-7)</td><td>**AWSManagedServices-TrustedRemediatorOptimizeLambdaMemory**<br />AWS Lambda function memory optimized according to Compute Optimizer recommendations.</td><td>**RecommendedMemorySize **: Custom memory size, if different from recommended options.<br />No constraints</td></tr>
  <tr><td colspan="3">Idle resources</td></tr>
  <tr><td>[Idle Amazon EBS volume](https://aws.amazon.com/compute-optimizer/faqs/#topic-9)</td><td>**AWSManagedServices-DeleteUnusedEBSVolume**<br />Unattached Amazon EBS volume will be deleted.</td><td>+ **CreateSnapshot**: To create a snapshot before deleting the volume, set to 'true.' To not create a snapshot, set to 'false.' The default is 'true'. <br />No constraints<br />+ **MinimumUnattachedDays**: Minimum unattached days of the Amazon EBS volume to delete, up to 62 days. Default is 7.  <br />No constraints</td></tr>
  <tr><td>[Idle Amazon EC2 instance](https://aws.amazon.com/compute-optimizer/faqs/#topic-9)</td><td>**AWSManagedServices-StopEC2Instance**<br />The idle Amazon EC2 instance will be stopped.</td><td>**ForceStopWithInstanceStore**: To force stop for instances using instance store, set to 'true.' To not force stop, set to 'false.' Default value 'false' prevents the instance from stopping.<br />No constraints</td></tr>
  <tr><td>[Idle Amazon RDS instance](https://aws.amazon.com/compute-optimizer/faqs/#topic-9)</td><td>**AWSManagedServices-StopIdleRDSInstance**<br />Stop an idle Amazon RDS instance. Supported engines are: MariaDB, Microsoft SQL Server, MySQL, Oracle, PostgreSQL. This document doesn't apply to Aurora MySQL and Aurora PostgreSQL. The instance will be stopped up to 7 days and relaunched automatically.</td><td>No preconfigured parameters are allowed.<br />No constraints</td></tr>
</tbody>
</table>
