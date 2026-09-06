---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-control-tower/high-level-steps.html
---

# High-level steps for the transition
<a name="high-level-steps"></a>

When deploying AWS Control Tower in an existing organization, be sure to check the existing quotas for AWS Organizations where you have AWS Landing Zone deployed. For more information about using an existing organization, see the [AWS documentation](https://docs.aws.amazon.com/controltower/latest/userguide/existing-orgs.html).

Enroll existing AWS accounts in AWS Control Tower by registering the organizational unit (OU) using the [Register OU](https://docs.aws.amazon.com/controltower/latest/userguide/how-to-register-existing-ou.html) feature.

After enrollment, check the new AWS Control Tower [guardrails](https://docs.aws.amazon.com/controltower/latest/userguide/guardrails.html) to confirm that guardrails aren't blocking another resource that you want to use.

Deploy the [Customizations for AWS Control Tower](https://aws.amazon.com/solutions/implementations/customizations-for-aws-control-tower/) solution to integrate existing baseline CloudFormation templates or service control policies (SCPs).

Decommission the resources deployed by the AWS Landing Zone solution where applicable.
