---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetView.html
---

# GetView
<a name="API_GetView"></a>

Returns the definition and metadata of the specified view.

## Request Parameters
<a name="API_GetView_RequestParameters"></a>

 ** name **
The name of the view.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 256.
Pattern: `view\.[a-z0-9][a-z0-9_-]{0,250}`
Required: Yes

## Response Elements
<a name="API_GetView_ResponseElements"></a>

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
<a name="API_GetView_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** errorCode **
The error code associated with the internal error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** errorCode **
The error code associated with the failure.
 ** resourceId **
The identifier of the resource that could not be found. Not always present.
 ** resourceType **
The type of the resource that could not be found. Not always present.
HTTP Status Code: 404

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
<a name="API_GetView_Examples"></a>

### Get a view
<a name="API_GetView_Example_1"></a>

The following example returns the definition and metadata of a view. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_GetView_Example_1_Request"></a>

```
{
  "name": "view.service_errors"
}
```

#### Sample Response
<a name="API_GetView_Example_1_Response"></a>

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
<a name="API_GetView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/GetView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/GetView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/GetView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/GetView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/GetView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/GetView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/GetView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/GetView)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/GetView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/GetView)
