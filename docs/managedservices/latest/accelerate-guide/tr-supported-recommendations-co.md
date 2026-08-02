---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-supported-recommendations-co.html
---

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
  <tr><td>[Amazon EC2 instance recommendations](https://aws.amazon.com/compute-optimizer/faqs/#topic-4)</td><td>**AWSManagedServices-TrustedRemediatorResizeInstanceByComputeOptimizerRecommendation**<br />Amazon EC2 instance type updated according Compute Optimizer recommendations. The most optimal options are chosen while maintain the same platform parameters (Architecture, Hypervisor, Network interface, Virtualization type, and so forth) if the option exists.</td><td>[See the AWS documentation website for more details](http://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-supported-recommendations-co.html)</td></tr>
  <tr><td>[Amazon EBS volume recommendations](https://aws.amazon.com/compute-optimizer/faqs/#topic-6)</td><td>**AWSManagedServices-ModifyEBSVolume**<br /> The Amazon EBS volume is modified according to Compute Optimizer recommendations. Modification may include volume type, size, IOPS, volume generation (gp2, gp3 etc).</td><td>[See the AWS documentation website for more details](http://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-supported-recommendations-co.html)</td></tr>
  <tr><td>[Lambda function recommendations](https://aws.amazon.com/compute-optimizer/faqs/#topic-7)</td><td>**AWSManagedServices-TrustedRemediatorOptimizeLambdaMemory**<br />AWS Lambda function memory optimized according to Compute Optimizer recommendations.</td><td>**RecommendedMemorySize **: Custom memory size, if different from recommended options.<br />No constraints</td></tr>
  <tr><td colspan="3">Idle resources</td></tr>
  <tr><td>[Idle Amazon EBS volume](https://aws.amazon.com/compute-optimizer/faqs/#topic-9)</td><td>**AWSManagedServices-DeleteUnusedEBSVolume**<br />Unattached Amazon EBS volume will be deleted.</td><td>[See the AWS documentation website for more details](http://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-supported-recommendations-co.html)</td></tr>
  <tr><td>[Idle Amazon EC2 instance](https://aws.amazon.com/compute-optimizer/faqs/#topic-9)</td><td>**AWSManagedServices-StopEC2Instance**<br />The idle Amazon EC2 instance will be stopped.</td><td>**ForceStopWithInstanceStore**: To force stop for instances using instance store, set to 'true.' To not force stop, set to 'false.' Default value 'false' prevents the instance from stopping.<br />No constraints</td></tr>
  <tr><td>[Idle Amazon RDS instance](https://aws.amazon.com/compute-optimizer/faqs/#topic-9)</td><td>**AWSManagedServices-StopIdleRDSInstance**<br />Stop an idle Amazon RDS instance. Supported engines are: MariaDB, Microsoft SQL Server, MySQL, Oracle, PostgreSQL. This document doesn't apply to Aurora MySQL and Aurora PostgreSQL. The instance will be stopped up to 7 days and relaunched automatically.</td><td>No preconfigured parameters are allowed.<br />No constraints</td></tr>
</tbody>
</table>
