---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_Entity.html
---

# Entity
<a name="API_Entity"></a>

The entity associated with the log events in a `PutLogEvents` call.

## Contents
<a name="API_Entity_Contents"></a>

 ** attributes **   <a name="CWL-Type-Entity-attributes"></a>
Additional attributes of the entity that are not used to specify the identity of the entity. A list of key-value pairs.
For details about how to use the attributes, see [How to add related information to telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/adding-your-own-related-telemetry.html) in the *CloudWatch User Guide*.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Value Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** keyAttributes **   <a name="CWL-Type-Entity-keyAttributes"></a>
The attributes of the entity which identify the specific entity, as a list of key-value pairs. Entities with the same `keyAttributes` are considered to be the same entity.
There are five allowed attributes (key names): `Type`, `ResourceType`, `Identifier` `Name`, and `Environment`.
For details about how to use the key attributes, see [How to add related information to telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/adding-your-own-related-telemetry.html) in the *CloudWatch User Guide*.
Type: String to string map
Map Entries: Minimum number of 2 items. Maximum number of 4 items.
Key Length Constraints: Minimum length of 1. Maximum length of 32.
Value Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_Entity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/Entity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/Entity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/Entity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
