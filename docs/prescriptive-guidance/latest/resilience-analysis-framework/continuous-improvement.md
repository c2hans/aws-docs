---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-analysis-framework/continuous-improvement.html
---

# Continuous improvement
<a name="continuous-improvement"></a>

Resilience is a [continuous process](https://medium.com/the-cloud-architect/towards-continuous-resilience-3c7fbc5d232b). Over your system's lifecycle, the environment in which it operates will change. To ensure that your system remains resilient, you should integrate the framework into your periodic operational and architectural reviews. You might find new failure modes that you didn't identify the first time through, or there might be new or previously unthought of mitigations that you can put in place. Resilience analysis should be an iterative process and not a one-time exercise.

You should empirically test your mitigation strategies with processes such as [chaos engineering](https://aws.amazon.com/solutions/resilience/chaos-engineering/) or [game days](https://aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.gameday.en.html) to validate that they work as expected. If you don't have a rigorous testing mechanism, you won't be confident that the mitigation will work as expected when you need it. During resilience analysis, you might determine that a failure mode is already handled by a specific mitigation, but it's important to test those assumptions as well. You should test for both existing mitigations and new mitigations that were created by using the resilience analysis framework.

You should also evaluate how well you performed the analysis through team retrospectives. Did everyone know what they were working on during the analysis? Did the number of failure modes you found through resilience analysis align with the team's expectations? Could you identify mitigations for all  the failure modes you discovered? Did the team find the process useful? Do you believe it will lead to improvements in the resilience of your workload?

When real failure events happen that impact your workload's availability, record the specific failure mode, the components that were part of the failure, and the mitigation pattern that was used. Make this metadata searchable in your post-incident analysis tool so you can determine which failure modes and components to focus on in the future. Throughout this process, you can engage your AWS account team and solutions architects.
