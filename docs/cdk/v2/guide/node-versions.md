---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/node-versions.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# Supported Node.js versions for the AWS CDK
<a name="node-versions"></a>

The AWS Cloud Development Kit (AWS CDK) runs on Node.js. This includes the AWS CDK CLI (`aws-cdk-cli`), AWS Construct Library (`aws-cdk-lib`), as well as broader ecosystem tools such as JSII, Projen, and CDK8s.

## Version support policy
<a name="node-version-support-policy"></a>

The AWS CDK supports Node.js Long Term Support (LTS) versions. When a Node.js version reaches its community End-of-Life (EOL), the AWS CDK continues to support it for an additional 6 months before ending support.

After support ends, the AWS CDK team will no longer provide security patches, bug fixes, or compatibility updates for that Node.js version. Using the AWS CDK with an unsupported Node.js version may result in unexpected behavior, errors, or security vulnerabilities.

For upcoming Node.js release and EOL dates, see the [Node.js release schedule](https://github.com/nodejs/Release#release-schedule).

## Supported Node.js versions
<a name="node-version-supported"></a>

The following table lists Node.js versions currently supported by the AWS CDK.

| Node.js version | Node.js EOL date | CDK support end date |
| --- | --- | --- |
| 24.x | 2028-04-30 | 2028-10-30 |
| 22.x | 2027-04-30 | 2027-10-30 |
| 20.x | 2026-04-30 | 2026-10-30 |

## Node.js versions no longer supported
<a name="node-version-deprecated"></a>

The following Node.js versions are no longer supported by the AWS CDK.

| Node.js version | Node.js EOL date | CDK support ended |
| --- | --- | --- |
| 18.x | 2025-05-30 | 2025-11-30 |
| 16.x | 2023-09-11 | 2025-05-30 |
| 14.x | 2023-04-30 | 2025-05-30 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
