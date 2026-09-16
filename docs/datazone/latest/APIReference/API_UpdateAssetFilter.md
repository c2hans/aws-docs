---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UpdateAssetFilter.html
---

# UpdateAssetFilter
<a name="API_UpdateAssetFilter"></a>

Updates an asset filter.

Prerequisites:
+ The domain, asset, and asset filter identifier must all exist.
+ The asset must contain the columns being referenced in the update.
+ If applying a row filter, ensure the column referenced in the expression exists in the asset schema.

## Request Syntax
<a name="API_UpdateAssetFilter_RequestSyntax"></a>

```
PATCH /v2/domains/{{domainIdentifier}}/assets/{{assetIdentifier}}/filters/{{identifier}} HTTP/1.1
Content-type: application/json

{
   "configuration": { ... },
   "description": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAssetFilter_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetIdentifier](#API_UpdateAssetFilter_RequestSyntax) **   <a name="datazone-UpdateAssetFilter-request-uri-assetIdentifier"></a>
The ID of the data asset.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [domainIdentifier](#API_UpdateAssetFilter_RequestSyntax) **   <a name="datazone-UpdateAssetFilter-request-uri-domainIdentifier"></a>
The ID of the domain where you want to update an asset filter.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_UpdateAssetFilter_RequestSyntax) **   <a name="datazone-UpdateAssetFilter-request-uri-identifier"></a>
The ID of the asset filter.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_UpdateAssetFilter_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuration](#API_UpdateAssetFilter_RequestSyntax) **   <a name="datazone-UpdateAssetFilter-request-configuration"></a>
The configuration of the asset filter.
Type: [AssetFilterConfiguration](API_AssetFilterConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [description](#API_UpdateAssetFilter_RequestSyntax) **   <a name="datazone-UpdateAssetFilter-request-description"></a>
The description of the asset filter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [name](#API_UpdateAssetFilter_RequestSyntax) **   <a name="datazone-UpdateAssetFilter-request-name"></a>
The name of the asset filter.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateAssetFilter_ResponseSyntax"></a>

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
<a name="API_UpdateAssetFilter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assetId](#API_UpdateAssetFilter_ResponseSyntax) **   <a name="datazone-UpdateAssetFilter-response-assetId"></a>
The ID of the data asset.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [configuration](#API_UpdateAssetFilter_ResponseSyntax) **   <a name="datazone-UpdateAssetFilter-response-configuration"></a>
The configuration of the asset filter.
Type: [AssetFilterConfiguration](API_AssetFilterConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [createdAt](#API_UpdateAssetFilter_ResponseSyntax) **   <a name="datazone-UpdateAssetFilter-response-createdAt"></a>
The timestamp at which the asset filter was created.
Type: Timestamp

 ** [description](#API_UpdateAssetFilter_ResponseSyntax) **   <a name="datazone-UpdateAssetFilter-response-description"></a>
The description of the asset filter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_UpdateAssetFilter_ResponseSyntax) **   <a name="datazone-UpdateAssetFilter-response-domainId"></a>
The ID of the domain where the asset filter was created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [effectiveColumnNames](#API_UpdateAssetFilter_ResponseSyntax) **   <a name="datazone-UpdateAssetFilter-response-effectiveColumnNames"></a>
The column names of the asset filter.
Type: Array of strings

 ** [effectiveRowFilter](#API_UpdateAssetFilter_ResponseSyntax) **   <a name="datazone-UpdateAssetFilter-response-effectiveRowFilter"></a>
The row filter of the asset filter.
Type: String

 ** [errorMessage](#API_UpdateAssetFilter_ResponseSyntax) **   <a name="datazone-UpdateAssetFilter-response-errorMessage"></a>
The error message that is displayed if the action is not completed successfully.
Type: String

 ** [id](#API_UpdateAssetFilter_ResponseSyntax) **   <a name="datazone-UpdateAssetFilter-response-id"></a>
The ID of the asset filter.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [name](#API_UpdateAssetFilter_ResponseSyntax) **   <a name="datazone-UpdateAssetFilter-response-name"></a>
The name of the asset filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [status](#API_UpdateAssetFilter_ResponseSyntax) **   <a name="datazone-UpdateAssetFilter-response-status"></a>
The status of the asset filter.
Type: String
Valid Values: `VALID | INVALID`

## Errors
<a name="API_UpdateAssetFilter_Errors"></a>

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
<a name="API_UpdateAssetFilter_Examples"></a>

### Example
<a name="API_UpdateAssetFilter_Example_1"></a>

This example illustrates one usage of UpdateAssetFilter.

#### Sample Request
<a name="API_UpdateAssetFilter_Example_1_Request"></a>

```
aws datazone update-asset-filter \
--domain-identifier "dzd_53ielnpxktdilj" \
--asset-identifier "ast7k9mpq2xvn4" \
--identifier "flt8p2mq3xvn5" \
--configuration '{
    "columnConfiguration": {
        "includedColumnNames": [
            "customer_id",
            "email",
            "phone_number",
            "address",
            "registration_date",
            "last_login_date"
        ]
    }
}'
```

#### Sample Response
<a name="API_UpdateAssetFilter_Example_1_Response"></a>

```
{
    "assetId": "ast7k9mpq2xvn4",
    "configuration": {
        "columnConfiguration": {
            "includedColumnNames": [
                "customer_id",
                "email",
                "phone_number",
                "address",
                "registration_date",
                "last_login_date"
            ]
        }
    },
    "createdAt": 1752651315.63,
    "domainId": "dzd_53ielnpxktdilj",
    "effectiveColumnNames": [
        "customer_id",
        "email",
        "phone_number",
        "address",
        "registration_date",
        "last_login_date"
    ],
    "id": "flt8p2mq3xvn5",
    "name": "customer-pii-filter",
    "status": "VALID"
}
```

### Example
<a name="API_UpdateAssetFilter_Example_2"></a>

Failure case - missing required field `--configuration`:

#### Sample Request
<a name="API_UpdateAssetFilter_Example_2_Request"></a>

```
aws datazone update-asset-filter \
--domain-identifier "dzd_53ielnpxktdilj" \
--asset-identifier "ast7k9mpq2xvn4" \
--identifier "flt8p2mq3xvn5"
```

#### Sample Response
<a name="API_UpdateAssetFilter_Example_2_Response"></a>

```
aws: error: the following arguments are required: --configuration
```

### Example
<a name="API_UpdateAssetFilter_Example_3"></a>

Failure case - invalid JSON in `--configuration`:

#### Sample Request
<a name="API_UpdateAssetFilter_Example_3_Request"></a>

```
aws datazone update-asset-filter \
--domain-identifier "dzd_53ielnpxktdilj" \
--asset-identifier "ast7k9mpq2xvn4" \
--identifier "flt8p2mq3xvn5" \
--configuration '{ "columnConfiguration": { "includedColumnNames": ["customer_id", "email" }'
```

#### Sample Response
<a name="API_UpdateAssetFilter_Example_3_Response"></a>

```
Error parsing parameter '--configuration': Invalid JSON: Expecting ',' delimiter: line 1 column 65 (char 64)
```

### Example
<a name="API_UpdateAssetFilter_Example_4"></a>

Failure case - both `columnConfiguration` and `rowConfiguration` present:

#### Sample Request
<a name="API_UpdateAssetFilter_Example_4_Request"></a>

```
aws datazone update-asset-filter \
--domain-identifier "dzd_53ielnpxktdilj" \
--asset-identifier "ast7k9mpq2xvn4" \
--identifier "flt8p2mq3xvn5" \
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
<a name="API_UpdateAssetFilter_Example_4_Response"></a>

```
Parameter validation failed:
Invalid number of parameters set for tagged union structure configuration. Can only set one of the following keys: columnConfiguration, rowConfiguration.
```

### Example
<a name="API_UpdateAssetFilter_Example_5"></a>

Failure case - empty `includedColumnNames`:

#### Sample Request
<a name="API_UpdateAssetFilter_Example_5_Request"></a>

```
aws datazone update-asset-filter \
--domain-identifier "dzd_53ielnpxktdilj" \
--asset-identifier "ast7k9mpq2xvn4" \
--identifier "flt8p2mq3xvn5" \
--configuration '{
    "columnConfiguration": {
        "includedColumnNames": []
    }
}'
```

#### Sample Response
<a name="API_UpdateAssetFilter_Example_5_Response"></a>

```
An error occurred (ValidationException) when calling the UpdateAssetFilter operation: Invalid column configuration. No valid columns found.
```

### Example
<a name="API_UpdateAssetFilter_Example_6"></a>

Failure case - invalid key in `rowFilter` expression:

#### Sample Request
<a name="API_UpdateAssetFilter_Example_6_Request"></a>

```
aws datazone update-asset-filter \
--domain-identifier "dzd_53ielnpxktdilj" \
--asset-identifier "ast7k9mpq2xvn4" \
--identifier "flt8p2mq3xvn5" \
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
<a name="API_UpdateAssetFilter_Example_6_Response"></a>

```
Parameter validation failed:
Unknown parameter in configuration.rowConfiguration.rowFilter.expression: "invalidOperator", must be one of: equalTo, greaterThan, greaterThanOrEqualTo, in, isNotNull, isNull, lessThan, lessThanOrEqualTo, like, notEqualTo, notIn, notLike
```

### Example
<a name="API_UpdateAssetFilter_Example_7"></a>

Failure case - missing `columnName` in row filter:

#### Sample Request
<a name="API_UpdateAssetFilter_Example_7_Request"></a>

```
aws datazone update-asset-filter \
--domain-identifier "dzd_53ielnpxktdilj" \
--asset-identifier "ast7k9mpq2xvn4" \
--identifier "flt8p2mq3xvn5" \
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
<a name="API_UpdateAssetFilter_Example_7_Response"></a>

```
Parameter validation failed:
Missing required parameter in configuration.rowConfiguration.rowFilter.expression.equalTo: "columnName"
```

## See Also
<a name="API_UpdateAssetFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/UpdateAssetFilter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/UpdateAssetFilter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UpdateAssetFilter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/UpdateAssetFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UpdateAssetFilter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/UpdateAssetFilter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/UpdateAssetFilter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/UpdateAssetFilter)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/UpdateAssetFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UpdateAssetFilter)
