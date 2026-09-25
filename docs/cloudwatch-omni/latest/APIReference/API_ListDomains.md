---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListDomains.html
---

# ListDomains
<a name="API_ListDomains"></a>

Returns the caller's domains: the account-scoped domain and the organization-scoped domain, if either exists. At most two domains are returned.

## Request Parameters
<a name="API_ListDomains_RequestParameters"></a>

 ** maxResults **
The maximum number of domains to return per page. Defaults to 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** nextToken **
A token to retrieve the next page of results. Tokens expire after 24 hours.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Elements
<a name="API_ListDomains_ResponseElements"></a>

The following elements are returned by the service.

 ** items **
The list of domain summaries.
Type: Array of [DomainSummary](API_DomainSummary.md) objects

 ** nextToken **
A token to retrieve the next page of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListDomains_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform this action.
HTTP Status Code: 403

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
<a name="API_ListDomains_Examples"></a>

### List domains
<a name="API_ListDomains_Example_1"></a>

The following example lists the caller's domains. At most two are returned — the account-scoped domain and the organization-scoped domain — so there is no nextToken. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_ListDomains_Example_1_Request"></a>

```
{}
```

#### Sample Response
<a name="API_ListDomains_Example_1_Response"></a>

```
{
  "items": [
    {
      "createdAt": "2026-09-16T14:22:31Z",
      "domainArn": "arn:aws:cloudwatch:us-east-1:123456789012:domain/d-1a2b3c4d5e",
      "domainId": "d-1a2b3c4d5e",
      "identityCenterInstanceArn": "arn:aws:sso:::instance/ssoins-1234567890abcdef",
      "name": "prod-observability",
      "region": "us-east-1",
      "status": "ACTIVE",
      "updatedAt": "2026-09-16T14:22:31Z"
    },
    {
      "createdAt": "2026-09-16T14:22:31Z",
      "domainArn": "arn:aws:cloudwatch:us-east-1:123456789012:organization-domain/d-9z8y7x6w5v",
      "domainId": "d-9z8y7x6w5v",
      "identityCenterInstanceArn": "arn:aws:sso:::instance/ssoins-1234567890abcdef",
      "name": "prod-observability-org",
      "region": "us-east-1",
      "status": "ACTIVE",
      "updatedAt": "2026-09-16T14:22:31Z"
    }
  ]
}
```

## See Also
<a name="API_ListDomains_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/ListDomains)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/ListDomains)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/ListDomains)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/ListDomains)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/ListDomains)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/ListDomains)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/ListDomains)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/ListDomains)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/ListDomains)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/ListDomains)
