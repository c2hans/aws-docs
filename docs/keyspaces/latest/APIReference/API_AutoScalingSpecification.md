---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_AutoScalingSpecification.html
---

# AutoScalingSpecification
<a name="API_AutoScalingSpecification"></a>

The optional auto scaling capacity settings for a table in provisioned capacity mode.

## Contents
<a name="API_AutoScalingSpecification_Contents"></a>

 ** readCapacityAutoScaling **   <a name="keyspaces-Type-AutoScalingSpecification-readCapacityAutoScaling"></a>
The auto scaling settings for the table's read capacity.
Type: [AutoScalingSettings](API_AutoScalingSettings.md) object
Required: No

 ** writeCapacityAutoScaling **   <a name="keyspaces-Type-AutoScalingSpecification-writeCapacityAutoScaling"></a>
The auto scaling settings for the table's write capacity.
Type: [AutoScalingSettings](API_AutoScalingSettings.md) object
Required: No

## See Also
<a name="API_AutoScalingSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/AutoScalingSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/AutoScalingSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/AutoScalingSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces (for Apache Cassandra). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
