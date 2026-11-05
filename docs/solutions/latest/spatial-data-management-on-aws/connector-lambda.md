---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connector-lambda.html
---

# AWS Lambda connector
<a name="connector-lambda"></a>

The AWS Lambda connector invokes Lambda functions with resource metadata as the payload. It is a dual-mode primitive — it can publish data outward to a Lambda function, or derive content by invoking a function and routing the response back into the asset record as metadata attributes or derived files.

Use this connector type when the integration needs custom code — transformations, validations, or processing that the declarative step types cannot express.

Check the declarative options first. Many integrations that once needed a function are now configuration only:

| To do this | Use |
| --- | --- |
| Call an external or AWS service API | A `rest` step. For AWS services, the request is signed with Signature Version 4. See [Working with REST APIs](connector-rest-api.md). |
| Write results back to the files they describe |  `output` routing with a `correlate` mapping. See [Correlate mapping](connector-configuration.md#correlate-mapping). |
| Process each file, or batches of files |  `applyTo`. See [Running steps per file](connector-configuration.md#trigger-apply-to). |
| Wait for long-running work | A `wait` step. See [Working with wait steps](connector-wait.md). |
| Run heavy or licensed software | A `deadlineJob` step. See [Create and transform content with AWS Deadline Cloud](connector-deadline-cloud.md). |

Step type: `lambdaInvoke`

Filters, `output` blocks, `${…​}` variables, `$temp` values, and type suffixes such as `:number` work the same way for every connector type. For more information, see [Trigger filters](connector-configuration.md#trigger-filters), [Output routing](connector-configuration.md#output-routing), [Variable substitution](connector-configuration.md#variable-substitution), [Intermediate state with $temp variables](connector-configuration.md#temp-variables), and [Type coercion](connector-configuration.md#type-coercion).

## Roles
<a name="lambda-roles"></a>

| Role | Description |
| --- | --- |
| Publisher | Invokes a Lambda function with a field-mapped payload when asset lifecycle events occur. The function receives the mapped fields and can process them however it needs — store data, call external APIs, trigger downstream workflows. |
| Content producer (deriver with output routing) | Invokes a Lambda function and routes the response back into the asset record. When an `output` block is present on the step, SDMA sends the full resource metadata as the payload and applies output routing to the response — writing fields to metadata attributes, ingesting derived files, or both. |
| Step type | Participates in multi-step triggers alongside other step types. A `lambdaInvoke` step can appear alongside REST calls, S3 writes, EventBridge events, or Deadline Cloud jobs in a single trigger. |

## Prerequisites
<a name="lambda-prerequisites"></a>

1. Create or identify the target Lambda function.

1. Create an IAM role:
   +  **Role name** must start with `SpatialDataManagementContentPublisher-` (publish connectors) or `SpatialDataManagementContentDerivation-` (derive connectors).
   +  **Trust policy** must allow the SDMA connector invocation Lambda to assume it:

     ```
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Principal": {
             "AWS": [
               "<connector-invocation-role-arn>",
               "<async-connector-invocation-role-arn>"
             ]
           },
           "Action": "sts:AssumeRole"
         }
       ]
     }
     ```

     Replace `<connector-invocation-role-arn>` and `<async-connector-invocation-role-arn>` with the execution role ARNs of the connector invocation Lambda functions in your SDMA deployment.

     If you have AWS CLI access, you can find these values by running:

     ```
     aws lambda get-function \
       --function-name SpatialDataManagement-ConnectorInvocationFunction \
       --query 'Configuration.Role' --output text

     aws lambda get-function \
       --function-name SpatialDataManagement-ConnectorInvocationAsyncFunction \
       --query 'Configuration.Role' --output text
     ```

     Alternatively, in the AWS Lambda console, open the [SpatialDataManagement-ConnectorInvocationFunction](https://console.aws.amazon.com/lambda/home#/functions/SpatialDataManagement-ConnectorInvocationFunction) and [SpatialDataManagement-ConnectorInvocationAsyncFunction](https://console.aws.amazon.com/lambda/home#/functions/SpatialDataManagement-ConnectorInvocationAsyncFunction) functions and find the role name for each under **Configuration** > **Permissions**. Use these names to construct the full ARNs (for example, `arn:aws:iam::<account-id>:role/<connector-invocation-role-name>`).
   +  **Permissions policy** must grant `lambda:InvokeFunction` on the target function:

     ```
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": "lambda:InvokeFunction",
           "Resource": "arn:aws:lambda:<region>:<account-id>:function:<function-name>"
         }
       ]
     }
     ```

## Using Lambda as a publisher
<a name="lambda-as-publisher"></a>

In publish mode, the connector builds a payload from field mappings and invokes the function. The function receives only the mapped fields — not the full resource metadata. No output routing is applied; the function’s response is not written back to the asset record.

### Example – invoke a processing function on asset creation
<a name="_example-invoke-a-processing-function-on-asset-creation"></a>

In the following example, replace the placeholder values in angle brackets with your own values.

```
{
  "securityConfig": {
    "type": "AssumeRole",
    "assumeRoleArn": "arn:aws:iam::<account-id>:role/SpatialDataManagementContentPublisher-Lambda"
  },
  "lambdaConfig": {
    "functionArn": "arn:aws:lambda:<region>:<account-id>:function:process-asset"
  },
  "defaultStepConfig": {
    "stepType": "lambdaInvoke"
  },
  "fieldMappings": [
    { "source": "asset.assetId", "target": "assetId" },
    { "source": "asset.assetName", "target": "name" },
    { "source": "project.projectId", "target": "projectId" }
  ],
  "triggers": [
    {
      "description": "Invoke processing function on asset creation",
      "resources": ["asset"],
      "events": ["create"],
      "steps": [
        {
          "payload": {
            "fields": ["assetId", "name", "projectId"]
          }
        }
      ]
    }
  ]
}
```

## Using Lambda as a content producer (deriver)
<a name="lambda-as-deriver"></a>

In derive mode, the connector routes the function’s response back into the asset record. Adding an `output` block to the step turns this on. What the function receives depends on whether the step also sets `payload.fields`:

| Step has | The function receives |
| --- | --- |
|  `output`, no `payload.fields`  | The complete resource context (project, asset, and file metadata). |
|  `output` and `payload.fields`  | Only the mapped fields you selected, as in publish mode. Use this when the function expects a specific request shape. For an example, see [Processing changed files and writing results back](connector-fan-out-write-back.md). |

The Lambda function processes the input and returns a JSON response. SDMA applies output routing to that response — writing fields to metadata attributes, ingesting derived files, or both.

### Example – invoke an analysis function and write results back
<a name="_example-invoke-an-analysis-function-and-write-results-back"></a>

```
{
  "securityConfig": {
    "type": "AssumeRole",
    "assumeRoleArn": "arn:aws:iam::<account-id>:role/SpatialDataManagementContentDerivation-Lambda"
  },
  "lambdaConfig": {
    "functionArn": "arn:aws:lambda:<region>:<account-id>:function:analyze-content"
  },
  "defaultStepConfig": {
    "stepType": "lambdaInvoke"
  },
  "triggers": [
    {
      "description": "Analyze uploaded files and write quality scores back",
      "resources": ["asset"],
      "events": ["uploadComplete"],
      "steps": [
        {
          "output": {
            "metadataAttributes": {
              "fieldMappings": [
                { "source": "qualityScore", "target": "asset.metadataAttributes.qualityScore:number" },
                { "source": "classification", "target": "asset.metadataAttributes.classification" }
              ]
            }
          }
        }
      ]
    }
  ]
}
```

The function receives the full resource metadata (project, asset, files) and returns a JSON object. The `output.metadataAttributes.fieldMappings` extract `qualityScore` and `classification` from the response and write them as typed metadata attributes on the asset.

**Note**
Without `payload.fields`, you do not need connector-level `fieldMappings` — the function receives the full resource context automatically. The `output` block’s `fieldMappings` control what comes back from the response, not what goes into the payload.

### Returning files from the function
<a name="lambda-response-files"></a>

Besides values for `fieldMappings`, the response can list derived files for SDMA to ingest, under a top-level `derivedFiles` key. The step needs an `output` block for SDMA to read the response. External systems that post a result through `UpdateConnectorInvocation` use the same entry shape. Each entry takes one of three forms:

| Form | Fields | What SDMA does |
| --- | --- | --- |
| Single object |  `s3Uri`, optional `path`, `mtime`, `hash`  | Reads the object, hashes it, and copies it into the content store. SDMA verifies a `hash` you supply instead of trusting it. |
| Prefix |  `s3UriPrefix`, optional `filter`, `path`, `mtime`  | Lists the objects under the prefix, keeps those that match `filter`, and treats each as a single object. The prefix must include at least one path segment; a whole bucket is rejected. |
| Already in place |  `path`, `hash`, `size`, `mtime`  | The producer already wrote the bytes to their key in the content store, so SDMA copies nothing. SDMA checks that the object exists. |

The following JSON shows a `derivedFiles` response with a single-object entry and a prefix entry:

```
{
  "derivedFiles": [
    { "s3Uri": "s3://amzn-s3-demo-bucket/jobs/123/preview.glb", "path": "preview.glb" },
    { "s3UriPrefix": "s3://amzn-s3-demo-bucket/jobs/123/tiles/", "filter": { "fileExtensionFilter": ".png" } }
  ]
}
```

When the source bucket needs a different role, add `securityConfig` to the entry with `assumeRoleArn`, and optionally `externalId` and `sessionName`. It replaces the connector’s security configuration for that entry’s reads. It is not accepted on the already-in-place form.

## Keeping payloads within the Lambda limits
<a name="lambda-payload-size"></a>

AWS Lambda limits how much data a single invocation can carry. SDMA measures each payload before it calls the function.

| What | Limit | What happens if it is larger |
| --- | --- | --- |
| Request, `RequestResponse` invocation | 6 MB | The step fails with `ConnectorPayloadTooLarge` before the function is called. |
| Request, `Event` invocation | 256 KB | The step fails with `ConnectorPayloadTooLarge` before the function is called. |
| Response from the function | 6 MB | Lambda returns an error instead of the response, and the step fails. |

The `ConnectorPayloadTooLarge` error reports the payload size, the limit, and the largest list in the payload, such as a list of files. That list is usually the one to reduce.

A payload most often grows too large when the step has an `output` block and no `payload.fields`. The function then receives the complete resource context, which includes every file in the asset. An asset with thousands of files can exceed the limit even though each file’s metadata is small.

To keep a payload within the limits, use one or more of the following approaches:
+  **Send only the fields the function needs.** Set `payload.fields` to the values the function reads. For more information, see [Using Lambda as a content producer (deriver)](#lambda-as-deriver).
+  **Split the work.** Use `applyTo` with a `batchSize` so that each invocation handles some of the files rather than all of them. For more information, see [Running steps per file](connector-configuration.md#trigger-apply-to).
+  **Pass a location, not the data.** Write the request to Amazon S3 with an `s3PutObject` step, and send the function the object’s location. The function reads the request from Amazon S3. For an example of this approach, see [Connector patterns for models and pipelines](connector-patterns.md).
+  **Return files by location.** Write large results to Amazon S3, and return them as `derivedFiles` entries with `s3Uri` or `s3UriPrefix`, rather than in the response body. For more information, see [Returning files from the function](#lambda-response-files).
+  **Use `RequestResponse` for large requests.** An `Event` invocation accepts much less data than a `RequestResponse` invocation.

## Using Lambda as a step type in multi-step triggers
<a name="lambda-as-step-type"></a>

The `lambdaInvoke` step type can appear in multi-step triggers alongside other step types. For example, a trigger might call a REST API, then invoke a Lambda function to post-process the result:

```
"steps": [
  {
    "stepType": "rest",
    "method": "POST",
    "path": "/api/analyze",
    "body": { "assetId": "${asset.assetId}" },
    "responseFieldMapping": [
      { "source": "jobId", "target": "$temp.jobId" }
    ]
  },
  {
    "stepType": "lambdaInvoke",
    "lambdaConfig": {
      "functionArn": "arn:aws:lambda:<region>:<account-id>:function:post-process"
    }
  }
]
```

## Configuration fields
<a name="lambda-config-fields"></a>

| Field | Required | Description |
| --- | --- | --- |
|  `lambdaConfig.functionArn`  | Yes | ARN of the Lambda function to invoke. |
|  `lambdaConfig.region`  | No | AWS Region of the Lambda function. Defaults to the SDMA deployment region. |
|  `lambdaConfig.invocationType`  | No |  `RequestResponse` (default) waits for the function and reads its response. `Event` hands the payload to Lambda and returns without waiting, so there is no response to route; use it for publish-only steps. |
|  `securityConfig`  | Yes | Connector-level authentication configuration, a sibling of `lambdaConfig`. Must use `AssumeRole` type. |
|  `payload.fields`  | No | Array of field names to include in the payload. If omitted, a publish step sends all mapped fields, and a step with `output` sends the complete resource context. |
|  `output`  | No | Output routing configuration. When present, switches to derive mode. See [Output routing](connector-configuration.md#output-routing). |
|  `securityConfig`  | No | Step-level security config that overrides the connector-level config. |
