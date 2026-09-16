---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateAssetFilter.html
---

# CreateAssetFilter
<a name="API_CreateAssetFilter"></a>

Creates a data asset filter.

Asset filters provide a sophisticated way to create controlled views of data assets by selecting specific columns or applying row-level filters. This capability is crucial for organizations that need to share data while maintaining security and privacy controls. For example, your database might be filtered to show only non-PII fields to certain users, or sales data might be filtered by region for different regional teams. Asset filters enable fine-grained access control while maintaining a single source of truth.

Prerequisites:
+ A valid domain (`--domain-identifier`) must exist.
+ A data asset (`--asset-identifier`) must already be created under that domain.
+ The asset must have the referenced columns available in its schema for column-based filtering.
+ You cannot specify both (`columnConfiguration`, `rowConfiguration`)at the same time.

## Request Syntax
<a name="API_CreateAssetFilter_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/assets/{{assetIdentifier}}/filters HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "configuration": { ... },
   "description": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateAssetFilter_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetIdentifier](#API_CreateAssetFilter_RequestSyntax) **   <a name="datazone-CreateAssetFilter-request-uri-assetIdentifier"></a>
The ID of the data asset.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [domainIdentifier](#API_CreateAssetFilter_RequestSyntax) **   <a name="datazone-CreateAssetFilter-request-uri-domainIdentifier"></a>
The ID of the domain in which you want to create an asset filter.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateAssetFilter_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateAssetFilter_RequestSyntax) **   <a name="datazone-CreateAssetFilter-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Required: No

 ** [configuration](#API_CreateAssetFilter_RequestSyntax) **   <a name="datazone-CreateAssetFilter-request-configuration"></a>
The configuration of the asset filter.
Type: [AssetFilterConfiguration](API_AssetFilterConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [description](#API_CreateAssetFilter_RequestSyntax) **   <a name="datazone-CreateAssetFilter-request-description"></a>
The description of the asset filter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [name](#API_CreateAssetFilter_RequestSyntax) **   <a name="datazone-CreateAssetFilter-request-name"></a>
The name of the asset filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: Yes

## Response Syntax
<a name="API_CreateAssetFilter_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateAssetFilter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [assetId](#API_CreateAssetFilter_ResponseSyntax) **   <a name="datazone-CreateAssetFilter-response-assetId"></a>
The ID of the asset.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [configuration](#API_CreateAssetFilter_ResponseSyntax) **   <a name="datazone-CreateAssetFilter-response-configuration"></a>
The configuration of the asset filter.
Type: [AssetFilterConfiguration](API_AssetFilterConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [createdAt](#API_CreateAssetFilter_ResponseSyntax) **   <a name="datazone-CreateAssetFilter-response-createdAt"></a>
The timestamp at which the asset filter was created.
Type: Timestamp

 ** [description](#API_CreateAssetFilter_ResponseSyntax) **   <a name="datazone-CreateAssetFilter-response-description"></a>
The description of the asset filter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_CreateAssetFilter_ResponseSyntax) **   <a name="datazone-CreateAssetFilter-response-domainId"></a>
The ID of the domain where the asset filter is created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [effectiveColumnNames](#API_CreateAssetFilter_ResponseSyntax) **   <a name="datazone-CreateAssetFilter-response-effectiveColumnNames"></a>
The column names in the asset filter.
Type: Array of strings

 ** [effectiveRowFilter](#API_CreateAssetFilter_ResponseSyntax) **   <a name="datazone-CreateAssetFilter-response-effectiveRowFilter"></a>
The row filter in the asset filter.
Type: String

 ** [errorMessage](#API_CreateAssetFilter_ResponseSyntax) **   <a name="datazone-CreateAssetFilter-response-errorMessage"></a>
The error message that is displayed if the asset filter is not created successfully.
Type: String

 ** [id](#API_CreateAssetFilter_ResponseSyntax) **   <a name="datazone-CreateAssetFilter-response-id"></a>
The ID of the asset filter.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [name](#API_CreateAssetFilter_ResponseSyntax) **   <a name="datazone-CreateAssetFilter-response-name"></a>
The name of the asset filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [status](#API_CreateAssetFilter_ResponseSyntax) **   <a name="datazone-CreateAssetFilter-response-status"></a>
The status of the asset filter.
Type: String
Valid Values: `VALID | INVALID`

## Errors
<a name="API_CreateAssetFilter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request has exceeded the specified service quota.
HTTP Status Code: 402

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
<a name="API_CreateAssetFilter_Examples"></a>

### Example
<a name="API_CreateAssetFilter_Example_1"></a>

This example illustrates one usage of CreateAssetFilter.

#### Sample Request
<a name="API_CreateAssetFilter_Example_1_Request"></a>

```
aws datazone create-asset-filter \
--domain-identifier "dzd_53ielnpxktdilj" \
--asset-identifier "ast7k9mpq2xvn4" \
--name "customer-pii-filter" \
--configuration '{
    "columnConfiguration": {
        "includedColumnNames": [
            "customer_id",
            "email",
            "phone_number",
            "address"
        ]
    }
}'
```

#### Sample Request
<a name="API_CreateAssetFilter_Example_1_Request"></a>

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
<a name="API_CreateAssetFilter_Example_2"></a>

Failure case - missing required field: `--configuration`:

#### Sample Request
<a name="API_CreateAssetFilter_Example_2_Request"></a>

```
aws datazone create-asset-filter \
--domain-identifier "dzd_53ielnpxktdilj" \
--asset-identifier "ast7k9mpq2xvn4" \
--name "missing-config"
```

#### Sample Response
<a name="API_CreateAssetFilter_Example_2_Response"></a>

```
aws: error: the following arguments are required: —configuration
```

### Example
<a name="API_CreateAssetFilter_Example_3"></a>

Failure case - invalid JSON in `--configuration`

#### Sample Request
<a name="API_CreateAssetFilter_Example_3_Request"></a>

```
aws datazone create-asset-filter \
--domain-identifier "dzd_53ielnpxktdilj" \
--asset-identifier "ast7k9mpq2xvn4" \
--name "invalid-json" \
--configuration '{ "columnConfiguration": { "includedColumnNames": ["customer_id", "email" }'
```

#### Sample Response
<a name="API_CreateAssetFilter_Example_3_Response"></a>

```
Error parsing parameter '--configuration': Invalid JSON: Expecting ',' delimiter: line 1 column 65 (char 64)
JSON received: { "columnConfiguration": { "includedColumnNames": ["customer_id", "email" }
```

### Example
<a name="API_CreateAssetFilter_Example_4"></a>

Failure case - both `columnConfiguration` and `rowConfiguration` present

#### Sample Request
<a name="API_CreateAssetFilter_Example_4_Request"></a>

```
aws datazone create-asset-filter \
--domain-identifier "dzd_53ielnpxktdilj" \
--asset-identifier "ast7k9mpq2xvn4" \
--name "dual-config" \
--configuration '{
    "columnConfiguration": {
        "includedColumnNames": ["customer_id"]
    },
    "rowConfiguration": {
        "rowFilter": {
            "expression": {
                "equalTo": {
                    "columnName": "customer_id",
                    "value": "CUST123"
                }
            }
        }
    }
}'
```

#### Sample Response
<a name="API_CreateAssetFilter_Example_4_Response"></a>

```
Parameter validation failed:
Invalid number of parameters set for tagged union structure configuration. Can only set one of the following keys: columnConfiguration, rowConfiguration.
```

### Example
<a name="API_CreateAssetFilter_Example_5"></a>

Failure case - empty `includedColumnNames`:

#### Sample Request
<a name="API_CreateAssetFilter_Example_5_Request"></a>

```
aws datazone create-asset-filter \
--domain-identifier "dzd_53ielnpxktdilj" \
--asset-identifier "ast7k9mpq2xvn4" \
--name "empty-columns" \
--configuration '{
    "columnConfiguration": {
        "includedColumnNames": []
    }
}'
```

#### Sample Response
<a name="API_CreateAssetFilter_Example_5_Response"></a>

```
An error occurred (ValidationException) when calling the CreateAssetFilter operation: Invalid column configuration. No valid columns found.
```

### Example
<a name="API_CreateAssetFilter_Example_6"></a>

Failure case - invalid key in `rowFilter` expression:

#### Sample Request
<a name="API_CreateAssetFilter_Example_6_Request"></a>

```
aws datazone create-asset-filter \
--domain-identifier "dzd_53ielnpxktdilj" \
--asset-identifier "ast7k9mpq2xvn4" \
--name "invalid-row-key" \
--configuration '{
    "rowConfiguration": {
        "rowFilter": {
            "expression": {
                "invalidOperator": {
                    "columnName": "customer_id",
                    "value": "CUST123"
                }
            }
        }
    }
}'
```

#### Sample Response
<a name="API_CreateAssetFilter_Example_6_Response"></a>

```
Parameter validation failed:
Unknown parameter in configuration.rowConfiguration.rowFilter.expression: "invalidOperator", must be one of: equalTo, greaterThan, greaterThanOrEqualTo, in, isNotNull, isNull, lessThan, lessThanOrEqualTo, like, notEqualTo, notIn, notLike
```

### Example
<a name="API_CreateAssetFilter_Example_7"></a>

Failure case - missing `columnName` in row filter:

#### Sample Request
<a name="API_CreateAssetFilter_Example_7_Request"></a>

```
aws datazone create-asset-filter \
--domain-identifier "dzd_53ielnpxktdilj" \
--asset-identifier "ast7k9mpq2xvn4" \
--name "missing-column-name" \
--configuration '{
    "rowConfiguration": {
        "rowFilter": {
            "expression": {
                "equalTo": {
                    "value": "CUST123"
                }
            }
        }
    }
}'
```

#### Sample Response
<a name="API_CreateAssetFilter_Example_7_Response"></a>

```
Parameter validation failed:
Missing required parameter in configuration.rowConfiguration.rowFilter.expression.equalTo: "columnName"
```

## See Also
<a name="API_CreateAssetFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateAssetFilter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateAssetFilter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateAssetFilter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateAssetFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateAssetFilter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateAssetFilter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateAssetFilter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateAssetFilter)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateAssetFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateAssetFilter)
