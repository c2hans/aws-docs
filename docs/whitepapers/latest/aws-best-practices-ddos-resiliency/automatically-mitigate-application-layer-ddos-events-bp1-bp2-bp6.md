---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/automatically-mitigate-application-layer-ddos-events-bp1-bp2-bp6.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Automatically mitigate application-layer DDoS events (BP1, BP2, BP6)
<a name="automatically-mitigate-application-layer-ddos-events-bp1-bp2-bp6"></a>

 If you are subscribed to AWS Shield Advanced, you can enable [Shield Advanced automatic application](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-automatic-app-layer-response.html) [layer DDoS mitigation](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-automatic-app-layer-response.html). This feature automatically creates, evaluates, and deploys AWS WAF rules to mitigate layer 7 DDoS events on your behalf.

 AWS Shield Advanced establishes a traffic baseline for each protected resource associated with a WAF WebACL. Traffic that significantly deviates from the established baseline is flagged as a potential DDoS event. After an event is detected, AWS Shield Advanced attempts to identify a signature of the web requests that constitute the event, and if a signature is identified, AWS WAF rules are created to mitigate traffic with that signature.

 Once rules are evaluated against the historical baseline and deemed to be safe, they are added to the Shield-managed rule group, and you can choose whether the rules are deployed in count or block mode. Shield Advanced automatically removes AWS WAF rules after it has determined that an event has fully subsided.
