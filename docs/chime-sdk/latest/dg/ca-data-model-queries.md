---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-data-model-queries.html
---

# Extracting data in your AWS Glue data catalog for Amazon Chime SDK call analytics
<a name="ca-data-model-queries"></a>

Use these sample queries to extract and organize the data in your Amazon Chime SDK call analytics Glue data catalog.

**Note**
For information about connecting to Amazon Athena and querying your Glue data catalog, see [Connecting to Amazon Athena with ODBC](https://docs.aws.amazon.com/athena/latest/ug/connect-with-odbc.html).

Expand each section as needed.

## Extracting values from metadata (STRING datatype) in the call\_analytics\_metadata table
<a name="qry-insights-metadata"></a>

`call_analytics_metadata` has the `metadata` field in a JSON string format. Use the [json\_extract\_scalar function](https://docs.aws.amazon.com/athena/latest/ug/extracting-data-from-JSON.html) in Athena to query the elements in this string.

```
SELECT
    json_extract_scalar(metadata,'$.voiceConnectorId') AS "VoiceConnector ID",
    json_extract_scalar(metadata,'$.fromNumber') AS "From Number",
    json_extract_scalar(metadata,'$.toNumber') AS "To Number",
    json_extract_scalar(metadata,'$.callId') AS "Call ID",
    json_extract_scalar(metadata,'$.direction') AS Direction,
    json_extract_scalar(metadata,'$.transactionId') AS "Transaction ID"
FROM
    "GlueDatabaseName"."call_analytics_metadata"
```

## Querying SIPRECMetadata updates in the call\_analytics\_metadata table
<a name="qry-insights-siprec-metadata"></a>

The `call_analytics_metadata` field has the metadata field in a JSON string format. `metadata` has another nested object called `oneTimeMetadata`, this object contains SIPRec Metadata in original XML and transformed JSON formats. Use the `json_extract_scalar` function in Athena to query the elements in this string.

```
SELECT
    json_extract_scalar(metadata,'$.voiceConnectorId') AS "VoiceConnector ID",
    json_extract_scalar(metadata,'$.fromNumber') AS "From Number",
    json_extract_scalar(metadata,'$.toNumber') AS "To Number",
    json_extract_scalar(metadata,'$.callId') AS "Call ID",
    json_extract_scalar(metadata,'$.direction') AS Direction,
    json_extract_scalar(metadata,'$.transactionId') AS "Transaction ID",
    json_extract_scalar(json_extract_scalar(metadata,'$.oneTimeMetadata'),'$.siprecMetadata') AS "siprec Metadata XML",
    json_extract_scalar(json_extract_scalar(metadata,'$.oneTimeMetadata'),'$.siprecMetadataJson') AS "Siprec Metadata JSON",
    json_extract_scalar(json_extract_scalar(metadata,'$.oneTimeMetadata'),'$.inviteHeaders') AS "Invite Headers"
FROM
    "GlueDatabaseName"."call_analytics_metadata"
WHERE
    callevent-type = "update";
```

## Extracting values from metadata (STRING datatype) in the call\_analytics\_recording\_metadata table
<a name="qry-recording-metadata"></a>

`call_analytics_recording_metadata` has the metadata field in a JSON string format. Use the [json\_extract\_scalar function](https://docs.aws.amazon.com/athena/latest/ug/extracting-data-from-JSON.html) in Athena to query the elements in this string.

```
SELECT
    json_extract_scalar(metadata,'$.voiceConnectorId') AS "VoiceConnector ID",
    json_extract_scalar(metadata,'$.fromNumber') AS "From Number",
    json_extract_scalar(metadata,'$.toNumber') AS "To Number",
    json_extract_scalar(metadata,'$.callId') AS "Call ID",
    json_extract_scalar(metadata,'$.direction') AS Direction,
    json_extract_scalar(metadata,'$.transactionId') AS "Transaction ID"
FROM
    "GlueDatabaseName"."call_analytics_recording_metadata"
WHERE
    detail-subtype = "Recording"
```

## Extracting values from detail (STRUCT datatype) in the voice\_analytics\_status table
<a name="qry-va-status"></a>

`voice_analytics_status` has a details field in the `struct` data type. The following example shows how to query a `struct` data type field:

```
SELECT
    detail.transactionId AS "Transaction ID",
    detail.voiceConnectorId AS "VoiceConnector ID",
    detail.siprecmetadata AS "Siprec Metadata",
    detail.inviteheaders AS "Invite Headers",
    detail.streamStartTime AS "Stream Start Time"
FROM
    "GlueDatabaseName"."voice_analytics_status"
```

## Joining the voice\_analytics\_status and call\_analytics\_metadata tables
<a name="qry-join-va-meta"></a>

The following example query joins `call_analytics_metadata` and `voice_analytics_status`:

```
SELECT
    a.detail.transactionId AS "Transaction ID",
    a.detail.voiceConnectorId AS "VoiceConnector ID",
    a.detail.siprecmetadata AS "Siprec Metadata",
    a.detail.inviteheaders AS "Invite Headers",
    a.detail.streamStartTime AS "Stream Start Time"
    json_extract_scalar(b.metadata,'$.fromNumber') AS "From Number",
    json_extract_scalar(b.metadata,'$.toNumber') AS "To Number",
    json_extract_scalar(b.metadata,'$.callId') AS "Call ID",
    json_extract_scalar(b.metadata,'$.direction') AS Direction
FROM
    "GlueDatabaseName"."voice_analytics_status" a
INNER JOIN
    "GlueDatabaseName"."call_analytics_metadata" b
ON a.detail.transactionId = json_extract_scalar(b.metadata,'$.transactionId')
```

## Extracting transcripts from the transcribe\_call\_analytics\_post\_call table
<a name="qry-transcribe-ca-post-call"></a>

transcribe\_call\_analytics\_post\_call has transcript field in struct format with nested arrays. Use the following query to un-nest the arrays:

```
SELECT
    jobstatus,
    languagecode,
    IF(CARDINALITY(m.transcript)=0 OR CARDINALITY(m.transcript) IS NULL, NULL, e.transcript.id) AS utteranceId,
    IF(CARDINALITY(m.transcript)=0 OR CARDINALITY(m.transcript) IS NULL, NULL, e.transcript.content) AS transcript,
    accountid,
    channel,
    sessionid,
    contentmetadata.output AS "Redaction"
FROM
    "GlueDatabaseName"."transcribe_call_analytics_post_call" m
CROSS JOIN UNNEST
    (IF(CARDINALITY(m.transcript)=0, ARRAY[NULL], transcript)) AS e(transcript)
```

## Joining the transcribe\_call\_analytics\_post\_call and call\_analytics\_metadata tables
<a name="qry-va-status"></a>

The following query joins transcribe\_call\_analytics\_post\_call and call\_analytics\_metadata:

```
WITH metadata AS(
  SELECT
    from_iso8601_timestamp(time) AS "Timestamp",
    date_parse(date_format(from_iso8601_timestamp(time), '%m/%d/%Y %H:%i:%s') , '%m/%d/%Y %H:%i:%s') AS "DateTime",
    date_parse(date_format(from_iso8601_timestamp(time) , '%m/%d/%Y') , '%m/%d/%Y') AS "Date",
    date_format(from_iso8601_timestamp(time) , '%H:%i:%s')  AS "Time",
    mediainsightspipelineid,
    json_extract_scalar(metadata,'$.toNumber') AS "To Number",
    json_extract_scalar(metadata,'$.voiceConnectorId') AS "VoiceConnector ID",
    json_extract_scalar(metadata,'$.fromNumber') AS "From Number",
    json_extract_scalar(metadata,'$.callId') AS "Call ID",
    json_extract_scalar(metadata,'$.direction') AS Direction,
    json_extract_scalar(metadata,'$.transactionId') AS "Transaction ID",
    REGEXP_REPLACE(REGEXP_EXTRACT(json_extract_scalar(metadata,'$.oneTimeMetadata.s3RecordingUrl'), '[^/]+(?=\.[^.]+$)'), '\.wav$', '') AS "SessionID"
  FROM
    "GlueDatabaseName"."call_analytics_metadata"
),
transcript_events AS(
  SELECT
    jobstatus,
    languagecode,
    IF(CARDINALITY(m.transcript)=0 OR CARDINALITY(m.transcript) IS NULL, NULL, e.transcript.id) AS utteranceId,
    IF(CARDINALITY(m.transcript)=0 OR CARDINALITY(m.transcript) IS NULL, NULL, e.transcript.content) AS transcript,
    accountid,
    channel,
    sessionid,
    contentmetadata.output AS "Redaction"
  FROM
    "GlueDatabaseName"."transcribe_call_analytics_post_call" m
  CROSS JOIN UNNEST
    (IF(CARDINALITY(m.transcript)=0, ARRAY[NULL], transcript)) AS e(transcript)
)
SELECT
    jobstatus,
    languagecode,
    a.utteranceId,
    transcript,
    accountid,
    channel,
    a.sessionid,
    "Redaction"
    "Timestamp",
    "DateTime",
    "Date",
    "Time",
    mediainsightspipelineid,
    "To Number",
    "VoiceConnector ID",
    "From Number",
    "Call ID",
    Direction,
    "Transaction ID"
FROM
    "GlueDatabaseName"."transcribe_call_analytics_post_call" a
LEFT JOIN
    metadata b
ON
    a.sessionid = b.SessionID
```

## Querying media object URLs for Voice enhancement call recording
<a name="qry-voice-enhancement-call-recording"></a>

The following example query joins `Voice enhancement call recording` URL:

```
SELECT
    json_extract_scalar(metadata,'$.voiceConnectorId') AS "VoiceConnector ID",
    json_extract_scalar(metadata,'$.fromNumber') AS "From Number",
    json_extract_scalar(metadata,'$.toNumber') AS "To Number",
    json_extract_scalar(metadata,'$.callId') AS "Call ID",
    json_extract_scalar(metadata,'$.direction') AS Direction,
    json_extract_scalar(metadata,'$.transactionId') AS "Transaction ID",
    s3MediaObjectConsoleUrl
FROM
    {GlueDatabaseName}."call_analytics_recording_metadata"
WHERE
    detail-subtype = "VoiceEnhancement"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
