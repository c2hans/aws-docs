---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/auth-concept-iam.html
---

# IAM concepts
<a name="auth-concept-iam"></a>

AWS Identity and Access Management provides fine-grained access control for Amazon Location Service resources. Use IAM for server-side applications, backend services, and administrative tasks where you need full control over permissions.

**IAM policy**
A JSON document that defines permissions for Amazon Location Service actions and resources. Policies specify which API operations are allowed or denied and can include conditions such as source IP address or request Region.

**IAM role**
An identity with specific permissions that can be assumed by AWS services, applications, or users. Roles provide temporary credentials and are the recommended approach for applications running on AWS compute services.

**Resource ARN**
The Amazon Resource Name that uniquely identifies an Amazon Location Service resource in IAM policies. For standalone APIs (Maps, Places, Routes), the resource ARN follows the format `arn:aws:geo-maps:{{region}}::provider/default`. For legacy resources (trackers, geofence collections), it includes the account ID and resource name.

**SigV4 signing**
The AWS Signature Version 4 process used to authenticate IAM and Amazon Cognito requests. The AWS SDKs handle SigV4 signing automatically. API keys bypass SigV4 signing entirely.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
