---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/failure-mode-effects-analysis/appendix-service-implementations.html
---

# Appendix: AWS service-specific FMEA implementation
<a name="appendix-service-implementations"></a>

This reference guide provides example pre-analyzed failure modes for common AWS services, including Risk Priority Number (RPN) calculations and recommended mitigation strategies. Use this as a starting point for your FMEA analysis and customize based on your specific application architecture and business requirements.

## Application Load Balancer
<a name="alb"></a>

Application Load Balancer high-priority failure modes affect traffic routing and availability at the edge of your application. Health check misconfigurations can silently pull healthy targets out of rotation, expired SSL certificates can make your site unreachable, and listener rule errors can send requests to the wrong backend.

### Target health check failures
<a name="target-health-check-failures.ed99ec01-8e21-510b-9815-f67b8e8f70c9"></a>
+ **Severity**:** **8 (Service unavailability)
+ **Occurrence**:** **4 (Common with application issues)
+ **Detection**:** **5 (Detected through Application Load Balancer monitoring)
+ **RPN**: 160
+ **Root causes**:** **Application startup delays, health check endpoint issues, network connectivity
+ **Mitigation strategies**:
  + [Configure appropriate health check parameters](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/modify-health-check-settings.html)
  + Create automated target registration procedures
  + Establish health check troubleshooting guides

### SSL certificate expiration
<a name="ssl-certificate-expiration.aa10fbb1-9ad6-51a9-b61b-fc5570a7313a"></a>
+ **Severity**:** **9 (Service unavailability, security warnings)
+ **Occurrence**:** **2 (Preventable with proper management)
+ **Detection**:** **8 (Often detected too late)
+ **RPN**:** **144
+ **Root causes**:** **Manual certificate management, notification failures, renewal process gaps
+ **Mitigation strategies**:
  + [Implement automated certificate renewal (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html)
  + [Configure certificate expiration monitoring](https://docs.aws.amazon.com/acm/latest/userguide/cloudwatch-metrics.html)
  + Create certificate management procedures
  + Establish automated renewal validation

### Listener rule misconfigurations
<a name="listener-rule-misconfigurations.06dfcfd6-f9f0-5e2f-82f3-e27803b408c6"></a>
+ **Severity**:** **7 (Traffic routing issues)
+ **Occurrence**:** **4 (Common during configuration changes)
+ **Detection**:** **6 (Detected through monitoring or user reports)
+ **RPN**:** **168
+ **Root causes**:** **Manual configuration errors, rule priority conflicts, condition mismatches
+ **Mitigation strategies**:
  + Implement infrastructure as code (IaC) for Application Load Balancer configurations
  + Create listener rule validation procedures
  + Establish configuration change management
  + Configure traffic routing monitoring

## Amazon ECS
<a name="ecs"></a>

Amazon Elastic Container Service (Amazon ECS) high-priority failure modes typically involve tasks failing to launch, scaling policies not responding to load, or misconfigurations in task definitions. These issues can be difficult to detect because Amazon ECS abstracts much of the underlying infrastructure, so problems often surface as degraded application performance rather than clear infrastructure alerts.

### Tasks stuck in PENDING state
<a name="tasks-stuck-in-pending-state.6857d705-b7b2-5889-937b-b3b27559b3c4"></a>
+ **Severity**:** **8 (Service unavailable, customer impact)
+ **Occurrence**:** **4 (Monthly occurrence possible)
+ **Detection**:** **7 (Difficult to detect until customer reports)
+ **RPN**:** **224
+ **Root causes**:** **IAM permissions, resource constraints, network issues
+ **Mitigation strategies**:
  + [Implement comprehensive IAM policy reviews](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_examples.html)
  + [Configure CloudWatch alarms for task state monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html#ECS)
  + [Establish automated task replacement procedures](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html)
  + Create detailed troubleshooting runbooks

### Service auto-scaling failures
<a name="service-auto-scaling-failures.e7159395-a636-53e3-b327-7c52adf6e7c1"></a>
+ **Severity**:** **7 (Performance degradation during peak load)
+ **Occurrence**:** **3 (Quarterly occurrence)
+ **Detection**:** **6 (Detected through performance monitoring)
+ **RPN**:** **126
+ **Root causes**:** **Incorrect scaling policies, resource limits, metric delays
+ **Mitigation strategies**:
  + [Configure predictive scaling based on historical patterns](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html)
  + [Implement multiple scaling metrics (CPU, memory, custom)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/predictive-scaling-custom-metrics.html)
  + Set up load testing for scaling validation
  + Create capacity planning procedures

### Task definition misconfigurations
<a name="task-definition-misconfigurations.dc20408c-1862-58c7-b679-f69928cd5f65"></a>
+ **Severity**:** **6 (Application functionality impacted)
+ **Occurrence**:** **5 (Common during deployments)
+ **Detection**:** **5 (Detected during deployment or runtime)
+ **RPN**:** **150
+ **Root causes**:** **Manual configuration errors, missing environment variables
+ **Mitigation strategies**:
  + [Implement IaC for task definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/tutorial-ecs-web-server-cdk.html)
  + Create automated validation pipelines
  + Establish peer review processes for configuration changes
  + Use configuration management tools

## Amazon ECR
<a name="ecr"></a>

Amazon Elastic Container Registry (Amazon ECR) high-priority failure modes center on the security and availability of container images in your deployment pipeline. Vulnerability scanning gaps and unsigned images can introduce security risk that goes undetected until an audit, while image pull failures can block deployments entirely.

### Vulnerability scanning failures
<a name="vulnerability-scanning-failures.f94328fc-bc98-55cd-a51a-d44de88b2012"></a>
+ **Severity**:** **8 (Security compliance risk)
+ **Occurrence**:** **4 (Regular occurrence with new images)
+ **Detection**:** **7 (May not be detected until audit)
+ **RPN**:** **224
+ **Root causes**:** **Scanner limitations, new vulnerability databases, image complexity
+ **Mitigation strategies**:
  + [Implement multiple vulnerability scanning tools](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html)
  + [Create automated security gates in CI/CD pipelines](https://aws.amazon.com/blogs/devops/enhance-release-control-with-aws-codepipeline-stage-level-conditions/)
  + Establish vulnerability remediation procedures
  + Configure continuous monitoring for new vulnerabilities

### Malicious image deployment
<a name="malicious-image-deployment.b900932c-9ded-52a1-a91b-f715e5903e1a"></a>
+ **Severity**:** **9 (Critical security breach)
+ **Occurrence**:** **2 (Rare but possible)
+ **Detection**:** **10 (Very difficult to detect)
+ **RPN**:** **180
+ **Root causes**:** **Compromised build pipeline, insider threats, supply chain attacks
+ **Mitigation strategies**:
  + [Implement image signing and verification](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-signing.html)
  + Create secure build environments with limited access
  + Establish image provenance tracking
  + Configure runtime security monitoring

### Image pull failures during deployment
<a name="image-pull-failures-during-deployment.ef015934-12a3-53c9-8770-604872a7047b"></a>
+ **Severity**:** **7 (Deployment failures, service disruption)
+ **Occurrence**:** **3 (Occasional network or permission issues)
+ **Detection**:** **4 (Quickly detected during deployment)
+ **RPN**:** **84
+ **Root causes**:** **Network connectivity, IAM permissions, registry availability
+ **Mitigation strategies**:
  + Configure multiple registry endpoints
  + [Implement image caching strategies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache-creating-rule.html)
  + Create automated retry mechanisms
  + Establish network connectivity monitoring

## Amazon EFS
<a name="efs"></a>

Amazon Elastic File System (Amazon EFS) high-priority failure modes revolve around data protection, network connectivity, and performance configuration. Backup failures are particularly high risk because they often go undetected until a restore is needed.

### Backup failures
<a name="backup-failures.f6a41031-db51-51fc-b36d-a6114df88678"></a>
+ **Severity**:** **9 (Data loss risk)
+ **Occurrence**:** **3 (Possible with configuration issues)
+ **Detection**:** **7 (May not be detected until restore needed)
+ **RPN**:** **189
+ **Root causes**:** **IAM permission issues, backup policy misconfigurations, storage constraints
+ **Mitigation strategies**:
  + [Implement automated backup validation procedures](https://aws.amazon.com/blogs/storage/implementing-restore-testing-for-recovery-validation-using-aws-backup/)
  + Configure multiple backup strategies (AWS Backup, custom scripts)
  + [Establish backup monitoring and alerting](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-best-practices/monitor-alert.html)

### Mount target connectivity issues
<a name="mount-target-connectivity-issues.689e6e27-fa2f-5e60-86df-a7e75040d798"></a>
+ **Severity**:** **8 (File system unavailable)
+ **Occurrence**:** **2 (Rare network issues)
+ **Detection**:** **6 (Detected through application errors)
+ **RPN**:** **96
+ **Root causes**:** **Network connectivity, security group misconfigurations, DNS resolution issues
+ **Mitigation strategies**:
  + [Configure multiple mount targets across Availability Zones](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html)
  + [Implement network connectivity monitoring](https://docs.aws.amazon.com/efs/latest/ug/efs-metrics.html)
  + Create automated mount target health checks
  + Establish network troubleshooting procedures

### Performance mode misconfigurations
<a name="performance-mode-misconfigurations.ed1b8d95-1cce-5483-91d0-7d0ccadf89e7"></a>
+ **Severity**:** **6 (Performance impact)
+ **Occurrence**:** **4 (Common during initial setup)
+ **Detection**:** **5 (Detected through performance monitoring)
+ **RPN**:** **120
+ **Root causes**:** **Incorrect performance mode selection, throughput mode misconfigurations
+ **Mitigation strategies**:
  + Implement performance testing during setup
  + Create performance mode selection guidelines
  + [Configure performance monitoring and alerting](https://docs.aws.amazon.com/efs/latest/ug/creating_alarms.html)
  + Establish performance optimization procedures

## Amazon RDS
<a name="rds"></a>

Amazon Relational Database Service (Amazon RDS) high-priority failure modes span licensing, storage, performance, and configuration. Because the database layer underpins most application functionality, failures here tend to score high on severity.

### Oracle license compliance violations
<a name="oracle-license-compliance-violations.241ae279-c24e-5c59-9531-b03970792860"></a>
+ **Severity**:** **8 (Legal and financial risk)
+ **Occurrence**:** **3 (Possible during scaling events)
+ **Detection**:** **8 (Difficult to detect without proper monitoring)
+ **RPN**:** **192
+ **Root causes**:** **Auto-scaling beyond license limits, manual instance modifications, license tracking gaps
+ **Mitigation strategies**:
  + Implement automated license usage monitoring
  + Configure scaling limits based on license capacity
  + Create license compliance dashboards
  + Establish regular license audit procedures

### Database storage exhaustion
<a name="database-storage-exhaustion.1cce2947-fd7b-5239-a88a-32059cb3c8a6"></a>
+ **Severity**:** **9 (Complete database unavailability)
+ **Occurrence**:** **2 (Rare with proper monitoring)
+ **Detection**:** **10 (Often detected too late)
+ **RPN**:** **180
+ **Root causes**:** **Unexpected data growth, failed cleanup procedures, monitoring gaps
+ **Mitigation strategies**:
  + [Enable storage auto-scaling with appropriate thresholds](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.Autoscaling.html)
  + [Implement proactive storage monitoring and alerting](https://aws.amazon.com/blogs/database/build-proactive-database-monitoring-for-amazon-rds-with-amazon-cloudwatch-logs-aws-lambda-and-amazon-sns/)
  + Create automated data archival procedures
  + Establish capacity planning processes

### Performance degradation
<a name="performance-degradation.8b1f10a1-3d30-599f-851e-771114118d94"></a>
+ **Severity**:** **7 (Application slowness, user impact)
+ **Occurrence**:** **4 (Common during peak usage)
+ **Detection**:** **6 (Detected through performance monitoring)
+ **RPN**:** **168
+ **Root causes**:** **Query inefficiencies, resource constraints, parameter misconfigurations
+ **Mitigation strategies**:
  + [Enable Performance Insights monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Enabling.html)
  + Implement automated query optimization
  + [Configure read replicas for read-heavy workloads](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
  + Create performance baseline and alerting

### Parameter group misconfigurations
<a name="parameter-group-misconfigurations.9a511c20-27b7-5def-b609-15bf67679869"></a>
+ **Severity**:** **7 (Performance or functionality issues)
+ **Occurrence**:** **4 (Common during configuration changes)
+ **Detection**:** **6 (Detected through monitoring or testing)
+ **RPN**:** **168
+ **Root causes**:** **Manual configuration errors, incompatible parameter combinations, version upgrade issues
+ **Mitigation strategies**:
  + Implement IaC for parameter groups
  + Create parameter validation and testing procedures
  + Establish configuration change management processes
  + Configure automated rollback capabilities

## Route 53
<a name="route53"></a>

Amazon Route 53 failure modes are high-severity because DNS sits at the front of every request path. A misconfigured failover policy or a false-positive health check can make your entire application unreachable or silently route traffic to an unhealthy endpoint. These issues are rare but difficult to detect before customers are affected.

### DNS failover mechanism failures
<a name="dns-failover-mechanism-failures.f2c659d4-c982-5e6f-9545-71b00f998d51"></a>
+ **Severity**: 9 (Complete service unavailability)
+ **Occurrence**: 3 (Rare but critical)
+ **Detection**: 8 (Difficult to detect until customer impact)
+ **RPN**: 216
+ **Root causes**:** **Health check misconfigurations, DNS propagation delays, routing policy errors
+ **Mitigation strategies**:
  + [Implement synthetic monitoring from multiple locations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html)
  + [Configure redundant health checks with different criteria](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-cloudwatch.html)
  + [Establish automated DNS failover testing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring.html)
  + Create geographic routing validation procedures

### Health check false positives or negatives
<a name="health-check-false-positives-or-negatives.ae565fbf-93f5-56ef-93b5-a822f3f54021"></a>
+ **Severity**:** **8 (Unnecessary failovers or missed failures)
+ **Occurrence**:** **4 (Common with complex health checks)
+ **Detection**:** **5 (Detected through monitoring)
+ **RPN**:** **160
+ **Root causes**:** **Network latency, application-specific health check logic, timeout configurations
+ **Mitigation strategies**:
  + [Configure multiple health check types (HTTP, TCP, calculated)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-cloudwatch.html)
  + Implement application-specific health endpoints
  + Set appropriate timeout and retry values
  + Create health check validation procedures

### Latency-based routing misconfigurations
<a name="latency-based-routing-misconfigurations.1f12eba5-17d0-5e02-b9ba-90e5d52ee1b1"></a>
+ **Severity**:** **6 (Suboptimal user experience)
+ **Occurrence**:** **4 (Common during configuration changes)
+ **Detection**:** **6 (Detected through performance monitoring)
+ **RPN**:** **144
+ **Root causes**:** **Incorrect latency measurements, routing policy conflicts, geographic misconfigurations
+ **Mitigation strategies**:
  + Implement continuous latency monitoring
  + Create routing policy validation procedures
  + Establish A/B testing for routing changes
  + Configure automated rollback mechanisms

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
