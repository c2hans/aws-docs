---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/require-access-from-specific-ip-addresses.html
---

# Require access from specific IP addresses
<a name="require-access-from-specific-ip-addresses"></a>

**Note**
We would love to hear from you. Please provide feedback on the AWS PRA by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_cMxJ0MG3jU91Fk2).

This policy allows the `john_stiles` user to assume IAM roles only if the call is coming from an IP address in the ranges `192.0.2.0/24` or `203.0.113.0/24`. This policy can help prevent unintended disclosure of personal data and unwanted cross-border data transfers. For example, if your organization has customer support staff that require access to personal data, you might want that support staff to access that data only from offices that are located in a subset of specific AWS Regions. Also, verify your organization's definition of PII because some policies might require `Condition` or `Principal` sections that restrict access to a specific user or IP address.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:user/john_stiles"
      },
      "Action": "sts:AssumeRole"
    },
    {
      "Effect": "Deny",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:user/john_stiles"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "NotIpAddress": {
          "aws:SourceIp": [
            "192.0.2.0/24",
            "203.0.113.0/24"
          ]
        }
      }
    }
  ]
}
```
