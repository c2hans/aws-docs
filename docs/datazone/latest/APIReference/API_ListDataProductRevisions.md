---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListDataProductRevisions.html
---

# ListDataProductRevisions
<a name="API_ListDataProductRevisions"></a>

Lists data product revisions.

Prerequisites:
+ The data product ID must exist within the domain.
+ User must have view permissions on the data product.
+ The domain must be in a valid and accessible state.

## Request Syntax
<a name="API_ListDataProductRevisions_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/data-products/{{identifier}}/revisions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataProductRevisions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListDataProductRevisions_RequestSyntax) **   <a name="datazone-ListDataProductRevisions-request-uri-domainIdentifier"></a>
The ID of the domain of the data product revisions that you want to list.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_ListDataProductRevisions_RequestSyntax) **   <a name="datazone-ListDataProductRevisions-request-uri-identifier"></a>
The ID of the data product revision.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListDataProductRevisions_RequestSyntax) **   <a name="datazone-ListDataProductRevisions-request-uri-maxResults"></a>
The maximum number of asset filters to return in a single call to `ListDataProductRevisions`. When the number of data product revisions to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListDataProductRevisions` to list the next set of data product revisions.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListDataProductRevisions_RequestSyntax) **   <a name="datazone-ListDataProductRevisions-request-uri-nextToken"></a>
When the number of data product revisions is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of data product revisions, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListDataProductRevisions` to list the next set of data product revisions.
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Request Body
<a name="API_ListDataProductRevisions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataProductRevisions_ResponseSyntax"></a>

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
<a name="API_ListDataProductRevisions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListDataProductRevisions_ResponseSyntax) **   <a name="datazone-ListDataProductRevisions-response-items"></a>
The results of the `ListDataProductRevisions` action.
Type: Array of [DataProductRevision](API_DataProductRevision.md) objects

 ** [nextToken](#API_ListDataProductRevisions_ResponseSyntax) **   <a name="datazone-ListDataProductRevisions-response-nextToken"></a>
When the number of data product revisions is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of data product revisions, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListDataProductRevisions` to list the next set of data product revisions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListDataProductRevisions_Errors"></a>

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
<a name="API_ListDataProductRevisions_Examples"></a>

### Example
<a name="API_ListDataProductRevisions_Example_1"></a>

This example illustrates one usage of ListDataProductRevisions.

#### Sample Request
<a name="API_ListDataProductRevisions_Example_1_Request"></a>

```
aws datazone list-data-product-revisions \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "dpd9m3nqx2wkfp"
```

#### Sample Response
<a name="API_ListDataProductRevisions_Example_1_Response"></a>

```
{
    "items": [
        {
            "createdAt": 1752602995.424,
            "createdBy": "usr7nx82mkl",
            "domainId": "dzd_53ielnpxktdilj",
            "id": "dpd9m3nqx2wkfp",
            "revision": "2"
        },
        {
            "createdAt": 1752602810.307,
            "createdBy": "usr7nx82mkl",
            "domainId": "dzd_53ielnpxktdilj",
            "id": "dpd9m3nqx2wkfp",
            "revision": "1"
        }
    ]
}
```

### Example
<a name="API_ListDataProductRevisions_Example_2"></a>

Failure case - missing parameter:

#### Sample Request
<a name="API_ListDataProductRevisions_Example_2_Request"></a>

```
aws datazone list-data-product-revisions \
--domain-identifier "dzd_53ielnpxktdilj"
```

#### Sample Response
<a name="API_ListDataProductRevisions_Example_2_Response"></a>

```
aws: error: the following arguments are required: —identifier
```

### Example
<a name="API_ListDataProductRevisions_Example_3"></a>

Failure case - resource not found:

#### Sample Request
<a name="API_ListDataProductRevisions_Example_3_Request"></a>

```
aws datazone list-data-product-revisions \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "dpd_nonexistent"
```

#### Sample Response
<a name="API_ListDataProductRevisions_Example_3_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the ListDataProductRevisions operation: Requested dataProduct cannot be found in domain
```

## See Also
<a name="API_ListDataProductRevisions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListDataProductRevisions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListDataProductRevisions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListDataProductRevisions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListDataProductRevisions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListDataProductRevisions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListDataProductRevisions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListDataProductRevisions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListDataProductRevisions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListDataProductRevisions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListDataProductRevisions)
