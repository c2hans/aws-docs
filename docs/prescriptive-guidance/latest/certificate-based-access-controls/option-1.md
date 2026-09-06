---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/certificate-based-access-controls/option-1.html
---

# Option 1: Applications can assume any role linked to an IAM Roles Anywhere profile
<a name="option-1"></a>

In this scenario, two certificates have been provisioned in AWS Certificate Manager (ACM) from the AWS Private Certificate Authority instance and shared with the applications that require access to AWS resources. These applications can assume any role that is linked to an IAM Roles Anywhere profile. This is because the trust policy doesn't limit which application can assume it.

**Note**
In this scenario, it is not required that the applications have separate certificates. They could share a single certificate.

When an application assumes a role, the permissions are the convergence of what is explicitly allowed in both the IAM role and in the IAM Roles Anywhere profile. Using this approach, you can limit session permissions through IAM Roles Anywhere profiles, regardless of the other permissions that are allowed in the IAM role.

The following image shows the access that each application has. Applications are denied access to some AWS resources because they are not explicitly granted access in both the IAM role and the IAM Roles Anywhere profile. If the Credential Helper call includes the Amazon Resource Name (ARN) for **Role 1**, then the application is granted temporary security credentials to access **Bucket 1** through **Role 1**. If the Credential Helper call includes the ARN for **Role 2**, then the application is granted temporary security credentials to access **Bucket 2** through **Role 2**.

![Applications use the same certificate and can access multiple roles. Profiles limit access.](http://docs.aws.amazon.com/prescriptive-guidance/latest/certificate-based-access-controls/images/guide-img/e306828d-cb6f-41be-b1da-12c08a777c76/images/f4e02c38-c66b-4b4f-be73-ddfbb667efc4.png)

The **Role 1** and **Role 2** trust policies are configured to allow IAM Roles Anywhere to assume the role, set the source identity, and tag the sessions. The following is a sample trust policy that allows the applications to assume any role that is linked to an IAM Roles Anywhere profile:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "rolesanywhere.amazonaws.com"
      },
      "Action": [
        "sts:AssumeRole",
        "sts:SetSourceIdentity",
        "sts:TagSession"
      ],
      "Condition": {
        "StringEquals": {
          "sts:SourceIdentity": [
            "${sourceIdentityPrefix}${sourceIdentityValue}"
          ]
        }
      }
    }
  ]
}
```

For more information about role trust policies and how you can modify this sample, see [Trust policy](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/trust-model.html#trust-policy) in the IAM Roles Anywhere documentation.

Sample role and profile policies for **Application 1** and **Application 2** are included in the [Appendix: Sample profile and role policies](appendix-sample-policies.md) section of this guide.
