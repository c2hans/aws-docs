---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-evaluating-security-service/service-evaluation.html
---

# AWS security service evaluation
<a name="service-evaluation"></a>

A *proof of technology (POT)* is similar to a proof of concept. The goal of a POT is to determine whether a potential solution to a technical problem is viable. For example, you might use a POT to prove that a specific configuration can achieve a certain outcome. In this section, you use a POT to evaluate and demonstrate whether a given AWS security service meets your business and technical requirements.

The [AWS Security Reference Architecture (AWS SRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html) provides prescriptive guidance for deploying the full complement of AWS security services in a multi-account environment. This architecture can help you plan and execute your POT evaluation.

This decision guide applies to all AWS security services, including the latest offerings. For an up-to-date list of services and current best practices, see AWS Cloud[ Security](https://aws.amazon.com/security/).

## 2.1 Does the AWS security service address your compliance, security, or privacy mandates?
<a name="2-1"></a>

The AWS security service must address any compliance, security, and privacy mandates that the current solution does not address. You can find AWS certifications and reports for security and compliance in [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html). In addition, you can use the [AWS service documentation](https://docs.aws.amazon.com/) for coverage validation.

## 2.2 Does the AWS security service help mitigate risk?
<a name="2-2"></a>

Risk management is a key factor to help protect companies against many threats. The decision to adopt a service might be directly connected with mitigating one or more high risks in your organization. The AWS security service must mitigate the risk to an acceptable level, based on your risk appetite and business context.

## 2.3 Does the POT show effectiveness of the security service?
<a name="2-3"></a>

The effectiveness of the AWS security service must be demonstrated through a POT, according to different metrics of each security service. For example, the POT might validate that the service can detect and respond to security threats quickly through a threat intelligence algorithm. You might evaluate success by confirming that threats where detected within minutes and that automated notifications and remediations ran successfully. For a vulnerability management service, you might evaluate effectiveness based on the following:
+ How many vulnerabilities were detected?
+ What is the success rate of applying patches and updates?
+ For web protection, were cross-site scripting (XSS) and SQL-injection attacks performed by the offensive security team (also known as the *red team*) immediately blocked?

[AWS Professional Services](https://aws.amazon.com/professional-services/) and [AWS Partners](https://partners.amazonaws.com/search/partners) can support you in this POT evaluation.

## 2.4 Is the TCO lower than the current control or solution?
<a name="2-4"></a>

Lower TCO can help you optimize costs in your organization. Some common metrics used in these comparisons are: acquisition and implementation costs, fixed and variable expenses, operation costs, maintenance and support costs, expansion and reliability costs, and training costs. There are other cost measurements and comparisons that you can perform based on your specific use case. The [AWS Pricing Calculator](https://calculator.aws/) can help you estimate costs for AWS services. Additionally, you can use products in the AWS Free Tier and free trails to evaluate many AWS services. For more information, see [Free AWS Cloud Security Trials](https://aws.amazon.com/free/security/).

## 2.5 Trade-off decision
<a name="2-5"></a>

The trade-off decision requires balancing multiple factors, particularly service effectiveness and TCO considerations. When exact calculations or clear-cut determinations aren't possible, evaluate the overall balance of benefits and limitations.

A positive balance might emerge even when factors seem to conflict. For example, a service might increase costs but provide enhanced scalability. This represents a positive balance where the improved effectiveness justifies the additional costs. Conversely, a reduction in capabilities might not be acceptable even if a service offers significant cost savings.

You should balance all available information to determine an overall positive or negative outcome. Based on this analysis, you can make your trade-off decision.
