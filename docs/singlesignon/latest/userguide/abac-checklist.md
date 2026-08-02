---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/abac-checklist.html
---

# Checklist: Configuring ABAC in AWS using IAM Identity Center
<a name="abac-checklist"></a>

This checklist includes the configuration tasks that are necessary to prepare your AWS resources and to set up IAM Identity Center for ABAC access. Complete the tasks in this checklist in order. When a reference link takes you to a topic, return back to this topic so that you can proceed with the remaining tasks in this checklist.

- **1**
  - **Task:** Review how to add tags to all your AWS resources. To implement ABAC in IAM Identity Center, you'll first need to add tags to all your AWS resources that you want to implement ABAC for.
  - **Reference:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/singlesignon/latest/userguide/abac-checklist.html)

- **2**
  - **Task:** Review how to configure your identity source in IAM Identity Center with the associated user identities and attributes in your identity store. IAM Identity Center lets you use user attributes from any supported IAM Identity Center identity source for ABAC in AWS.
  - **Reference:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/singlesignon/latest/userguide/abac-checklist.html)

- **3**
  - **Task:** Based on the following criteria, determine which attributes you want to use for making access control decisions in AWS and send them to IAM Identity Center.  / **Reference:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/singlesignon/latest/userguide/abac-checklist.html)
  - **Task:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/singlesignon/latest/userguide/abac-checklist.html)  / **Reference:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/singlesignon/latest/userguide/abac-checklist.html)
  - **Task:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/singlesignon/latest/userguide/abac-checklist.html)  / **Reference:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/singlesignon/latest/userguide/abac-checklist.html)
  - **Task:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/singlesignon/latest/userguide/abac-checklist.html)  / **Reference:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/singlesignon/latest/userguide/abac-checklist.html)
  - **Task:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/singlesignon/latest/userguide/abac-checklist.html)  / **Reference:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/singlesignon/latest/userguide/abac-checklist.html)

- **4**
  - **Task:** Select the attributes to use for ABAC using the **Attributes for access control** page in the IAM Identity Center console. From this page you can select attributes for access control from the identity source that you configured in step 2. After your identities and their attributes are in IAM Identity Center, you must create key-value pairs (mappings) which will be passed to your AWS accounts for use in access control decisions.
  - **Reference:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/singlesignon/latest/userguide/abac-checklist.html)

- **5**
  - **Task:** Create custom permissions policies within your permission set and use access control attributes to create ABAC rules so that users can only access resources with matching tags. User attributes that you configured in step 4 are used as tags in AWS for access control decisions. You can refer to the access control attributes in the permissions policy using the `aws:PrincipalTag/key` condition.
  - **Reference:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/singlesignon/latest/userguide/abac-checklist.html)

- **6**
  - **Task:** In your various AWS accounts, assign users to permissions sets you created in step 5. Doing so ensures that when they federate into their accounts and access AWS resources, they only get access based on matching tags.
  - **Reference:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/singlesignon/latest/userguide/abac-checklist.html)

After you complete these steps, users who federate into an AWS account using single sign-on will get access to their AWS resources based on matching attributes.
