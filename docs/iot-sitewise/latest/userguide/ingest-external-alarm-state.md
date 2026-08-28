---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ingest-external-alarm-state.html
---

# Ingest an external alarm state in AWS IoT SiteWise
<a name="ingest-external-alarm-state"></a>

External alarms are alarms that you evaluate outside of AWS IoT SiteWise. You can use external alarms when you have a data source that reports alarm state that you want to ingest to AWS IoT SiteWise.

Alarm state properties require a specific format for alarm state data values. Each data value must be a JSON object serialized to a string. Then, you ingest the serialized string as a string value. For more information, see [Alarm state properties](industrial-alarms.md#alarm-state-properties).

**Example alarm state data value (not serialized)**

```
{
  "stateName": "Active"
}
```

**Example alarm state data value (serialized)**

```
{\"stateName\":\"Active\"}
```

**Note**
If your data source can't report data in this format, or you can't convert your data to this format before you ingest it, you might choose not to use an alarm property. Instead, you can ingest the data as a measurement property with the string data type, for example. For more information, see [Define data streams from equipment (measurements)](measurements.md) and [Ingest data to AWS IoT SiteWise](industrial-data-ingestion.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
