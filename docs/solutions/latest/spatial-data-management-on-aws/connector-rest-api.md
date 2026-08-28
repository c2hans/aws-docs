---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connector-rest-api.html
---

# Working with REST APIs
<a name="connector-rest-api"></a>

The REST API connector sends resource metadata to external REST endpoints. It supports all HTTP methods and works for both publishing and synchronization.

## Prerequisites
<a name="rest-prerequisites"></a>

1. Identify the target REST API endpoint URL.

1. Determine the authentication method. The REST connector supports:
   +  **API key** – Stored in AWS Secrets Manager
   +  **OAuth 2.0 / Token auth** – Client credentials flow through a token endpoint
   +  **Basic authentication** – Username and password stored in AWS Secrets Manager
   +  **IAM role assumption** – For AWS service endpoints

1. If using API key or token auth, store the credentials in AWS Secrets Manager.

1. Create an IAM role with the following:
   +  **Role name** must start with `SpatialDataManagementContentPublisher-` (for example, `SpatialDataManagementContentPublisher-MyRestConnector`).
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
   +  **Permissions policy** must grant access to the Secrets Manager secret (if using API key, token, or basic auth):

     ```
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": "secretsmanager:GetSecretValue",
           "Resource": "arn:aws:secretsmanager:<REGION>:<ACCOUNT_ID>:secret:<SECRET_NAME>"
         }
       ]
     }
     ```

## Step types
<a name="rest-step-types"></a>

The REST API connector supports the following step type.

| Step type | Description |
| --- | --- |
|  `rest`  | Executes an HTTP request to the configured endpoint. Supports GET, POST, PUT, PATCH, and DELETE methods. The HTTP method, path, headers, and body are configurable per step. |

## Create this connector
<a name="rest-create"></a>

1. In the Spatial Data Portal, go to **Library settings** > **Connectors**.

1. Choose the **Publish content** tab (or **Derive content** if using REST API import for derivation).

1. Choose **Create publisher** (or **Create deriver**).

1. Enter a connector name.

1. For **Connector type**, select **REST API** (or **REST API import** for derivation).

1. Paste the connector configuration JSON (see below) into the JSON editor.

1. Choose **Create**.

## Configuration
<a name="rest-configuration"></a>

```
{
  "restConfig": {
    "apiBase": "https://api.example.com/v1",
    "securityConfig": {
      "type": "ApiKey",
      "secretArn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:my-api-key"
    }
  },
  "fieldMappings": [
    { "source": "asset.assetId", "target": "externalId" },
    { "source": "asset.assetName", "target": "title" }
  ],
  "triggers": [
    {
      "description": "Create record in external system on asset creation",
      "resources": ["asset"],
      "events": ["create"],
      "stepType": "rest",
      "steps": [{
        "restConfig": {
          "method": "POST",
          "path": "/records"
        }
      }]
    },
    {
      "description": "Update record on asset update",
      "resources": ["asset"],
      "events": ["update"],
      "stepType": "rest",
      "steps": [{
        "restConfig": {
          "method": "PUT",
          "path": "/records/${project.connectedResource.externalId}"
        }
      }]
    },
    {
      "description": "Delete record on asset deletion",
      "resources": ["asset"],
      "events": ["delete"],
      "stepType": "rest",
      "steps": [{
        "restConfig": {
          "method": "DELETE",
          "path": "/records/${project.connectedResource.externalId}"
        }
      }]
    }
  ]
}
```

## Configuration fields
<a name="rest-config-fields"></a>

The following table describes the configuration fields for the REST API connector.

### Connector-level fields (`restConfig`)
<a name="_connector-level-fields-restconfig"></a>

| Field | Required | Description |
| --- | --- | --- |
|  `restConfig.apiBase`  | Yes | Base URL for the REST API (for example, `https://api.example.com/v1`). |
|  `restConfig.securityConfig`  | Yes | Authentication configuration. Supports `ApiKey`, `TokenAuth`, `BasicAuth`, and `AssumeRole` types. |
|  `restConfig.headers`  | No | Default HTTP headers included in every request. Values are strings. |
|  `restConfig.queryParams`  | No | Default query parameters included in every request. Values support `${variable}` substitution. |
|  `restConfig.allowMultilineInSubstitution`  | No | When `true`, variable substitution preserves single quotes, tabs, newlines, and carriage returns in request body values. Use this when substituting multi-line content such as SQL or WKT. URL path and query-string substitution remains strict regardless of this flag. Defaults to `false`. |
|  `restConfig.initialize`  | No | Session initialization configuration. See [Session initialization](#rest-session-initialization). |
|  `restConfig.sampling`  | No | Sampling configuration. See [Sampling](#rest-sampling). |
|  `fieldMappings`  | No | Default field mappings for request body construction. |

### Step-level fields
<a name="_step-level-fields"></a>

| Field | Required | Description |
| --- | --- | --- |
|  `method`  | Yes | HTTP method (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`). |
|  `path`  | Yes | URL path appended to `apiBase`. Supports `${variable}` substitution. |
|  `headers`  | No | Per-step HTTP headers. Merged with connector-level headers; step-level values override connector-level values for the same header name. |
|  `queryParams`  | No | Per-step query parameters with `${variable}` substitution. Appended to the request URL. |
|  `body`  | No | A JSON body template with `${variable}` references that are resolved at execution time. Use this when the request body structure differs from what field mappings produce. |
|  `bodyFromFile`  | No | Sends binary file content as the request body instead of a JSON payload. See [Sending file content as the request body](#rest-body-from-file). |
|  `fieldMappings`  | No | Step-level field mappings that override connector-level mappings. |
|  `responseFieldMapping`  | No | Maps fields from the API response to `$temp.*` variables (for use in subsequent steps) or to connected resource fields. |
|  `payload.fields`  | No | Array of target field names to include in the output. If omitted, all mapped fields are included. |
|  `securityConfig`  | No | Step-level security config that overrides the connector-level config. |
|  `retryCount`  | No | Maximum number of retry attempts for this step. |
|  `sleepTime`  | No | Seconds to wait between retries. |
|  `successConditions`  | No | Custom success criteria. Use `expectSuccess: false` with `responseMatch` to wait for a specific response (for example, polling until a resource is deleted). |
|  `onError`  | No | Error handling: `fail` (default) or `record-and-continue`. |

## Connected resources
<a name="rest-connected-resources"></a>

When a REST `POST` or `PUT` step creates or updates a record in an external system, SDMA automatically captures the external ID from the response. This stored ID is called a *connected resource* and you can reference it in subsequent steps.

### How it works
<a name="_how-it-works"></a>

1. A `POST` step sends a request to the external API (for example, `POST /records`).

1. SDMA inspects the JSON response and looks for an ID field. It checks the following field names in order: `id`, `_id`, `projectId`, `assetId`, `fileId`, `externalId`, `resourceId`.

1. SDMA stores the first matching field as a connected resource, linked to the connector and the SDMA resource (project or asset).

1. On subsequent update or delete triggers, you can reference the stored ID using `${project.connectedResource.<field>}` in step paths or other interpolated fields.

### Controlling the stored field name
<a name="_controlling-the-stored-field-name"></a>

Use `responseFieldMapping` in the step to control which response field SDMA captures and what name SDMA stores it under:

```
{
  "method": "POST",
  "path": "/records",
  "responseFieldMapping": [
    { "source": "id", "target": "project.externalRecordId" }
  ]
}
```

In this example, SDMA stores the `id` field from the API response as `externalRecordId`. You can then reference it as `${project.connectedResource.externalRecordId}` in later steps.

### Example
<a name="_example"></a>

In the full configuration example above, the `POST /records` step creates a record. The external API returns a response containing an `externalId` field. SDMA stores this value automatically. The update and delete triggers then use `${project.connectedResource.externalId}` in their paths to target the correct external record.

## Sending file content as the request body
<a name="rest-body-from-file"></a>

The `bodyFromFile` step field sends binary file content directly as the HTTP request body instead of a JSON payload constructed from field mappings. Use this when an external API expects the raw file content — for example, uploading a derived file to a third-party system.

```
{
  "stepType": "rest",
  "method": "PUT",
  "path": "/models/${file.metadataAttributes.modelId}/${derivedfile.name}",
  "bodyFromFile": {
    "contentType": "application/octet-stream"
  }
}
```
+  `contentType` — (Optional) The `Content-Type` header value for the request. If omitted, no explicit content type is set.
+  `parseAndReSerializeJson` — (Optional) When `true`, reads the file content as JSON, parses it, and re-serializes it before sending. Use this when the file contains JSON that needs to be sent as a structured request body rather than raw bytes. Defaults to `false`.

When `bodyFromFile` is present, SDMA reads the file content from the asset’s content-addressable storage using the file hash from the resource metadata. SDMA ignores the `body` and `fieldMappings` fields for that step.

## Request body templates
<a name="rest-body-template"></a>

The `body` step field provides a JSON body template with `${variable}` references that SDMA resolves at execution time. Use this when the request body structure differs from what field mappings produce. For example, use `body` when the external API expects a specific JSON shape with nested objects or when you need to include values from `$temp.*` variables set by previous steps.

```
{
  "method": "POST",
  "path": "/v1/jobs",
  "body": {
    "imageUrl": "${file.contentUrl}",
    "assetId": "${asset.assetId}",
    "options": {
      "quality": "high"
    }
  }
}
```

SDMA scans each string value in the body for `${variable}` references and resolves them against resource metadata and `$temp.*` variables. Non-string values (numbers, booleans, nested objects without variables) pass through unchanged.

**Note**
 `body` and `fieldMappings` serve different purposes. Field mappings construct a flat or nested payload from source/target pairs and are the standard approach for most connectors. `body` is for cases where you need explicit control over the JSON structure. If both are present, `body` takes precedence.

## SIGv4 signing for AWS service endpoints
<a name="rest-sigv4"></a>

When the security config type is `AssumeRole`, SDMA signs all HTTP requests with [AWS Signature Version 4 (SIGv4)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) using the assumed role’s credentials. This allows REST connectors to call AWS service endpoints directly — for example, Amazon SageMaker inference endpoints, AWS Lambda function URLs, or Amazon Bedrock APIs.

SDMA determines the AWS service name for signing from the endpoint hostname:
+ Hostnames containing `sagemaker` → signed as `sagemaker`
+ Hostnames containing `lambda` → signed as `lambda`
+ Hostnames containing `bedrock` → signed as `bedrock`
+ All other hostnames → signed as `execute-api` (suitable for Amazon API Gateway endpoints)

```
{
  "restConfig": {
    "apiBase": "https://runtime.sagemaker.us-west-2.amazonaws.com",
    "securityConfig": {
      "type": "AssumeRole",
      "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentPublisher-SageMaker"
    }
  }
}
```

The assumed role must have permissions to invoke the target AWS service endpoint.

## Session initialization
<a name="rest-session-initialization"></a>

Some REST APIs require a session handshake before accepting requests. The `restConfig.initialize` block configures this. When present, SDMA sends a POST request to the specified endpoint before the first step executes and captures a session token from the response to include in all subsequent requests.

```
"restConfig": {
  "apiBase": "https://api.example.com",
  "initialize": {
    "path": "/session",
    "body": { "capabilities": {} },
    "sessionHeader": "X-Session-Id",
    "sessionField": "result.sessionId"
  },
  "securityConfig": { "..." }
}
```
+  `path` — The initialization endpoint path, appended to `apiBase`.
+  `body` — The JSON body to send in the initialization POST request.
+  `sessionHeader` — The response header name containing the session token.
+  `sessionField` — (Optional) Dot-notation path to extract the session token from the response body, used as a fallback when the token is not in a header.

Session initialization runs once per connector invocation. If initialization fails, the connector invocation fails.

## Sampling
<a name="rest-sampling"></a>

The `restConfig.sampling` block enables SDMA to respond to text-generation callbacks from external APIs that support this pattern. When configured, SDMA invokes a configured provider to generate a response and returns it to the external API before continuing with the connector step.

```
"restConfig": {
  "sampling": {
    "modelId": "abcd-20240307-v1:0",
    "securityConfig": {
      "type": "AssumeRole",
      "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentPublisher-Model"
    }
  }
}
```

Sampling requires session initialization (`restConfig.initialize`).

## Safety and limits
<a name="rest-safety"></a>

The REST API client enforces the following safety measures:
+  **SSRF protection** — Requests to internal IP addresses (EC2 metadata service at `169.254.169.254`, link-local addresses, and loopback addresses) are blocked. Non-HTTP schemes are also blocked.
+  **Response size limit** — Responses larger than 100 MB are rejected. For responses with a `Content-Length` header, the check happens before reading the body. For streamed responses without a `Content-Length` header, the body is read incrementally and the connection is terminated once the 100 MB limit is exceeded.
+  **Redirect blocking** — HTTP redirects are not followed. This prevents open-redirect attacks where a malicious endpoint redirects the connector to an internal resource.
+  **Automatic retries** — The client retries failed requests with exponential backoff for transient errors (connection errors, 429 Too Many Requests, 500/502/503/504 server errors).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
