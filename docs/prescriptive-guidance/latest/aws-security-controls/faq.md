---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/faq.html
---

# FAQ
<a name="faq"></a>

## What should I focus on if I have limited time and resources and can't implement all of these control types?
<a name="faq1"></a>

We recommend implementing AWS Security Hub CSPM. Security Hub CSPM has a set of automated security controls called the [AWS Foundational Security Best Practices standard](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp.html) (Security Hub CSPM documentation). This is a highly curated set of security best practices managed by AWS security experts. You can run these standard controls either continuously, whenever there are changes to the associated resources, or periodically, on a regular schedule. Each control has a specific severity score to help you prioritize your remediation efforts. For more information, see [Running security checks](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-controls-finding-generation.html#securityhub-standards-results-severity) (Security Hub CSPM documentation). If you are using AWS Control Tower, you can also review and choose to enable its preventative, detective, and proactive [controls](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html).
