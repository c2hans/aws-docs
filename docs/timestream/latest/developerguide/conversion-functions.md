---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/conversion-functions.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Conversion functions
<a name="conversion-functions"></a>

Timestream for LiveAnalytics supports the following conversion functions.

**Topics**
+ [cast()](#conversion-functions.cast)
+ [try\_cast()](#conversion-functions.try-cast)

## cast()
<a name="conversion-functions.cast"></a>

 The syntax of the cast function to explicitly cast a value as a type is as follows.

```
cast(value AS type)
```

## try\_cast()
<a name="conversion-functions.try-cast"></a>

Timestream for LiveAnalytics also supports the try\_cast function that is similar to cast but returns null if cast fails. The syntax is as follows.

```
try_cast(value AS type)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
