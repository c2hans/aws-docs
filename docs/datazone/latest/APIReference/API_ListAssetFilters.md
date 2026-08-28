---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListAssetFilters.html
---

# ListAssetFilters
<a name="API_ListAssetFilters"></a>

Lists asset filters.

Prerequisites:
+ A valid domain and asset must exist.
+ The asset must have at least one filter created to return results.

## Request Syntax
<a name="API_ListAssetFilters_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/assets/{{assetIdentifier}}/filters?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAssetFilters_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetIdentifier](#API_ListAssetFilters_RequestSyntax) **   <a name="datazone-ListAssetFilters-request-uri-assetIdentifier"></a>
The ID of the data asset.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [domainIdentifier](#API_ListAssetFilters_RequestSyntax) **   <a name="datazone-ListAssetFilters-request-uri-domainIdentifier"></a>
The ID of the domain where you want to list asset filters.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListAssetFilters_RequestSyntax) **   <a name="datazone-ListAssetFilters-request-uri-maxResults"></a>
The maximum number of asset filters to return in a single call to `ListAssetFilters`. When the number of asset filters to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListAssetFilters` to list the next set of asset filters.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListAssetFilters_RequestSyntax) **   <a name="datazone-ListAssetFilters-request-uri-nextToken"></a>
When the number of asset filters is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of asset filters, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListAssetFilters` to list the next set of asset filters.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [status](#API_ListAssetFilters_RequestSyntax) **   <a name="datazone-ListAssetFilters-request-uri-status"></a>
The status of the asset filter.
Valid Values: `VALID | INVALID`

## Request Body
<a name="API_ListAssetFilters_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAssetFilters_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "assetId": "string",
         "createdAt": number,
         "description": "string",
         "domainId": "string",
         "effectiveColumnNames": [ "string" ],
         "effectiveRowFilter": "string",
         "errorMessage": "string",
         "id": "string",
         "name": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAssetFilters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListAssetFilters_ResponseSyntax) **   <a name="datazone-ListAssetFilters-response-items"></a>
The results of the `ListAssetFilters` action.
Type: Array of [AssetFilterSummary](API_AssetFilterSummary.md) objects

 ** [nextToken](#API_ListAssetFilters_ResponseSyntax) **   <a name="datazone-ListAssetFilters-response-nextToken"></a>
When the number of asset filters is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of asset filters, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListAssetFilters` to list the next set of asset filters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListAssetFilters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## Examples
<a name="API_ListAssetFilters_Examples"></a>

### Example
<a name="API_ListAssetFilters_Example_1"></a>

This example illustrates one usage of ListAssetFilters.

#### Sample Request
<a name="API_ListAssetFilters_Example_1_Request"></a>

```
aws datazone list-asset-filters \
--domain-identifier "dzd_53ielnpxktdilj" \
--asset-identifier "ast7k9mpq2xvn4"
```

#### Sample Response
<a name="API_ListAssetFilters_Example_1_Response"></a>

```
{
    "items": [{
        "assetId": "ast7k9mpq2xvn4",
        "createdAt": 1752651315.63,
        "description": "Filter for customer PII data",
        "domainId": "dzd_53ielnpxktdilj",
        "effectiveColumnNames": [
            "customer_id",
            "email",
            "phone_number",
            "address"
        ],
        "id": "flt8p2mq3xvn5",
        "name": "customer-pii-filter",
        "status": "VALID"
    }]
}
```

### Example
<a name="API_ListAssetFilters_Example_2"></a>

Failure case - missing required `--asset-identifier`:

#### Sample Request
<a name="API_ListAssetFilters_Example_2_Request"></a>

```
aws datazone list-asset-filters \
--domain-identifier "dzd_53ielnpxktdilj"
```

#### Sample Response
<a name="API_ListAssetFilters_Example_2_Response"></a>

```
aws: error: the following arguments are required: —asset-identifier
```

## See Also
<a name="API_ListAssetFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListAssetFilters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListAssetFilters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListAssetFilters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListAssetFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListAssetFilters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListAssetFilters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListAssetFilters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListAssetFilters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListAssetFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListAssetFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
