---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

## Amazon WorkMail
<a name="Welcome_Amazon_WorkMail"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

WorkMail is a secure, managed business email and calendaring service with support for existing desktop and mobile email clients. You can access your email, contacts, and calendars using Microsoft Outlook, your browser, or other native iOS and Android email applications. You can integrate WorkMail with your existing corporate directory and control both the keys that encrypt your data and the location in which your data is stored.

The WorkMail API is designed for the following scenarios:
+ Listing and describing organizations
+ Managing users
+ Managing groups
+ Managing resources

All WorkMail API operations are Amazon-authenticated and certificate-signed. They not only require the use of the AWS SDK, but also allow for the exclusive use of AWS Identity and Access Management users and roles to help facilitate access, trust, and permission policies. By creating a role and allowing an IAM user to access the WorkMail site, the IAM user gains full administrative visibility into the entire WorkMail organization (or as set in the IAM policy). This includes, but is not limited to, the ability to create, update, and delete users, groups, and resources. This allows developers to perform the scenarios listed above, as well as give users the ability to grant access on a selective basis using the IAM model.

## Amazon WorkMail Message Flow
<a name="Welcome_Amazon_WorkMail_Message_Flow"></a>

The WorkMail Message Flow API provides access to email messages as they are being sent and received by a WorkMail organization.
