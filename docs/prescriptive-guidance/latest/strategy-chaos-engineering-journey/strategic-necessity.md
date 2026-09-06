---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-chaos-engineering-journey/strategic-necessity.html
---

# Transitioning from ROI to chaos engineering as a strategic necessity
<a name="strategic-necessity"></a>

Although it's tempting to monitor ROI, the challenges in measuring chaos engineering's value often lead organizations to prioritize immediate, short-term efficiencies over strategic resilience investments. This approach overlooks chaos engineering as a key driver of resilience and the competitive advantages of avoiding outages. The real value of chaos engineering is in preventing future failures. Chaos engineering supports long-term business continuity.

Instead of focusing on ROI, treat chaos engineering like cybersecurity. As explained in the *Forbes* article [Cybersecurity As A Strategic Investment: How ROI Optimization Can Lead To A More Secure Future](https://www.forbes.com/councils/forbestechcouncil/2023/08/16/cybersecurity-as-a-strategic-investment-how-roi-optimization-can-lead-to-a-more-secure-future/), cybersecurity shouldn't be viewed as a cost center or obligatory expense for organizations because that mindset fails to recognize the strategic value that robust cybersecurity measures can provide over time. Instead, the author argues that by shifting perspectives to treat cybersecurity as a long-term investment that drives competitive advantages, organizations can unlock new avenues for innovation, operational efficiencies, and differentiation within their respective markets. By adopting this approach, the author concludes that Chief Information Security Officers (CISOs) can better secure leadership buy-in and funding. They can then position their companies to outpace competitors in an increasingly risky cyber landscape. This long-term, strategic value creation of cybersecurity parallels the continuous improvements inherent in chaos engineering practices.

Whereas security safeguards an organization's ability to operate and protect assets, chaos engineering helps ensure the availability, reliability, and recoverability of core systems and services. To realize long-term value and competitive advantage, treat chaos engineering as a core capability and strategic imperative, not as an initiative that requires constant justification.

The following diagram shows the evolution of chaos engineering from the grass roots to goals and ROI, to becoming a strategy.

![Evolution starting with grassroots efforts, to goals, to ROI, to necessary strategy.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-chaos-engineering-journey/images/guide-img/4a45128d-5b70-46b6-b625-98d89da7e822/images/751a9b0e-f3d0-49f3-9999-61aec10ff374.png)

At the grassroots level, individual teams typically experiment independently, driven by local needs. These experiments are championed by passionate engineers who demonstrate value through reduced incidents and improved observability.

When these efforts prove successful, teams can elevate their learning to leadership. With this visibility, efforts transition into a goals-driven phase. The organization sets formal objectives for resilience and recovery, backed by resources and support for broader implementation.

Finally, chaos engineering matures beyond requiring constant ROI justification to become recognized as a strategic necessity, similar to cybersecurity. At this stage, chaos engineering becomes fully integrated into organizational processes. Implementation focuses on long-term resilience rather than short-term metrics. Chaos engineering is treated as a core capability essential for maintaining competitive advantage and customer trust.

## Integrating chaos engineering into your organization
<a name="integration"></a>

To elevate chaos engineering to the same level of importance as security, consider the following suggestions:
+ **Establish chaos engineering as a non-negotiable practice** ‒ Just as cybersecurity is considered a fundamental requirement for organizations, view chaos engineering as a mandatory practice for ensuring system resilience and reliability. Integrate chaos engineering into your organization's processes, tools, and culture, rather than regarding it as an optional or discretionary activity. For more information, see the [Resilience lifecycle framework](https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-lifecycle-framework/introduction.html) guide.
+ **Secure executive-level buy-in and support** ‒ As with security initiatives, chaos engineering efforts must have buy-in and active support from executive leadership. This includes allocating dedicated resources, budget, and personnel to implement and sustain chaos engineering practices across the organization.
+ **Implement governance and oversight** ‒ Similar to a CISO and security governance framework, establish a dedicated chaos engineering team or a Chief Resilience Officer. This team or role is responsible for overseeing and coordinating chaos engineering efforts across different teams and business units.
+ **Integrate chaos engineering into development and operations cycles** ‒ Just as security practices are integrated into software development and deployment processes, make chaos engineering a seamless part of the software development and delivery lifecycle.
+ **Conduct regular chaos engineering drills and simulations** ‒ Similar to security breach simulations and incident response drills, conduct regular chaos engineering experiments to validate incident response capabilities and identify potential blind spots proactively.
+ **Use chaos engineering to maintain runbooks** ‒ As with conducting security reviews, use chaos engineering experiments to validate the effectiveness and accuracy of runbooks for incident response and recovery. Additionally, chaos engineering experiments can serve as realistic simulations for on-call engineers to practice executing runbook procedures. Simulations help engineers maintain their operational muscle memory and preparedness for handling real-world incidents.
+ **Foster a culture of resilience** ‒ As with security-awareness training, invest in chaos engineering education and knowledge-sharing initiatives to foster a culture of resilience. Include training programs, cross-functional collaboration, and incentives for teams that adopt chaos engineering practices.
+ **Measure and report on resilience metrics** ‒ Regularly monitor resilience metrics and report them to stakeholders. Use the quantitative and qualitative metrics discussed in this document as a starting point.
+ **Treat resilience as a competitive advantage** ‒ Cybersecurity measures can provide a competitive edge. Similarly, view your chaos engineering and resilience capabilities as a differentiator that helps you offer more reliable and trustworthy services to your customers.

## Getting executive buy-in
<a name="executive-buy-in"></a>

Chaos engineering often lacks a clear owner within the C-suite's traditional responsibilities. The CEO cares about growth, profitability, and market leadership. The CFO focuses on financial performance, cost control, and risk management. The CTO prioritizes technology strategy, product roadmaps, and engineering excellence. The CISO oversees security and compliance.

With no single executive truly owning resilience, it's often difficult to gain buy-in and support. Yet system failures impact revenue, customer satisfaction, and brand reputation, which are concerns for the CEO and CFO. The CTO and CISO are tasked with implementing resilience measures, but they might lack organizational mandate. This ambiguity can get in the way of making strategic investments and aligning the organization toward a common resilience strategy.

This ambiguity also makes it challenging to get executive buy-in for resilience initiatives such as chaos engineering. After all, C-level leaders are juggling a multitude of strategic priorities: growth, innovation, customer experience, compliance, and more.

To effectively communicate the value of chaos engineering to C-level executives, consider the following approaches:
+ **Determine the key concerns and decision drivers of your C-suite executives.**

  For example, are the C-suite executives worried about customer churn, regulatory compliance, cost reduction, or competitive pressures? Position chaos engineering as a force multiplier that aligns with the company's unique challenges and goals.
+ **Identify shared objectives and strategic outcomes.**

  How does your chaos engineering strategy support the overall organization's growth strategy, customer experience, market opportunities, and operational efficiency? Prioritize initiatives based on goals, business impact, ROI, and the risk of not doing the initiatives.
+ **Communicate the effectiveness of your chaos engineering strategy in quantifiable terms by using key resilience indicators.**

  Start with these four key resilience indicators: availability, time to detect, time to respond, and time to recover. Tie these directly to business outcomes such as revenue, cost savings, and brand reputation.
+ **Don't get lost in the technical details.**

  Focus on the overall sentiment and the measurable business impact. The C-suite cares about the outcomes that drive growth, enhance customer trust, and foster innovation.

## The prevention paradox
<a name="prevention-paradox"></a>

When faults are successfully mitigated before they manifest, it becomes challenging to convince stakeholders of the value and necessity of the preventive measures taken. This phenomenon is known as the *prevention paradox*. The prevention paradox is the biggest obstacle to integrating chaos engineering as a strategic necessity, and it stems from the inherent biases in human cognition.

The Y2K bug serves as a great illustration of this paradox. Years of preparation and billions of dollars were invested in updating computer systems worldwide. However, the smooth transition into 2000 was interpreted by many as a testament to the overblown nature of the Y2K concerns. The success of the preventive efforts undertaken was rarely recognized.

This prevention paradox continues to challenge organizations investing in chaos engineering today. When potential outages are successfully averted through proactive measures, the very absence of catastrophe can paradoxically make it difficult to justify the resources spent on prevention.

The root cause of this phenomenon lies in the way our minds are wired to process information. Human cognitive processes are geared toward responding to and remembering actual events and visible outcomes. When a disaster is prevented, there is no dramatic narrative to hold onto or share. Another aspect of the prevention paradox is hindsight bias. After a nonevent, individuals tend to conclude that nothing happened, so it wasn't a real problem. The possibility that appropriate precautions prevented a real problem isn't recognized. This psychological blind spot creates a perpetual challenge for organizations. The more successful you are at prevention and resilience, the more your efforts appear unnecessary in retrospect.

To address the prevention paradox, your organization can take specific steps to make the invisible work of prevention visible, measurable, and valued. Potential steps include the following:
+ Document and simulate what could have happened without preventive measures.
+ Share stories of events in which preventive measures averted potential disasters.
+ Point to peer organizations that did not prepare and that suffered consequences as a result.
+ Present prevention costs in the context of the potential impacts they are preventing.
+ Break down prevention efforts into visible milestones and achievements.
+ Build institutional memory on why preventive measures exist and their historical importance.
+ Regularly educate stakeholders on the value of resilience and chaos engineering practices.
