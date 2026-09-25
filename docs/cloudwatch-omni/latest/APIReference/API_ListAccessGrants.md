---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListAccessGrants.html
---

# ListAccessGrants
<a name="API_ListAccessGrants"></a>

Returns AccessGrants, with optional filtering by domain, space, principal, or permission. A grant is returned only when it matches every filter supplied. With no filters, returns the grants for the current account and Region.

## Request Parameters
<a name="API_ListAccessGrants_RequestParameters"></a>

 ** domainId **
Filter by domain ID.
Type: String
Pattern: `d-[0-9a-z]{1,25}`
Required: No

 ** maxResults **
The maximum number of access grants to return per page. Defaults to 100. A page can contain fewer results than this value even when more results remain; continue while nextToken is present.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** nextToken **
A token to retrieve the next page of results. Supply the same filters used on the request that returned it. Tokens expire after 24 hours.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** permission **
Filter by permission level.
Type: String
Valid Values: `SPACE_ADMIN | READ | READ_WRITE_DELETE | CUSTOM`
Required: No

 ** principalId **
Filter by principal ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9:/_+=,.@-]*`
Required: No

 ** principalType **
Filter by principal type.
Type: String
Valid Values: `IDC_USER | IDC_GROUP | IAM_USER | IAM_ROLE | IAM_ROOT | ACCESS_PROFILE | ALERT | AGENT`
Required: No

 ** spaceId **
Filter by space ID.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## Response Elements
<a name="API_ListAccessGrants_ResponseElements"></a>

The following elements are returned by the service.

 ** items **
The list of access grant summaries.
Type: Array of [AccessGrantSummary](API_AccessGrantSummary.md) objects

 ** nextToken **
A token to retrieve the next page of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListAccessGrants_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform this action.
HTTP Status Code: 403

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
<a name="API_ListAccessGrants_Examples"></a>

### List access grants in a space
<a name="API_ListAccessGrants_Example_1"></a>

The following example lists the first page of access grants in a space and returns a nextToken to retrieve the next page. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_ListAccessGrants_Example_1_Request"></a>

```
{
  "domainId": "d-1a2b3c4d5e",
  "maxResults": 50,
  "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
}
```

#### Sample Response
<a name="API_ListAccessGrants_Example_1_Response"></a>

```
{
  "items": [
    {
      "domainId": "d-1a2b3c4d5e",
      "grantArn": "arn:aws:cloudwatch:us-east-1:123456789012:access-grant/7f3e9d21-4c8b-4f6a-b1d2-3e4f5a6b7c8d",
      "grantId": "7f3e9d21-4c8b-4f6a-b1d2-3e4f5a6b7c8d",
      "grantType": "CUSTOMER_MANAGED",
      "name": "analyst-read-access",
      "permission": "CUSTOM",
      "principal": {
        "principalId": "94b6c7d8-1a2b-4c3d-9e4f-5a6b7c8d9e0f",
        "principalType": "IDC_USER"
      },
      "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
    },
    {
      "domainId": "d-1a2b3c4d5e",
      "grantArn": "arn:aws:cloudwatch:us-east-1:123456789012:access-grant/8a1b2c3d-4e5f-4a6b-8c7d-9e0f1a2b3c4d",
      "grantId": "8a1b2c3d-4e5f-4a6b-8c7d-9e0f1a2b3c4d",
      "grantType": "CUSTOMER_MANAGED",
      "name": "oncall-read-write",
      "permission": "READ_WRITE_DELETE",
      "principal": {
        "principalId": "2f5a8c1b-6d3e-4f7a-8b9c-0d1e2f3a4b5c",
        "principalType": "IDC_GROUP"
      },
      "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
    }
  ],
  "nextToken": "eyJvZmZzZXQiOjIwfQ=="
}
```

## See Also
<a name="API_ListAccessGrants_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/ListAccessGrants)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/ListAccessGrants)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/ListAccessGrants)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/ListAccessGrants)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/ListAccessGrants)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/ListAccessGrants)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/ListAccessGrants)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/ListAccessGrants)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/ListAccessGrants)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/ListAccessGrants)
