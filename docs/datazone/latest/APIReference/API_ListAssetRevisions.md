---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListAssetRevisions.html
---

# ListAssetRevisions
<a name="API_ListAssetRevisions"></a>

Lists the revisions for the asset.

Prerequisites:
+ The asset must exist in the domain.
+ There must be at least one revision of the asset (which happens automatically after creation).
+ The domain must be valid and active.
+ User must have permissions on the asset and domain.

## Request Syntax
<a name="API_ListAssetRevisions_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/assets/{{identifier}}/revisions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAssetRevisions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListAssetRevisions_RequestSyntax) **   <a name="datazone-ListAssetRevisions-request-uri-domainIdentifier"></a>
The identifier of the domain.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_ListAssetRevisions_RequestSyntax) **   <a name="datazone-ListAssetRevisions-request-uri-identifier"></a>
The identifier of the asset.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListAssetRevisions_RequestSyntax) **   <a name="datazone-ListAssetRevisions-request-uri-maxResults"></a>
The maximum number of revisions to return in a single call to `ListAssetRevisions`. When the number of revisions to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListAssetRevisions` to list the next set of revisions.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListAssetRevisions_RequestSyntax) **   <a name="datazone-ListAssetRevisions-request-uri-nextToken"></a>
When the number of revisions is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of revisions, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListAssetRevisions` to list the next set of revisions.
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Request Body
<a name="API_ListAssetRevisions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAssetRevisions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "createdAt": number,
         "createdBy": "string",
         "domainId": "string",
         "id": "string",
         "revision": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAssetRevisions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListAssetRevisions_ResponseSyntax) **   <a name="datazone-ListAssetRevisions-response-items"></a>
The results of the `ListAssetRevisions` action.
Type: Array of [AssetRevision](API_AssetRevision.md) objects

 ** [nextToken](#API_ListAssetRevisions_ResponseSyntax) **   <a name="datazone-ListAssetRevisions-response-nextToken"></a>
When the number of revisions is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of revisions, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListAssetRevisions` to list the next set of revisions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListAssetRevisions_Errors"></a>

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
<a name="API_ListAssetRevisions_Examples"></a>

### Example
<a name="API_ListAssetRevisions_Example_1"></a>

This example illustrates one usage of ListAssetRevisions.

#### Sample Request
<a name="API_ListAssetRevisions_Example_1_Request"></a>

```
aws datazone list-asset-revisions \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "ast7k9mpq2xvn4"
```

#### Sample Response
<a name="API_ListAssetRevisions_Example_1_Response"></a>

```
{
    "items": [
        {
            "createdAt": 1752601021.227,
            "createdBy": "usr7nx82mkl",
            "domainId": "dzd_53ielnpxktdilj",
            "id": "ast7k9mpq2xvn4",
            "revision": "2"
        },
        {
            "createdAt": 1752554243.917,
            "createdBy": "usr7nx82mkl",
            "domainId": "dzd_53ielnpxktdilj",
            "id": "ast7k9mpq2xvn4",
            "revision": "1"
        }
    ]
}
```

### Example
<a name="API_ListAssetRevisions_Example_2"></a>

Failure case - resource does not exist:

#### Sample Request
<a name="API_ListAssetRevisions_Example_2_Request"></a>

```
aws datazone list-asset-revisions \ --domain-identifier "dzd_53ielnpxktdilj" \ --identifier "ast_nonexistent"
```

#### Sample Response
<a name="API_ListAssetRevisions_Example_2_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the ListAssetRevisions operation: The given Asset doesn't exist. Try creating Asset before accessing it.
```

### Example
<a name="API_ListAssetRevisions_Example_3"></a>

Failure case - missing required parameter

#### Sample Request
<a name="API_ListAssetRevisions_Example_3_Request"></a>

```
aws datazone list-asset-revisions \
--identifier "ast7k9mpq2xvn4"
```

#### Sample Response
<a name="API_ListAssetRevisions_Example_3_Response"></a>

```
aws: error: the following arguments are required: —domain-identifier
```

## See Also
<a name="API_ListAssetRevisions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListAssetRevisions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListAssetRevisions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListAssetRevisions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListAssetRevisions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListAssetRevisions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListAssetRevisions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListAssetRevisions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListAssetRevisions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListAssetRevisions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListAssetRevisions)
