---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ServiceHealth.html
---

# ServiceHealth
<a name="API_ServiceHealth"></a>

Represents the health of an AWS service.

## Contents
<a name="API_ServiceHealth_Contents"></a>

 ** AnalyzedResourceCount **   <a name="DevOpsGuru-Type-ServiceHealth-AnalyzedResourceCount"></a>
 Number of resources that DevOps Guru is monitoring in an analyzed AWS service.
Type: Long
Required: No

 ** Insight **   <a name="DevOpsGuru-Type-ServiceHealth-Insight"></a>
Represents the health of an AWS service. This is a `ServiceInsightHealth` that contains the number of open proactive and reactive insights for this service.
Type: [ServiceInsightHealth](API_ServiceInsightHealth.md) object
Required: No

 ** ServiceName **   <a name="DevOpsGuru-Type-ServiceHealth-ServiceName"></a>
The name of the AWS service.
Type: String
Valid Values: `API_GATEWAY | APPLICATION_ELB | AUTO_SCALING_GROUP | CLOUD_FRONT | DYNAMO_DB | EC2 | ECS | EKS | ELASTIC_BEANSTALK | ELASTI_CACHE | ELB | ES | KINESIS | LAMBDA | NAT_GATEWAY | NETWORK_ELB | RDS | REDSHIFT | ROUTE_53 | S3 | SAGE_MAKER | SNS | SQS | STEP_FUNCTIONS | SWF`
Required: No

## See Also
<a name="API_ServiceHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/ServiceHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/ServiceHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/ServiceHealth)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
