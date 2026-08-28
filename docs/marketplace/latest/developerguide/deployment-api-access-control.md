---
source_url: https://docs.aws.amazon.com/marketplace/latest/developerguide/deployment-api-access-control.html
---

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Access control for the AWS Marketplace Deployment API
<a name="deployment-api-access-control"></a>

To manage deployments in AWS Marketplace, you must ensure that you have the necessary AWS Identity and Access Management (IAM) roles and permissions.

Before calling the `PutDeploymentParameter` action, buyers must create the **AWSServiceRoleForMarketplaceDeployment** service-linked role. This provides AWS Marketplace with the permissions required to create, manage, and tag the necessary deployment parameter related resources in the buyer's account. Buyers create this role using prompts as they progress through the configuration process for any Quick Launch experience. For more information, see [Using roles to configure and launch products](https://docs.aws.amazon.com/marketplace/latest/buyerguide/using-service-linked-roles-secrets.html) in * AWS Marketplace Buyer Guide*.

To call `PutDeploymentParameter`, sellers must have IAM permissions for the following actions:

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Action": [
                "aws-marketplace:PutDeploymentParameter",
                "aws-marketplace:TagResource"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

------

The `aws-marketplace:PutDeploymentParameter` action permits the user to call the `PutDeploymentParameter` API. The API also accepts an optional `tags` attribute. If the `tags` attribute is included in the request, the caller must also have permissions for `aws-marketplace:TagResource` on the relevant resource. For more information about creating users, see [Creating a user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) in the *IAM User Guide.* For more information about creating and assigning policies, see [Changing permissions for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
