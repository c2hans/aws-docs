---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/awsserverlessapplicationrepository.html
---

# Data retrieval APIs for AWS Serverless Application Repository
<a name="awsserverlessapplicationrepository"></a>

AWS Serverless Application Repository provides the following APIs for data retrieval.

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="serverlessrepo-GetApplication"></a>[GetApplication](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid.html) | Get the specified application | Read |
| <a name="serverlessrepo-GetApplicationPolicy"></a>[GetApplicationPolicy](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-policy.html) | Get the policy for the specified application | Read |
| <a name="serverlessrepo-GetCloudFormationTemplate"></a>[GetCloudFormationTemplate](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-templates-templateid.html) | Get the specified AWS CloudFormation template | Read |
| <a name="serverlessrepo-ListApplicationDependencies"></a>[ListApplicationDependencies](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-dependencies.html) | Retrieve the list of applications nested in the containing application | List |
| <a name="serverlessrepo-ListApplicationVersions"></a>[ListApplicationVersions](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-versions.html) | List versions for the specified application owned by the requester | List |
| <a name="serverlessrepo-ListApplications"></a>[ListApplications](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications.html) | List applications owned by the requester | List |
| <a name="serverlessrepo-SearchApplications"></a>[SearchApplications](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid.html) | Get all applications authorized for this user | Read |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query online-register` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
