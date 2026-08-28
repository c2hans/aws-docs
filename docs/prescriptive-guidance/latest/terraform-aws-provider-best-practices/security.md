---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/security.html
---

# Security best practices
<a name="security"></a>

Properly managing authentication, access controls, and security is critical for secure usage of the Terraform AWS Provider. This section outlines best practices around:
+ IAM roles and permissions for least-privilege access
+ Securing credentials to help prevent unauthorized access to AWS accounts and resources
+ Remote state encryption to help protect sensitive data
+ Infrastructure and source code scanning to identify misconfigurations
+ Access controls for remote state storage
+ Sentinel policy enforcement to implement governance guardrails

Following these best practices helps strengthen your security posture when you use Terraform to manage AWS infrastructure.

## Follow the principle of least privilege
<a name="least-privilege"></a>

[Least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) is a fundamental security principle that refers to granting only the minimum permissions required for a user, process, or system to perform its intended functions. It's a core concept in access control and a preventative measure against unauthorized access and potential data breaches.

The principle of least privilege is emphasized multiple times in this section because it directly relates to how Terraform authenticates and runs actions against cloud providers such as AWS.

When you use Terraform to provision and manage AWS resources, it acts on behalf of an entity (user or role) that requires appropriate permissions to make API calls. Not following least privilege opens up major security risks:
+ If Terraform has excessive permissions beyond what's needed, an unintended misconfiguration could make undesired changes or deletions.
+ Overly permissive access grants increase the scope of impact if Terraform state files or credentials are compromised.
+ Not following least privilege goes against security best practices and regulatory compliance requirements for granting minimal required access.

## Use IAM roles
<a name="iam-roles"></a>

Use IAM roles instead of IAM users wherever possible to enhance security with the Terraform AWS Provider. IAM roles provide temporary security credentials that automatically rotate, which eliminates the need to manage long-term access keys. Roles also offer precise access controls through IAM policies.

### Grant least privilege access by using IAM policies
<a name="grant-least-privilege-access-by-using-9999999999999999iam--policies.66cf2042-85b6-5efb-9778-459c4a9b5378"></a>

Carefully construct IAM policies to ensure that roles and users have only the minimum set of permissions that are required for their workload. Start with an empty policy and iteratively add allowed services and actions. To accomplish this:
+ Enable [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html#access-analyzer-policy-generation-console) to evaluate policies and highlight unused permissions that can be removed.
+ Manually review policies to remove any capabilities that aren't essential for the role's intended responsibility.
+ Use [IAM policy variables and tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html) to simplify permission management.

Well-constructed policies grant just enough access to accomplish the workload's responsibilities and nothing more. Define actions at the operation level, and allow calls only to required APIs on specific resources.

Following this best practice reduces the scope of impact and follows the fundamental security principles of separation of duties and least privilege access. Start strict and open access gradually as needed, instead of starting open and trying to restrict access later.

### Assume IAM roles for local authentication
<a name="assume-9999999999999999iam--roles-for-local-authentication.3435846f-0968-5e54-9b7d-bb3202366bf1"></a>

When you run Terraform locally, avoid configuring static access keys. Instead, use [IAM roles to grant privileged access temporarily](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html) without exposing long-term credentials.

First, create an IAM role with the necessary minimum permissions and add a [trust relationship](https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/) that allows the IAM role to be assumed by your user account or federated identity. This authorizes temporary usage of the role.

Trust relationship policy example:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/terraform-execution"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

Then, run the AWS CLI command **aws sts assume-role** to retrieve short-lived credentials for the role. These credentials are typically valid for one hour.

AWS CLI command example:

```
aws sts assume-role --role-arn arn:aws:iam::111122223333:role/terraform-execution --role-session-name terraform-session-example
```

The output of the command contains an access key, secret key, and session token that you can use to authenticate to AWS:

```
{
    "AssumedRoleUser": {
        "AssumedRoleId": "AROA3XFRBF535PLBIFPI4:terraform-session-example",
        "Arn": "arn:aws:sts::111122223333:assumed-role/terraform-execution/terraform-session-example"
    },
    "Credentials": {
        "SecretAccessKey": " wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
        "SessionToken": " AQoEXAMPLEH4aoAH0gNCAPyJxz4BlCFFxWNE1OPTgk5TthT+FvwqnKwRcOIfrRh3c/LTo6UDdyJwOOvEVPvLXCrrrUtdnniCEXAMPLE/IvU1dYUg2RVAJBanLiHb4IgRmpRV3zrkuWJOgQs8IZZaIv2BXIa2R4OlgkBN9bkUDNCJiBeb/AXlzBBko7b15fjrBs2+cTQtpZ3CYWFXG8C5zqx37wnOE49mRl/+OtkIKGO7fAE",
        "Expiration": "2024-03-15T00:05:07Z",
        "AccessKeyId": "ASIAIOSFODNN7EXAMPLE"
    }
}
```

The AWS Provider can also automatically handle [assuming the role](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#assuming-an-iam-role).

Provider configuration example for assuming an IAM role:

```
provider "aws" {
  assume_role {
    role_arn     = "arn:aws:iam::111122223333:role/terraform-execution"
    session_name = "terraform-session-example"
  }
}
```

This grants elevated privilege strictly for the Terraform session's duration. The temporary keys cannot be leaked because they expire automatically after the maximum duration of the session.

The key benefits of this best practice include improved security compared with long-lived access keys, fine-grained access controls on the role for least privileges, and the ability to easily revoke access by modifying the role's permissions. By using IAM roles, you also avoid having to directly store secrets locally in scripts or on disk, which helps you share Terraform configuration securely across a team.

### Use IAM roles for Amazon EC2 authentication
<a name="use-9999999999999999iam--roles-for-9999999999999999ec2--authentication.479e9020-4c45-5346-994d-62490f10ad6c"></a>

When you run Terraform from Amazon Elastic Compute Cloud (Amazon EC2) instances, avoid storing long-term credentials locally. Instead, use IAM roles and [instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) to grant least-privilege permissions automatically.

First, create an IAM role with the minimum permissions and assign the role to the instance profile. The instance profile allows EC2 instances to inherit the permissions defined in the role. Then, launch instances by specifying that instance profile. The instance will authenticate through the attached role.

Before you run any Terraform operations, verify that the role is present in the [instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html) to confirm that the credentials were successfully inherited.

```
TOKEN=$(curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")

curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

This approach avoids hardcoding permanent AWS keys into scripts or Terraform configuration within the instance. The temporary credentials are made available to Terraform transparently through the instance role and profile.

The key benefits of this best practice include improved security over long-term credentials, reduced credential management overhead, and consistency between development, test, and production environments. IAM role authentication simplifies Terraform runs from EC2 instances while enforcing least-privilege access.

### Use dynamic credentials for HCP Terraform workspaces
<a name="use-dynamic-credentials-for-hcp-terraform-workspaces.f2a1d4c2-1270-5799-8240-7fb55f031220"></a>

HCP Terraform is a managed service provided by HashiCorp that helps teams use Terraform to provision and manage infrastructure across multiple projects and environments. When you run Terraform in HCP Terraform, use [dynamic credentials](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/dynamic-provider-credentials/aws-configuration) to simplify and secure AWS authentication. Terraform automatically exchanges temporary credentials on each run without needing IAM role assumption.

Benefits include easier secret rotation, centralized credential management across workspaces, least-privilege permissions, and eliminating hardcoded keys. Relying on hashed ephemeral keys enhances security compared with long-lived access keys.

### Use IAM roles in AWS CodeBuild
<a name="use-9999999999999999iam--roles-in-9999999999999999acblong-.1712093e-64ed-5bd2-80b8-d7eb145f81a4"></a>

In AWS CodeBuild, run your builds by using an [IAM role that's assigned to the CodeBuild project](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html). This allows each build to automatically inherit temporary credentials from the role instead of using long-term keys.

### Run GitHub Actions remotely on HCP Terraform
<a name="run-github-actions-remotely-on-hcp-terraform.e8e3e806-aaaa-5d6d-87ee-d61ff809bc03"></a>

Configure GitHub Actions workflows to run Terraform remotely on HCP Terraform workspaces. Rely on dynamic credentials and remote state locking instead of GitHub secrets management.

### Use GitHub Actions with OIDC and configure the AWS Credentials action
<a name="use-github-actions-with-oidc-and-configure-the-9999999999999999aws--credentials-action.cfd1e2c5-712c-566a-bb72-44f7401eefab"></a>

Use the [OpenID Connect (OIDC) standard to federate GitHub Actions identity through IAM](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services). Use the [Configure AWS Credentials action](https://github.com/aws-actions/configure-aws-credentials) to exchange the GitHub token for temporary AWS credentials without needing long-term access keys.

### Use GitLab with OIDC and the AWS CLI
<a name="use-gitlab-with-oidc-and-the-9999999999999999cli-.3e62b8db-b783-5100-a08c-a83743e507f4"></a>

Use the [OIDC standard to federate GitLab identities through IAM](https://docs.gitlab.com/ee/ci/cloud_services/aws/) for temporary access. By relying on OIDC, you avoid needing to directly manage long-term AWS access keys within GitLab. Credentials are exchanged just-in-time, which improves security. Users also gain least privilege access according to the permissions in the IAM role.

## Use unique IAM users with legacy automation tools
<a name="legacy-automation-tools"></a>

If you have automation tools and scripts that lack native support for using IAM roles, you can create individual IAM users to grant programmatic access. The principle of least privilege still applies. Minimize policy permissions and rely on separate roles for each pipeline or script. As you migrate to more modern tools or scripts, begin supporting roles natively and gradually transition to them.

**Warning**
IAM users have long-term credentials, which present a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed.

### Use the Jenkins AWS Credentials plugin
<a name="use-the-jenkins-9999999999999999aws--credentials-plugin.6d944e4f-b57c-5f0e-a6e6-07ddb036a0d8"></a>

Use the [AWS Credentials plugin](https://plugins.jenkins.io/aws-credentials/) in Jenkins to centrally configure and inject AWS credentials into builds dynamically. This avoids checking secrets into source control.

## Continuously monitor, validate, and optimize least privilege
<a name="continuous-monitoring"></a>

Over time, additional permissions might get granted that can exceed the minimum policies required. Continuously analyze access to identify and remove any unnecessary entitlements.

### Continuously monitor access key usage
<a name="continuously-monitor-access-key-usage.b3967a30-33f3-5b79-8897-f1f1da29cd90"></a>

If you cannot avoid using access keys, use [IAM credential reports](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html) to find unused access keys that are older than 90 days, and revoke inactive keys across both user accounts and machine roles. Alert administrators to manually confirm the removal of keys for active employees and systems.

Monitoring key usage helps you optimize permissions because you can identify and remove unused entitlements. When you follow this best practice with [access key rotation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey), it limits credential lifespan and enforces least privilege access.

AWS provides several services and features that you can use to set up alerts and notifications for administrators. Here are some options:
+ [**AWS Config**](https://aws.amazon.com/config/): You can use AWS Config rules to evaluate the configuration settings of your AWS resources, including IAM access keys. You can create custom rules to check for specific conditions, such as unused access keys that are older than a specific number of days. When a rule is violated, AWS Config can start an evaluation for remediation or send notifications to an Amazon Simple Notification Service (Amazon SNS) topic.
+ [**AWS Security Hub CSPM**](https://aws.amazon.com/security-hub/): Security Hub CSPM provides a comprehensive view of your AWS account's security posture and can help detect and notify you about potential security issues, including unused or inactive IAM access keys. Security Hub CSPM can integrate with Amazon EventBridge and Amazon SNS or Amazon Q Developer in chat applications to send notifications to administrators.
+ [**AWS Lambda**](https://aws.amazon.com/lambda/): Lambda functions can be called by various events, including Amazon CloudWatch Events or AWS Config rules. You can write custom Lambda functions to evaluate IAM access key usage, perform additional checks, and send notifications by using services such as Amazon SNS or Amazon Q Developer in chat applications.

### Continually validate IAM policies
<a name="continually-validate-9999999999999999iam--policies.d38c4fc9-52cb-5cd9-b71b-26b4b3226da0"></a>

Use [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html#access-analyzer-policy-generation-console) to evaluate policies that are attached to roles and identify any unused services or excess actions that were granted. Implement periodic access reviews to manually verify that policies match current requirements.

Compare the existing policy with the policy generated by IAM Access Analyzer and remove any unnecessary permissions. You should also provide reports to users and automatically revoke unused permissions after a grace period. This helps ensure that minimal policies remain in effect.

Proactively and frequently revoking obsolete access minimizes the credentials that might be at risk during a breach. Automation provides sustainable, long-term credential hygiene and permissions optimization. Following this best practice limits the scope of impact by proactively enforcing least privilege across AWS identities and resources.

## Secure remote state storage
<a name="remote-state-storage"></a>

[Remote state storage](https://developer.hashicorp.com/terraform/language/state/remote) refers to storing the Terraform state file remotely instead of locally on the machine where Terraform is running. The state file is crucial because it keeps track of the resources that are provisioned by Terraform and their metadata.

Failure to secure remote state can lead to serious issues such as loss of state data, inability to manage infrastructure, inadvertent resource deletion, and exposure of sensitive information that might be present in the state file. For this reason, securing remote state storage is crucial for production-grade Terraform usage.

### Enable encryption and access controls
<a name="enable-encryption-and-access-controls.53a9ea18-d889-5dcd-8129-2c636401431b"></a>

Use Amazon Simple Storage Service (Amazon S3)[ server-side encryption (SSE)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html) to encrypt remote state at rest.

### Limit direct access to collaborative workflows
<a name="limit-direct-access-to-collaborative-workflows.d98bf1d0-556d-5eb2-a170-c3a39981bb9a"></a>
+ Structure collaboration workflows in HCP Terraform or in a CI/CD pipeline within your Git repository to limit direct state access.
+ Rely on pull requests, run approvals, policy checks, and notifications to coordinate changes.

Following these guidelines helps secure sensitive resource attributes and avoids conflicts with team members' changes. Encryption and strict access protections help reduce the attack surface, and collaboration workflows enable productivity.

## Use AWS Secrets Manager
<a name="secrets"></a>

There are many resources and data sources in Terraform that store secret values in plaintext in the state file. Avoid storing secrets in state―use [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) instead.

Instead of attempting to [manually encrypt sensitive values](https://developer.hashicorp.com/terraform/plugin/best-practices/sensitive-state), rely on Terraform's built-in support for sensitive state management. When exporting sensitive values to output, make sure that the values are marked as [sensitive](https://www.terraform.io/docs/configuration/outputs.html#sensitive-suppressing-values-in-cli-output).

## Continuously scan infrastructure and source code
<a name="iac-code"></a>

Proactively scan both infrastructure and source code continuously for risks such as exposed credentials or misconfigurations to harden your security posture. Address findings promptly by reconfiguring or patching resources.

### Use AWS services for dynamic scanning
<a name="use-9999999999999999aws--services-for-dynamic-scanning.3faf69bc-9e54-50f7-abeb-7eacc9d1fa63"></a>

Use AWS native tools such as [Amazon Inspector](https://aws.amazon.com/inspector/), [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/), [Amazon Detective](https://aws.amazon.com/detective/), and [Amazon GuardDuty](https://aws.amazon.com/guardduty/) to monitor provisioned infrastructure across accounts and Regions. Schedule recurring scans in Security Hub CSPM to track deployment and configuration drift. Scan EC2 instances, Lambda functions, containers, S3 buckets, and other resources.

### Perform static analysis
<a name="perform-static-analysis.2b1940e5-69e1-5370-91df-943b77423e83"></a>

Embed static analyzers such as [Checkov](https://www.checkov.io/) directly into CI/CD pipelines to scan Terraform configuration code (HCL) and identify risks preemptively before deployment. This moves security checks to an earlier point in the development process (referred to as *shifting left*) and prevents misconfigured infrastructure.

### Ensure prompt remediation
<a name="ensure-prompt-remediation.81fa9255-e495-5bea-922f-af2f977c5955"></a>

For all scan findings, ensure prompt remediation by either updating Terraform configuration, applying patches, or reconfiguring resources manually as appropriate. Lower risk levels by addressing the root causes.

Using both infrastructure scanning and code scanning provides layered insight across Terraform configurations, the provisioned resources, and application code. This maximizes the coverage of risk and compliance through preventative, detective, and reactive controls while embedding security earlier into the software development lifecycle (SDLC).

## Enforce policy checks
<a name="policy-checks"></a>

Use code frameworks such as [HashiCorp Sentinel policies](https://developer.hashicorp.com/terraform/tutorials/policy) to provide governance guardrails and standardized templates for infrastructure provisioning with Terraform.

Sentinel policies can define requirements or restrictions on Terraform configuration to align with organizational standards and best practices. For example, you can use Sentinel policies to:
+ Require tags on all resources.
+ Restrict instance types to an approved list.
+ Enforce mandatory variables.
+ Prevent the destruction of production resources.

Embedding policy checks into Terraform configuration lifecycles enables proactive enforcement of standards and architecture guidelines. Sentinel provides shared policy logic that helps accelerate development while preventing unapproved practices.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
