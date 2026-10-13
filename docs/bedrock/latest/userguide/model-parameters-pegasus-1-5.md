---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-pegasus-1-5.html
---

# TwelveLabs Pegasus 1.5
<a name="model-parameters-pegasus-1-5"></a>

The TwelveLabs Pegasus 1.5 model provides comprehensive video understanding and analysis capabilities. Building on TwelveLabs Pegasus 1.2, it adds video segmentation that transforms raw video into structured, timestamped metadata across an entire video. It can analyze video content and generate textual descriptions, insights, and answers to questions about the video.

Use this information to make inference calls to TwelveLabs models with the [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) and [InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html) (streaming) operations.
+ Provider — TwelveLabs
+ Categories — Video understanding, content analysis, video segmentation
+ Model ID — `twelvelabs.pegasus-1-5-v1:0`
+ Input modality — Video
+ Output modality — Text
+ Max video size — up to 2 hours long (less than 2 GB file size)

**Note**
TwelveLabs Pegasus 1.5 is available through cross-Region inference only. Use the geo inference ID (`us.twelvelabs.pegasus-1-5-v1:0`) or the global inference ID (`global.twelvelabs.pegasus-1-5-v1:0`) rather than the base model ID.

## TwelveLabs Pegasus 1.5 request parameters
<a name="model-parameters-pegasus-1-5-request"></a>

The following table describes the input parameters for the TwelveLabs Pegasus 1.5 model:

**TwelveLabs Pegasus 1.5 request parameters**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| analysis\_mode | string | No | The analysis to perform. Valid values: general (default) returns free-form text analysis driven by inputPrompt; time\_based\_metadata returns structured, timestamped segments defined by segment\_definitions. |
| inputPrompt | string | Conditional | Prompt to analyze the video. Required when analysis\_mode is general. |
| mediaSource | object | Yes | Describes the media source. Either base64String or s3Location must be provided. |
| mediaSource.base64String | string | No | Base64 encoded byte string for the video. Max: 25 MB. For larger videos, use s3Location. |
| mediaSource.s3Location.uri | string | No | S3 URI where the video can be downloaded from. Max: up to 2 hours long (less than 2 GB file size). |
| mediaSource.s3Location.bucketOwner | string | Conditional | AWS account ID of the bucket owner. Required when s3Location is used. |
| temperature | double | No | Controls randomness in the output. Default: 0.2, Min: 0, Max: 1. |
| maxOutputTokens | integer | No | The maximum number of tokens to generate. Min: 512, Max: 98304. |
| responseFormat | object | No | Specifies a structured-output JSON Schema. Set the schema object directly under responseFormat.jsonSchema. Applies to general analysis mode. |
| segment\_definitions | array | Conditional | Required when analysis\_mode is time\_based\_metadata. Each entry defines a segment type to extract, with an id, a description, and a list of fields (each with name, type, and description) to populate per segment. |

## TwelveLabs Pegasus 1.5 response fields
<a name="model-parameters-pegasus-1-5-response"></a>

The following table describes the output fields for the TwelveLabs Pegasus 1.5 model:

**TwelveLabs Pegasus 1.5 response fields**

| Field | Type | Description |
| --- | --- | --- |
| message | string | Output message containing the model's analysis of the video. When responseFormat.jsonSchema is set, this field returns a JSON string that conforms to the supplied schema. Parse the string to access individual fields. |
| stopReason | string | Reason the output ended. Valid values: stop (the model returned the full response without reaching any limits), length (the generation reached the maxOutputTokens limit). |
| segments | array | Present when analysis\_mode is time\_based\_metadata. The list of extracted segments, each carrying the fields declared in the matching segment\_definitions entry along with its time range. |
| definition\_errors | array | Present when analysis\_mode is time\_based\_metadata. Lists any segment\_definitions entries that could not be processed; empty ([]) when all definitions were applied successfully. |
| finish\_reason | string | Present when analysis\_mode is time\_based\_metadata. Returned alongside stopReason in the segmentation response and carries the same value. |

**Note**
TwelveLabs Pegasus 1.5 returns the stop reason in the `stopReason` field. This differs from TwelveLabs Pegasus 1.2, which returns `finishReason`. In `time_based_metadata` mode, the response additionally includes a `finish_reason` field carrying the same value alongside `stopReason`.

## TwelveLabs Pegasus 1.5 request and response
<a name="model-parameters-pegasus-1-5-examples"></a>

The following examples show how to use the TwelveLabs Pegasus 1.5 model with different input sources and analysis modes.

------
#### [ Request ]

The following examples show request formats for the TwelveLabs Pegasus 1.5 model.

**Using base64 encoded video:**

```
{
  "analysis_mode": "general",
  "inputPrompt": "Tell me about this video",
  "mediaSource": {
      "base64String": "<BASE64 STRING OF VIDEO FILE>"
  },
  "temperature": 0.2
}
```

**Using S3 stored video:**

```
{
    "analysis_mode": "general",
    "inputPrompt": "Summarize this video and list key scenes with timestamps",
    "mediaSource": {
        "s3Location": {
            "uri": "s3://path-to-video-object-in-s3",
            "bucketOwner": "bucket-owner-account-id"
        }
    },
    "temperature": 0.2,
    "maxOutputTokens": 2048
}
```

**Using structured output format:**

```
{
    "analysis_mode": "general",
    "inputPrompt": "Analyze this video and provide a structured summary",
    "mediaSource": {
        "s3Location": {
            "uri": "s3://path-to-video-object-in-s3",
            "bucketOwner": "bucket-owner-account-id"
        }
    },
    "temperature": 0.2,
    "maxOutputTokens": 2048,
    "responseFormat": {
        "jsonSchema": {
            "type": "object",
            "properties": {
                "summary":    { "type": "string" },
                "key_scenes": { "type": "array", "items": { "type": "string" } },
                "duration":   { "type": "string" }
            },
            "required": ["summary", "key_scenes"]
        }
    }
}
```

**Using time-based metadata (video segmentation):**

```
{
    "analysis_mode": "time_based_metadata",
    "mediaSource": {
        "s3Location": {
            "uri": "s3://path-to-video-object-in-s3",
            "bucketOwner": "bucket-owner-account-id"
        }
    },
    "maxOutputTokens": 4096,
    "temperature": 0,
    "segment_definitions": [
        {
            "id": "scenes",
            "description": "What happens in this segment",
            "fields": [
                { "name": "summary", "type": "string", "description": "What happens in the segment" }
            ]
        }
    ]
}
```

------
#### [ Response ]

The following examples show response formats from the TwelveLabs Pegasus 1.5 model.

**Standard response:**

```
{
  "message": "This video shows a person walking through a park during sunset. The scene includes trees, a walking path, and golden lighting from the setting sun.",
  "stopReason": "stop"
}
```

**Response with structured output:**

```
{
  "message": "{\"summary\": \"A peaceful evening walk through a park at sunset\", \"key_scenes\": [\"Person entering the park\", \"Walking along tree-lined path\", \"Sunset lighting through trees\"], \"duration\": \"Approximately 2 minutes\"}",
  "stopReason": "stop"
}
```

**Response with time-based metadata:**

```
{
  "segments": [
    {
      "id": "scenes",
      "start_sec": 0,
      "end_sec": 12,
      "summary": "Opening shot establishing the location"
    },
    {
      "id": "scenes",
      "start_sec": 12,
      "end_sec": 30,
      "summary": "Main subject enters and the action begins"
    }
  ],
  "definition_errors": [],
  "stopReason": "stop",
  "finish_reason": "stop"
}
```

**Response when max tokens reached:**

```
{
  "message": "This video contains multiple scenes showing various activities. The first scene shows...",
  "stopReason": "length"
}
```

------
