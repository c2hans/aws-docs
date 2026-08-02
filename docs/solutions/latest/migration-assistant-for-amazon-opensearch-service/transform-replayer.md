---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/transform-replayer.html
---

# Transform live traffic (Traffic Replayer)
<a name="transform-replayer"></a>

During migrations, some requests may need to be transformed between versions. Traffic Replayer automatically rewrites host and authentication headers. For more complex transformations, specify custom transformation rules in your workflow configuration using the `replayerConfig` section.

## Elasticsearch content-type header compatibility
<a name="elastic-content-type"></a>

Newer Elasticsearch clients (version 7.11 and later, including all 8.x versions) use Elasticsearch-specific media types in `Content-Type` and `Accept` headers, such as `application/vnd.elasticsearch+json;compatible-with=8`. Amazon OpenSearch Service and Amazon OpenSearch Serverless NextGen do not support these media types.

If you are migrating traffic from Elasticsearch clients version 7.11 or later, apply a transformation to convert these headers to standard `application/json`.

### Recommended: use `requestTransforms`
<a name="replayer-content-type-pipeline"></a>

Use the workflow transform pipeline when you want the workflow to mount the transform file and generate the Traffic Replayer transformer configuration.

1. Create a JavaScript transformation file. You can author it anywhere you run `kubectl`, such as the Migration Console pod:

   ```
   cat > content-type-transformer.js << 'SCRIPT'
   const NEW_CONTENT_TYPE = "application/json";
   const ELASTIC_CONTENT_TYPE = "application/vnd.elasticsearch+json";

   function transform(request, context) {
     let headers = request.get("headers");
     if (headers) {
       let contentType = headers.get("Content-Type");
       if (Array.isArray(contentType)) {
         headers.set("Content-Type", contentType.map(v => v.includes(ELASTIC_CONTENT_TYPE) ? NEW_CONTENT_TYPE : v));
       } else if (typeof contentType === "string") {
         if (contentType.includes(ELASTIC_CONTENT_TYPE)) {
           headers.set("Content-Type", NEW_CONTENT_TYPE);
         }
       }
       let accept = headers.get("Accept");
       if (Array.isArray(accept)) {
         headers.set("Accept", accept.map(v => v.includes(ELASTIC_CONTENT_TYPE) ? NEW_CONTENT_TYPE : v));
       } else if (typeof accept === "string") {
         if (accept.includes(ELASTIC_CONTENT_TYPE)) {
           headers.set("Accept", NEW_CONTENT_TYPE);
         }
       }
     }
     return request;
   }

   function main(context) {
     return (request) => {
       if (Array.isArray(request)) {
         return request.flat().map(item => transform(item, context));
       }
       return transform(request, context);
     };
   }
   (() => main)();
   SCRIPT
   ```

1. Create a ConfigMap from the transformation file:

   ```
   kubectl create configmap replayer-transforms -n ma \
     --from-file=content-type-transformer.js=content-type-transformer.js
   ```

1. Add the transformation to the workflow configuration under the replayer’s `replayerConfig`. The examples in this section show only the relevant replayer entry; keep the rest of the workflow configuration, including the captured-traffic source referenced by `fromCapturedTraffic` and the target cluster referenced by `toTarget`.

   ```
   {
     "traffic": {
       "replayers": {
         "replay1": {
           "fromCapturedTraffic": "capture-proxy",
           "toTarget": "target",
           "replayerConfig": {
             "requestTransforms": [
               {
                 "entryPoint": {
                   "javascriptFile": {
                     "configMap": "replayer-transforms",
                     "path": "content-type-transformer.js"
                   }
                 }
               }
             ]
           }
         }
       }
     }
   }
   ```

   The ConfigMap must already exist in the migration namespace, and `path` is the ConfigMap key that contains the transform file. Keep the replayer’s existing `fromCapturedTraffic` and `toTarget` values when you add `replayerConfig`. For image-backed transforms, use `{"image": "example.com/transforms@sha256:…​", "path": "request.js"}` instead. For the full workflow transform schema, including inline scripts, Python, named providers, and context values, see [Workflow transform pipeline model](data-transforms.md#transform-pipeline-model).

### Alternative: use a raw inline transformer configuration
<a name="replayer-content-type-raw-config"></a>

If you are not using the workflow transform pipeline, provide the raw transformer configuration inline through `transformerConfig`. The workflow passes the value directly to the Traffic Replayer, so no ConfigMap or shared filesystem is required. The Traffic Replayer pod does not read files from the Migration Console filesystem, so use `transformerConfigFile` only when you mount the file into the replayer container yourself.

Build the configuration from your JavaScript file with `jq`, which embeds the script as the `initializationScript` value without manual escaping:

```
jq -Rs '[{"JsonJSTransformerProvider":{"initializationScript":.,"bindingsObject":"{}"}}]' \
  content-type-transformer.js
```

Use the single-line output as the `transformerConfig` value:

```
{
  "traffic": {
    "replayers": {
      "replay1": {
        "fromCapturedTraffic": "capture-proxy",
        "toTarget": "target",
        "replayerConfig": {
          "transformerConfig": "[{\"JsonJSTransformerProvider\":{\"initializationScript\":\"...\",\"bindingsObject\":\"{}\"}}]"
        }
      }
    }
  }
}
```

For configurations that are cumbersome to encode as a single-line JSON string, pipe the same output through `base64 -w0` and provide it through `transformerConfigEncoded` instead.

## Replayer transformation configuration fields
<a name="replayer-transform-config-fields"></a>

Use request transforms when you need to modify a captured request before Traffic Replayer sends it to the target. Use tuple transforms when you need to modify the request/response tuple output that Traffic Replayer records for validation or analysis.

| Field | Use |
| --- | --- |
|  `requestTransforms`  | Preferred workflow pipeline for request transforms. Each entry uses either `entryPoint` for inline or file-backed JavaScript/Python, or `transformName` for a named transformer provider. |
|  `transformerConfig`  | Inline raw request transformer configuration as a JSON string. |
|  `transformerConfigEncoded`  | Base64-encoded raw request transformer configuration. |
|  `transformerConfigFile`  |  **[Expert]** Path to a raw request transformer configuration file. The file must already be mounted into the Traffic Replayer container by the user; it is not wired through the workflow, and Migration Console files are not mounted into the replayer pod. |
|  `tupleTransforms`  | Preferred workflow pipeline for tuple transforms. |
|  `tupleTransformerConfig`  | Inline raw tuple transformer configuration as a JSON string. |
|  `tupleTransformerConfigBase64`  | Base64-encoded raw tuple transformer configuration. |
|  `tupleTransformerConfigFile`  |  **[Expert]** Path to a raw tuple transformer configuration file that is already mounted into the Traffic Replayer container by the user. |

**Note**
For each pipeline type, use either the workflow pipeline field or the raw configuration fields, not both. For example, do not configure `requestTransforms` together with `transformerConfig`, `transformerConfigEncoded`, or `transformerConfigFile`.

The raw request transformer configuration is an array of transformer-provider objects. For JavaScript request transforms, use `JsonJSTransformerProvider` with either `initializationScript` or `initializationScriptFile`.

```
[
  {
    "JsonJSTransformerProvider": {
      "initializationScriptFile": "/path/to/request-transform.js",
      "bindingsObject": "{}"
    }
  }
]
```
