---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_UsagePlan.html
---

# UsagePlan
<a name="API_UsagePlan"></a>

Represents a usage plan used to specify who can assess associated API stages. Optionally, target request rate and quota limits can be set. In some cases clients can exceed the targets that you set. Don’t rely on usage plans to control costs. Consider using [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) to monitor costs and [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) to manage API requests.

## Contents
<a name="API_UsagePlan_Contents"></a>

 ** apiStages **   <a name="apigw-Type-UsagePlan-apiStages"></a>
The associated API stages of a usage plan.
Type: Array of [ApiStage](API_ApiStage.md) objects
Required: No

 ** description **   <a name="apigw-Type-UsagePlan-description"></a>
The description of a usage plan.
Type: String
Required: No

 ** id **   <a name="apigw-Type-UsagePlan-id"></a>
The identifier of a UsagePlan resource.
Type: String
Required: No

 ** name **   <a name="apigw-Type-UsagePlan-name"></a>
The name of a usage plan.
Type: String
Required: No

 ** productCode **   <a name="apigw-Type-UsagePlan-productCode"></a>
The AWS Marketplace product identifier to associate with the usage plan as a SaaS product on the AWS Marketplace.
Type: String
Required: No

 ** quota **   <a name="apigw-Type-UsagePlan-quota"></a>
The target maximum number of permitted requests per a given unit time interval.
Type: [QuotaSettings](API_QuotaSettings.md) object
Required: No

 ** tags **   <a name="apigw-Type-UsagePlan-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map
Required: No

 ** throttle **   <a name="apigw-Type-UsagePlan-throttle"></a>
A map containing method level throttling information for API stage in a usage plan.
Type: [ThrottleSettings](API_ThrottleSettings.md) object
Required: No

## See Also
<a name="API_UsagePlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/UsagePlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/UsagePlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/UsagePlan)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
