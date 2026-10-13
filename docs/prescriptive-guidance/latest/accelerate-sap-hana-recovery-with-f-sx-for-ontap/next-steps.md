---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/next-steps.html
---

# Next steps
<a name="next-steps"></a>

This guide covered implementing snapshot-based SAP HANA backups using

## Immediate actions
<a name="immediate-actions.9073ff3a-c03e-5310-b561-b202edea99c2"></a>

1. **Assess your current state**: Evaluate whether your existing backup environment meets your RPO/RTO targets. Calculate your current backup window duration, storage costs, and recovery testing frequency.

1. **Engage AWS and Commvault**: Contact your AWS account team or visit the [AWS Partner Network](https://aws.amazon.com/partners/) to connect with Commvault specialists who can assess your specific requirements and provide sizing guidance.

1. **Design your architecture**: Work with AWS Solutions Architects to plan:
   + Infrastructure sizing based on your database footprint
   + Dual-account architecture and network connectivity
   + Commvault infrastructure placement and scaling

## Validation phase
<a name="validation-phase.4cdd1390-4959-51df-85f5-2efde86bf814"></a>

1. **Conduct proof-of-concept: **Follow the step-by-step implementation in this guide to validate performance and recovery results in a non-production environment.

1. **Measure results**: Compare POC results against current backup performance across backup window reduction, storage efficiency, recovery time, and operational overhead.

## Production rollout
<a name="production-rollout.a486d914-8186-575c-a084-fae67dfa8687"></a>

1. **Phased migration**: Implement for non-production SAP HANA systems first, then gradually migrate production instances based on validated success criteria.

1. **Establish operations**: Configure Amazon CloudWatch alarms, Commvault monitoring, and establish the quarterly DR testing cadence outlined in the Monitoring and Maintenance section.
