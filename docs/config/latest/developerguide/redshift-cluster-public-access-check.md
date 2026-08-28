---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/redshift-cluster-public-access-check.html
---

# redshift-cluster-public-access-check
<a name="redshift-cluster-public-access-check"></a>

Checks whether Amazon Redshift clusters are not publicly accessible. The rule is NON\_COMPLIANT if the publiclyAccessible field is true in the cluster configuration item.

**Identifier:** REDSHIFT\_CLUSTER\_PUBLIC\_ACCESS\_CHECK

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Mexico (Central) Region

**Parameters:**

None

## Proactive Evaluation
<a name="w2aac20c16c17b7e1305c19"></a>

 For steps on how to run this rule in proactive mode, see [Evaluating Your Resources with AWS Config Rules](./evaluating-your-resources.html#evaluating-your-resources-proactive). For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API needs to include the following inputs, encoded as a string:

```
"ResourceConfiguration":
...
{
   "PubliclyAccessible": {{BOOLEAN}}
}
...
```

 For more information on proactive evaluation, see [Evaluation Mode](./evaluate-config-rules.html).

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1305c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
