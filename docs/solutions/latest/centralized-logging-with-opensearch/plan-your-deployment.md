---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/plan-your-deployment.html
---

# Plan your deployment
<a name="plan-your-deployment"></a>

This section describes the [cost](cost.md), [security](security.md), and other considerations before deploying the solution.

## Supported AWS Regions
<a name="supported-aws-regions"></a>

This solution uses services that may not be currently available in all AWS Regions. Launch this solution in an AWS Region where required services are available. For the most current availability by Region, refer to the AWS Regional Services List.

Centralized Logging with OpenSearch provides two types of authentications, [Amazon Cognito User Pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) and [OpenID Connect (OIDC) Provider](https://openid.net/connect/). Choose to launch the solution with OpenID Connect if one of the following cases occurs:
+ Amazon Cognito User Pool is not available in your AWS Region.
+ You already have an OpenID Connect Provider and want to authenticate against it.

 **Supported Regions for deployment**

| Region Name | Launch with Amazon Cognito User Pool | Launch with OpenID Connect |
| --- | --- | --- |
| US East (N. Virginia) | ✓ | ✓ |
| US East (Ohio) | ✓ | ✓ |
| US West (N. California) | ✓ | ✓ |
| US West (Oregon) | ✓ | ✓ |
| Canada (Central) | ✓ | ✓ |
| Canada (Calgary) | X | ✓ |
| Africa (Cape Town) | X | ✓ |
| Asia Pacific (Hong Kong) | X | ✓ |
| Asia Pacific (Mumbai) | ✓ | ✓ |
| Asia Pacific (Osaka) | X | ✓ |
| Asia Pacific (Seoul) | ✓ | ✓ |
| Asia Pacific (Singapore) | ✓ | ✓ |
| Asia Pacific (Sydney) | ✓ | ✓ |
| Asia Pacific (Tokyo) | ✓ | ✓ |
| Asia Pacific (Hyderabad) | X | ✓ |
| Asia Pacific (Jakarta) | ✓ | ✓ |
| Asia Pacific (Melbourne) | X | ✓ |
| Israel (Tel Aviv) | X | ✓ |
| Middle East (Bahrain) | ✓ | ✓ |
| Middle East (UAE) | X | ✓ |
| Europe (Frankfurt) | ✓ | ✓ |
| Europe (Ireland) | ✓ | ✓ |
| Europe (London) | ✓ | ✓ |
| Europe (Milan) | X | ✓ |
| Europe (Paris) | ✓ | ✓ |
| Europe (Stockholm) | ✓ | ✓ |
| Europe (Spain) | X | ✓ |
| Europe (Zurich) | X | ✓ |
| South America (Sao Paulo) | ✓ | ✓ |
| China (Beijing) Region Operated by Sinnet | X | ✓ |
| China (Ningxia) Regions operated by NWCD | X | ✓ |

**Important**
You can have only one active Centralized Logging with OpenSearch solution stack in one Region. If your deployment failed, make sure you have deleted the failed stack before retrying the deployment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Logging with OpenSearch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
