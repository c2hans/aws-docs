---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GroupingAttributeDefinition.html
---

# GroupingAttributeDefinition
<a name="API_GroupingAttributeDefinition"></a>

A structure that defines how services should be grouped based on specific attributes. This includes the friendly name for the grouping, the source keys to derive values from, and an optional default value.

## Contents
<a name="API_GroupingAttributeDefinition_Contents"></a>

 ** GroupingName **   <a name="applicationsignals-Type-GroupingAttributeDefinition-GroupingName"></a>
The friendly name for this grouping attribute, such as `BusinessUnit` or `Environment`. This name is used to identify the grouping in the console and APIs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\s+\-=\._:/@]*`
Required: Yes

 ** DefaultGroupingValue **   <a name="applicationsignals-Type-GroupingAttributeDefinition-DefaultGroupingValue"></a>
The default value to use for this grouping attribute when no value can be derived from the source keys. This ensures all services have a grouping value even if the source data is missing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\s+\-=\._:/@]*`
Required: No

 ** GroupingSourceKeys **   <a name="applicationsignals-Type-GroupingAttributeDefinition-GroupingSourceKeys"></a>
An array of source keys used to derive the grouping attribute value from telemetry data, AWS tags, or other sources. For example, ["business\_unit", "team"] would look for values in those fields.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\s+\-=\._:/@]*`
Required: No

## See Also
<a name="API_GroupingAttributeDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/GroupingAttributeDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/GroupingAttributeDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/GroupingAttributeDefinition)
