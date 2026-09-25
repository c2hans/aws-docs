---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_SearchPrincipals.html
---

# SearchPrincipals
<a name="API_SearchPrincipals"></a>

Searches Identity Center for users and groups in a domain. The domain must be configured with Identity Center.

To grant access to a result, pass its principalId to CreateAccessGrant with a principalType of IDC\_USER for a user or IDC\_GROUP for a group.

## Request Parameters
<a name="API_SearchPrincipals_RequestParameters"></a>

 ** domainId **
The ID of the domain to search within.
Type: String
Pattern: `d-[0-9a-z]{1,25}`
Required: Yes

 ** maxResults **
The maximum number of results to return. Defaults to 10. Valid only when searchQuery is \*; other searches reject this parameter and return at most 10 results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** nextToken **
A token to retrieve the next page of results. Valid only when searchQuery is \*; other searches do not paginate and reject this parameter. Tokens expire after 24 hours.
Type: String
Required: No

 ** searchQuery **
A search term to match against user names, display names, and IDs. Pass \* to list all principals. Maximum 128 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Response Elements
<a name="API_SearchPrincipals_ResponseElements"></a>

The following elements are returned by the service.

 ** nextToken **
A token to retrieve the next page of results, or null if there are no more results.
Type: String

 ** results **
The list of matching principals.
Type: Array of [PrincipalSearchResult](API_PrincipalSearchResult.md) objects

## Errors
<a name="API_SearchPrincipals_Errors"></a>

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
<a name="API_SearchPrincipals_Examples"></a>

### Search principals by name
<a name="API_SearchPrincipals_Example_1"></a>

The following example searches a domain for principals whose name matches a text query. A text search (any searchQuery other than \*) returns at most 10 results and does not paginate, so maxResults and nextToken are not supplied and no nextToken is returned. To grant access to a result, pass its principalId to CreateAccessGrant with a principalType of IDC\_USER for a user or IDC\_GROUP for a group. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_SearchPrincipals_Example_1_Request"></a>

```
{
  "domainId": "d-1a2b3c4d5e",
  "searchQuery": "jane"
}
```

#### Sample Response
<a name="API_SearchPrincipals_Example_1_Response"></a>

```
{
  "results": [
    {
      "displayName": "Jane Doe",
      "principalId": "94b6c7d8-1a2b-4c3d-9e4f-5a6b7c8d9e0f",
      "principalType": "USER",
      "userName": "jane.doe"
    },
    {
      "displayName": "Jane's Analysts",
      "principalId": "2f5a8c1b-6d3e-4f7a-8b9c-0d1e2f3a4b5c",
      "principalType": "GROUP"
    }
  ]
}
```

## See Also
<a name="API_SearchPrincipals_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/SearchPrincipals)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/SearchPrincipals)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/SearchPrincipals)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/SearchPrincipals)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/SearchPrincipals)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/SearchPrincipals)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/SearchPrincipals)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/SearchPrincipals)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/SearchPrincipals)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/SearchPrincipals)
