---
source_url: https://docs.aws.amazon.com/marketplace/latest/developerguide/deployment-service-quotas.html
---

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Service quotas for AWS Marketplace Deployment API
<a name="deployment-service-quotas"></a>

Your AWS account has the following quotas related to the AWS Marketplace Deployment Service.

**Request quotas**

|  **Quota**  | **Default** |  **Description**  |
| --- | --- | --- |
| Deployment parameter | 10 | The maximum number of deployment parameters per buyer and product combination |
| Deployment parameter update frequency | 100 | The maximum number of times you can update a deployment parameter per 24 hours |
| PutDeploymentParameter throttle | 1 | The maximum number of PutDeploymentParameter requests that you can make per second |
| ListTagsForResource throttle | 20 | The maximum number of ListTagsForResource requests that you can make per second |
| TagResource throttle | 20 | The maximum number of TagResource requests that you can make per second |
| UntagResource throttle | 20 | The maximum number of UntagResource requests that you can make per second |
| Deployment parameter SecretString name length | 15,000 | The maximum number of characters for the deployment parameter SecretString string |
| Deployment parameter name length | 400 | The maximum number of characters in a deployment parameter name |
| TagList | 50 | The maximum number of tags per deployment parameter request |
| ClientToken | 64 | The maximum number of characters for the ClientToken string |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
