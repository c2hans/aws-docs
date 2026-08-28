---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_AddOn.html
---

# AddOn
<a name="API_AddOn"></a>

Describes an add-on that is enabled for an Amazon Lightsail resource.

## Contents
<a name="API_AddOn_Contents"></a>

 ** duration **   <a name="Lightsail-Type-AddOn-duration"></a>
The amount of idle time in minutes after which your virtual computer will automatically stop.
This add-on only applies to Lightsail for Research resources.
Type: String
Required: No

 ** name **   <a name="Lightsail-Type-AddOn-name"></a>
The name of the add-on.
Type: String
Required: No

 ** nextSnapshotTimeOfDay **   <a name="Lightsail-Type-AddOn-nextSnapshotTimeOfDay"></a>
The next daily time an automatic snapshot will be created.
The time shown is in `HH:00` format, and in Coordinated Universal Time (UTC).
The snapshot is automatically created between the time shown and up to 45 minutes after.
Type: String
Pattern: `^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$`
Required: No

 ** snapshotTimeOfDay **   <a name="Lightsail-Type-AddOn-snapshotTimeOfDay"></a>
The daily time when an automatic snapshot is created.
The time shown is in `HH:00` format, and in Coordinated Universal Time (UTC).
The snapshot is automatically created between the time shown and up to 45 minutes after.
Type: String
Pattern: `^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$`
Required: No

 ** status **   <a name="Lightsail-Type-AddOn-status"></a>
The status of the add-on.
Type: String
Required: No

 ** threshold **   <a name="Lightsail-Type-AddOn-threshold"></a>
The trigger threshold of the action.
This add-on only applies to Lightsail for Research resources.
Type: String
Required: No

## See Also
<a name="API_AddOn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/AddOn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/AddOn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/AddOn)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
