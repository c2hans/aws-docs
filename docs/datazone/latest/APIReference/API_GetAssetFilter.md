---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetAssetFilter.html
---

# GetAssetFilter
<a name="API_GetAssetFilter"></a>

Gets an asset filter.

Prerequisites:
+ Domain (`--domain-identifier`), asset (`--asset-identifier`), and filter (`--identifier`) must all exist.
+ The asset filter should not have been deleted.
+ The asset must still exist (since the filter is linked to it).

## Request Syntax
<a name="API_GetAssetFilter_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/assets/{{assetIdentifier}}/filters/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAssetFilter_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetIdentifier](#API_GetAssetFilter_RequestSyntax) **   <a name="datazone-GetAssetFilter-request-uri-assetIdentifier"></a>
The ID of the data asset.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [domainIdentifier](#API_GetAssetFilter_RequestSyntax) **   <a name="datazone-GetAssetFilter-request-uri-domainIdentifier"></a>
The ID of the domain where you want to get an asset filter.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetAssetFilter_RequestSyntax) **   <a name="datazone-GetAssetFilter-request-uri-identifier"></a>
The ID of the asset filter.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetAssetFilter_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAssetFilter_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assetId": "string",
   "configuration": { ... },
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
```

## Response Elements
<a name="API_GetAssetFilter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assetId](#API_GetAssetFilter_ResponseSyntax) **   <a name="datazone-GetAssetFilter-response-assetId"></a>
The ID of the data asset.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [configuration](#API_GetAssetFilter_ResponseSyntax) **   <a name="datazone-GetAssetFilter-response-configuration"></a>
The configuration of the asset filter.
Type: [AssetFilterConfiguration](API_AssetFilterConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [createdAt](#API_GetAssetFilter_ResponseSyntax) **   <a name="datazone-GetAssetFilter-response-createdAt"></a>
The timestamp at which the asset filter was created.
Type: Timestamp

 ** [description](#API_GetAssetFilter_ResponseSyntax) **   <a name="datazone-GetAssetFilter-response-description"></a>
The description of the asset filter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_GetAssetFilter_ResponseSyntax) **   <a name="datazone-GetAssetFilter-response-domainId"></a>
The ID of the domain where you want to get an asset filter.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [effectiveColumnNames](#API_GetAssetFilter_ResponseSyntax) **   <a name="datazone-GetAssetFilter-response-effectiveColumnNames"></a>
The column names of the asset filter.
Type: Array of strings

 ** [effectiveRowFilter](#API_GetAssetFilter_ResponseSyntax) **   <a name="datazone-GetAssetFilter-response-effectiveRowFilter"></a>
The row filter of the asset filter.
Type: String

 ** [errorMessage](#API_GetAssetFilter_ResponseSyntax) **   <a name="datazone-GetAssetFilter-response-errorMessage"></a>
The error message that is displayed if the action does not complete successfully.
Type: String

 ** [id](#API_GetAssetFilter_ResponseSyntax) **   <a name="datazone-GetAssetFilter-response-id"></a>
The ID of the asset filter.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [name](#API_GetAssetFilter_ResponseSyntax) **   <a name="datazone-GetAssetFilter-response-name"></a>
The name of the asset filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [status](#API_GetAssetFilter_ResponseSyntax) **   <a name="datazone-GetAssetFilter-response-status"></a>
The status of the asset filter.
Type: String
Valid Values: `VALID | INVALID`

## Errors
<a name="API_GetAssetFilter_Errors"></a>

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
<a name="API_GetAssetFilter_Examples"></a>

### Example
<a name="API_GetAssetFilter_Example_1"></a>

This example illustrates one usage of GetAssetFilter.

#### Sample Request
<a name="API_GetAssetFilter_Example_1_Request"></a>

```
aws datazone get-asset-filter \
--domain-identifier "dzd_53ielnpxktdilj" \
--asset-identifier "ast7k9mpq2xvn4" \
--identifier "flt8p2mq3xvn5"
```

#### Sample Response
<a name="API_GetAssetFilter_Example_1_Response"></a>

```
{
    "assetId": "ast7k9mpq2xvn4",
    "configuration": {
        "columnConfiguration": {
            "includedColumnNames": [
                "customer_id",
                "email",
                "phone_number",
                "address"
            ]
        }
    },
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
}
```

### Example
<a name="API_GetAssetFilter_Example_2"></a>

Failure case - missing required option `--identifier`:

#### Sample Request
<a name="API_GetAssetFilter_Example_2_Request"></a>

```
aws datazone get-asset-filter \
--domain-identifier "dzd_53ielnpxktdilj" \
--asset-identifier "ast7k9mpq2xvn4"
```

#### Sample Response
<a name="API_GetAssetFilter_Example_2_Response"></a>

```
aws: error: the following arguments are required: —identifier
```

## See Also
<a name="API_GetAssetFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetAssetFilter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetAssetFilter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetAssetFilter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetAssetFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetAssetFilter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetAssetFilter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetAssetFilter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetAssetFilter)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetAssetFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetAssetFilter)
