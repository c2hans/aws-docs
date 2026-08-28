---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GroupingConfiguration.html
---

# GroupingConfiguration
<a name="API_GroupingConfiguration"></a>

A structure that contains the complete grouping configuration for an account, including all defined grouping attributes and metadata about when it was last updated.

## Contents
<a name="API_GroupingConfiguration_Contents"></a>

 ** GroupingAttributeDefinitions **   <a name="applicationsignals-Type-GroupingConfiguration-GroupingAttributeDefinitions"></a>
An array of grouping attribute definitions that specify how services should be grouped based on various attributes and source keys.
Type: Array of [GroupingAttributeDefinition](API_GroupingAttributeDefinition.md) objects
Required: Yes

 ** UpdatedAt **   <a name="applicationsignals-Type-GroupingConfiguration-UpdatedAt"></a>
The timestamp when this grouping configuration was last updated. When used in a raw HTTP Query API, it is formatted as epoch time in seconds.
Type: Timestamp
Required: Yes

## See Also
<a name="API_GroupingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/GroupingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/GroupingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/GroupingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
