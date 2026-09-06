---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connector-lambda.html
---

# AWS Lambda connector
<a name="connector-lambda"></a>

The AWS Lambda connector invokes Lambda functions with resource metadata as the payload. It is a dual-mode primitive — it can publish data outward to a Lambda function, or derive content by invoking a function and routing the response back into the asset record as metadata attributes or derived files.

Use this connector type when the integration requires custom code — transformations, validations, enrichment logic, or processing that cannot be expressed through the declarative configuration of other step types.

Step type: `lambdaInvoke`

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
               "<CONNECTOR_INVOCATION_ROLE_ARN>",
               "<ASYNC_CONNECTOR_INVOCATION_ROLE_ARN>"
             ]
           },
           "Action": "sts:AssumeRole"
         }
       ]
     }
     ```

     Replace `<CONNECTOR_INVOCATION_ROLE_ARN>` and `<ASYNC_CONNECTOR_INVOCATION_ROLE_ARN>` with the execution role ARNs of the connector invocation Lambda functions in your SDMA deployment.

     If you have AWS CLI access, you can find these values by running:

     ```
     aws lambda get-function \
       --function-name SpatialDataManagement-ConnectorInvocationFunction \
       --query 'Configuration.Role' --output text

     aws lambda get-function \
       --function-name SpatialDataManagement-ConnectorInvocationAsyncFunction \
       --query 'Configuration.Role' --output text
     ```

     Alternatively, in the [Lambda console](https://console.aws.amazon.com/lambda/), open the `SpatialDataManagement-ConnectorInvocationFunction` and `SpatialDataManagement-ConnectorInvocationAsyncFunction` functions and find the role name for each under **Configuration** > **Permissions**. Use these names to construct the full ARNs (for example, `arn:aws:iam::<ACCOUNT_ID>:role/<CONNECTOR_INVOCATION_ROLE_NAME>`).
   +  **Permissions policy** must grant `lambda:InvokeFunction` on the target function:

     ```
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": "lambda:InvokeFunction",
           "Resource": "arn:aws:lambda:<REGION>:<ACCOUNT_ID>:function:<FUNCTION_NAME>"
         }
       ]
     }
     ```

## Using Lambda as a publisher
<a name="lambda-as-publisher"></a>

In publish mode, the connector builds a payload from field mappings and invokes the function. The function receives only the mapped fields — not the full resource metadata. No output routing is applied; the function’s response is not written back to the asset record.

### Example: invoke a processing function on asset creation
<a name="_example-invoke-a-processing-function-on-asset-creation"></a>

```
{
  "defaultStepConfig": {
    "stepType": "lambdaInvoke",
    "lambdaConfig": {
      "functionArn": "arn:aws:lambda:<REGION>:<ACCOUNT_ID>:function:process-asset",
      "securityConfig": {
        "type": "AssumeRole",
        "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentPublisher-Lambda"
      }
    }
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

In derive mode, the connector sends the full resource metadata to the function and routes the response back into the asset record. This is triggered by adding an `output` block to the step. When `output` is present, SDMA automatically switches to derive mode — sending the complete resource context (project, asset, file metadata) as the payload instead of the field-mapped subset.

The Lambda function processes the input and returns a JSON response. SDMA applies output routing to that response — writing fields to metadata attributes, ingesting derived files, or both.

### Example: invoke an analysis function and write results back
<a name="_example-invoke-an-analysis-function-and-write-results-back"></a>

```
{
  "defaultStepConfig": {
    "stepType": "lambdaInvoke",
    "lambdaConfig": {
      "functionArn": "arn:aws:lambda:<REGION>:<ACCOUNT_ID>:function:analyze-content",
      "securityConfig": {
        "type": "AssumeRole",
        "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentDerivation-Lambda"
      }
    }
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
In derive mode, you do not need connector-level `fieldMappings` — the function receives the full resource context automatically. The `output` block’s `fieldMappings` control what comes back from the response, not what goes into the payload.

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
      "functionArn": "arn:aws:lambda:<REGION>:<ACCOUNT_ID>:function:post-process"
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
|  `lambdaConfig.securityConfig`  | Yes | Authentication configuration. Must use `AssumeRole` type. |
|  `payload.fields`  | No | Array of field names to include in the payload (publish mode only). If omitted, all mapped fields are included. |
|  `output`  | No | Output routing configuration. When present, switches to derive mode. See [Output routing](connector-configuration.md#output-routing). |
|  `securityConfig`  | No | Step-level security config that overrides the connector-level config. |
