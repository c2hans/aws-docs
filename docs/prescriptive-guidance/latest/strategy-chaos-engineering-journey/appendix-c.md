---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-chaos-engineering-journey/appendix-c.html
---

# Appendix C ‒ Incident classification
<a name="appendix-c"></a>

Tracking incidents within a classification framework is crucial because the framework provides a holistic view of failure types and issues that impact the system. If your organization tracks incidents only within a single class, such as infrastructure faults, you might miss insights and opportunities for improvement in other areas. By tracking incidents across multiple classes, you gain a better understanding of the diverse range of chaos experiments to conduct. This perspective helps identify potential blind spots and supports expansion of the engineering scope, which leads to a more resilient and fault-tolerant system.

The suggested incident classification framework is designed to help categorize incidents based on their nature and potential impact. It uses a high-level classification that groups incidents into eight main categories:
+ **Deployment issues**:
  + Failed deployments
  + Rollback failures
  + Configuration issues during deployment
+ **Software bugs and regressions**:
  + Functional bugs
  + Integration issues
  + Performance issues
  + Quota issues
  + Resilience mechanism issues (retries, timeouts)
  + Data integrity issues
+ **Testing issues**:
  + Missing tests
  + Ineffective tests
  + Flaky tests
+ **Infrastructure faults**:
  + Hardware failures (servers, network devices, storage)
  + Scaling issues
  + Dependency failures (third-party services, APIs)
  + Network connectivity issues
+ **Operational issues**:
  + Human errors (misconfiguration, accidental changes)
  + Monitoring and alerting failures
  + Capacity planning issues
  + Backup and restore failures
+ **Security incidents**:
  + Unauthorized access attempts
  + Data breaches
  + Denial of service (DoS) attacks
+ **Third-party service outages**:
  + Cloud provider outages
  + DNS failures
  + External API and service disruptions
+ **Environmental factors**:
  + Natural disasters (earthquakes, fires, floods, power outages)
  + Weather-related issues

This is a nonconclusive example classification framework that you can tailor to fit your specific needs and organization. We recommend reviewing and updating the classification framework periodically as your system evolves or new types of incidents emerge.
