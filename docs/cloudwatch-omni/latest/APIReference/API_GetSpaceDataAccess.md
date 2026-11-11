---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetSpaceDataAccess.html
---

# GetSpaceDataAccess
<a name="API_GetSpaceDataAccess"></a>

Returns temporary credentials for working with data in a space, limited to the actions you request.

The credentials allow only the requested actions that can be granted in the space and that your access grants allow. Requested actions that cannot be conferred are ignored rather than rejected.

## Request Parameters
<a name="API_GetSpaceDataAccess_RequestParameters"></a>

 ** auditContext **
Caller-supplied key-value pairs that are recorded for auditing. They do not affect authorization or the permissions of the credentials.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[A-Za-z0-9_.:/=+@-]+(?![\s\S]).*`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `[^\u0000-\u001F\u007F-\u009F]+(?![\s\S]).*`
Required: No

 ** durationSeconds **
The lifetime of the credentials, in seconds. Defaults to 3600.
Type: Integer
Valid Range: Minimum value of 900. Maximum value of 3600.
Required: No

 ** spaceId **
The unique ID of the space to return credentials for.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** targetScopes **
The actions to include in the credentials, grouped by service.
Type: Array of [DataAccessTarget](API_DataAccessTarget.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## Response Elements
<a name="API_GetSpaceDataAccess_ResponseElements"></a>

The following element is returned by the service.

 ** credentials **
The temporary AWS credentials for the space.
Type: [AwsCredentials](API_AwsCredentials.md) object

## Errors
<a name="API_GetSpaceDataAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** errorCode **
The error code associated with the internal error.
HTTP Status Code: 500

 ** PolicyTooLargeException **
The requested actions produce a credential that exceeds the maximum size. Request fewer actions.
 ** message **
A description of the error.
HTTP Status Code: 400

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
<a name="API_GetSpaceDataAccess_Examples"></a>

### Get data credentials for log queries
<a name="API_GetSpaceDataAccess_Example_1"></a>

The following example requests credentials that allow running log queries and reading metric data in a space. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_GetSpaceDataAccess_Example_1_Request"></a>

```
{
  "auditContext": {
    "source": "logs-console"
  },
  "durationSeconds": 3600,
  "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
  "targetScopes": [
    {
      "actions": [
        "logs:StartQuery",
        "logs:GetQueryResults"
      ]
    },
    {
      "actions": [
        "cloudwatch:GetMetricData"
      ]
    }
  ]
}
```

#### Sample Response
<a name="API_GetSpaceDataAccess_Example_1_Response"></a>

```
{
  "credentials": {
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "expiration": "2026-10-20T19:22:31Z",
    "secretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    "sessionToken": "EXAMPLE-SESSION-TOKEN"
  }
}
```

## See Also
<a name="API_GetSpaceDataAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/GetSpaceDataAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/GetSpaceDataAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/GetSpaceDataAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/GetSpaceDataAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/GetSpaceDataAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/GetSpaceDataAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/GetSpaceDataAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/GetSpaceDataAccess)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/GetSpaceDataAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/GetSpaceDataAccess)
