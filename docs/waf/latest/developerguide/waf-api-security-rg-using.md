---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-rg-using.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Adding the API Security managed rule group to your protection pack (web ACL)

This section explains how to add and configure the `AWSManagedRulesAPISecurityRuleSet` rule group.

The API Security managed rule group doesn't require a configuration of its own. You add it with a managed rule group reference statement. It doesn't require you to describe your application's endpoints or responses, and it doesn't require the application integration SDKs. For the rule group description and rules listing, see [AWS WAF API Security rule group](aws-managed-rule-groups-api-security.md).

This guidance is intended for users who know generally how to create and manage AWS WAF protection packs (web ACLs), rules, and rule groups. Those topics are covered in earlier sections of this guide. For basic information about how to add a managed rule group to your protection pack (web ACL), see [Adding a managed rule group to a protection pack (web ACL) through the console](waf-using-managed-rule-group.md).

## Follow best practices
<a name="waf-api-security-rg-using-best-practices"></a>

Use the API Security rule group in accordance with the best practices at [Best practices for intelligent threat mitigation in AWS WAF](waf-managed-protections-best-practices.md).

## Prerequisites
<a name="waf-api-security-rg-using-prerequisites"></a>

Before you add the rule group, make sure you have the following:
+ **A protection pack (web ACL) associated with a supported resource type.** The API Security rule group is supported for Amazon CloudFront distributions, Application Load Balancers, and Amazon API Gateway REST APIs.
+ **Traffic reaching the endpoints you want to protect.** The behavioral detections learn from the traffic that the rule group evaluates, so they provide no coverage until a baseline has formed. Plan to add the rule group in count mode and leave it there while the baseline establishes.

You don't need to provide a login endpoint, response inspection criteria, or the AWS WAF JavaScript and mobile application integration SDKs.

## Add the rule group
<a name="waf-api-security-rg-using-adding"></a>

**To use the `AWSManagedRulesAPISecurityRuleSet` rule group in your protection pack (web ACL)**

1. Add the AWS managed rule group `AWSManagedRulesAPISecurityRuleSet` to your protection pack (web ACL), and edit the rule group settings before saving. For the full rule group description, see [AWS WAF API Security rule group](aws-managed-rule-groups-api-security.md).
**Note**
You are charged additional fees when you use this managed rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/).

1. Set the rule actions to count. Do this for your first deployment even though several rules default to Block, so that you can review what the rule group detects on your own traffic before any of it is blocked. Override the action of each rule that blocks by default, rather than the rule group's override action (`OverrideAction` in the rule group statement). A rule group override action of Count doesn't change how the rule group evaluates a request, so evaluation stops at the first rule that would block, and later rules don't add their labels. For the rules and their default actions, see [AWS WAF API Security rule group](aws-managed-rule-groups-api-security.md). For how to set rule action overrides, see [Overriding rule actions in a rule group](web-acl-rule-group-settings.md#web-acl-rule-group-rule-action-override).

1. Add a scope-down statement for the rule group to limit the requests that the rule group evaluates. Scope it to the paths that serve your APIs, so that requests for static content and your web front end aren't evaluated.

   For this rule group, a scope-down statement also narrows what the behavioral detections can learn from. Traffic you exclude is excluded from the baseline as well as from billing. Scope to the endpoints you want to protect, rather than to a sample of them.

1. Select a rule group version, or leave it at the default to use the latest.

1. Save your changes to the protection pack (web ACL).

## Where to place the rule group in your rule order
<a name="waf-api-security-rg-using-order"></a>

AWS WAF evaluates the rules in a protection pack (web ACL) in priority order. A rule with a terminating action ends evaluation for that request. Placement determines both what the rule group protects and what it can learn from. For this rule group, placement matters more than it does for signature-based rule groups.

**Place rules that consume API Security labels after the rule group.** Labels are added as the rule group evaluates a request and are available only to rules that run later in the same protection pack (web ACL). A label match rule placed before the rule group never matches. This includes any rate-based rule that aggregates on an API Security label.

**Understand what you lose by terminating traffic earlier.** Any request terminated by an earlier rule is never evaluated by the API Security rule group, so it is absent from the behavioral baseline as well as unprotected. For a rule group whose detections are built on a learned pattern of normal activity, that is a larger consequence than it would be for a signature-based rule group.

This gives you a trade-off to make deliberately rather than by accident:
+ **Placing broad controls first**, such as an IP reputation rule group, a geographic match, or a volumetric rate-based rule, sheds unwanted traffic before you pay to evaluate it. This is usually the right choice for traffic that is clearly not a legitimate API client.
+ **Placing the API Security rule group before a control that would block real API clients** keeps those clients in the baseline. If you block a category of client that does use your APIs, consider whether you want the rule group to see that traffic first.

**Baseline managed rule groups can go before API Security.** The core rule set and the known bad inputs rule set match on exploit signatures in a single request. A request carrying a SQL injection payload isn't the behavioral evidence that API Security needs, so terminating it first costs little and reduces what you are billed for.

**Consider the overlap with Fraud Control.** Account takeover prevention (ATP) inspects credentials submitted in the body of login requests. API Security detects credential stuffing against credentials sent in the Authorization header. Each covers credentials the other doesn't read. If you run both on the same login endpoint, decide which one you want to act on that traffic, and use a scope-down statement on one of them so that you aren't blocking the same requests twice from two rule groups.

Before you deploy your API Security implementation for production traffic, test and tune it in a staging or testing environment until you are comfortable with the potential impact to your traffic. Then test and tune the rules in count mode with your production traffic before enabling them. See the sections that follow for guidance.
