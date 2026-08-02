---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/load-testing.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Load testing
<a name="load-testing"></a>

 Regularly load test your application using the guidelines in our [Load Testing Applications](https://docs.aws.amazon.com/prescriptive-guidance/latest/load-testing/welcome.html) whitepaper with both expected and above expected traffic levels so you can see how effective your architecture is, how your Auto Scaling policies function and how your error handling functions. Test for expected traffic scale-up and down but also for "flash-crowd" type behavior. Retest either periodically or before any major release. For layer 3 or 4 DDoS simulation testing, such as SYN flood, follow our [DDoS Simulation Testing Policy](https://aws.amazon.com/security/ddos-simulation-testing/).
