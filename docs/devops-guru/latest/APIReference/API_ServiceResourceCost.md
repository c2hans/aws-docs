---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ServiceResourceCost.html
---

# ServiceResourceCost
<a name="API_ServiceResourceCost"></a>

An object that contains information about the estimated monthly cost to analyze an AWS resource. For more information, see [Estimate your Amazon DevOps Guru costs](https://docs.aws.amazon.com/devops-guru/latest/userguide/cost-estimate.html) and [Amazon DevOps Guru pricing](http://aws.amazon.com/devops-guru/pricing/).

## Contents
<a name="API_ServiceResourceCost_Contents"></a>

 ** Cost **   <a name="DevOpsGuru-Type-ServiceResourceCost-Cost"></a>
The total estimated monthly cost to analyze the active resources for this resource.
Type: Double
Required: No

 ** Count **   <a name="DevOpsGuru-Type-ServiceResourceCost-Count"></a>
The number of active resources analyzed for this service to create a monthly cost estimate.
Type: Integer
Required: No

 ** State **   <a name="DevOpsGuru-Type-ServiceResourceCost-State"></a>
The state of the resource. The resource is `ACTIVE` if it produces metrics, events, or logs within an hour, otherwise it is `INACTIVE`. You pay for the number of active AWS resource hours analyzed for each resource. Inactive resources are not charged.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

 ** Type **   <a name="DevOpsGuru-Type-ServiceResourceCost-Type"></a>
The type of the AWS resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z]+[a-zA-Z0-9-_:]*$`
Required: No

 ** UnitCost **   <a name="DevOpsGuru-Type-ServiceResourceCost-UnitCost"></a>
The price per hour to analyze the resources in the service. For more information, see [Estimate your Amazon DevOps Guru costs](https://docs.aws.amazon.com/devops-guru/latest/userguide/cost-estimate.html) and [Amazon DevOps Guru pricing](http://aws.amazon.com/devops-guru/pricing/).
Type: Double
Required: No

## See Also
<a name="API_ServiceResourceCost_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/ServiceResourceCost)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/ServiceResourceCost)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/ServiceResourceCost)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
