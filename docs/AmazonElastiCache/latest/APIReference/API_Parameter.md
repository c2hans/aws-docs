---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_Parameter.html
---

# Parameter
<a name="API_Parameter"></a>

Describes an individual setting that controls some aspect of ElastiCache behavior.

## Contents
<a name="API_Parameter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AllowedValues **
The valid range of values for the parameter.
Type: String
Required: No

 ** ChangeType **
Indicates whether a change to the parameter is applied immediately or requires a reboot for the change to be applied. You can force a reboot or wait until the next maintenance window's reboot. For more information, see [Rebooting a Cluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.Rebooting.html).
Type: String
Valid Values: `immediate | requires-reboot`
Required: No

 ** DataType **
The valid data type for the parameter.
Type: String
Required: No

 ** Description **
A description of the parameter.
Type: String
Required: No

 ** IsModifiable **
Indicates whether (`true`) or not (`false`) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
Type: Boolean
Required: No

 ** MinimumEngineVersion **
The earliest cache engine version to which the parameter can apply.
Type: String
Required: No

 ** ParameterName **
The name of the parameter.
Type: String
Required: No

 ** ParameterValue **
The value of the parameter.
Type: String
Required: No

 ** Source **
The source of the parameter.
Type: String
Required: No

## See Also
<a name="API_Parameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/Parameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/Parameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/Parameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
