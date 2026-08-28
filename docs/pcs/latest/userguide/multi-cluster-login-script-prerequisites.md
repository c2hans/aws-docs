---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/multi-cluster-login-script-prerequisites.html
---

# Prerequisites for the AWS PCS multi-cluster login node configuration script
<a name="multi-cluster-login-script-prerequisites"></a>

## System requirements
<a name="system-requirements"></a>
+ Linux OS with `systemd` support
+ Root privileges for system configuration

## Required commands and packages
<a name="required-commands"></a>
+ `bash` – Shell interpreter (version 4.0\+)
+ `curl` – For AWS IMDS v2 metadata retrieval
+ `jq` – JSON processor for parsing AWS API responses
+ `aws` – AWS CLI v2 to run AWS PCS API actions and for Secrets Manager access
+ `systemctl` – `systemd` service management
+ `find` – File system search utility
+ `grep` – Text pattern matching
+ `sed` – Stream editor for text manipulation
+ `sort` – Text sorting utility
+ `tail` – Displays the last lines of a file
+ `mkdir` – Directory creation
+ `chmod` – Changes file permissions
+ `chown` – Changes file ownership
+ `ldconfig` – Dynamic linker configuration

## AWS requirements
<a name="aws-requirements"></a>
+ An AWS PCS cluster that runs Slurm version 25.05 or later
+ AWS credentials configured (through an IAM role, credentials file, or environment variables)
+ Permissions for:
  + `pcs:GetCluster`
  + `secretsmanager:GetSecretValue` (if you use an alternate secret)

## System users and groups
<a name="system-users-groups"></a>
+ The `slurm` user and group must exist on the system

## Slurm installation
<a name="slurm-installation"></a>
+ Slurm must be installed in the same location as AWS PCS Slurm installer packages:

  ```
  /opt/aws/pcs/scheduler/slurm-{{version}}
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
