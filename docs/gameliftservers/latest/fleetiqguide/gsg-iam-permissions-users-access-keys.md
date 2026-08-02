---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-iam-permissions-users-access-keys.html
---

# Set up programmatic access for users
<a name="gsg-iam-permissions-users-access-keys"></a>

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

****

| Which user needs programmatic access? | To | By |
| --- | --- | --- |
| IAM | (Recommended) Use console credentials as temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.[See the AWS documentation website for more details](http://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-iam-permissions-users-access-keys.html) |
| Workforce identity<br />(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.[See the AWS documentation website for more details](http://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-iam-permissions-users-access-keys.html) |
| IAM | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions in [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the IAM User Guide. |
| IAM | (Not recommended)Use long-term credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.[See the AWS documentation website for more details](http://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-iam-permissions-users-access-keys.html) |

If you use access keys, see [ Best practices for managing AWS access keys](https://docs.aws.amazon.com/accounts/latest/reference/credentials-access-keys-best-practices.html).
