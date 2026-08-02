---
source_url: https://docs.aws.amazon.com/inspector/v1/userguide/inspector_slr.html
---

 End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic no longer available to new accounts and accounts that have not completed an assessment in the last 6 months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

# Using service-linked roles for Amazon Inspector Classic
<a name="inspector_slr"></a>

Amazon Inspector Classic uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Amazon Inspector Classic. Service-linked roles are predefined by Amazon Inspector Classic and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up Amazon Inspector Classic easier because you don’t have to manually add the necessary permissions. Amazon Inspector Classic defines the permissions of its service-linked roles, and unless defined otherwise, only Amazon Inspector Classic can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting its related resources. This protects your Amazon Inspector Classic resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes **in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

## Service-linked role permissions for Amazon Inspector Classic
<a name="slr-permissions"></a>

Amazon Inspector Classic uses the service-linked role named **AWSServiceRoleForAmazonInspector** – ServiceLinkedRoleDescription.

The AWSServiceRoleForAmazonInspector service-linked role trusts the following services to assume the role:
+ `inspector.amazonaws.com`

The role permissions policy named AmazonInspectorServiceRolePolicy allows Amazon Inspector Classic to complete the following actions on the specified resources:
+ Action: `iam:CreateServiceLinkedRole` on `arn:aws:iam::*:role/aws-service-role/inspector.amazonaws.com/AWSServiceRoleForAmazonInspector`

You must configure permissions to allow an IAM entity (such as an IAM user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for Amazon Inspector Classic
<a name="create-slr"></a>

You don't need to manually create a service-linked role. When you CompleteThisCreateActionInThisService in the AWS Management Console, the AWS CLI, or the AWS API, Amazon Inspector Classic creates the service-linked role for you.

## Editing a service-linked role for Amazon Inspector Classic
<a name="edit-slr"></a>

Amazon Inspector Classic does not allow you to edit the AWSServiceRoleForAmazonInspector service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for Amazon Inspector Classic
<a name="delete-slr"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way, you don’t have an unused entity that's not actively monitored or maintained. However, you must clean up the resources for your service-linked role before you can manually delete it.

**Note**
If the Amazon Inspector Classic service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

**To delete Amazon Inspector Classic resources used by `AWSServiceRoleForAmazonInspector`**
+ Delete your assessment targets for this AWS account in all the AWS Regions where you have Amazon Inspector Classic running. For more information, see [Amazon Inspector Classic assessment targets](inspector_applications.md).

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAmazonInspector service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported Regions for Amazon Inspector Classic service-linked roles
<a name="slr-regions"></a>

Amazon Inspector Classic supports using service-linked roles in all of the Regions where the service is available. For more information, see [AWS regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).
