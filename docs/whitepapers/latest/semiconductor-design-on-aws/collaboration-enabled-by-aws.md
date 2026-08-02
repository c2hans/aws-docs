---
source_url: https://docs.aws.amazon.com/whitepapers/latest/semiconductor-design-on-aws/collaboration-enabled-by-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Collaboration enabled by AWS
<a name="collaboration-enabled-by-aws"></a>

Across the semiconductor industry, collaboration is part of the design process, fabrication, and product manufacturing. AWS enables you to securely collaborate with third-party IP providers, EDA tool vendors, foundries, and contract manufacturers. For example, you might have a requirement to work with a third-party IP provider or contract engineering team to create or validate a portion of your system-on-chip (SoC). Using AWS for collaboration makes it possible to segregate roles and data, lock down the environment to only authorized users, and monitor activity in the environment.

When trying to create similar collaborative environments in your on-premises data center, you might have the ability to isolate users and groups through existing network policies; however, you are still allowing external access to your internal infrastructure, and the collaboration environment is not scalable. On AWS, you can set up a completely separate, secure, and scalable environment that enables you to isolate access to only what is needed for the collaborative effort. This can be accomplished in several ways, but usually starts with a separate [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) with specific security settings for the level of security and access required. The setup of these secure chambers is covered in detail in [Run Semiconductor Design Workflows on AWS](https://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/run-semiconductor-design-workflows-on-aws.html).
