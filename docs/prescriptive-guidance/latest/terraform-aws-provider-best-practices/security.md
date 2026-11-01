---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/security.html
---

# Security best practices
<a name="security"></a>

Properly managing authentication, access controls, and security is critical for secure use of the Terraform AWS Provider. This section outlines best practices around:
+ IAM roles and permissions for least-privilege access
+ Temporary credentials for people and pipelines, to help prevent unauthorized access to AWS accounts and resources
+ Encryption and access controls for remote state
+ Keeping secrets out of the Terraform state file
+ Infrastructure and source code scanning to identify misconfigurations and drift
+ Policy as code to enforce governance guardrails

Following these best practices helps strengthen your security posture when you use Terraform to manage AWS infrastructure.

## Follow the principle of least privilege
<a name="least-privilege"></a>

[Least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) is a fundamental security principle that refers to granting only the minimum permissions required for a user, process, or system to perform its intended functions. It's a core concept in access control and a preventative measure against unauthorized access and potential data breaches.

The principle of least privilege is central to how Terraform authenticates and performs actions against AWS.

When you use Terraform to provision and manage AWS resources, it acts on behalf of an entity (user or role) that requires only the minimum permissions necessary to make API calls. Not following least privilege introduces the following security risks:
+ If Terraform has excessive permissions beyond what's needed, an unintended misconfiguration could make undesired changes or deletions.
+ Overly permissive access grants increase the scope of impact if Terraform state files or credentials are compromised.
+ Failing to follow least privilege violates security best practices and regulatory compliance requirements for granting minimal required access.

## Use IAM roles
<a name="iam-roles"></a>

Use IAM roles instead of IAM users wherever possible to enhance security with the Terraform AWS Provider. IAM roles provide temporary security credentials that expire automatically, which eliminates the need to manage long-term access keys. Roles also offer precise access controls through IAM policies.

### Grant least privilege access by using IAM policies
<a name="grant-least-privilege-access-by-using-9999999999999999iam--policies.17ff0272-2206-52df-8bc3-10283c2d34c5"></a>

Carefully construct IAM policies to ensure that roles and users have only the minimum set of permissions that are required for their workload. Start with an empty policy and iteratively add allowed services and actions. To accomplish this:
+ Use [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) to create a policy from the actions that a role called, as recorded in AWS CloudTrail.
+ Manually review policies to remove any capabilities that aren't essential for the role's intended responsibility.
+ Use [IAM policy variables and tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html) to simplify permission management.

Well-constructed policies grant just enough access to accomplish the workload's responsibilities and nothing more. Define actions at the operation level, and allow calls only to required APIs on specific resources.

Following this best practice reduces the scope of impact and follows the fundamental security principles of separation of duties and least privilege access. Start strict and open access gradually as needed, instead of starting open and trying to restrict access later.

### Use temporary credentials for local runs
<a name="use-temporary-credentials-for-local-runs.da15ab11-b534-53f4-a2b7-ab0c4ae32322"></a>

When you run Terraform from a workstation, don't configure long-term access keys. Sign in with a named AWS Command Line Interface (AWS CLI) profile that supplies temporary credentials, and let the AWS Provider assume the role that Terraform runs as.
+ If your organization uses AWS IAM Identity Center, create a profile with [aws configure sso](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html), and sign in with `aws sso login --profile <profile-name>`.
+ If you sign in to the AWS Management Console as an IAM user, or through federation directly with IAM, sign in with [aws login](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html) (AWS CLI version 2.32.0 or later). The identity needs the permissions in the `SignInLocalDevelopmentAccess` AWS managed policy. Terraform 1.15 and later (for the S3 backend) and AWS Provider 6.23.0 and later accept `aws login` credentials, and the CLI refreshes them for up to 12 hours.

Next, create an IAM role for Terraform that has the minimum permissions, and a trust policy that allows only the identities that run Terraform. Don't make the role its own principal. For IAM Identity Center users, set the principal to the account and add an `ArnLike` condition on `aws:PrincipalArn` that matches `arn:aws:iam::<account-id>:role/aws-reserved/sso.amazonaws.com/*AWSReservedSSO_<permission-set-name>_*`. IAM Identity Center adds a random suffix to the role names that it creates, and puts the roles under a path that can include a Region, so the condition needs both wildcards.

Then add an [assume\_role](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#assuming-an-iam-role) block with the role's ARN and a `session_name` to the provider configuration. AWS CloudTrail records the session name, so you can tell which runs came from which people or pipelines.

Choose between the two sign-in methods based on how your people already access AWS:
+ **IAM Identity Center** gives you one sign-in for every account and central permission sets. It requires an organization instance of IAM Identity Center, and sessions last as long as the permission set's session duration.
+ `aws login` needs no new identity infrastructure if your users already sign in to the console as IAM users or through IAM federation. Each user still needs an identity in each account that they work in, which is harder to manage at scale.

Select the profile when you run Terraform, for example `AWS_PROFILE=terraform-dev terraform plan`. Don't set `profile` in the `provider` block of shared code, because pipelines authenticate differently.

The key benefits of this best practice include temporary credentials that expire on their own, nothing to copy into scripts or files, fine-grained access controls on the role, and the ability to revoke access by changing the role or the permission set. The same configuration works for everyone on the team because no one's credentials are in it.

### Use IAM roles for Amazon EC2 authentication
<a name="use-9999999999999999iam--roles-for-9999999999999999ec2--authentication.3387e50a-c603-55d1-9221-9cf1c1a1a297"></a>

When you run Terraform from Amazon Elastic Compute Cloud (Amazon EC2) instances, avoid storing long-term credentials locally. Instead, use IAM roles and [instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) to grant least-privilege permissions automatically.

First, create an IAM role with the minimum permissions and assign the role to the instance profile. The instance profile allows Amazon EC2 instances to inherit the permissions defined in the role. Then, launch instances by specifying that instance profile. The instance authenticates through the attached role.

Before you run any Terraform operations, run `aws sts get-caller-identity` on the instance. The output should show the ARN of the instance role's session (`arn:aws:sts::<account-id>:assumed-role/<role-name>/<instance-id>`), which confirms that the instance profile supplies the credentials.

This approach avoids hardcoding permanent AWS keys into scripts or Terraform configuration within the instance. The instance role and profile supply temporary credentials to Terraform transparently.

The key benefits of this best practice include improved security over long-term credentials, reduced credential management overhead, and consistency between development, test, and production environments. IAM role authentication simplifies Terraform runs from Amazon EC2 instances while enforcing least-privilege access.

### Use dynamic credentials for HCP Terraform workspaces
<a name="use-dynamic-credentials-for-hcp-terraform-workspaces.893b70d4-2dd6-545f-bf72-283f1a344c70"></a>

HCP Terraform is a managed service provided by HashiCorp that helps teams use Terraform to provision and manage infrastructure across multiple projects and environments. When you run Terraform in HCP Terraform, use [dynamic provider credentials](https://developer.hashicorp.com/terraform/cloud-docs/dynamic-provider-credentials/aws-configuration) instead of stored access keys. For each run, HCP Terraform issues a workload identity token, which is an OpenID Connect (OIDC) token. The AWS Provider exchanges this token for temporary credentials by calling `AssumeRoleWithWebIdentity` on an IAM role that trusts HCP Terraform.

To set this up, add an IAM OIDC identity provider for `app.terraform.io` to your account, and create a role whose trust policy checks the token's `aud` and `sub` claims. The `sub` claim names the organization, project, workspace, and run phase. You can therefore give plan runs a read-only role and apply runs a role that can make changes, by setting the `TFC_AWS_PLAN_ROLE_ARN` and `TFC_AWS_APPLY_ROLE_ARN` workspace variables. In the apply role's trust policy, require `app.terraform.io:aud` to equal `aws.workload.identity`, and require `app.terraform.io:sub` to equal the exact workspace and phase, for example `organization:example-org:project:networking:workspace:network-prod:run_phase:apply`.

Benefits include no long-term keys to store or rotate, credentials that last only for the run, and separate permissions for each workspace and run phase.

### Use IAM roles in AWS CodeBuild
<a name="use-9999999999999999iam--roles-in-9999999999999999acblong-.8dd8125e-1b22-56df-b363-2d23da5d65ac"></a>

In AWS CodeBuild, run your builds by using an [IAM role that's assigned to the CodeBuild project](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html). This allows each build to automatically inherit temporary credentials from the role instead of using long-term keys.

### Run GitHub Actions remotely on HCP Terraform
<a name="run-github-actions-remotely-on-hcp-terraform.e8e3e806-aaaa-5d6d-87ee-d61ff809bc03"></a>

Configure GitHub Actions workflows to run Terraform remotely on HCP Terraform workspaces. Rely on dynamic credentials and remote state locking instead of GitHub secrets management.

### Use GitHub Actions with OIDC and configure the AWS Credentials action
<a name="use-github-actions-with-oidc-and-configure-the-9999999999999999aws--credentials-action.7d36660e-255d-5c6d-87d6-5dc7230a8cd1"></a>

Use the [OpenID Connect (OIDC) standard to federate GitHub Actions identity through IAM](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws). Use the [Configure AWS Credentials action](https://github.com/aws-actions/configure-aws-credentials) to exchange the GitHub token for temporary AWS credentials without needing long-term access keys.

In the role's trust policy, check the token's `sub` claim so that only the intended repository, branch, or environment can assume the role. IAM rejects a GitHub OIDC trust policy that doesn't restrict `token.actions.githubusercontent.com:sub` (or `job_workflow_ref`). When `sub` names a GitHub environment, also restrict the branch with the `ref` claim, as IAM Access Analyzer recommends. The following condition block lets only jobs in the `production` environment of one repository, on the `main` branch, assume the role:

```
"Condition": {
  "StringEquals": {
    "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
    "token.actions.githubusercontent.com:sub": "repo:example-org/infrastructure:environment:production",
    "token.actions.githubusercontent.com:ref": "refs/heads/main"
  }
}
```

The role's principal is the account's GitHub OIDC identity provider, `arn:aws:iam::<account-id>:oidc-provider/token.actions.githubusercontent.com`, and the action is `sts:AssumeRoleWithWebIdentity`.

Choose HCP Terraform dynamic credentials when HCP Terraform runs your plans and applies, and GitHub or GitLab OIDC when the CI runner runs Terraform. With HCP Terraform, the run phase in the token separates plan and apply permissions for you, but you depend on HashiCorp's service for every run. With CI runner OIDC, you keep the runs in your own pipeline, and you separate plan and apply permissions yourself, for example with a GitHub environment that requires approval before the apply job runs.

### Use GitLab with OIDC and the AWS CLI
<a name="use-gitlab-with-oidc-and-the-9999999999999999cli-.ad0e2296-df42-5592-9472-d40d7da73771"></a>

Use the [OIDC standard to federate GitLab identities through IAM](https://docs.gitlab.com/ci/cloud_services/aws/) for temporary access. By relying on OIDC, you avoid managing long-term AWS access keys in GitLab. Credentials are issued just in time, which improves security. Restrict the role's trust policy on the `sub` claim, which names the project and branch (for example, `project_path:example-group/infrastructure:ref_type:branch:ref:main`), so that only that pipeline can assume the role with the permissions you grant it.

## Use unique IAM users with legacy automation tools
<a name="legacy-automation-tools"></a>

If you have automation tools and scripts that lack native support for using IAM roles, you can create individual IAM users to grant programmatic access. The principle of least privilege still applies. Minimize policy permissions and rely on separate roles for each pipeline or script. If the workload runs outside AWS and can hold an X.509 certificate, use [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) to obtain temporary credentials instead of access keys. As you migrate to more modern tools or scripts, begin supporting roles natively and gradually transition to them.

**Warning**
IAM users have long-term credentials, which present a security risk. To help mitigate this risk, provide these users with only the permissions they require to perform the task, and remove these users when they are no longer needed.

### Use the Jenkins AWS Credentials plugin
<a name="use-the-jenkins-9999999999999999aws--credentials-plugin.6d944e4f-b57c-5f0e-a6e6-07ddb036a0d8"></a>

Use the [AWS Credentials plugin](https://plugins.jenkins.io/aws-credentials/) in Jenkins to centrally configure and inject AWS credentials into builds dynamically. This avoids checking secrets into source control.

## Continuously monitor, validate, and optimize least privilege
<a name="continuous-monitoring"></a>

Over time, you might grant additional permissions that exceed the minimum required policies. Continuously analyze access to identify and remove any unnecessary entitlements.

### Continuously monitor access key usage
<a name="continuously-monitor-access-key-usage.408eb3d6-af4c-563d-9daf-a3ae62581ffc"></a>

If you cannot avoid using access keys, use [IAM credential reports](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html) to find access keys that are older than 90 days, and revoke inactive keys across both user accounts and machine roles. Alert administrators to manually confirm the removal of keys for active employees and systems.

Monitoring key usage helps you optimize permissions because you can identify and remove unused entitlements. When you follow this best practice with [access key rotation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey), it limits credential lifespan and enforces least privilege access.

AWS provides several services and features that you can use to find unused credentials and notify administrators:
+ **IAM Access Analyzer:** [Unused access findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-concepts.html) report roles, access keys, passwords, and permissions that haven't been used for the number of days you choose, across an account or an organization.
+ **AWS Security Hub CSPM:** [IAM controls](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html) such as IAM.3 (access keys rotated every 90 days or less) and IAM.22 (credentials unused for 45 days removed) check every account and send findings that you can route to administrators through Amazon EventBridge and Amazon Simple Notification Service (Amazon SNS).
+ **AWS Config:** Managed rules such as `access-keys-rotated` and `iam-user-unused-credentials-check` evaluate IAM users continuously, and can start remediation or send notifications to an Amazon SNS topic.

### Continually validate IAM policies
<a name="continually-validate-9999999999999999iam--policies.c73f5d3f-008e-531d-9f96-d8cd8cb919c6"></a>

Use IAM Access Analyzer to keep policies close to what each role needs:
+ [Validate policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) before deployment. In your pipeline, run `aws accessanalyzer validate-policy` on each policy document that Terraform manages, and fail the build on security warnings and errors. Validation flags issues such as overly broad wildcards and GitHub OIDC trust policies without a repository condition.
+ Run [custom policy checks](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-custom-policy-checks.html) such as `check-no-new-access`, which fails when a changed policy grants more access than the deployed version, and `check-access-not-granted` for actions that must never be allowed.
+ Review unused access findings, compare existing policies with policies generated from CloudTrail activity, and remove permissions that aren't used. Provide reports to role owners, and revoke unused permissions after a grace period.

Proactively and frequently revoking obsolete access minimizes the credentials that might be at risk during a security event. Automation provides sustainable, long-term credential hygiene and permissions optimization. Following this best practice limits the scope of impact by proactively enforcing least privilege across AWS identities and resources.

## Secure remote state storage
<a name="remote-state-storage"></a>

[Remote state storage](https://developer.hashicorp.com/terraform/language/state/remote) refers to storing the Terraform state file remotely instead of locally on the machine where Terraform is running. The state file is crucial because it keeps track of the resources that are provisioned by Terraform and their metadata.

Unsecured remote state can result in loss of state data, inability to manage infrastructure, inadvertent resource deletion, and exposure of sensitive information stored in the state file. Securing remote state storage is therefore essential for production-grade Terraform usage.

### Enable encryption and access controls
<a name="enable-encryption-and-access-controls.5f7fa692-7bfc-5a1e-8618-c67c0ae9685c"></a>

Amazon Simple Storage Service (Amazon S3) encrypts every new object with server-side encryption with Amazon S3 managed keys (SSE-S3) by default. For a state bucket, add the following controls:
+ Encrypt state with an AWS Key Management Service (AWS KMS) customer managed key (SSE-KMS), so that reading state also requires permission to use the key. Set `kms_key_id` in the backend configuration, and enable an S3 Bucket Key to reduce AWS KMS requests.
+ Add a bucket policy that denies requests that don't use TLS (`aws:SecureTransport` is `false`).
+ Turn on S3 Block Public Access, and set S3 Object Ownership to **Bucket owner enforced** so that access control lists (ACLs) are disabled.
+ Give the role that Terraform runs as access only to its own state object, its `.tflock` lock object, and the AWS KMS key.

For one state file with S3 native locking, the role needs these permissions and no others on the state bucket and key:
+ `s3:ListBucket` on the bucket, limited with an `s3:prefix` condition to the state key and its lock file
+ `s3:GetObject` and `s3:PutObject` on the state key
+ `s3:GetObject`, `s3:PutObject`, and `s3:DeleteObject` on the lock file (`<key>.tflock`)
+ `kms:Decrypt`, `kms:Encrypt`, and `kms:GenerateDataKey` on the AWS KMS key

A role that only plans needs the same lock file permissions, because `terraform plan` takes the state lock. It doesn't need `s3:PutObject` on the state key. For details, see the [S3 backend permissions](https://developer.hashicorp.com/terraform/language/backend/s3#permissions-required) in the Terraform documentation.

For the backend configuration and the bucket policy, see [Backend best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/backend.html).

### Limit direct access to collaborative workflows
<a name="limit-direct-access-to-collaborative-workflows.5539db89-e3fd-577d-a6b7-0042dab48e7b"></a>
+ Structure collaboration workflows in HCP Terraform or in a CI/CD pipeline within your Git repository to limit direct state access.
+ Rely on pull requests, run approvals, policy checks, and notifications to coordinate changes.

Following these guidelines helps secure sensitive resource attributes and avoids conflicts with team members' changes. Encryption and strict access controls help reduce the scope of exposure, and collaboration workflows support consistent, coordinated change management.

## Keep secrets out of state
<a name="keep-secrets-out-of-state"></a>

Terraform stores resource attributes and data source results in state. A secret that a data source reads, or that you pass to a regular argument, is written to the state file in plain text. Marking a value as `sensitive` hides it from CLI output, but it's still stored in state. Keep secrets in AWS Secrets Manager, and use the following features so that secret values never reach the plan or state:
+ **Ephemeral resources** (Terraform 1.10 and later) read a value during a run and never store it. For example, the ephemeral `aws_secretsmanager_secret_version` resource reads a secret. The `aws_secretsmanager_secret_version` data source reads the same secret but stores its value in state.
+ **Write-only arguments** (Terraform 1.11 and later) accept ephemeral values and never store them, for example `password_wo` on `aws_db_instance`, `secret_string_wo` on `aws_secretsmanager_secret_version`, and `value_wo` on `aws_ssm_parameter`. Terraform sends a write-only value only when the matching version argument, such as `password_wo_version`, changes. Increment the version to rotate the value.
+ **Ephemeral variables and outputs** (Terraform 1.10 and later) pass secrets between modules without storing them.
+ **Service-managed passwords:** For Amazon RDS, `manage_master_user_password = true` makes Amazon RDS generate the master user password and store it in Secrets Manager, so Terraform never handles it. Amazon RDS doesn't support this for a DB instance that is the source of a read replica (except for RDS for SQL Server and RDS for Db2). For those, use a write-only password, as in the following example.

The following example reads a database password from Secrets Manager and passes it to Amazon RDS. The password doesn't appear in the plan, the state, or the logs. The other `aws_db_instance` arguments are omitted:

```
ephemeral "aws_secretsmanager_secret_version" "db" {
  secret_id = "orders/db-master"
}

resource "aws_db_instance" "primary" {
  password_wo         = ephemeral.aws_secretsmanager_secret_version.db.secret_string
  password_wo_version = 1
}
```

To create the secret from Terraform as well, generate the value with the ephemeral `random_password` resource and store it with `secret_string_wo` on `aws_secretsmanager_secret_version`. Then read it back with the ephemeral resource, so that the database and the secret remain in sync.

Choose service-managed passwords where the service supports them, because Terraform never handles the secret and the service rotates it. Choose write-only arguments when the service can't manage the secret, or when other systems need the same value. In that case, you are responsible for rotation: increment the version argument, and account for the brief window when the new value is in AWS Secrets Manager but not yet in the database.

For more information, see [Securing sensitive data by using AWS Secrets Manager and HashiCorp Terraform](https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/introduction.html) and HashiCorp's documentation on [ephemeral resources](https://developer.hashicorp.com/terraform/language/manage-sensitive-data/ephemeral) and [write-only arguments](https://developer.hashicorp.com/terraform/language/manage-sensitive-data/write-only).

## Continuously scan infrastructure and source code
<a name="iac-code"></a>

Proactively scan both infrastructure and source code continuously for risks such as exposed credentials or misconfigurations to harden your security posture. Address findings promptly by reconfiguring or patching resources.

### Use AWS services for dynamic scanning
<a name="use-9999999999999999aws-services--for-dynamic-scanning.8fea5d0e-a51e-54f7-adea-183b225ac217"></a>

Use AWS native tools to monitor provisioned infrastructure across accounts and Regions. AWS Config records configuration changes and evaluates them against rules. [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/) runs security controls and aggregates findings. [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/) continuously scans Amazon Elastic Compute Cloud (Amazon EC2) instances, AWS Lambda functions, and container images for software vulnerabilities. [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) detects threats in your accounts, workloads, and Amazon S3 buckets.

### Detect drift
<a name="detect-drift.d73135db-0b32-5a16-aaa6-6bffd179252d"></a>

AWS Config shows changes to resources, but not whether they still match your Terraform configuration. To detect Terraform drift, run `terraform plan -detailed-exitcode` on a schedule in your pipeline. Exit code 0 means that the infrastructure matches the configuration, 1 means that the plan failed, and 2 means that there's drift or pending changes. Save the plan with `-out`, and on exit code 2, publish `terraform show` output for the saved plan so that someone can review the drift before deciding whether to apply or update the configuration.

Keep these points in mind:
+ Don't use the exit code of `terraform plan -refresh-only -detailed-exitcode` as the drift signal. With Terraform 1.17.0 and AWS Provider 6.70.0, it returns 2 even when nothing has drifted. If you want a refresh-only check, count the `resource_drift` entries in the saved plan instead: `terraform show -json refresh.tfplan | jq '.resource_drift // [] | length'`.
+ Don't add `-minimal-refresh` to drift jobs. That option refreshes only resources that already have proposed changes, so the plan misses changes made outside Terraform.
+ In HCP Terraform, [health assessments](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/health) check workspaces for drift on a schedule.

### Perform static analysis
<a name="perform-static-analysis.03b7c670-6cd1-5b15-8eca-3a2b7f4419a9"></a>

Embed static analyzers directly into CI/CD pipelines to scan Terraform configuration code (HCL) and identify risks before deployment. This moves security checks to an earlier point in the development process (referred to as *shifting left*) and prevents misconfigured infrastructure. Options include [Checkov](https://www.checkov.io/), [Trivy](https://trivy.dev/docs/latest/scanner/misconfiguration/) (`trivy config`), and [TFLint](https://github.com/terraform-linters/tflint) with the AWS ruleset.

### Ensure prompt remediation
<a name="ensure-prompt-remediation.c3b73bc5-cd68-5a93-b5a9-c70e0e04657b"></a>

For all scan findings, ensure prompt remediation by either updating Terraform configuration, applying patches, or reconfiguring resources manually as appropriate. Lower risk levels by addressing the root causes.

Using both infrastructure scanning and code scanning provides layered insight across Terraform configurations, the provisioned resources, and application code. This maximizes the coverage of risk and compliance through preventive, detective, and reactive controls while embedding security earlier into the software development lifecycle (SDLC).

## Enforce policy as code
<a name="enforce-policy-as-code"></a>

Use policy-as-code frameworks to provide governance guardrails for infrastructure provisioning with Terraform. HCP Terraform and Terraform Enterprise evaluate policies on each run, by using one of the following frameworks:
+ [Sentinel](https://developer.hashicorp.com/sentinel), HashiCorp's policy language
+ [Open Policy Agent (OPA)](https://www.openpolicyagent.org/), with policies written in Rego
+ [Terraform policy](https://developer.hashicorp.com/terraform/policy), with policies written in HCL. The Terraform CLI can also evaluate these policies, starting with Terraform 1.17. HashiCorp labels the framework as beta in its documentation.

For example, you can use policies to:
+ Require tags on all resources.
+ Restrict instance types to an approved list.
+ Require encryption at rest, for example `storage_encrypted` on Amazon RDS instances.
+ Require `allowed_account_ids` on every AWS provider configuration.
+ Allow modules only from approved sources and versions.
+ Prevent the destruction of production resources.

A Terraform policy file contains `provider_policy`, `resource_policy`, and `module_policy` blocks. Each has an `enforce` block with a condition and an error message, like a Terraform validation rule. A `resource_policy` for `aws_db_instance` can require `storage_encrypted = true`, and a `module_policy` can require a minimum module version before Terraform downloads the module. For the syntax, see the [Terraform policy documentation](https://developer.hashicorp.com/terraform/policy).

Choose the framework based on where your runs happen and what your team already knows:
+ **Sentinel** is a well-established option in HCP Terraform and Terraform Enterprise, with policy libraries from HashiCorp. Its language is specific to HashiCorp products, and it doesn't run outside them.
+ **OPA** uses an open standard that you can also apply to Kubernetes and other tools, and open source tools can evaluate the JSON plan in any pipeline. Your team must learn Rego, and you build and maintain the policy integration in each pipeline yourself.
+ **Terraform policy** uses HCL, so Terraform authors can write policies without learning another language, and it can check module sources before download. It is the most recently introduced framework, its CLI enforcement needs an HCP Terraform organization, and HashiCorp still labels it beta.

When you adopt Terraform policy, keep the following in mind:
+ Write tests for each policy and run them with `tfpolicy test`. Authoring and testing don't need an HCP Terraform account.
+ Label registry module policies with the full address, including `registry.terraform.io`. When Terraform evaluates module policies during `init`, a module's source includes the hostname, so a policy labeled `terraform-aws-modules/lambda/aws` matches no module. Use the full address in test mocks too, or the tests pass while the policy never runs.
+ Prefer attributes that are known at plan time. A policy on a computed attribute, such as `tags_all` on a resource that has no tags, can't be evaluated until after the apply. Check `default_tags` on the provider configuration instead.
+ In HCP Terraform, Terraform policy sets come from a version control repository or are uploaded through the API, which requires the Standard or Premium edition. A Terraform policy set that has no policies fails every run that it applies to. Attach a new policy set to a test workspace until its first version has uploaded, before you apply it to projects or the whole organization.
+ To evaluate policies from the CLI, run `terraform init`, `plan`, or `apply` with `-policies=<directory>`. The CLI needs the separate `tfpolicy-plugin` binary, and a `cloud` block that selects a workspace in an HCP Terraform organization, which supplies the policy entitlement. With Terraform 1.17.0, `init -policies` stops when a module policy fails, but `plan -policies` and `apply -policies` report failed policies and still exit 0, and `apply` still makes the changes. In a pipeline, fail the job based on the policy results in the JSON output instead of the exit code. Run `terraform plan -json -policies=<directory>`, and fail when any `policy_result` message has the result `DenyResult` and an enforcement level other than `advisory`.

Policy checks complement IAM permissions. IAM limits what Terraform can do, and policies limit what your configuration is allowed to ask for.

## Guard against applying to the wrong account
<a name="guard-against-applying-to-the-wrong-account"></a>

Set `allowed_account_ids` in every `provider "aws"` block. If the credentials in use belong to any other account, the provider stops the run with an error before it changes anything. This protects against a stale `AWS_PROFILE` or a pipeline that picks up the wrong role. The provider example in **Configure providers for Regions and accounts**, under [Structure for modularity](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/structure.html#modularity), shows the setting. If one configuration must work in several accounts, use `forbidden_account_ids` to exclude production accounts instead.
