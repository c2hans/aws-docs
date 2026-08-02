---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/user-creation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# User creation
<a name="user-creation"></a>

You need to create a user for the WordPress plugin to store static assets in Amazon S3. For steps, refer to [Creating a user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html).

 **Note:** Roles provide a better way of managing access to AWS resources, but at the time of writing, the W3 Total Cache plugin does not support [ roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html).

 Take a note of the user security credentials and store them in a secure manner – you need these credentials later.
