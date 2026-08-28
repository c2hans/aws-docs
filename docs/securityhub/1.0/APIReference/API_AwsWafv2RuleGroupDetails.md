---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafv2RuleGroupDetails.html
---

# AwsWafv2RuleGroupDetails
<a name="API_AwsWafv2RuleGroupDetails"></a>

 Details about an AWS WAFv2 rule group.

## Contents
<a name="API_AwsWafv2RuleGroupDetails_Contents"></a>

 ** Arn **   <a name="securityhub-Type-AwsWafv2RuleGroupDetails-Arn"></a>
 The Amazon Resource Name (ARN) of the entity.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Capacity **   <a name="securityhub-Type-AwsWafv2RuleGroupDetails-Capacity"></a>
 The web ACL capacity units (WCUs) required for this rule group.
Type: Long
Required: No

 ** Description **   <a name="securityhub-Type-AwsWafv2RuleGroupDetails-Description"></a>
 A description of the rule group that helps with identification.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Id **   <a name="securityhub-Type-AwsWafv2RuleGroupDetails-Id"></a>
 A unique identifier for the rule group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-AwsWafv2RuleGroupDetails-Name"></a>
 The name of the rule group. You cannot change the name of a rule group after you create it.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Rules **   <a name="securityhub-Type-AwsWafv2RuleGroupDetails-Rules"></a>
 The Rule statements used to identify the web requests that you want to allow, block, or count. Each rule includes one top-level statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.
Type: Array of [AwsWafv2RulesDetails](API_AwsWafv2RulesDetails.md) objects
Required: No

 ** Scope **   <a name="securityhub-Type-AwsWafv2RuleGroupDetails-Scope"></a>
 Specifies whether the rule group is for an Amazon CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB), an Amazon API Gateway REST API, an AWS AppSync GraphQL API, or an Amazon Cognito user pool.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VisibilityConfig **   <a name="securityhub-Type-AwsWafv2RuleGroupDetails-VisibilityConfig"></a>
 Defines and enables Amazon CloudWatch metrics and web request sample collection.
Type: [AwsWafv2VisibilityConfigDetails](API_AwsWafv2VisibilityConfigDetails.md) object
Required: No

## See Also
<a name="API_AwsWafv2RuleGroupDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafv2RuleGroupDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafv2RuleGroupDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafv2RuleGroupDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
