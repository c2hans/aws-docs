---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/tcp-middlebox-reflection.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# TCP middlebox reflection
<a name="tcp-middlebox-reflection"></a>

 This relatively new attack vector was first disclosed in an [academic whitepaper](https://www.usenix.org/system/files/sec21fall-bock.pdf) in August 2021 which explained how TCP non-compliance in both nation-state and commercially available firewalls could result in these being tricked into becoming a TCP amplification vector. We have seen these attacks "in the wild" since early 2022 and continue to see them today. The amplification factor varies due to the different ways in which vendors have implemented this "feature", but can exceed Memcached UDP amplification.
