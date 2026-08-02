---
source_url: https://docs.aws.amazon.com/aws-iq/latest/experts-user-guide/set-up-expert-account-permissions-to-use-aws-iq.html
---

End of support notice: On May 28, 2026, AWS will end support for AWS IQ. After May 28, 2026, you will no longer be able to access the AWS IQ console or AWS IQ resources. For more information, see [AWS IQ end of support](https://docs.aws.amazon.com/aws-iq/latest/experts-user-guide/aws-iq-end-of-support.html).

# Setting up permissions to use AWS IQ
<a name="set-up-expert-account-permissions-to-use-aws-iq"></a>

To access AWS IQ, you must have the necessary permissions. Navigate to the AWS Management Console to view or set up permissions. To leverage all resources on AWS IQ, add the [`AWSIQFullAccess` managed policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSIQFullAccess.html). For more granular controls, add specific permissions to your IAM identity.

**Note**
As a security best practice, we recommend periodically changing your user access keys. For more information, see [Managing access keys in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey).

This topic describes how to create an IAM user, attach policies to an existing user, and set up granular permissions in the AWS Management Console.

**Topics**
+ [Creating a user with `AWSIQFullAccess` permissions](#create-iam-user-AWSIQFullAccess-IAMFullAccess-permissions)
+ [Attaching managed policies to an existing user](#attach-managed-policies-AWSIQFullAccess-IAMFullAccess)
+ [Granular IAM permissions](#iq-granular-iam-permissions)

## Creating a user with `AWSIQFullAccess` permissions
<a name="create-iam-user-AWSIQFullAccess-IAMFullAccess-permissions"></a>

You, or your AWS account administrator, can create a new user with the `AWSIQFullAccess` managed policy on your AWS account. You can also attach this managed policy to an existing user. For more information, see [https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSIQFullAccess.html](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSIQFullAccess.html) in the AWS *Managed Policy Reference Guide*.

**To create an IAM user with managed policies**

1. Sign in to the **AWS Management Console**.

1. Choose **Users** and then choose **Add users**.

1. Enter a **User name**, and then choose **AWS Management Console access**. Accept the default information or change to custom values.

1. Choose **Next: Permissions** and then choose **Attach existing policies directly**.

1. Choose **`AWSIQFullAccess`** from the list of policy names, and then choose **Next: Tags**.

   1. *(Optional)* Add tags and then choose **Next: Review**.

1. Choose **Create user**.

1. Choose **Show** to display the password, and then copy your password to a secure location. You can also choose **Send email** to send the login instructions within an email message.

## Attaching managed policies to an existing user
<a name="attach-managed-policies-AWSIQFullAccess-IAMFullAccess"></a>

If you already have an IAM user, you can attach the `AWSIQFullAccess` managed policy using the following procedure.

**To attach managed policies to an existing IAM user**

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam/).

1. Choose **Users**.

1. Choose the user name to see the summary page for the user.

1. Choose **Add permissions**.

1. Choose **Attach existing policies directly**.

1. Choose `AWSIQFullAccess` from the list of policy names.

   If you don't see the policy names on the first page, filter the policies or search for the names using the console.

1. Choose **Next: Review**.

1. Choose **Add permissions**.

For more information, see [Adding and removing identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html).

## Granular IAM permissions
<a name="iq-granular-iam-permissions"></a>

As a user with administrative access, you can create one or more users in your AWS account. To configure your users with chosen levels of access on AWS IQ, you can deny specific permissions. First, add the `AWSIQFullAccess` managed policy. Then, you can add inline policies to deny specific permissions. For more information, see [Actions, resource, and condition keys for AWS IQ](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiq.html).

The following are examples of how to use granular permissions in AWS IQ.

**To use granular permissions in AWS IQ**

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam/).

1. To restrict a user from requesting access to a customer’s AWS account, create a deny policy on the **CreatePermissionRequest**, which is used to grant permission for creating permission requests.

------
#### [ JSON ]

****

   ```
   {
       "Version":"2012-10-17",
       "Statement": [
           {
               "Effect": "Deny",
               "Action": [
                   "iq-permission:CreatePermissionRequest"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

------

1. To restrict a user from requesting payments and proposals, create a deny policy for the following permissions:
   + `CreatePaymentRequest` – grants permission to create a payment request.
   + `CreateMilestoneProposal` – grants permission to create a milestone proposal.
   + `CreateUpfrontProposal` – grants permission to create an upfront proposal.
   + `CreateScheduledProposal` – grants permission to create a scheduled billing proposal.

------
#### [ JSON ]

****

     ```
     {
         "Version":"2012-10-17",
         "Statement": [
             {
                 "Effect": "Deny",
                 "Action": [
                     "iq:CreatePaymentRequest",
                     "iq:CreateMilestoneProposal",
                     "iq:CreateUpfrontProposal",
                     "iq:CreateScheduledProposal"
                 ],
                 "Resource": "*"
             }
         ]
     }
     ```

------

1. To restrict a user from sending chat messages, create a deny policy on all resources for the following permissions:
   + `SendIndividualChatMessage` – grants permission to chat messages as an individual.
   + `SendCompanyChatMessage` – grants permission to send chat messages as a company.

------
#### [ JSON ]

****

   ```
   {
       "Version":"2012-10-17",
       "Statement": [
           {
               "Effect": "Deny",
               "Action": [
                   "iq:SendIndividualChatMessage",
                   "iq:SendCompanyChatMessage"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

------

**To attach inline policies to an existing IAM identity**

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam/).

1. Choose **Users**.

1. Choose the username to see the summary page for the user.

1. Choose **Add permissions**.

1. Choose **Create inline policy**.

1. Select **Switch to deny permissions** to deny access.

1. Under **Service**, search for **IQ** or **IQ Permissions**.
**Note**
If you’re searching for permission requests and access grants, use **IQ Permissions**. For all other permissions, use **IQ**.

1. Under **Access level**, select the permissions to deny.

1. Choose **Review policy**, provide the name for your policy, and then choose **Create policy**.
