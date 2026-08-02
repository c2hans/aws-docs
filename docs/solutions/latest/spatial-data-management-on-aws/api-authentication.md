---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/api-authentication.html
---

# API Authentication
<a name="api-authentication"></a>

You can authenticate with the Spatial Data Management on AWS representational state transfer (REST) API using AWS IAM credentials and Signature Version 4 (SigV4) signing.

**Note**
If you are a user logged in through the Spatial Data Management portal using Amazon Cognito credentials, you can view the interactive API documentation at `<SDMA-PORTAL-FQDN>/api-docs`. You can find the portal fully qualified domain name (FQDN) in the AWS CloudFormation stack outputs after deployment. For more information, see [Deploy the solution](deploy-the-solution.md). The instructions below are for programmatic access using IAM SigV4 authentication.

## Placeholders used in this guide
<a name="placeholders"></a>

The examples in this guide use the following placeholders. You can find these values in the AWS CloudFormation stack outputs after deployment.

| Placeholder | Description |
| --- | --- |
|  `<REGION>`  | The AWS Region where the solution is deployed (for example, `us-east-1`). |
|  `<ACCOUNT_ID>`  | The AWS account ID where the solution is deployed. |
|  `<API_ID>`  | The Amazon API Gateway REST API identifier. Available from the `ApiId` CloudFormation output. |
|  `<API_ENDPOINT>`  | The full API base URL. Available from the `SpatialDataManagementApiEndpoint` parameter in AWS Systems Manager Parameter Store. |
|  `<SDMA-PORTAL-FQDN>`  | The Spatial Data Management on AWS (SDMA) portal fully qualified domain name. Available from the AWS CloudFormation stack outputs. |
|  `<API_HOST>`  | The hostname portion of the API endpoint (for example, `<API_ID>.execute-api.<REGION>.amazonaws.com`). |

## Overview
<a name="overview"></a>

All endpoints documented in the [API Reference](api-reference.md) use the `/iam/` path prefix and require [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html) authentication. Amazon API Gateway validates the SigV4 signature on every request before forwarding it to the backend.

The high-level flow is:

1. Obtain AWS credentials (access key, secret key, and optional session token) for an IAM principal that has `execute-api:Invoke` permission.

1. Sign the HTTP request using SigV4 with the service name `execute-api`.

1. Send the signed request. API Gateway validates the signature and processes the call.

## Setting up IAM access
<a name="iam-permissions"></a>

The calling IAM principal (user or role) must have the `execute-api:Invoke` permission on the API. This section walks through creating a role with the correct policy and obtaining credentials.

### Creating an IAM role for API access
<a name="_creating-an-iam-role-for-api-access"></a>

If you do not already have a role with the required permissions, create one:

1. Open the [IAM console](https://console.aws.amazon.com/iam/) and choose **Roles** > **Create role**.

1. Choose **AWS account** as the trusted entity and enter the account ID where callers reside (use the same account ID if callers are in the deployment account).

1. Choose **Next**.

1. Choose **Create policy** and enter the following JSON:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "execute-api:Invoke",
         "Resource": "arn:aws:execute-api:<REGION>:<ACCOUNT_ID>:<API_ID>/2025-04-18/*/iam/*"
       }
     ]
   }
   ```

   Replace the placeholders with your deployment values. See [Placeholders used in this guide](#placeholders) for details.

1. Name the policy (for example, `SpatialDataMgmtApiInvoke`), create it, and attach it to the role.

1. Name the role (for example, `SpatialDataMgmtApiRole`) and create it.

To restrict access to specific operations, narrow the `Resource` ARN. For example, to allow only read operations on libraries:

```
"Resource": "arn:aws:execute-api:<REGION>:<ACCOUNT_ID>:<API_ID>/2025-04-18/GET/iam/libraries*"
```

#### Example: Assets and Projects access
<a name="_example-assets-and-projects-access"></a>

The following policy grants a user full access to Assets and Projects APIs, but no access to other resources such as Libraries, Connectors, or Asset Templates:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "execute-api:Invoke",
      "Resource": [
        "arn:aws:execute-api:<REGION>:<ACCOUNT_ID>:<API_ID>/2025-04-18/*/iam/libraries/*/projects/*",
        "arn:aws:execute-api:<REGION>:<ACCOUNT_ID>:<API_ID>/2025-04-18/*/iam/libraries/*/projects/*/assets/*"
      ]
    }
  ]
}
```

The Amazon Resource Name (ARN) pattern breakdown:

| Segment | Meaning |
| --- | --- |
|  `2025-04-18`  | API stage name |
|  `*` (after stage) | Any HTTP method (GET, POST, PUT, DELETE) |
|  `/iam/libraries//projects/ `  | All project operations under any library |
|  `/iam/libraries//projects//assets/*`  | All asset operations under any project |

#### Example: Read-only access
<a name="_example-read-only-access"></a>

To grant read-only access across all resources:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "execute-api:Invoke",
      "Resource": "arn:aws:execute-api:<REGION>:<ACCOUNT_ID>:<API_ID>/2025-04-18/GET/iam/*"
    }
  ]
}
```

Alternatively, using the AWS CLI:

```
# Create the role (replace the trust policy principal as needed)
aws iam create-role \
  --role-name SpatialDataMgmtApiRole \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::<ACCOUNT_ID>:root" },
      "Action": "sts:AssumeRole"
    }]
  }'

# Attach the invoke permission
aws iam put-role-policy \
  --role-name SpatialDataMgmtApiRole \
  --policy-name SpatialDataMgmtApiInvoke \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Action": "execute-api:Invoke",
      "Resource": "arn:aws:execute-api:<REGION>:<ACCOUNT_ID>:<API_ID>/2025-04-18/*/iam/*"
    }]
  }'
```

### Obtaining credentials
<a name="obtaining-credentials"></a>

Once the role exists, obtain credentials to sign your requests.

#### Temporary credentials with `AssumeRole`
<a name="_temporary-credentials-with-assumerole"></a>

If you have an IAM role with the `execute-api:Invoke` permission, assume it to get temporary credentials:

```
aws sts assume-role \
  --role-arn arn:aws:iam::<ACCOUNT_ID>:role/<ROLE_NAME> \
  --role-session-name api-session
```

This returns `AccessKeyId`, `SecretAccessKey`, and `SessionToken`. Export them as environment variables:

```
export AWS_ACCESS_KEY_ID=<AccessKeyId>
export AWS_SECRET_ACCESS_KEY=<SecretAccessKey>
export AWS_SESSION_TOKEN=<SessionToken>
```

#### AWS IAM Identity Center
<a name="_aws-iam-identity-center"></a>

If your organization uses [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html):

```
aws sso login --profile <PROFILE_NAME>
```

Then use `--profile <PROFILE_NAME>` with the AWS CLI, or set `AWS_PROFILE=<PROFILE_NAME>` so that SDKs and tools like `awscurl` pick up the credentials automatically.

#### IAM user access keys
<a name="_iam-user-access-keys"></a>

**Important**
Long-lived access keys are less secure than temporary credentials. We recommend using IAM roles with `AssumeRole` or IAM Identity Center whenever possible.

For programmatic access with a long-lived IAM user, configure the AWS CLI:

```
aws configure
```

Provide your `Access Key ID` and `Secret Access Key` when prompted. The AWS CLI stores your credentials in `~/.aws/credentials`.

## Signing requests
<a name="signing-requests"></a>

All requests to `/iam/` endpoints must include a SigV4 signature with the service name `execute-api` and the region where the API is deployed.

### Python (botocore)
<a name="python-example"></a>

This example requires the `requests` and `botocore` Python packages.

```
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.session import Session
import requests

session = Session()
credentials = session.get_credentials().get_frozen_credentials()

api_url = "<API_ENDPOINT>/iam/libraries"

aws_request = AWSRequest(method="GET", url=api_url, headers={
    "Content-Type": "application/json"
})
SigV4Auth(credentials, "execute-api", "<REGION>").add_auth(aws_request)

response = requests.get(api_url, headers=dict(aws_request.headers))
print(response.json())
```

This uses the default credential chain (environment variables, `~/.aws/credentials`, instance profile, etc.).

### cURL (with awscurl)
<a name="curl-example"></a>

 [awscurl](https://github.com/okigan/awscurl) is a cURL wrapper that handles SigV4 signing automatically.

**Note**
 `awscurl` is a third-party tool and is not maintained by AWS.

```
awscurl --service execute-api \
  --region <REGION> \
  "<API_ENDPOINT>/iam/libraries"
```

 `awscurl` reads credentials from the standard AWS credential chain. You can also pass `--profile <name>` to use a specific AWS CLI profile.

### JavaScript (AWS SDK v3)
<a name="javascript-example"></a>

```
import { SignatureV4 } from "@aws-sdk/signature-v4";
import { Sha256 } from "@aws-crypto/sha256-js";
import { HttpRequest } from "@aws-sdk/protocol-http";
import { defaultProvider } from "@aws-sdk/credential-provider-node";

const signer = new SignatureV4({
  service: "execute-api",
  region: "<REGION>",
  credentials: defaultProvider(),
  sha256: Sha256,
});

const request = new HttpRequest({
  method: "GET",
  hostname: "<API_HOST>",
  path: "/2025-04-18/iam/libraries",
  headers: { host: "<API_HOST>", "content-type": "application/json" },
});

const signed = await signer.sign(request);
// Use signed.headers with fetch or axios
```

## API stage and URL format
<a name="api-stage"></a>

The API is deployed under the stage name `2025-04-18`. The full URL pattern is:

```
https://<API_ID>.execute-api.<REGION>.amazonaws.com/2025-04-18/iam/<resource-path>
```

If a custom domain is configured, the stage name may be omitted depending on the base path mapping.

## Rate limits
<a name="rate-limits"></a>

The API enforces the following default limits. These values are configurable through Amazon API Gateway usage plan settings.

| Setting | Value |
| --- | --- |
| Steady-state rate | 500 requests/second |
| Burst limit | 1,000 requests |
| Daily quota | 100,000 requests |

If you exceed these limits, the API returns HTTP `429 Too Many Requests`. Implement exponential backoff and retry logic in your client. For more information, see [Error retries and exponential backoff in AWS](https://docs.aws.amazon.com/general/latest/gr/api-retries.html).

## Troubleshooting
<a name="troubleshooting-auth"></a>

 `403 Forbidden`
+ Verify your IAM principal has `execute-api:Invoke` permission on the correct API resource ARN.
+ Verify you are calling the `/iam/` prefixed endpoints.
+ Check that the SigV4 signature uses `execute-api` as the service name.
+ Confirm the region in your signature matches the API Gateway region.

 `401 Unauthorized`
+ Your temporary credentials may have expired. Refresh them (for example, re-assume the role) and retry.

 `Missing Authentication Token`
+ The request was not signed or the `Authorization` header is missing. Verify your HTTP client is applying SigV4 signing.
