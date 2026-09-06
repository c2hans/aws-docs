---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/assign-users-groups.html
---

# Assign users to groups
<a name="assign-users-groups"></a>

As you add new users to IAM Identity Center, you will have to assign them to one of the groups for them to access Innovation Sandbox.

**Note**
If you have configured IAM Identity Center to use an external identity provider you must assign group access to users through the external identity provider itself and have the changes synced over to your IAM Identity Center instance.

1. Sign in to the [AWS IAM Identity Center console](https://console.aws.amazon.com/singlesignon/).

1. From the left pane, choose **Users**.

1. On the Users page, choose the user name for the user you want to add to a group. The User details page displays.

1. On the **Groups** tab, choose **Add user to groups**.

1. Choose the groups you want to add the user to. You can choose from one of these relevant groups, depending on user role:
   +  `<NAMESPACE>_IsbUsersGroup`
   +  `<NAMESPACE>_IsbManagersGroup`
   +  `<NAMESPACE>_IsbAdminsGroup`

1. Choose **Add user to group**.

Alternatively, you can choose a group and add users to the group.

1. From the left pane, choose **Groups**.

1. On the Groups page, choose the group name you want to add users to. The Group details page displays. You can choose one of these relevant groups:
   +  `<NAMESPACE>_IsbUsersGroup`
   +  `<NAMESPACE>_IsbManagersGroup`
   +  `<NAMESPACE>_IsbAdminsGroup`

1. On the **Users** tab, choose **Add users to group**.

1. Choose the users you want to add to this group.

1. Choose **Add users to group**.

For more information, refer to the [Manage identities in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-sso.html) topic.
