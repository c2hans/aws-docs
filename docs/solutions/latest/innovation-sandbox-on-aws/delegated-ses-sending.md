---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/delegated-ses-sending.html
---

# Send email through an SES identity in another account

By default, the solution sends email through an Amazon SES identity in the Hub account. If your organization verifies senders in a separate account, that account can authorize the Hub account to send through its identity. This is called sending authorization. For more information, see [Using sending authorization with Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html) in the *Amazon Simple Email Service Developer Guide*.

Sending through another account’s identity requires permission on both sides. The Hub account sends the email, so its own SES sending quotas and production access status apply. The identity owner’s account must also have SES production access in the same Region; otherwise, neither account can send to unverified recipients. The identity owner’s sending authorization policy must allow the Hub account to send, and the solution’s own IAM policy must allow it to use that identity. The solution grants its side when you set the **Delegated SES Identity ARN** parameter. Neither permission works without the other.

To send email through an SES identity in another account:

1. In the account that owns the identity, verify the email address or domain in Amazon SES in the Region where you deploy the solution. An identity in a different Region doesn’t work.

1. In the same account, add a sending authorization policy to the identity that allows the Hub account to call `ses:SendEmail`. For example:

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": { "AWS": "arn:aws:iam::<hub-account-id>:root" },
         "Action": "ses:SendEmail",
         "Resource": "arn:aws:ses:<region>:<identity-account-id>:identity/example.com"
       }
     ]
   }
   ```

   Replace `<hub-account-id>`, `<region>`, and `<identity-account-id>` with your values.

1. Deploy (or update) the Compute stack with **Delegated SES Identity ARN** set to the identity’s ARN.

1. On the **Settings** page, enter an **Email from address (SES)** that the identity covers. For an email address identity, use that address. For a domain identity, use an address in the domain or one of its subdomains.

When you save the sender address, the solution checks only that the identity covers it. The Hub account can’t read SES identities in another account, so it can’t confirm that the identity is verified or that the policy allows sending. These problems appear when the solution sends email. Failed sends are logged and raise the SES send failure alarm. For more information, see [Notifications are not delivered](troubleshooting.md#notifications-not-delivered).

To change or remove the delegated identity, update the Compute stack with a new value or an empty value. The solution scopes its IAM permission to the exact identity ARN, so a stack update is required for any change.
