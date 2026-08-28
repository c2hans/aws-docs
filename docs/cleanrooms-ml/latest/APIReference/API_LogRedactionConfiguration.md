---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_LogRedactionConfiguration.html
---

# LogRedactionConfiguration
<a name="API_LogRedactionConfiguration"></a>

The configuration for log redaction.

## Contents
<a name="API_LogRedactionConfiguration_Contents"></a>

 ** entitiesToRedact **   <a name="API-Type-LogRedactionConfiguration-entitiesToRedact"></a>
Specifies the entities to be redacted from logs. Entities to redact are "ALL\_PERSONALLY\_IDENTIFIABLE\_INFORMATION", "NUMBERS","CUSTOM". If CUSTOM is supplied or configured, custom patterns (customDataIdentifiers) should be provided, and the patterns will be redacted in logs or error messages.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `ALL_PERSONALLY_IDENTIFIABLE_INFORMATION | NUMBERS | CUSTOM`
Required: Yes

 ** customEntityConfig **   <a name="API-Type-LogRedactionConfiguration-customEntityConfig"></a>
Specifies the configuration for custom entities in the context of log redaction.
Type: [CustomEntityConfig](API_CustomEntityConfig.md) object
Required: No

## See Also
<a name="API_LogRedactionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/LogRedactionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/LogRedactionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/LogRedactionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
