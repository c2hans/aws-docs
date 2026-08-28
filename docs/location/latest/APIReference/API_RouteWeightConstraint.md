---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteWeightConstraint.html
---

# RouteWeightConstraint
<a name="API_RouteWeightConstraint"></a>

The weight constraint for the route.

 **Unit**: `kilograms`

## Contents
<a name="API_RouteWeightConstraint_Contents"></a>

 ** Type **   <a name="location-Type-RouteWeightConstraint-Type"></a>
The type of constraint.
Type: String
Valid Values: `Current | Gross | Unknown`
Required: Yes

 ** Value **   <a name="location-Type-RouteWeightConstraint-Value"></a>
The constraint value.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

## See Also
<a name="API_RouteWeightConstraint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteWeightConstraint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteWeightConstraint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteWeightConstraint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
