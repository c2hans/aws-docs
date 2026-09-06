---
source_url: https://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/appendix-a.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix A: Adding IAM user policies
<a name="appendix-a"></a>

 This section describes how to add IAM user policies to an AWS account. For more information, see [Creating an IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_SettingUpUser.html) in the *User Guide*.

1.  In the AWS Management Console, choose **Services > IAM**.
![Screen capture of the IAM console](http://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/images/iam-in-console.jpg)

1.  Choose **Users**.

1.  Choose **Add Users**.
![Screen showing Add Users.](http://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/images/add-users.png)

1.  Enter name of the IAM user to be created.

1.  Choose **Next**.
![Screen shot of Set User Details.](http://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/images/set-user-details.png)

1.  Choose **Next** to attach a user policy.
![Screen showing Attach existing policies.](http://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/images/add-policy.png)

1.  If none of these policies work for your use case, you can Create a policy and attach it. You can create the policy using the Interface, or you can create a custom JSON policy with one of the examples from [Appendix B](appendix-b.md)***.***
![Screen shot of Create Policy](http://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/images/create-policy.png)

1.  Paste the proper policy from [Appendix B](appendix-b.md).

1.  Choose **Apply Policy**.

1.  On the previous screen, refresh the policy list, and attach the policy you just created.

1. Choose **Download Credentials**. Save the downloaded file in a secure location, as these are the user’s access key ID and secret access key. They will need these to use the AWS API.
![Screen showing success.](http://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/images/success-screen.png)
