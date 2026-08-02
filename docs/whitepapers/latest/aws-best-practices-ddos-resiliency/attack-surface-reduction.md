---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/attack-surface-reduction.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Attack surface reduction
<a name="attack-surface-reduction"></a>

 Another important consideration when architecting an AWS solution is to limit the opportunities an attacker has to target your application. This concept is known as attack *surface reduction*. Resources that are not exposed to the internet are more difficult to attack, which limits the options an attacker has to target your application’s availability.

 For example, if you do not expect users to directly interact with certain resources, make sure that those resources are not accessible from the internet. Similarly, do not accept traffic from users or external applications on ports or protocols that aren’t necessary for communication.

 In the following section, AWS provides best practices to guide you in reducing your attack surface and limiting your application’s internet exposure.
