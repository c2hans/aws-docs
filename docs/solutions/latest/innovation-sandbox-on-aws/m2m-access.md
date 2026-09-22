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
|  `MaxSessionDuration`  | The maximum duration, in seconds, of credentials issued for the client role. The default is 3,600 seconds (one hour); the supported range is 3,600–43,200 seconds. |
|  `RestApiIdSsmParam`  | The name of the Compute stack’s SSM parameter that stores the current API Gateway REST API ID. Use the `RestApiIdSsmParamName` Compute stack output, or `InnovationSandbox_<Namespace>_Compute_RestApiId`. |

Deploy the stack from the solution’s published CloudFormation template using the AWS CloudFormation console or the AWS CLI. The template is available at:

```
https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-M2mClient.template
```

After deployment, record these stack outputs for role assumption and API requests:

| Output key | Description |
| --- | --- |
|  `M2MRoleArn`  | The ARN of the IAM role the client assumes. |
|  `M2MExternalId`  | A per-stack ExternalId that must be passed on the `sts:AssumeRole` call. |
|  `ApiGatewayArn`  | The API Gateway ARN to which the client role is permitted to send requests. |
|  `ApiGatewayUrl`  | The base URL for API requests. |

## Construct a SigV4 client
<a name="construct-sigv4-client"></a>

From the trusted principal, use the stack outputs to obtain temporary credentials and sign requests:

1. Call `sts:AssumeRole` with `M2MRoleArn` and `M2MExternalId`. The calling principal’s own credentials must have `sts:AssumeRole` permission on the client role. The call returns a temporary access key, secret key, and session token.

1. Sign each API request with SigV4 using those temporary credentials. Target the `execute-api` service in the solution’s home Region. Any AWS SDK, `curl --aws-sigv4`, or the AWS CLI can produce the signature. Include the temporary session token in each request.

Temporary credentials expire after one hour by default. Long-running automation must re-assume the role before expiration.

**Note**
The assumed role is scoped to `execute-api:Invoke` only. Record the `ApiGatewayUrl` client stack output before assuming the role, or resolve it using credentials that can describe the stack. The M2M role cannot describe CloudFormation stacks.

The [`scripts/m2m` tooling](https://github.com/aws-solutions/innovation-sandbox-on-aws/tree/main/scripts/m2m) in the GitHub repository provides scripts for deploying clients, assuming roles, sending requests, testing access, listing clients, and revoking access. You can use these scripts directly or adapt them for your own automation.

## Use the `aws isb` CLI
<a name="aws-isb-cli"></a>

The solution source distribution includes a generated AWS CLI model and installer. The `aws isb` CLI does not introduce a separate API or authentication mechanism. It maps each modeled command to the corresponding HTTP route, signs the request with SigV4 using the AWS credentials selected for the command, and sends it to the API endpoint configured by the installer. You can perform the same steps manually or with the `scripts/m2m` tooling described previously. The modeled CLI provides familiar AWS CLI command syntax, generated `help` for operations and parameters, automatic pagination for paginated operations, client-side `--query` filtering, selectable output formats, and output that you can pipe to other tools.

After installation, you can call modeled solution operations with commands such as:

```
aws isb list-lease-templates --profile isb-m2m-deploy-pipeline
```

The installer requires Python 3 and AWS CLI version 2.13.0 or later. From the repository root:

```
./scripts/m2m/assume-m2m-role.sh \
  --client-stack InnovationSandbox-M2mClient-Admin-deploy-pipeline \
  --output profile

./scripts/m2m/aws-cli/install-aws-isb-cli.py \
  --profile isb-m2m-deploy-pipeline \
  --client-stack InnovationSandbox-M2mClient-Admin-deploy-pipeline \
  --region us-east-1

aws isb list-lease-templates --profile isb-m2m-deploy-pipeline
```

The installer uses the current ambient credentials to resolve the client stack and API endpoint. The optional `--profile` argument selects the profile that receives the endpoint configuration and is later used to call the API. If the ambient credentials cannot read the client stack, pass its `ApiGatewayUrl` output with `--api-url` instead. For all options, refer to the [`aws isb` installer documentation](https://github.com/aws-solutions/innovation-sandbox-on-aws/tree/main/scripts/m2m/aws-cli).

## Remove an M2M client
<a name="remove-m2m-client"></a>

To permanently remove a client’s access, delete its CloudFormation stack using the AWS CloudFormation console or `aws cloudformation delete-stack`. This also deletes the IAM role. To immediately block access while leaving the stack intact — for example, in response to a suspected credential leak — use the `revoke-m2m-role.sh` script in the `scripts/m2m` tooling. This script denies or restores a client’s access and invalidates in-flight sessions without destroying the stack. For uninstall instructions, see [Delete machine-to-machine client stacks](delete-m2m-clients.md).
