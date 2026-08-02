---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-formation-version-control-guide/targeted-business-outcomes.html
---

# Targeted business outcomes
<a name="targeted-business-outcomes"></a>

The approach in this guide helps organizations achieve the following outcomes.

## Feature release management
<a name="feature-release-management"></a>

Use version-specific deployments to roll out new features to isolated environments before promoting to production. This approach reduces release risk and provides early feedback from select customers. For example, you can deploy a commit tagged preview-20230725-008 to an isolated environment for early customer validation while production remains on a stable release.

## Incident response
<a name="incident-response"></a>

Deploy hotfixes rapidly by tagging specific commits for expedited promotion to production. This reduces mean time to recovery (MTTR) and minimizes the testing overhead for critical fixes. Teams can create a hotfix branch, tag it (for example, v1.0.1-hotfix), and deploy through an expedited approval process.

## Sales and demo operations
<a name="sales-and-demo-operations"></a>

Create ephemeral environments on demand by deploying specific version tags for client demonstrations. This accelerates the sales cycle without affecting production stability. Sales teams can request exact product versions spun up for prospect engagements.

## Compliance and audit readiness
<a name="compliance-and-audit-readiness"></a>

Reference specific commit IDs to verify point-in-time infrastructure configurations during audits. For example, an auditor can request the configuration state at prod-20240701-010 and the team can reproduce that exact infrastructure state. This simplifies compliance verification and provides a complete audit trail.

## A/B testing infrastructure
<a name="a-b-testing-infrastructure"></a>

Deploy parallel variants of infrastructure by using different version tags (for example, preprod-20230710-011A and preprod-20230710-011B) to compare performance. This supports data-driven decisions for feature implementations.
