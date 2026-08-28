---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SmallMultiplesAxisProperties.html
---

# SmallMultiplesAxisProperties
<a name="API_SmallMultiplesAxisProperties"></a>

Configures the properties of a chart's axes that are used by small multiples panels.

## Contents
<a name="API_SmallMultiplesAxisProperties_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Placement **   <a name="QS-Type-SmallMultiplesAxisProperties-Placement"></a>
Defines the placement of the axis. By default, axes are rendered `OUTSIDE` of the panels. Axes with `INDEPENDENT` scale are rendered `INSIDE` the panels.
Type: String
Valid Values: `OUTSIDE | INSIDE`
Required: No

 ** Scale **   <a name="QS-Type-SmallMultiplesAxisProperties-Scale"></a>
Determines whether scale of the axes are shared or independent. The default value is `SHARED`.
Type: String
Valid Values: `SHARED | INDEPENDENT`
Required: No

## See Also
<a name="API_SmallMultiplesAxisProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SmallMultiplesAxisProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SmallMultiplesAxisProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SmallMultiplesAxisProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
