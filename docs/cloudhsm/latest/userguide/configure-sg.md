---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-sg.html
---

# Review the security group for your cluster in AWS CloudHSM
<a name="configure-sg"></a>

 When you create a cluster or add an HSM to a cluster, AWS CloudHSM creates a security group with the name `cloudhsm-cluster-{{<clusterID>}}-sg` if one doesn't already exist. This security group contains a preconfigured TCP rule that allows inbound and outbound communication within the cluster security group over ports 2223-2225. This SG allows your EC2 instances to use your VPC to talk to HSMs in your cluster.

**Warning**
 Do not delete or modify the preconfigured TCP rule, which is populated in the cluster security group. This rule can prevent connectivity issues and unauthorized access to your HSMs.
 The cluster security group prevents unauthorized access to your HSMs. Anyone that can access instances in the security group can access your HSMs. Most operations require a user to log in to the HSM. However, it's possible to zeroize HSMs without authentication, which destroys the key material, certificates, and other data. If this happens, data created or modified after the most recent backup is lost and unrecoverable. To prevent unauthorized access, ensure that only trusted administrators can modify or access the instances in the default security group.
 The hsm2m.medium clusters introduces mTLS feature to restrict unauthorized users from connecting to the cluster. Unauthorized users will require a valid mTLS credentials to successfully connect to cluster before attempting zeroization.

 In the next step, you can [launch an Amazon EC2 instance](launch-client-instance.md) and connect it to your HSMs by [attaching the cluster security group](configure-sg-client-instance.md) to it.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
