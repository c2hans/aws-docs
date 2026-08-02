---
source_url: https://docs.aws.amazon.com/workmail/latest/adminguide/identity_center_overview.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

# Working with IAM Identity Center
<a name="identity_center_overview"></a>

You can enable multi-factor authentication (MFA) in Amazon WorkMail by associating your Amazon WorkMail users with IAM Identity Center. For more information, see [What is IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).

The table below describes the steps to address different scenarios.

| Scenario | Steps |
| --- | --- |
| Associating Amazon WorkMail users to IAM Identity Center | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workmail/latest/adminguide/identity_center_overview.html)  |
| Existing Amazon WorkMail users |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workmail/latest/adminguide/identity_center_overview.html)  |
| Existing IAM Identity Center users | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workmail/latest/adminguide/identity_center_overview.html) |
| Connecting an external directory to IAM Identity Center | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workmail/latest/adminguide/identity_center_overview.html) |

Once the above steps are completed you can view the IAM Identity Center status, link to the AWS IAM Identity Center to manage users and groups, MFA enabled Amazon WorkMail web application URL, authentication mode, personal access token status and timeline under IAM Identity Center under **Settings** in the Amazon WorkMail console. For more information on managing MFA in the IAM Identity Center console, see [Multi-factor authentication for IAM Identity Center users .](https://docs.aws.amazon.com//singlesignon/latest/userguide/enable-mfa.html)

**Note**
Make sure the configuration between Amazon WorkMail and IAM Identity Center is well tested and verified. Users could lose access to their mailboxes when the configuration is not correct and complete.

**Topics**
+ [Enabling IAM Identity Center in Amazon WorkMail](enabling_identity_center.md)
+ [Assigning IAM Identity Center users and groups to Amazon WorkMail application](assigning_usersandgroups.md)
+ [Associating Amazon WorkMail users with IAM Identity Center users](connecting_wmusers.md)
+ [Authentication mode](authenticate_mode.md)
+ [Configuring personal access tokens](personal_access-token.md)
+ [Disabling IAM Identity Center](disabling_sso.md)
