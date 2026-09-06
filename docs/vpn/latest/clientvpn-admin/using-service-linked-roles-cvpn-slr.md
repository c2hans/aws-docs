---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/using-service-linked-roles-cvpn-slr.html
---

# Using roles for AWS Client VPN
<a name="using-service-linked-roles-cvpn-slr"></a>

AWS Client VPN uses AWS Identity and Access Management (IAM) service-linked roles. A service-linked role is a unique type of IAM role that is linked directly to Client VPN. Service-linked roles are predefined by Client VPN and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up Client VPN easier because you don’t have to manually add the necessary permissions. Client VPN defines the permissions of its service-linked roles, and unless defined otherwise, only Client VPN can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This protects your Client VPN resources because you can't inadvertently remove permission to access the resources.

## Service-linked role permissions for Client VPN
<a name="service-linked-role-permissions-cvpn-slr"></a>

Client VPN uses the service-linked role named **AWSServiceRoleForClientVPN** – Allow Client VPN to create and manage resources related to your VPN connections.

The **AWSServiceRoleForClientVPN** service-linked role trusts the following service to assume the role:
+ `clientvpn.amazonaws.com`

This service-linked role uses the managed policy ClientVPNServiceRolePolicy. To view the permissions for this policy, see [ClientVPNServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ClientVPNServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## Create a service-linked role for Client VPN
<a name="create-service-linked-role-cvpn-slr"></a>

You don't need to manually create a service-linked role. When you create the first Client VPN endpoint in your account with the AWS Management Console, the AWS CLI, or the AWS API, Client VPN creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you create the first Client VPN endpoint in your account, Client VPN creates the service-linked role for you again.

## Edit a service-linked role for Client VPN
<a name="edit-service-linked-role-cvpn-slr"></a>

Client VPN does not allow you to edit the AWSServiceRoleForClientVPN service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Edit a service-linked role description](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-service-linked-role.html#edit-service-linked-role-iam-console) in the *IAM User Guide*.

## Delete a service-linked role for Client VPN
<a name="delete-service-linked-role-cvpn-slr"></a>

If you no longer need to use Client VPN, we recommend that you delete the **AWSServiceRoleForClientVPN** service-linked role.

You must first delete the related Client VPN resources. This ensures that you do not inadvertently remove permission to access the resources.

Use the IAM console, the IAM CLI, or the IAM API to delete the service-linked roles. For more information, see [Delete a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#id_roles_manage_delete_slr) in the *IAM User Guide*.
