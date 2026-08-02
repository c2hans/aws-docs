---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/exposure-sagemaker-notebook-instance.html
---

# Remediating exposures for Amazon SageMaker notebook instances
<a name="exposure-sagemaker-notebook-instance"></a>

AWS Security Hub can generate exposure findings for Amazon SageMaker notebook instances.

On the Security Hub console, the notebook instance involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details. Programmatically, you can retrieve resource details with the [https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsV2.html](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsV2.html) operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it. Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential, follow these recommended remediation steps to help mitigate the risk. The remediation topics are divided based on the type of trait.

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down its severity level by addressing just one remediation topic. Your approach to risk remediation depends on your organizational requirements and workloads.

**Note**
 The remediation guidance provided in this topic might require additional consultation in other AWS resources.

**Contents**
+ [Misconfiguration traits for Amazon SageMaker notebook instances](#sagemaker-misconfiguration)
  + [The Amazon SageMaker notebook instance has direct internet access enabled](#outbound-internet-enabled)
  + [The Amazon SageMaker notebook instance has root access enabled](#notebook-root-access-enabled)
+ [Impact traits for Amazon SageMaker notebook instances](#sagemaker-impact)
  + [Full control privileged executor](#full-control-privileged-executor)
  + [Direct policy escalation](#direct-policy-escalation)
  + [Trust policy hijack](#trust-policy-hijack)
  + [Data ransomware](#data-ransomware)
  + [Remove restriction](#remove-restriction)
  + [Pass role create executor](#pass-role-create-executor)
  + [Swap role existing executor](#swap-role-existing-executor)
  + [Role chain escalation](#role-chain-escalation)
  + [Inject code privileged executor](#inject-code-privileged-executor)
  + [Disable audit trail](#disable-audit-trail)
  + [Access existing executor](#access-existing-executor)
  + [Credential minting](#credential-minting)
  + [Pass role data access](#pass-role-data-access)
  + [Pass role task hijack](#pass-role-task-hijack)
  + [Single hop data access](#single-hop-data-access)
  + [Capability advancing](#capability-advancing)

## Misconfiguration traits for Amazon SageMaker notebook instances
<a name="sagemaker-misconfiguration"></a>

Here are misconfiguration traits for Amazon SageMaker notebook instances and suggested remediation steps.

### The Amazon SageMaker notebook instance has direct internet access enabled
<a name="outbound-internet-enabled"></a>

 When `DirectInternetAccess` is enabled on an Amazon SageMaker notebook instance, outbound traffic is routed through a SageMaker-managed network address translation (NAT) gateway to the internet. This provides an egress path that can be used for data exfiltration or as a command-and-control channel if the notebook is compromised. Following security best practices, AWS recommends disabling direct internet access and placing notebook instances in a VPC with VPC endpoints for required AWS services.

**Disable direct internet access**
 The `DirectInternetAccess` setting cannot be changed after a notebook instance is created. To disable it, create a new notebook instance with `DirectInternetAccess` set to `Disabled` in a private subnet within a VPC, then migrate your notebooks and data from the existing instance. For instructions, see [Connect a notebook instance in a VPC to external resources](https://docs.aws.amazon.com/sagemaker/latest/dg/appendix-notebook-and-internet-access.html) in the *Amazon SageMaker Developer Guide*.

**Configure VPC endpoints**
 When direct internet access is disabled, the notebook instance requires VPC endpoints to access AWS services such as Amazon S3 and the Amazon SageMaker API. Create interface VPC endpoints for the services your notebook needs. For information on VPC endpoints, see [What is AWS PrivateLink?](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) in the *AWS PrivateLink Guide*.

### The Amazon SageMaker notebook instance has root access enabled
<a name="notebook-root-access-enabled"></a>

 When `RootAccess` is enabled on an Amazon SageMaker notebook instance, users have full OS-level root privileges. Root access allows arbitrary system modifications, persistent backdoors, and unrestricted package installation. Following security best practices, AWS recommends disabling root access for notebook instances unless it is explicitly required for your workflow.

**Disable root access**
 You cannot change the `RootAccess` setting on a running notebook instance. To disable it, stop the instance, then update the instance configuration to set `RootAccess` to `Disabled`. Most notebook workflows, including installing packages with `pip` and running lifecycle configurations, continue to work without root access. For instructions, see [Control root access to a Amazon SageMaker notebook instance](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-root-access.html) in the *Amazon SageMaker Developer Guide*.

**Additional considerations**
 If root access is required for specific tasks, consider using Amazon SageMaker Studio notebooks instead, which provide isolated container-based environments with more granular access controls. You can also use lifecycle configurations to pre-install required packages at instance creation time, reducing the need for root access during normal use.

## Impact traits for Amazon SageMaker notebook instances
<a name="sagemaker-impact"></a>

Impact traits describe the potential blast radius of an exposure. Security Hub analyzes the effective permissions of the AWS Identity and Access Management principal associated with the SageMaker notebook instance to determine the downstream resources an attacker could reach if the notebook instance is compromised. Each impact trait identifies a specific privilege escalation pattern. To reduce your blast radius, review the permission paths described in each trait and remove any unnecessary privileges.

Following standard security principles, AWS recommends that you grant least privilege — only the permissions required to perform a task. Replace broad policies with scoped-down policies that grant only the specific actions and resources needed. To identify unused permissions to remove, use IAM Access Analyzer to generate recommendations based on access history. For more information, see [Findings for external and unused access](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html) and [Apply least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) in the *IAM User Guide*.

### Full control privileged executor
<a name="full-control-privileged-executor"></a>

The associated principal can pass a role to and inject code into a compute resource that already has elevated permissions. This allows the principal to gain full control over the executor and perform any action that the executor's role permits.

### Direct policy escalation
<a name="direct-policy-escalation"></a>

The associated principal can directly modify IAM policies to grant itself additional permissions, escalating its own privileges without intermediate resources.

### Trust policy hijack
<a name="trust-policy-hijack"></a>

The associated principal can modify the trust policy of an IAM role to allow itself to assume that role, gaining the role's permissions.

### Data ransomware
<a name="data-ransomware"></a>

The associated principal can encrypt or delete data in a way that could be used for ransomware, such as encrypting Amazon S3 objects with a customer-managed AWS KMS key and then modifying the key policy.

### Remove restriction
<a name="remove-restriction"></a>

The associated principal can remove security restrictions such as permission boundaries, service control policies, or resource-based policy deny statements, expanding what other principals or the resource itself can do.

### Pass role create executor
<a name="pass-role-create-executor"></a>

The associated principal can create a new compute resource (such as a Lambda function or Amazon EC2 instance) and pass it a privileged role, effectively laundering its own permissions through the new resource.

### Swap role existing executor
<a name="swap-role-existing-executor"></a>

The associated principal can change the IAM role attached to an existing compute resource, replacing it with a more privileged role to escalate access.

### Role chain escalation
<a name="role-chain-escalation"></a>

The associated principal can assume a sequence of roles, where each role in the chain has progressively broader permissions, ultimately reaching a highly privileged role.

### Inject code privileged executor
<a name="inject-code-privileged-executor"></a>

The associated principal can inject code into a running compute resource that has elevated permissions, executing arbitrary operations under that resource's privileged role.

### Disable audit trail
<a name="disable-audit-trail"></a>

The associated principal can disable logging or monitoring services such as CloudTrail, effectively covering its tracks during or after an escalation.

### Access existing executor
<a name="access-existing-executor"></a>

The associated principal can invoke or connect to an existing compute resource and use its attached role to perform privileged actions.

### Credential minting
<a name="credential-minting"></a>

The associated principal can create new long-term credentials (such as access keys or login profiles) for other principals, establishing persistent access paths that survive password rotations or session expirations.

### Pass role data access
<a name="pass-role-data-access"></a>

The associated principal can create a service resource and pass it a role that has access to sensitive data, gaining indirect access to that data through the new resource.

### Pass role task hijack
<a name="pass-role-task-hijack"></a>

The associated principal can pass a role to a scheduled or event-driven task (such as a Lambda function triggered by an event), allowing it to execute arbitrary code with that role's permissions.

### Single hop data access
<a name="single-hop-data-access"></a>

The associated principal can directly access sensitive data resources (such as Amazon S3 buckets or DynamoDB tables) through its existing permissions, without needing intermediate escalation steps.

### Capability advancing
<a name="capability-advancing"></a>

The associated principal has a privilege escalation path that advances its overall capabilities beyond what its directly assigned permissions would suggest. This is a general classification for paths that do not match a more specific pattern.
