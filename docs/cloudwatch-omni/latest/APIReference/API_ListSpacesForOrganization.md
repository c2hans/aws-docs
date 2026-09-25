---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListSpacesForOrganization.html
---

# ListSpacesForOrganization
<a name="API_ListSpacesForOrganization"></a>

Returns the spaces across all member accounts in the organization.

## Request Parameters
<a name="API_ListSpacesForOrganization_RequestParameters"></a>

 ** maxResults **
The maximum number of spaces to return per page. Defaults to 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** nextToken **
A token to retrieve the next page of results. Tokens expire after 24 hours.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Elements
<a name="API_ListSpacesForOrganization_ResponseElements"></a>

The following elements are returned by the service.

 ** items **
The list of space summaries.
Type: Array of [SpaceSummary](API_SpaceSummary.md) objects

 ** nextToken **
A token to retrieve the next page of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListSpacesForOrganization_Errors"></a>

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
<a name="API_ListSpacesForOrganization_Examples"></a>

### List spaces across the organization
<a name="API_ListSpacesForOrganization_Example_1"></a>

The following example lists the first page of spaces across all member accounts in the organization. The results include spaces owned by different accounts, along with a nextToken to retrieve the next page. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_ListSpacesForOrganization_Example_1_Request"></a>

```
{
  "maxResults": 50
}
```

#### Sample Response
<a name="API_ListSpacesForOrganization_Example_1_Response"></a>

```
{
  "items": [
    {
      "createdAt": "2026-09-16T14:22:31Z",
      "name": "prod-observability",
      "ownerAccountId": "111122223333",
      "region": "us-east-1",
      "spaceArn": "arn:aws:cloudwatch:us-east-1:111122223333:space/c1d2e3f4-5a6b-4c7d-8e9f-0a1b2c3d4e5f",
      "spaceId": "c1d2e3f4-5a6b-4c7d-8e9f-0a1b2c3d4e5f",
      "status": "ACTIVE",
      "updatedAt": "2026-09-16T14:22:31Z"
    },
    {
      "createdAt": "2026-09-16T14:22:31Z",
      "name": "prod-observability",
      "ownerAccountId": "444455556666",
      "region": "us-east-1",
      "spaceArn": "arn:aws:cloudwatch:us-east-1:444455556666:space/d4e5f6a7-8b9c-4d0e-8f1a-2b3c4d5e6f7a",
      "spaceId": "d4e5f6a7-8b9c-4d0e-8f1a-2b3c4d5e6f7a",
      "status": "ACTIVE",
      "updatedAt": "2026-09-16T14:22:31Z"
    }
  ],
  "nextToken": "eyJvZmZzZXQiOjIwfQ=="
}
```

## See Also
<a name="API_ListSpacesForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/ListSpacesForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/ListSpacesForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/ListSpacesForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/ListSpacesForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/ListSpacesForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/ListSpacesForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/ListSpacesForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/ListSpacesForOrganization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/ListSpacesForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/ListSpacesForOrganization)
