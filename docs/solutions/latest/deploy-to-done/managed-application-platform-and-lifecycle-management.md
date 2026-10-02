---
source_url: https://docs.aws.amazon.com/solutions/latest/deploy-to-done/managed-application-platform-and-lifecycle-management.html
---

# Managed Application Platform and Lifecycle Management
<a name="managed-application-platform-and-lifecycle-management"></a>

Elastic Beanstalk accepts your application as source code, a Dockerfile, or a pre-built container image, and takes ongoing operational responsibility for the running environment. You define the application. AWS handles deploying, scaling, patching, monitoring, and upgrading the platform underneath it. That responsibility does not expire, does not require renewal, and does not shift back to you when the platform evolves.

**What AWS takes responsibility for:**
+ **Deployment orchestration:** Rolling updates with health-aware progression and automatic rollback on failure. A release either succeeds completely or gets reversed automatically.
+ **Scaling:** Auto-scaling responds to application-level signals (request rate, queue depth, resource utilization), not static thresholds configured once and forgotten.
+ **Patching:** OS patches, runtime updates, and security fixes applied on a managed schedule during configurable maintenance windows. Immutable deployment mechanism ensures zero-downtime patching.
+ **Health monitoring:** Continuous monitoring with automated response to degradation. Health events are detected, responded to, and documented automatically.
+ **Platform lifecycle:** Infrastructure upgrades happen without migration plans or maintenance sprints. Your application continues running while the platform evolves underneath it.
+ **AI-powered troubleshooting:** Environment analysis identifies root causes and suggests remediation, reducing mean time to resolution for application issues.

**What you retain control over:**
+ Application code and dependencies
+ Environment configuration (instance type, environment variables, secrets)
+ Deployment timing (you trigger deploys; the platform executes them safely)
+ Scaling boundaries (you set min/max; the platform manages within those bounds)
+ Maintenance window scheduling

**Two Deployment Models**

Elastic Beanstalk offers two deployment models. Both share the same application-centric interface and the same operational promise. The difference is how the underlying infrastructure is organized:

**Two Deployment Models**

| Dimension | Standard Mode | Cluster Mode |
| --- | --- | --- |
| Best for | Windows/.NET Framework workloads on IIS, applications that cannot be containerized, teams that want one dedicated environment per application | Multiple applications that benefit from shared infrastructure, teams consolidating a growing application portfolio |
| Infrastructure model | Each application gets its own dedicated compute resources | Multiple applications share infrastructure automatically for better efficiency |
| Deployment speed | Standard provisioning per deployment cycle | Fast one-time initial setup, then significantly faster subsequent deployments |
| Scaling signals | Infrastructure-level metrics (CPU, network) | Application-level signals (request rate, queue depth) |
| Cost model | Pay for dedicated resources per environment | Shared infrastructure: cost per application decreases as portfolio grows |
| Supported inputs | Source code in supported runtimes (Java, Python, Node.js, Ruby, PHP, Go, .NET) | Source code, Dockerfiles, or pre-built container images: any Linux runtime |
| Observability | CloudWatch integration for metrics, logs, health | Built-in OpenTelemetry with native CloudWatch and third-party compatibility |

Scaling signals are specific to each deployment mode and cannot be mixed across modes. Standard Mode scales on infrastructure metrics; Cluster Mode scales on application-level signals.

Both models are production-grade. Standard Mode remains the right choice for Windows/.NET Framework workloads on IIS and for teams that want one dedicated environment per application, where dedicated instances also satisfy per-instance Windows licensing requirements.

## Go Deeper
<a name="managed-application-platform-go-deeper"></a>

**Go Deeper**
[Managed Platform Updates](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-platform-update-managed.html) - How automatic patching works
[Troubleshooting with AI Analysis in AWS Elastic Beanstalk](https://aws.amazon.com/blogs/devops/troubleshooting-environment-with-ai-analysis-in-aws-elastic-beanstalk/) - AI-powered environment diagnostics
[Deploying with Docker Containers to Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/docker-platform.html) - Container platform branches
[AWS Elastic Beanstalk Introduces Cluster Mode (AWS News Blog)](https://aws.amazon.com/blogs/aws/aws-elastic-beanstalk-introduces-cluster-mode/) - Cluster Mode overview and first look
[Elastic Beanstalk Compliance Validation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/compliance-validation.html) - HIPAA, PCI, SOC, FedRAMP eligibility
