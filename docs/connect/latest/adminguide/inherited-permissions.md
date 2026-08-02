---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/inherited-permissions.html
---

# Inherited permissions for Connect Customer and Contact Control Panel (CCP) security profiles
<a name="inherited-permissions"></a>

Some security profiles included inherited permissions: when you give a user explicit permissions to **View** or **Edit** one resource type, such as queues, they implicitly inherit permissions to **View** another resource type, such as phone numbers.

For example, assume you explicitly grant someone permission to **Edit/View** queues, as shown in the following image:

![The security profile permissions section of the security profiles page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/SecurityProfile_cloudscape_edit_view_queues.png)

By doing this you also implicitly grant them permissions to **View** a list of all phone numbers and hours of operation in your Connect Customer instance, **when they add them to the queue**. On the **Add new queue** page, the available phone numbers and hours of operation appear in dropdown lists, as shown in the following image.

![The add new queue page, the hours of operation dropdown list, the outbound caller id number dropdown list.](http://docs.aws.amazon.com/connect/latest/adminguide/images/SecurityProfile_cloudscape_add_queue_dropdowns.png)

However, they don't have permissions to **Edit** the phone numbers and hours of operation.

In this case, they also don't inherit permissions to **View** contact flows (the outbound whisper flow) and quick connects because those resources are optional.

## List of inherited permissions
<a name="list-of-inherited-permissions"></a>

The following table lists permissions that are implicitly inherited when you assign dedicated permissions to a user.

**Tip**
When a user has only explicit **View** permissions and not also **Edit** permissions, the objects are retrieved but Connect Customer doesn't surface them in drop-down lists for the user to peruse.

| Dedicated permission | Inherited permissions |
| --- | --- |
| Users - View or Edit | When someone edits a user's information in the Connect Customer console, they can **view** the following information in drop-down boxes when they add it to the user's account: [See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/inherited-permissions.html) |
| Queues - View or Edit | When someone edits queues in the Connect Customer console, they can **view** the following information in drop-down and search boxes when they add it to the queue:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/inherited-permissions.html) |
| Quick connects - View |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/inherited-permissions.html)  |
| Quick connects - Edit |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/inherited-permissions.html)  |
| Phone numbers - View or Edit | When someone edits phone numbers in the Connect Customer console (not the CCP), they can **view** the following information in a drop-down box when they associate it with the phone number: [See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/inherited-permissions.html) |
