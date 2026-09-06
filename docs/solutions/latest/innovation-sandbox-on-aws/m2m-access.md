---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/m2m-access.html
---

# Programmatic access (machine-to-machine)
<a name="m2m-access"></a>

In addition to the web UI, you can call the solution API programmatically — for example, from a CI/CD pipeline or a scheduled job. Each programmatic caller authenticates as a **machine-to-machine (M2M) client**. The client is a dedicated IAM role deployed as its own AWS CloudFormation stack. Assume the role to obtain temporary credentials for signing API requests with AWS Signature Version 4 (SigV4). Each client role is isolated, can be revoked independently, and appears as a distinct principal in AWS CloudTrail.

**Note**
If your automation host makes programmatic calls, keep its clock synchronized (for example, using Network Time Protocol (NTP)). SigV4 rejects requests whose timestamp is more than five minutes out of sync with AWS.

## Deploy an M2M client stack
<a name="deploy-m2m-client"></a>

Deploy one AWS CloudFormation stack for each client into the **Hub account** (the account where the Compute and Data stacks are deployed). Name the stack `<stackPrefix>-M2mClient-<Role>-<clientName>` and provide the following parameters:

| Parameter | Description |
| --- | --- |
|  `Namespace`  | The solution namespace of your deployment (for example, `myisb`). |
|  `ClientName`  | A short identifier for the automation (for example, `deploy-pipeline`). |
|  `Role`  | The role tier the client acts as: `Admin`, `Manager`, or `User`. |
|  `TrustedPrincipal`  | The principal allowed to assume the client role — either a full IAM ARN (pins to one principal) or a 12-digit account ID (trusts any principal in that account that has `sts:AssumeRole` permission). |
|  `RestApiId`  | The solution API Gateway REST API ID. Read it from the SSM parameter `InnovationSandbox_<Namespace>_Compute_RestApiId` in the Hub account. |

Deploy the stack from the solution’s published CloudFormation template using the AWS CloudFormation console or the AWS CLI. The template is available at:

```
https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-M2mClient.template
```

After deployment, record these stack outputs; you need them to obtain credentials:

| Output key | Description |
| --- | --- |
|  `M2MRoleArn`  | The ARN of the IAM role the client assumes. |
|  `M2MExternalId`  | A per-stack ExternalId that must be passed on the `sts:AssumeRole` call. |

## Construct a SigV4 client
<a name="construct-sigv4-client"></a>

From the trusted principal, use the stack outputs to obtain temporary credentials and sign requests:

1. Call `sts:AssumeRole` with `M2MRoleArn` and `M2MExternalId`. The calling principal’s own credentials must have `sts:AssumeRole` permission on the client role. The call returns a temporary access key, secret key, and session token.

1. Sign each API request with SigV4 using those temporary credentials. Target the `execute-api` service in the solution’s home Region. Any AWS SDK, `curl --aws-sigv4`, or the AWS CLI can produce the signature. Include the temporary session token in each request.

Temporary credentials expire after one hour by default. Long-running automation must re-assume the role before expiration.

**Note**
The assumed role is scoped to `execute-api:Invoke` only. Resolve the API Gateway invoke URL from the Compute stack outputs using your own credentials — the M2M role cannot describe stacks.

The [`scripts/m2m` tooling](https://github.com/aws-solutions/innovation-sandbox-on-aws/tree/main/scripts/m2m) in the GitHub repository provides two reference scripts — `assume-m2m-role.sh` (assumes the role and exports credentials) and `call-api.sh` (signs and sends a request) — that you can use directly or adapt for your own automation.

## Remove an M2M client
<a name="remove-m2m-client"></a>

To permanently remove a client’s access, delete its CloudFormation stack using the AWS CloudFormation console or `aws cloudformation delete-stack`. This also deletes the IAM role. To immediately block access while leaving the stack intact — for example, in response to a suspected credential leak — use the `revoke-m2m-role.sh` script in the `scripts/m2m` tooling. This script denies or restores a client’s access and invalidates in-flight sessions without destroying the stack. For uninstall instructions, see [Delete machine-to-machine client stacks](delete-m2m-clients.md).
