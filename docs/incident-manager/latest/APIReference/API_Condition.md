---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_Condition.html
---

# Condition
<a name="API_Condition"></a>

A conditional statement with which to compare a value, after a timestamp, before a timestamp, or equal to a string or integer. If multiple conditions are specified, the conditionals become an `AND`ed statement. If multiple values are specified for a conditional, the values are `OR`d.

## Contents
<a name="API_Condition_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** after **   <a name="IncidentManager-Type-Condition-after"></a>
After the specified timestamp.
Type: Timestamp
Required: No

 ** before **   <a name="IncidentManager-Type-Condition-before"></a>
Before the specified timestamp
Type: Timestamp
Required: No

 ** equals **   <a name="IncidentManager-Type-Condition-equals"></a>
The value is equal to the provided string or integer.
Type: [AttributeValueList](API_AttributeValueList.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_Condition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/Condition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/Condition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/Condition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
