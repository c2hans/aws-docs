---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/account-migration.html
---

# Account migration
<a name="account-migration"></a>

In [Invite your preexisting account](manage-member-accounts.md#invite-account), you invited your preexisting account to join the **Workloads > Prod** organizational unit. This account is now managed as part of your organization.

You also provisioned a new **dev-nonprod** account in the **Workloads > NonProd** organizational unit. Team members should now be able to access the appropriate accounts through AWS IAM Identity Center. Remove any individual user accounts in AWS Identity and Access Management (IAM).

If you have followed the recommendations in this guide, your organization now has the following structure.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/images/guide-img/b35f7443-fbaf-4ce8-bb48-32b6441d573f/images/178a8dc0-7b47-4c4b-a166-453a9fea58d6.png)

If there are workloads running within the preexisting account, you now migrate these workloads into independent accounts, according to the criteria you established in [Define scoping criteria](manage-member-accounts.md#define-scoping-criteria). Migrate any non-production workloads to the new **dev-nonprod** organizational unit, and migrate production workloads to the **network-prod** account. For more information about migrating common AWS resources, see the following section of this guide, [Resource migration](resource-migration.md).
