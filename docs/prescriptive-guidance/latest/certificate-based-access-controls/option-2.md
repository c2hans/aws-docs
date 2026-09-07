---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/certificate-based-access-controls/option-2.html
---

# Option 2: Applications can assume only the role that the trust policy allows
<a name="option-2"></a>

In this scenario, two certificates have been provisioned in AWS Certificate Manager (ACM) from AWS Private Certificate Authority and shared with the applications that require access to AWS resources. **Application 1** can assume only **Role 1**, and **Application 2** can assume only **Role 2**. In the role trust policy, you configure certificate subject fields as conditions. These conditions allow the application to assume only a specific role. Because of the role permissions, only **Application 1** can access **Bucket 1**, and only **Application 2** can access **Bucket 2**. The following image shows the access that each application has.

![Applications that use different certificates and can assume only specific roles.](https://docs.aws.amazon.com/prescriptive-guidance/latest/certificate-based-access-controls/images/guide-img/e306828d-cb6f-41be-b1da-12c08a777c76/images/8b64315e-fef5-4004-aee2-ec281fc606ff.png)

In this option, you configure the trust policies to allow `AssumeRole` only when specific certificate attributes are met. The sample role trust policy demonstrates how to configure the `Condition` section to require a specific certificate common name (`CN`), which is different for **Role 1** and **Role 2**. Each application can assume a specific role because IAM Roles Anywhere has a trust anchor relationship with AWS Private CA. This approach helps prevent unauthorized access to roles and data because the application cannot assume any role that is linked to the target profile. For example, you can segregate business data into different buckets, configure roles to allow access to only one of those buckets, and then use certificate-based access controls in the trust policy to define which role the application can assume.

The following sample trust policy for **Role 1** has a condition that allows role assumption only if the certificate name is `application-1.com` and if the trust anchor Amazon Resource Name (ARN) matches:

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
          "aws:PrincipalTag/x509Subject/CN": "application-1.com"
        },
        "ArnEquals": {
          "aws:SourceArn": [
            "arn:aws:rolesanywhere:<region>:<account-ID>:trust-anchor/<TA_ID>"
          ]
        }
      }
    }
  ]
}
```

The following sample trust policy for **Role 2** has a condition that allows role assumption only if the certificate name is `application-2.com` and if the trust anchor ARN matches:

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
          "aws:PrincipalTag/x509Subject/CN": "application-2.com"
        },
        "ArnEquals": {
          "aws:SourceArn": [
            "arn:aws:rolesanywhere:<region>:<account-ID>:trust-anchor/<TA_ID>"
          ]
        }
      }
    }
  ]
}
```

For more information about role trust policies and how you can modify these samples, see [Trust policy](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/trust-model.html#trust-policy) in the IAM Roles Anywhere documentation.

Sample role and profile policies for **Application 1** and **Application 2** are included in the [Appendix: Sample profile and role policies](appendix-sample-policies.md) section of this guide.
