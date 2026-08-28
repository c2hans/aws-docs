---
source_url: https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/comparison-of-blue-green-deployment-techniques.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix: Comparison of Blue/Green Deployment Techniques
<a name="comparison-of-blue-green-deployment-techniques"></a>

 The following table offers an overview and comparison of the different blue/green deployment techniques discussed in this paper. The risk potential is evaluated from desirable lower risk (X) to less desirable higher risk (XXX).

- ** Update DNS Routing with Amazon Route 53 **
  - **Risk Category:**  Application Issues  / **Risk Potential:** X / **Reasoning:**  Facilitates canary analysis
  - **Risk Category:**  Application Performance  / **Risk Potential:** X / **Reasoning:**  Gradual switch, traffic split management
  - **Risk Category:**  People/Process Errors  / **Risk Potential:** XX / **Reasoning:**  Depends on automation framework, overall simple process
  - **Risk Category:**  Infrastructure Failures  / **Risk Potential:** XX / **Reasoning:**  Depends on automation framework
  - **Risk Category:**  Rollback  / **Risk Potential:** XXX / **Reasoning:**  DNS TTL complexities (reaction time, flip/flop)
  - **Risk Category:**  Cost  / **Risk Potential:** X / **Reasoning:**  Optimized via Auto Scaling

- ** Swap the Auto Scaling group behind Elastic Load Balancer **
  - **Risk Category:**  Application Issues  / **Risk Potential:** X / **Reasoning:**  Facilitates canary analysis
  - **Risk Category:**  Application Performance  / **Risk Potential:** XX / **Reasoning:**  Less granular traffic split management, already warm load balancer
  - **Risk Category:**  People/Process Errors  / **Risk Potential:** XX / **Reasoning:**  Depends on automation framework
  - **Risk Category:**  Infrastructure Failures  / **Risk Potential:** X / **Reasoning:**  Auto Scaling
  - **Risk Category:**  Rollback  / **Risk Potential:** X / **Reasoning:**  No DNS complexities
  - **Risk Category:**  Cost  / **Risk Potential:** X / **Reasoning:**  Optimized via Auto Scaling

- ** Update Auto Scaling Group launch configurations **
  - **Risk Category:**  Application Issues  / **Risk Potential:** XXX / **Reasoning:**  Detection of errors/issues in a heterogeneous fleet is complex
  - **Risk Category:**  Application Performance  / **Risk Potential:** XXX / **Reasoning:**  Less granular traffic split, initial traffic load
  - **Risk Category:**  People/Process Errors  / **Risk Potential:** XX / **Reasoning:**  Depends on automation framework
  - **Risk Category:**  Infrastructure Failures  / **Risk Potential:** X / **Reasoning:**  Auto Scaling
  - **Risk Category:**  Rollback  / **Risk Potential:** X / **Reasoning:**  No DNS complexities
  - **Risk Category:**  Cost  / **Risk Potential:** XX / **Reasoning:**  Optimized via Auto Scaling, but initial scale-out overprovisions

- ** Swap the environment of an Elastic Beanstalk application **
  - **Risk Category:**  Application Issues  / **Risk Potential:** XX / **Reasoning:**  Ability to do canary analysis ahead of cutover, but not with production traffic
  - **Risk Category:**  Application Performance  / **Risk Potential:** XXX / **Reasoning:**  Full cutover
  - **Risk Category:**  People/Process Errors  / **Risk Potential:** X / **Reasoning:**  Simple process, automated
  - **Risk Category:**  Infrastructure Failures  / **Risk Potential:** X / **Reasoning:**  Auto Scaling, CloudWatch monitoring, Elastic Beanstalk health reporting
  - **Risk Category:**  Rollback  / **Risk Potential:** XXX / **Reasoning:**  DNS TTL complexities
  - **Risk Category:**  Cost  / **Risk Potential:** XX / **Reasoning:**  Optimized via Auto Scaling, but initial scale-out may overprovision

- ** Clone a stack in OpsWorks and update DNS **
  - **Risk Category:**  Application Issues  / **Risk Potential:** X / **Reasoning:**  Facilitates canary analysis
  - **Risk Category:**  Application Performance  / **Risk Potential:** X / **Reasoning:**  Gradual switch, traffic split management
  - **Risk Category:**  People/Process Errors  / **Risk Potential:** X / **Reasoning:**  Highly automated
  - **Risk Category:**  Infrastructure Failures  / **Risk Potential:** X / **Reasoning:**  Auto-healing capability
  - **Risk Category:**  Rollback  / **Risk Potential:** XXX / **Reasoning:**  DNS TTL complexities
  - **Risk Category:**  Cost  / **Risk Potential:** XXX / **Reasoning:**  Dual stack of resources

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
