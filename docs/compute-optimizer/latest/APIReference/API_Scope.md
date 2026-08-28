---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_Scope.html
---

# Scope
<a name="API_Scope"></a>

Describes the scope of a recommendation preference.

Recommendation preferences can be created at the organization level (for management accounts of an organization only), account level, and resource level. For more information, see [Activating enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the * AWS Compute Optimizer User Guide*.

**Note**
You cannot create recommendation preferences for Auto Scaling groups at the organization and account levels. You can create recommendation preferences for Auto Scaling groups only at the resource level by specifying a scope name of `ResourceArn` and a scope value of the Auto Scaling group Amazon Resource Name (ARN). This will configure the preference for all instances that are part of the specified Auto Scaling group. You also cannot create recommendation preferences at the resource level for instances that are part of an Auto Scaling group. You can create recommendation preferences at the resource level only for standalone instances.

## Contents
<a name="API_Scope_Contents"></a>

 ** name **   <a name="computeoptimizer-Type-Scope-name"></a>
The name of the scope.
The following scopes are possible:
+  `Organization` - Specifies that the recommendation preference applies at the organization level, for all member accounts of an organization.
+  `AccountId` - Specifies that the recommendation preference applies at the account level, for all resources of a given resource type in an account.
+  `ResourceArn` - Specifies that the recommendation preference applies at the individual resource level.
Type: String
Valid Values: `Organization | AccountId | ResourceArn`
Required: No

 ** value **   <a name="computeoptimizer-Type-Scope-value"></a>
The value of the scope.
If you specified the `name` of the scope as:
+  `Organization` - The `value` must be `ALL_ACCOUNTS`.
+  `AccountId` - The `value` must be a 12-digit AWS account ID.
+  `ResourceArn` - The `value` must be the Amazon Resource Name (ARN) of an EC2 instance or an Auto Scaling group.
Only EC2 instance and Auto Scaling group ARNs are currently supported.
Type: String
Required: No

## See Also
<a name="API_Scope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/Scope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/Scope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/Scope)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
