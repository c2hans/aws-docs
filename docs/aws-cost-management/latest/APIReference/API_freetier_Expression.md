---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_Expression.html
---

# Expression
<a name="API_freetier_Expression"></a>

Use `Expression` to filter in the `GetFreeTierUsage` API operation.

You can use the following patterns:
+ Simple dimension values (`Dimensions` root operator)
+ Complex expressions with logical operators (`AND`, `NOT`, and `OR` root operators).

For *simple dimension values*, you can set the dimension name, values, and match type for the filters that you plan to use.

 **Example for simple dimension values**

You can filter to match exactly for `REGION==us-east-1 OR REGION==us-west-1`.

The corresponding `Expression` appears like the following: `{ "Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ], "MatchOptions": ["EQUALS"] } }`

As shown in the previous example, lists of dimension values are combined with `OR` when you apply the filter.

For *complex expressions with logical operators*, you can have nested expressions to use the logical operators and specify advanced filtering.

 **Example for complex expressions with logical operators**

You can filter by `((REGION == us-east-1 OR REGION == us-west-1) OR (SERVICE CONTAINS AWSLambda)) AND (USAGE_TYPE !CONTAINS DataTransfer)`.

The corresponding `Expression` appears like the following: `{ "And": [ {"Or": [ {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ], "MatchOptions": ["EQUALS"] }}, {"Dimensions": { "Key": "SERVICE", "Values": ["AWSLambda"], "MatchOptions": ["CONTAINS"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"], "MatchOptions": ["CONTAINS"] }}} ] }`

In the following **Contents**, you must specify exactly one of the following root operators.

## Contents
<a name="API_freetier_Expression_Contents"></a>

 ** And **   <a name="awscostmanagement-Type-freetier_Expression-And"></a>
Return results that match all `Expressions` that you specified in the array.
Type: Array of [Expression](#API_freetier_Expression) objects
Required: No

 ** Dimensions **   <a name="awscostmanagement-Type-freetier_Expression-Dimensions"></a>
The specific dimension, values, and match type to filter objects with.
Type: [DimensionValues](API_freetier_DimensionValues.md) object
Required: No

 ** Not **   <a name="awscostmanagement-Type-freetier_Expression-Not"></a>
Return results that don’t match the `Expression` that you specified.
Type: [Expression](#API_freetier_Expression) object
Required: No

 ** Or **   <a name="awscostmanagement-Type-freetier_Expression-Or"></a>
Return results that match any of the `Expressions` that you specified. in the array.
Type: Array of [Expression](#API_freetier_Expression) objects
Required: No

## See Also
<a name="API_freetier_Expression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/freetier-2023-09-07/Expression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/freetier-2023-09-07/Expression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/freetier-2023-09-07/Expression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
