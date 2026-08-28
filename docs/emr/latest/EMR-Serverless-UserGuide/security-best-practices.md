---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-best-practices.html
---

# Security best practices for Amazon EMR Serverless
<a name="security-best-practices"></a>

Amazon EMR Serverless provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions.

## Apply principle of least privilege
<a name="security-least-privilege"></a>

EMR Serverless provides a granular access policy for applications using IAM roles, such as execution roles. We suggest that execution roles be granted only the minimum set of privileges required by the job, such as covering your application and access to log destination. We also recommend auditing the jobs for permissions on a regular basis and upon any change to application code.

## Isolate untrusted application code
<a name="security-isolate-untrusted"></a>

EMR Serverless creates full network isolation between jobs belonging to different EMR Serverless applications. In cases where job-level isolation is desired, consider isolating jobs into different EMR Serverless applications.

## Role-based access control (RBAC) permissions
<a name="security-practice-rbac"></a>

Administrators should strictly control Role-based access control (RBAC) permissions for EMR Serverless applcations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
