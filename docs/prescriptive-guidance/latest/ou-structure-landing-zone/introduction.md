---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ou-structure-landing-zone/introduction.html
---

# OU structure in regulated AWS landing zones: an example from the pharmaceutical industry
<a name="introduction"></a>

*Katja Mueller, Petar Forai, and Keval Sheth, Amazon Web Services*

AWS provides several [Landing Zone Accelerator](https://aws.amazon.com/solutions/implementations/landing-zone-accelerator-on-aws/) configurations that support specific industries, including healthcare. The [Landing Zone Accelerator for Healthcare](https://aws.amazon.com/blogs/industries/introducing-landing-zone-accelerator-for-healthcare) is used in conjunction with AWS Control Tower to ease the management and governance of a multi-account environment that is aligned with AWS best practices and multiple global compliance frameworks. One important aspect of orchestrating governance is to group AWS accounts together by using organizational units (OUs), so you can administer them as a single unit.

This guide discusses best practices and considerations for redesigning existing OU structures as your company's cloud maturity grows. It introduces a practical example based on the AWS Control Tower implementation for a large pharmaceutical company, and discusses the lessons learned from that implementation. AWS landing zone design is not a one-time effort. It can and should be allowed to evolve. This evolution can be achieved successfully and efficiently by applying the AWS best practices and tips highlighted in this guide.
