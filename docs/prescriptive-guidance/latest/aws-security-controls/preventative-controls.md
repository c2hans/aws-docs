---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/preventative-controls.html
---

# Preventative controls
<a name="preventative-controls"></a>

*Preventative controls* are security controls that are designed to prevent an event from occurring. These guardrails are a first line of defense to help prevent unauthorized access or unwanted changes to your network. An example of a preventative control is an AWS Identity and Access Management (IAM) role that has read-only access because it helps prevent unintended write actions from unauthorized users.

Review the following about this type of control:
+ [Objectives](#preventative-objectives)
+ [Process](#preventative-process)
+ [Use cases](#preventative-use-cases)
+ [Technology](#preventative-technology)
+ [Business outcomes](#preventative-business-outcomes)

## Objectives
<a name="preventative-objectives"></a>

The primary purpose of preventative controls is to minimize or avoid the likelihood of a threat event from occurring. The control should help prevent unauthorized access to the system and help prevent unintentional changes from affecting the system. The following are the objectives of preventative controls:
+ **Segregation of duties** – Preventative controls can establish logical boundaries that limit privileges, allowing permissions to perform only specific tasks in designated accounts or environments. Examples include:
  + Segmenting workloads to different accounts for specific services
  + Separating and accounts into isolated production, development, and test environments
  + Delegating access and responsibilities to multiple entities to perform specific functions, such as using IAM roles or assumed roles to allow only specific job functions to perform certain actions
+ **Access control** – Preventative controls can consistently grant or deny access to resources and data in the environment. Examples include:
  + Preventing users from exceeding their intended permissions, known as *privilege* *escalation*
  + Restricting access to applications and data to only authorized users and services
  + Keeping the administrator group small
  + Avoiding use of the root user credentials
+ **Enforcement** – Preventative controls can help your company adhere to its policies, guidelines, and standards. Examples include:
  + Locking configurations that serve as the minimum security baseline
  + Implementing additional security measures, such as multi-factor authentication
  + Avoiding nonstandard tasks and actions that are performed by unapproved roles

## Process
<a name="preventative-process"></a>

*Preventative control mapping* is the process of mapping controls to requirements and using policies to implement those controls by restricting, disabling, or blocking. When mapping controls, consider the proactive effect they have on the environment, resources, and users. The following are best practices for mapping controls:
+ Strict controls that disallow an activity should be mapped to production environments where the action requires review, approval, and change processes.
+ Development or contained environments might have fewer preventative controls in order to provide the agility to build and test.
+ The classification of data, risk level of an asset, and risk management policy dictate the preventative controls.
+ Map to existing frameworks as evidence of compliance with standards and regulations.
+ Implement preventative controls by geographical location, environment, accounts, networks, users, roles, or resources.

## Use cases
<a name="preventative-use-cases"></a>

### Data handling
<a name="data-handling.68287bfa-45c3-5016-b9cb-44d9a3a277c8"></a>

A role is created that can access all data in an account. If there is sensitive and encrypted data, overly permissive privileges might present a risk, depending on the users or groups that can assume the role. By using a key policy in AWS Key Management Service (AWS KMS), you can control who has access to the key and can decrypt the data.

### Privilege escalation
<a name="privilege-escalation.72ba2717-8243-5c3c-b3ee-669bb188001a"></a>

If administrative and write permissions are assigned too broadly, a user can circumvent the limits of their intended permissions and grant themselves additional privileges. The user who creates and manages a role can assign a *permissions boundary*, which defines the maximum allowable privileges for the role.

### Workload lockdown
<a name="workload-lockdown.7dc21813-991b-567f-a56d-f5f36a0f3c5c"></a>

If your business does not have a foreseeable need to use specific services, enable a *service control policy *that limits which services can operate in an organization's member accounts or restricts services based on the AWS Region. This preventative control can reduce the scope of impact if a threat actor manages to compromise and access an account in your organization. For more information, see [Service control policies](#preventative-technology) in this guide.

### Impact to other applications
<a name="impact-to-other-applications.4d729c56-2bf6-5907-96e6-a476bb7f01d7"></a>

Preventative controls can enforce the use of services and features, such as IAM, encryption, and logging, in order to meet the security requirements of your applications. You can also use these controls to help protect against vulnerabilities by limiting the actions that a threat actor can exploit due to unintentional errors or misconfiguration.

## Technology
<a name="preventative-technology"></a>

### Service control policies
<a name="service-control-policies.c8c18627-b8d4-5d85-b986-2b2dbef00a1e"></a>

In AWS Organizations, [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (SCPs) define the maximum available permissions for member accounts in an organization. These policies help accounts stay within access control guidelines of the organization. Note the following when designing SCPs for your organization:
+ SCPs are preventative controls because they define and enforce the maximum allowable permissions for IAM roles and users in the organization's member accounts.
+ SCPs affect only the IAM roles and users in the member accounts of the organization. It does not affect users and roles in the management account of the organization.

You can make an SCP more granular by defining the maximum permissions for each AWS Region.

### IAM permissions boundaries
<a name="iam-permissions-boundaries.8ccfd44f-6403-5a87-a942-89c22d9f8d1c"></a>

In AWS Identity and Access Management (IAM), a [permissions boundary](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) is used to set the maximum permissions that an identity-based policy can grant to an IAM entity (users or roles). An entity's permission boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permission boundaries. Note the following when using permissions boundaries:
+ You can use an AWS managed policy or a customer managed policy to set the boundary for an IAM entity.
+ A permissions boundary does not grant permissions on its own. The permissions boundary policy limits the permissions that are granted to the IAM entity.

## Business outcomes
<a name="preventative-business-outcomes"></a>

### Time savings
<a name="time-savings.6f3bc2c4-be5e-5f22-a8d3-6d4e0c941ea6"></a>
+ By adding automation after you set up preventative controls, you can reduce the need for manual intervention and reduce the frequency of errors.
+ Using permission boundaries as a preventative control helps security and IAM teams focus on critical tasks, such as governance and support.

### Regulatory compliance
<a name="regulatory-compliance.798168da-3d26-59ce-baff-cea3b4313cdf"></a>
+ Companies might need to comply with internal or industry regulations. These might be regional restrictions, user and role restrictions, or service restrictions. SCPs can help you stay compliant and avoid violation penalties.

### Risk reduction
<a name="risk-reduction.2183d541-722c-5a1a-8e0c-e7ffe9e1cffd"></a>
+ With growth, the number of requests to create and manage new roles and policies increases. It becomes more challenging to understand the context of what is required to manually create the permissions for each application. Establishing preventative controls acts as a baseline and helps prevent users from performing unintended actions, even if they were accidentally given access.
+ Applying preventative controls to access policies provides an additional layer to help protect data and assets.
