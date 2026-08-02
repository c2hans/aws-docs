---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tft-custom-transformer.html
---

# Custom field type transformer (JavaScript)
<a name="tft-custom-transformer"></a>

When a field type is not covered by the built-in transformations, you can supply a custom JavaScript transformer that rewrites mappings as metadata is migrated. The transformer is a JavaScript function that receives each metadata document and returns the modified document. For workflow runs, reference the script with `metadataTransforms`; for one-off manual runs, pass a raw transformer descriptor to the metadata migration command.

The following procedure runs from the Migration Console pod. It writes the transformer script to a temporary file so you can package it in a ConfigMap for the workflow or reference it from a raw descriptor for a manual metadata run.

1. Open a shell on the Migration Console pod:

   ```
   kubectl exec -it migration-console-0 -n ma -- /bin/bash
   ```

1. Create the JavaScript transformer file. The following example walks the metadata tree and applies a small set of rules — here, mapping `string` to `text` and `flattened` to `flat_object` and removing the `index` property — but you can extend the `rules` array to handle any field type your source uses:

   ```
   cat > /tmp/field-type-converter.js << 'SCRIPT'
   function main(context) {
     const rules = [
       {
         when: { type: "string" },
         set: { type: "text" }
       },
       {
         when: { type: "flattened" },
         set: { type: "flat_object" },
         remove: ["index"]
       }
     ];

     function applyRules(node, rules) {
       if (Array.isArray(node)) {
         node.forEach((child) => applyRules(child, rules));
       } else if (node instanceof Map) {
         for (const { when, set, remove = [] } of rules) {
           const matches = Object.entries(when).every(([k, v]) => node.get(k) === v);
           if (matches) {
             Object.entries(set).every(([k, v]) => node.set(k, v));
             remove.forEach((key) => node.delete(key));
           }
         }
         for (const child of node.values()) {
           applyRules(child, rules);
         }
       } else if (node && typeof node === "object") {
         for (const { when, set, remove = [] } of rules) {
           const matches = Object.entries(when).every(([k, v]) => node[k] === v);
           if (matches) {
             Object.assign(node, set);
             remove.forEach((key) => delete node[key]);
           }
         }
         Object.values(node).forEach((child) => applyRules(child, rules));
       }
     }

     return (doc) => {
       if (doc && doc.type && doc.name && doc.body) {
         applyRules(doc, rules);
       }
       return doc;
     };
   }
   (() => main)();
   SCRIPT
   ```

1. For a workflow run, create a ConfigMap from the transformer file:

   ```
   kubectl create configmap metadata-transforms -n ma \
     --from-file=field-type-converter.js=/tmp/field-type-converter.js
   ```

1. Add the transform under `metadataMigrationConfig.metadataTransforms` in the workflow configuration:

   ```
   {
     "snapshotMigrationConfigs": [
       {
         "fromSource": "source",
         "toTarget": "target",
         "perSnapshotConfig": {
           "snap1": [
             {
               "metadataMigrationConfig": {
                 "metadataTransforms": [
                   {
                     "entryPoint": {
                       "javascriptFile": {
                         "configMap": "metadata-transforms",
                         "path": "field-type-converter.js"
                       }
                     }
                   }
                 ]
               }
             }
           ]
         }
       }
     ]
   }
   ```

   The ConfigMap must already exist in the migration namespace, and `path` is the ConfigMap key that contains the transform file. For image-backed transforms, use `{"image": "example.com/transforms@sha256:…​", "path": "metadata.js"}` instead. For the full workflow transform schema, including inline scripts, Python, named providers, and context values, see [Workflow transform pipeline model](data-transforms.md#transform-pipeline-model).

1. For a manual metadata run, create a transformer descriptor that points to the script. The `JsonJSTransformerProvider` loads your JavaScript from `initializationScriptFile`, and `bindingsObject` passes optional context to the script (use `"{}"` when you have no bindings):

   ```
   [
     {
       "JsonJSTransformerProvider": {
         "initializationScriptFile": "/tmp/field-type-converter.js",
         "bindingsObject": "{}"
       }
     }
   ]
   ```

   Save this descriptor to a file on the Migration Console pod, for example `/tmp/transformation.json`.

1. Run metadata migration with the descriptor applied:

   ```
   console metadata migrate --transformer-config-file /tmp/transformation.json
   ```

## Ways to supply the transformer configuration
<a name="tft-supplying-config"></a>

The workflow accepts a transform pipeline and the older raw descriptor fields, so you can choose whichever fits how you manage configuration:

| Field | Use it when |
| --- | --- |
|  `metadataTransforms`  | You want the workflow to mount JavaScript or Python transform files from a ConfigMap or OCI image and generate the metadata transformer configuration. This is the preferred workflow form. |
|  `transformerConfig`  | You want to embed the raw descriptor JSON inline in the workflow configuration. |
|  `transformerConfigBase64`  | You want to pass the raw descriptor as a Base64-encoded string — useful for avoiding quoting or escaping problems when the JSON is set through automation. |
|  `transformerConfigFile`  | You want to reference a descriptor file that is already mounted into the metadata migration container rather than inline the JSON. This is the workflow-configuration equivalent of the `console metadata migrate --transformer-config-file` flag shown in the preceding procedure, but the workflow does not mount Migration Console files into metadata pods by default. |

**Note**
Use either `metadataTransforms` or one raw configuration field, not both. When you run `console metadata migrate` interactively, use the `--transformer-config-file` flag; when you declare the transformer in the migration workflow configuration, set `metadataTransforms`, `transformerConfig`, `transformerConfigBase64`, or `transformerConfigFile` on the metadata migration configuration. Load the version-matched sample with `workflow configure sample --load` and edit it with `workflow configure edit` to confirm the exact placement for your installed release.
