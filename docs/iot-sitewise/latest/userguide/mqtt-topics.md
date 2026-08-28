---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/mqtt-topics.html
---

# Understand asset properties in MQTT topics
<a name="mqtt-topics"></a>

Every asset property has a unique MQTT topic path in the following format.

```
$aws/sitewise/asset-models/{{assetModelId}}/assets/{{assetId}}/properties/{{propertyId}}
```

**Note**
AWS IoT SiteWise doesn't support the `#` (multi-level) topic filter wildcard in the AWS IoT Core rules engine. You can use the `+` (single-level) wildcard. For example, you can use the following topic filter to match all updates for a particular asset model.

```
$aws/sitewise/asset-models/{{assetModelId}}/assets/+/properties/+
```
To learn more about topic filter wildcards, see [Topics](https://docs.aws.amazon.com/iot/latest/developerguide/topics.html) in the *AWS IoT Core Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
