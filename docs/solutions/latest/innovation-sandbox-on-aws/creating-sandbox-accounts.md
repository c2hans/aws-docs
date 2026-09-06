---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/creating-sandbox-accounts.html
---

# Creating sandbox accounts
<a name="creating-sandbox-accounts"></a>

The Innovation Sandbox on AWS solution works with existing AWS accounts and does not create new accounts. Create new accounts using AWS Organizations. For more information, refer to [Creating a member account in an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html).

Create the number of accounts that you want to start with in your Account Pool based on the number of expected concurrent users. For example, if you expect 10 concurrent users, create 10 sandbox accounts using AWS Organizations.

**Note**
The size of the account pool can be adjusted at any time. If you are unsure of how many accounts you will need, you can start with a smaller number and expand the pool as necessary ([Adding new accounts to the account pool](administrator-guide.md#new-accounts)). You can also reduce the pool size in the future ([Managing existing accounts](administrator-guide.md#manage-accounts)).

**Note**
If you use accounts that are created or managed from AWS Control Tower, they will show as drifted in the AWS Control Tower console because the solution moves the accounts between OUs.
