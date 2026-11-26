---
source_url: https://docs.aws.amazon.com/devopsagent/latest/userguide/aws-devops-agent-security-controlling-web-app-access-with-access-profiles.html
---

# Controlling web app access with access profiles

Access profiles control what each person can do in the [web app](about-aws-devops-agent-what-is-a-devops-agent-web-app.md) for an Agent Space. Each profile assigns an AWS Identity and Access Management (IAM) role to a set of AWS IAM Identity Center groups and users. When a person signs in to the web app, AWS DevOps Agent uses the IAM role from their [highest matching profile](#how-aws-devops-agent-chooses-a-profile).

This topic explains how access profiles work, how AWS DevOps Agent chooses a profile, and how to create, edit, reorder, and delete profiles.

Use access profiles to give different teams different levels of access. For example, on-call engineers can run investigations and approve actions, and other teams can only view investigations.

## Prerequisites
<a name="prerequisites"></a>

Before you create access profiles, make sure that you have the following:
+ An Agent Space connected to IAM Identity Center. For more information, see [Configuring IAM Identity Center during Agent Space creation](aws-devops-agent-security-setting-up-iam-identity-center-authentication.html#configuring-iam-identity-center-during-agent-space-creation).
+ At least one group or user invited to the web app. You can assign only invited groups and users to an access profile.
+ For an IAM Identity Center instance that uses a customer managed AWS Key Management Service (AWS KMS) key, a key policy that lets AWS managed applications use the key through Identity Store. You need this key policy to assign groups to access profiles. For more information, see [Key management](aws-devops-agent-security-encryption-at-rest-for-devops-agent.html#key-management).
+ IAM permissions to manage access profiles. The [AIDevOpsAgentFullAccess](aws-devops-agent-security-devops-agent-iam-permissions.html#aidevopsagentfullaccess) managed policy includes them. The [AIDevOpsAgentReadOnlyAccess](aws-devops-agent-security-devops-agent-iam-permissions.html#aidevopsagentreadonlyaccess) managed policy includes the actions to view access profiles. For the full list of actions, see [Access profile management actions](aws-devops-agent-security-devops-agent-iam-permissions.html#access-profile-management-actions).
+ Permission to pass an IAM role (`iam:PassRole`), if you set the IAM role of an access profile. For more information, see [Required permissions to set an access profile's IAM role](#required-permissions-to-set-an-access-profiles-iam-role).

### Required permissions to set an access profile's IAM role
<a name="required-permissions-to-set-an-access-profiles-iam-role"></a>

When you set or change the IAM role of an access profile, AWS DevOps Agent checks that the calling principal can pass an IAM role. The principal is the IAM user or role that makes the request. If the principal doesn't have `iam:PassRole`, AWS DevOps Agent denies the request with an HTTP 403 `AccessDeniedException` that names `iam:PassRole`. AWS DevOps Agent denies the request even when the principal already has full access to AWS DevOps Agent, for example, `aidevops:*`. The `AIDevOpsAgentFullAccess` managed policy doesn't include `iam:PassRole`. Add it to your identity policy before you set the IAM role of an access profile.

**Example – Minimum IAM policy for setting an access profile's IAM role**

The following JSON policy lets you set one role, `MyAccessProfileRole`, as the IAM role of an access profile. The `iam:PassedToService` condition limits the permission to AWS DevOps Agent. Replace `111122223333` with your AWS account ID and `MyAccessProfileRole` with the name of your role.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::111122223333:role/MyAccessProfileRole",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "aidevops.amazonaws.com"
        }
      }
    }
  ]
}
```

Keep the following in mind:
+ Scope `Resource` to the roles that you want to allow in access profiles. To allow every role in your account, use a wildcard such as `arn:aws:iam::111122223333:role/*`.
+ For least-privilege access, set the `iam:PassedToService` condition to `aidevops.amazonaws.com`.
+ If you already scope `iam:PassRole` to specific services, add `aidevops.amazonaws.com` to the existing condition.

## How access profiles work
<a name="how-access-profiles-work"></a>

An access profile has the following parts.

| Part | Description |
| --- | --- |
| Name and description | The name and description identify the access profile in the console. |
| Members | The IAM Identity Center groups and users that the access profile applies to. You match an access profile when it's assigned to you directly or to a group that you belong to. |
| IAM role | The IAM role defines what members can do in the web app. An access profile without a role grants no permissions until you set a role. |
| Precedence | The position of the access profile in the list. AWS DevOps Agent checks access profiles higher in the list first. |

### How AWS DevOps Agent chooses a profile
<a name="how-aws-devops-agent-chooses-a-profile"></a>

A person can match more than one access profile, for example, through membership in several groups. When AWS DevOps Agent issues web app credentials to a person, it checks the access profiles that the person matches, in order of precedence:

1. If the highest matching access profile has an IAM role, AWS DevOps Agent uses that role.

1. If that access profile has no IAM role, AWS DevOps Agent skips it and checks the next matching access profile.

1. AWS DevOps Agent continues until it finds a matching access profile with an IAM role. If no matching access profile has one, the AWS default profile applies.

The web app session uses only the role of the access profile that AWS DevOps Agent chooses. AWS DevOps Agent doesn't combine the roles of several access profiles.

### Limits on profile permissions
<a name="limits-on-profile-permissions"></a>

AWS DevOps Agent applies the following limits to access profiles.

| Limit | Description |
| --- | --- |
| Who access profiles apply to | Access profiles apply only to people who sign in through IAM Identity Center. People who sign in with admin access (IAM) or an external identity provider keep the web app role on the Access tab. |
| Maximum permissions | Every web app session, with or without access profiles, can use only the actions that the [AIDevOpsOperatorAppAccessPolicy](aws-devops-agent-security-devops-agent-iam-permissions.html#aidevopsoperatorappaccesspolicy) managed policy allows. AWS DevOps Agent applies this policy as a session policy. A role with broader permissions, such as administrator access, still gets only these actions. An access profile's IAM role can narrow these permissions, but it can't add to them. AWS DevOps Agent limits its own role the same way. For more information, see [Understanding permission guardrails](aws-devops-agent-security-limiting-agent-access-in-an-aws-account.html#understanding-permission-guardrails). |
| Access management | A web app session that uses an access profile's IAM role can't create, change, reorder, or delete access profiles or their members. It also can't change the web app configuration of the Agent Space. Manage these in the AWS DevOps Agent console. |

### What a profile can control
<a name="what-a-profile-can-control"></a>

You control access one action at a time. Members of an access profile can use a feature in the web app only if the access profile's role allows every action that the feature needs. For the list of actions, see [AWS DevOps Agent IAM permissions](aws-devops-agent-security-devops-agent-iam-permissions.html).

When you design an access profile's role, keep in mind how asset actions apply. Skills, AGENTS.md files, custom agents, and memory stores are all assets. Asset actions, such as `aidevops:UpdateAsset`, apply to every asset in the Agent Space. A role can't allow an action for one type of asset, or for one agent's assets, and deny it for others.

The web app shows the same pages to every member. If you try an action that your role doesn't allow, you see an access denied error.

### Access tokens and access profiles
<a name="access-tokens-and-access-profiles"></a>

Access tokens belong to the Agent Space, not to a person. With an access token, Model Context Protocol (MCP) and Agent2Agent (A2A) clients, such as automation and integrations, can connect to AWS DevOps Agent without signing in to the web app.

Each token uses the web app role on the **Access** tab, limited to the scope that you choose when you create it. A token keeps the same access for its lifetime, even if your own access changes later.

Creating a token grants access, so treat `aidevops:CreateAccessToken` as an administrative permission. Include the access token actions only in access profiles for people who manage integrations for the Agent Space. For more information, see [Create an access token](connecting-to-devops-agent-remote-servers-authentication-and-security.html#create-an-access-token).

### The AWS default profile
<a name="the-aws-default-profile"></a>

AWS DevOps Agent creates an access profile named **AWS default** for every Agent Space, including Agent Spaces that you created before access profiles were available. Its members are **Any principal**, so it applies to every person who signs in to the web app. AWS DevOps Agent always checks it last.

The AWS default profile represents the web app permissions that you configured when you set up the web app. People receive the web app role on the **Access** tab, as if you hadn't created any access profiles. Until you create your own access profiles, nothing changes for the people who use the web app.

The AWS default profile is read-only. You can't change its name, members, or position, you can't set its IAM role, and you can't delete it. To customize access, create your own access profiles above it.

The AWS default profile always uses the web app role that you chose when you set up the web app. That role's permissions apply to everyone who matches no other access profile. To change those permissions, edit the role's policies in IAM. For example, to let only the members of your own access profiles take actions, remove permissions from the web app role and grant them through the IAM roles of your access profiles.

Access profiles control what people can do after they sign in, not who can sign in. To stop a person from signing in, remove them from the web app on the **Access** tab. For more information, see [Managing user access](aws-devops-agent-security-setting-up-iam-identity-center-authentication.html#managing-user-access).

### When changes take effect
<a name="when-changes-take-effect"></a>

AWS DevOps Agent checks a member's access profiles and group memberships each time the web app receives new credentials. Changes to access profiles, members, or precedence take effect the next time the web app receives new credentials. When a member reloads the page, changes take effect immediately, and removed access can take up to 2 minutes. Otherwise, changes take effect within an hour. Members don't need to sign out.

### Access profile quotas
<a name="access-profile-quotas"></a>

The following quota applies to access profiles.

| Quota | Value | Adjustable |
| --- | --- | --- |
| Maximum number of access profiles per Agent Space, including the AWS default profile | 20 | No |

## Viewing access profiles
<a name="viewing-access-profiles"></a>

To view the access profiles for an Agent Space, use the following procedure.

1. Open the [Agent Spaces page](https://console.aws.amazon.com/aidevops/home#/agent-spaces) in the AWS DevOps Agent console and choose your Agent Space.

1. Choose the **Access profiles** tab.

The list shows your access profiles in order of precedence, with **AWS default** last. Choose an access profile to see its IAM role and members. An access profile labeled **No role** grants no permissions until you set a role.

If the tab shows **Connect IAM Identity Center to use access profiles**, connect IAM Identity Center on the **Access** tab.

## Creating an access profile
<a name="creating-an-access-profile"></a>

This procedure creates an access profile that assigns an IAM role to a set of groups and users.

The **Choose permissions** page offers the following options for the IAM role.

| Option | Description |
| --- | --- |
| Operator | Members can run investigations and approve actions, but can't change configuration. AWS DevOps Agent creates the role for you with the [AIDevOpsOperatorAppAccessPolicy](aws-devops-agent-security-devops-agent-iam-permissions.html#aidevopsoperatorappaccesspolicy) managed policy. If the Agent Space uses a customer managed key, the role also gets permission to use the key. You can use the same role for access profiles in other Agent Spaces. |
| Use an existing role | Use a role that already has the permissions that you want. The role must be in the same AWS account as the Agent Space, and its trust policy must allow AWS DevOps Agent to assume it. The list shows only roles that trust AWS DevOps Agent. |
| Create a role yourself | Create a role in the IAM console by following the steps shown, and then enter its ARN. |
| No role | The access profile grants no permissions until you set a role. Until then, its members get their next matching access profile. |

1. On the **Access profiles** tab, choose **Create profile**.

1. On the **Specify profile details** page, enter a **Name** and, optionally, a **Description**, and then choose **Next**. The name can have up to 64 characters. It must start with a letter or number. It can contain letters, numbers, hyphens (-), and underscores (\_), but no spaces. The description can have up to 1,000 characters.

1. On the **Assign members** page, select the groups and users that get this access profile, and then choose **Next**.

1. On the **Choose permissions** page, select an option, and then choose **Next**. If you select **Operator**, enter a **Role name**. If you select **Use an existing role** and the console can't list the roles in your account, enter the role ARN.

1. On the **Set precedence** page, move the new access profile to its position in the list, and then choose **Next**.

1. On the **Review and create** page, review your choices, and then choose **Create profile**.

AWS DevOps Agent checks the role when you create the access profile. If the check fails with an `AccessDeniedException` that names `iam:PassRole`, add the permission in [Required permissions to set an access profile's IAM role](#required-permissions-to-set-an-access-profiles-iam-role), and then try again.

## Editing an access profile
<a name="editing-an-access-profile"></a>

To change the details, members, IAM role, or precedence of an access profile, use the following procedure.

1. On the **Access profiles** tab, choose the access profile.

1. Choose **Edit**.

1. Update the details, members, IAM role, or precedence of the access profile. You can replace a saved description, but you can't remove it.

1. Choose **Save changes**.

## Changing precedence
<a name="changing-precedence"></a>

To control which access profile AWS DevOps Agent checks first, use the following procedure.

1. On the **Access profiles** tab, move access profiles to their new positions in the list.

1. Choose **Save changes**.

1. Review the access profiles that moved, and then choose **Save changes**.

To undo changes that you haven't saved, choose **Discard**.

## Deleting an access profile
<a name="deleting-an-access-profile"></a>

To delete an access profile that you no longer need, use the following procedure.

1. On the **Access profiles** tab, choose the access profile.

1. Choose **Delete**.

1. Choose **Save changes**.

1. Review how many members lose the access profile, and then choose **Save changes**.

After you delete an access profile, its members get the next access profile that they match. Members that match no other access profile get the AWS default profile.

## Security considerations
<a name="security-considerations"></a>
+ Review the web app role on the **Access** tab. The AWS default profile uses it for anyone without an access profile, including people you invite to the web app later.
+ Assign access profiles to groups instead of individual users. Group assignments follow membership changes in your identity provider.
+ Start from the **Operator** option, and use your own roles to narrow access for teams that need less.
