---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateView.html
---

# CreateView
<a name="API_CreateView"></a>

Creates a new SQL view.

A view is a named, reusable SQL query that can be referenced from telemetry queries. View names must be unique within the account and region. Only USER views can be created — MANAGED views are provisioned by AWS.

## Request Parameters
<a name="API_CreateView_RequestParameters"></a>

 ** clientToken **
Idempotency token for safe retries. Retrying with the same token returns the original view instead of creating a duplicate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** definition **
The SQL query that defines the view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: Yes

 ** description **
A description of the view.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** name **
The name of the view. Must begin with the "view." prefix. View names must be unique within the account and region.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 256.
Pattern: `view\.[a-z0-9][a-z0-9_-]{0,250}`
Required: Yes

 ** tags **
Resource tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Elements
<a name="API_CreateView_ResponseElements"></a>

The following elements are returned by the service.

 ** arn **
The ARN of the view.
Type: String

 ** createdAt **
The timestamp when the view was created.
Type: Timestamp

 ** definition **
The SQL query that defines the view.
Type: String

 ** description **
The description of the view.
Type: String

 ** name **
The name of the view.
Type: String

 ** type **
The ownership category of the view.
Type: String
Valid Values: `USER | MANAGED`

 ** updatedAt **
The timestamp when the view was last updated.
Type: Timestamp

## Errors
<a name="API_CreateView_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The operation could not be completed because of a conflict with the current state of the resource.
 ** conflictType **
The type of conflict that caused the request to fail. Not always present.
 ** errorCode **
The error code associated with the conflict. Not always present.
 ** message **
A human-readable description of the conflict.
 ** resourceId **
The identifier of the resource that is in conflict. Not always present.
 ** resourceType **
The type of the resource that is in conflict. Not always present.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** errorCode **
The error code associated with the internal error.
HTTP Status Code: 500

 ** ThrottlingException **
The request was throttled due to exceeding the allowed request rate.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request. Not always present.
HTTP Status Code: 429

 ** ValidationException **
A parameter is specified incorrectly.
 ** errorCode **
The error code associated with the validation failure.
HTTP Status Code: 400

## Examples
<a name="API_CreateView_Examples"></a>

### Create a view
<a name="API_CreateView_Example_1"></a>

The following example creates a user view that saves an error-count-by-service query. View names must begin with the view. prefix and be unique within the account and Region. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_CreateView_Example_1_Request"></a>

```
{
  "clientToken": "3f2a9c1e-7b04-4d8a-9e15-6c2b8d0f4a73",
  "definition": "SELECT resource['attributes']['service.name'] AS service, COUNT(*) AS error_count FROM "logs.default" WHERE severityText = 'ERROR' GROUP BY service",
  "description": "Error counts by service",
  "name": "view.service_errors",
  "tags": {
    "Team": "observability"
  }
}
```

#### Sample Response
<a name="API_CreateView_Example_1_Response"></a>

```
{
  "arn": "arn:aws:cloudwatch:us-east-1:123456789012:view/view.service_errors",
  "createdAt": "2026-09-16T14:22:31Z",
  "definition": "SELECT resource['attributes']['service.name'] AS service, COUNT(*) AS error_count FROM "logs.default" WHERE severityText = 'ERROR' GROUP BY service",
  "description": "Error counts by service",
  "name": "view.service_errors",
  "type": "USER",
  "updatedAt": "2026-09-16T14:22:31Z"
}
```

## See Also
<a name="API_CreateView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/CreateView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/CreateView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/CreateView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/CreateView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/CreateView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/CreateView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/CreateView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/CreateView)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/CreateView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/CreateView)
