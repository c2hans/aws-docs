---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/approach-2-no-personal-data-in-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Approach 2 – no personal data in AWS
<a name="approach-2-no-personal-data-in-aws"></a>

 Alternatively, customers may decide not to move personal data to the AWS Cloud and implement some techniques on their side to anonymize or obfuscate the data—whatever is needed to remove the portion of the data that may be considered to be personal data.

![Transfer and store non-personal data in the AWS Cloud](https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/images/no-personal-data-external.png)

 Transfer and store non-personal data in the AWS Cloud

 With this approach, the customer works with data in the AWS Cloud as usual by using tools, services, and workflows that are available on AWS. It’s the customer’s responsibility to ensure that *no personal data is processed in the AWS Cloud for this particular scenario*, and proper mechanisms to remove, or [tokenize](https://aws.amazon.com/blogs/security/how-to-use-tokenization-to-improve-data-security-and-reduce-audit-scope/), personal data from the transferred data is implemented. The customer either implements a *modification layer* to remove personal data from transferred data, or just transfer non-personal data to the AWS Cloud. For more information about a “modification layer”, refer to the [How to protect sensitive data for its entire lifecycle in AWS](https://aws.amazon.com/blogs/security/how-to-protect-sensitive-data-for-its-entire-lifecycle-in-aws/) and [Building a serverless tokenization solution to mask sensitive data](https://aws.amazon.com/blogs/compute/building-a-serverless-tokenization-solution-to-mask-sensitive-data/) AWS blog posts.
