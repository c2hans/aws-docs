---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-security-perspective/planning-your-security-journey.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Planning your security journey
<a name="planning-your-security-journey"></a>

****
 Improve your security posture over time. First, implement the security recommendations that mitigate the largest risks, with the least effort. Then, advance your security posture *coherently*, by investing in diverse capabilities to reduce the overall risk as soon as possible.

 Today, organizations must innovate quickly. To enable rapid innovation, security teams need to prioritize critical initiatives, business goal focused security risk reduction, and iterate often to improve their security posture over time. With so many security recommendations available, customers often ask: *"How should we prioritize what to do first?"*

 In this document, you will find multiple security capabilities. In each capability, we show:
+ Which security recommendations are foundational for that capability (*Start*)
+ Which ones are a more advanced implementation of that capability (*Advance*)
+ How can you get to an ideal state (*Excel*)

 Begin with the Start phase of each capability to be comprehensive with your approach, but priorities will vary depending on many factors, including:
+ Your security and compliance requirements
+ Industry
+ Use cases, types of workloads
+ Sensitivity of the data managed in the organization
+ How critical cybersecurity is for the core business of the organization

 And even though we should make every effort to reduce the time that risks are unmitigated, some security controls take more time and effort to implement. Consider what recommendations will strengthen your security posture more quickly—the quick wins.
+  **Ease of implementation** - An easy implementation is one that is quick to implement, has lower effort, and lower cost.
+  **Increased security benefits** - A higher security posture mitigates *critical risks*, defined as high likelihood of occurrence, and greater impact.

 Once you've identified the quickest wins for your organization, plan security activities that will strengthen your security posture and coherence over time. If you are currently running workloads in the cloud, perform a quick assessment to identify gaps, and then start the improvements for each phase:
+  **Start** - Important recommendations that form the basis of your security posture, but may take time.
+  **Advance** - Recommendations that enable efficient governance of cloud security.
+  **Excel** - Recommendations for nearly continuous improvement.

 Always strive to maintain the maturity and coherence of your security controls, and plan accordingly. A strong [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) foundation is important, but if you spend months focused only on defining IAM Governance and refinding IAM policies to least privilege, and you don't have threat visibility in place during that time, you might fail to detect and incident. By enabling [Amazon GuardDuty](https://aws.amazon.com/guardduty/), you can get threat detection capabilities within minutes.

 A sample journey with specific guidance can be found in the [https://maturitymodel.security.aws.dev/en/model](https://maturitymodel.security.aws.dev/en/model).
