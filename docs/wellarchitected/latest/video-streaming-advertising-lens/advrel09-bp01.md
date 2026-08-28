---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel09-bp01.html
---

# ADVREL09-BP01 Implement redundant ad-verification systems with automated failover mechanisms
<a name="advrel09-bp01"></a>

 Implement redundant ad-verification systems with automated failover capabilities. Use multiple verification providers and automated monitoring for continuous, reliable advertising measurement and validation.

## Implementation guidance
<a name="implementation-guidance-advrel09-bp01"></a>
+  Deploy multiple third-party verification providers for cross-validation
+  Implement automated failover mechanisms for measurement systems
+  Use data quality checks and anomaly detection
+  Maintain backup measurement methodologies
+  Configure automated retry mechanisms for failed measurements
+  Implement circuit breakers for degraded third-party services
+  Set up monitoring and alerting for measurement system health

## Key AWS services
<a name="aws-key-services-3"></a>
+  Amazon CloudWatch
+  AWS Lambda
+  Amazon EventBridge
+  AWS Step Functions
+  Amazon DynamoDB

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
