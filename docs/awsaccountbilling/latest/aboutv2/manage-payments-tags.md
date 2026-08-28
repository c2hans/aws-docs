---
source_url: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-payments-tags.html
---

# Manage payment method access using tags
<a name="manage-payments-tags"></a>

You can use attribute-based access control (ABAC) to manage access to your purchase methods. When you create your payment methods, you can tags with key-value pairs. You can then create IAM policies and specify the tags. For example, if you add the `project` key and assign it a value of `test`, your IAM policies can explicitly allow or deny access to any payment instruments that has this tag.

To add tags to new payment instruments or update existing ones, see [Managing credit cards](manage-cc.md).

**Example Use tags to allow access**
The following policy allows the IAM entity to access payment instruments that have the `creditcard` key and a value of visa.
****

```
{
"Version":"2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Action": [
            "payments:ListPaymentInstruments",
            "payments:GetPaymentInstrument",
            "payments:ListTagsForResource"
        ],
        "Resource": "arn:aws:payments::123456789012:payment-instrument/*",
        "Condition": {
            "StringEquals": {
            "aws:ResourceTag/creditcard": "visa"
            }
        }
    }]
}
```

**Example Use tags to deny access**
The following policy denies the IAM entity from completing any payment action on payment methods that have the `creditcard` key and a value of `visa`.
****

```
{
"Version":"2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Action": "payments:*",
        "Resource": "*"
    },
    {
        "Effect": "Deny",
        "Action": "payments:GetPaymentInstrument",
        "Resource": "arn:aws:payments::123456789012:payment-instrument:*",
        "Condition": {
            "StringEquals": {
            "aws:ResourceTag/creditcard": "visa"
            }
        }
    }]
}
```

For more information, see the following topics in the *IAM User Guide*:
+ [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html)
+ [Controlling access to AWS resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awsaccountbilling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
