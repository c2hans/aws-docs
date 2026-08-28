---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateAssetRevision.html
---

# CreateAssetRevision
<a name="API_CreateAssetRevision"></a>

Creates a revision of the asset.

Asset revisions represent new versions of existing assets, capturing changes to either the underlying data or its metadata. They maintain a historical record of how assets evolve over time, who made changes, and when those changes occurred. This versioning capability is crucial for governance and compliance, allowing organizations to track changes, understand their impact, and roll back if necessary.

Prerequisites:
+ Asset must already exist in the domain with identifier.
+  `formsInput` is required when asset has the form type. `typeRevision` should be the latest version of form type.
+ The form content must include all required fields (e.g., `bucketArn` for `S3ObjectCollectionForm`).
+ The owning project of the original asset must still exist and be active.
+ User must have write access to the project and domain.

## Request Syntax
<a name="API_CreateAssetRevision_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/assets/{{identifier}}/revisions HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "formsInput": [
      {
         "content": "{{string}}",
         "formName": "{{string}}",
         "typeIdentifier": "{{string}}",
         "typeRevision": "{{string}}"
      }
   ],
   "glossaryTerms": [ "{{string}}" ],
   "name": "{{string}}",
   "predictionConfiguration": {
      "businessNameGeneration": {
         "enabled": {{boolean}}
      }
   },
   "typeRevision": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateAssetRevision_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateAssetRevision_RequestSyntax) **   <a name="datazone-CreateAssetRevision-request-uri-domainIdentifier"></a>
The unique identifier of the domain where the asset is being revised.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_CreateAssetRevision_RequestSyntax) **   <a name="datazone-CreateAssetRevision-request-uri-identifier"></a>
The identifier of the asset.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateAssetRevision_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateAssetRevision_RequestSyntax) **   <a name="datazone-CreateAssetRevision-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [description](#API_CreateAssetRevision_RequestSyntax) **   <a name="datazone-CreateAssetRevision-request-description"></a>
The revised description of the asset.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [formsInput](#API_CreateAssetRevision_RequestSyntax) **   <a name="datazone-CreateAssetRevision-request-formsInput"></a>
The metadata forms to be attached to the asset as part of asset revision.
Type: Array of [FormInput](API_FormInput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [glossaryTerms](#API_CreateAssetRevision_RequestSyntax) **   <a name="datazone-CreateAssetRevision-request-glossaryTerms"></a>
The glossary terms to be attached to the asset as part of asset revision.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** [name](#API_CreateAssetRevision_RequestSyntax) **   <a name="datazone-CreateAssetRevision-request-name"></a>
Te revised name of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [predictionConfiguration](#API_CreateAssetRevision_RequestSyntax) **   <a name="datazone-CreateAssetRevision-request-predictionConfiguration"></a>
The configuration of the automatically generated business-friendly metadata for the asset.
Type: [PredictionConfiguration](API_PredictionConfiguration.md) object
Required: No

 ** [typeRevision](#API_CreateAssetRevision_RequestSyntax) **   <a name="datazone-CreateAssetRevision-request-typeRevision"></a>
The revision type of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## Response Syntax
<a name="API_CreateAssetRevision_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "createdBy": "string",
   "description": "string",
   "domainId": "string",
   "externalIdentifier": "string",
   "firstRevisionCreatedAt": number,
   "firstRevisionCreatedBy": "string",
   "formsOutput": [
      {
         "content": "string",
         "formName": "string",
         "typeName": "string",
         "typeRevision": "string"
      }
   ],
   "glossaryTerms": [ "string" ],
   "governedGlossaryTerms": [ "string" ],
   "id": "string",
   "latestTimeSeriesDataPointFormsOutput": [
      {
         "contentSummary": "string",
         "formName": "string",
         "id": "string",
         "timestamp": number,
         "typeIdentifier": "string",
         "typeRevision": "string"
      }
   ],
   "listing": {
      "listingId": "string",
      "listingStatus": "string"
   },
   "name": "string",
   "owningProjectId": "string",
   "predictionConfiguration": {
      "businessNameGeneration": {
         "enabled": boolean
      }
   },
   "readOnlyFormsOutput": [
      {
         "content": "string",
         "formName": "string",
         "typeName": "string",
         "typeRevision": "string"
      }
   ],
   "revision": "string",
   "typeIdentifier": "string",
   "typeRevision": "string"
}
```

## Response Elements
<a name="API_CreateAssetRevision_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-createdAt"></a>
The timestamp of when the asset revision occured.
Type: Timestamp

 ** [createdBy](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-createdBy"></a>
The Amazon DataZone user who performed the asset revision.
Type: String

 ** [description](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-description"></a>
The revised asset description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-domainId"></a>
The unique identifier of the Amazon DataZone domain where the asset was revised.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [externalIdentifier](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-externalIdentifier"></a>
The external identifier of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 600.

 ** [firstRevisionCreatedAt](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-firstRevisionCreatedAt"></a>
The timestamp of when the first asset revision occured.
Type: Timestamp

 ** [firstRevisionCreatedBy](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-firstRevisionCreatedBy"></a>
The Amazon DataZone user who performed the first asset revision.
Type: String

 ** [formsOutput](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-formsOutput"></a>
The metadata forms that were attached to the asset as part of the asset revision.
Type: Array of [FormOutput](API_FormOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [glossaryTerms](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-glossaryTerms"></a>
The glossary terms that were attached to the asset as part of asset revision.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [governedGlossaryTerms](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-governedGlossaryTerms"></a>
The glossary terms in a restricted glossary.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-id"></a>
The unique identifier of the asset revision.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [latestTimeSeriesDataPointFormsOutput](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-latestTimeSeriesDataPointFormsOutput"></a>
The latest data point that was imported into the time series form for the asset.
Type: Array of [TimeSeriesDataPointSummaryFormOutput](API_TimeSeriesDataPointSummaryFormOutput.md) objects

 ** [listing](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-listing"></a>
The details of an asset published in an Amazon DataZone catalog.
Type: [AssetListingDetails](API_AssetListingDetails.md) object

 ** [name](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-name"></a>
The revised name of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [owningProjectId](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-owningProjectId"></a>
The unique identifier of the revised project that owns the asset.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [predictionConfiguration](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-predictionConfiguration"></a>
The configuration of the automatically generated business-friendly metadata for the asset.
Type: [PredictionConfiguration](API_PredictionConfiguration.md) object

 ** [readOnlyFormsOutput](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-readOnlyFormsOutput"></a>
The read-only metadata forms that were attached to the asset as part of the asset revision.
Type: Array of [FormOutput](API_FormOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [revision](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-revision"></a>
The revision of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [typeIdentifier](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-typeIdentifier"></a>
The identifier of the revision type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 513.
Pattern: `(?!\.)[\w\.]*\w`

 ** [typeRevision](#API_CreateAssetRevision_ResponseSyntax) **   <a name="datazone-CreateAssetRevision-response-typeRevision"></a>
The revision type of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_CreateAssetRevision_Errors"></a>

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
<a name="API_CreateAssetRevision_Examples"></a>

### Example
<a name="API_CreateAssetRevision_Example_1"></a>

This example illustrates one usage of CreateAssetRevision.

#### Sample Request
<a name="API_CreateAssetRevision_Example_1_Request"></a>

```
aws datazone create-asset-revision \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "ast7k9mpq2xvn4" \
--name "CustomerDataset-v2" \
--forms-input '[
    {
        "formName": "S3ObjectCollectionForm",
        "typeIdentifier": "amazon.datazone.S3ObjectCollectionFormType",
        "typeRevision": "7",
        "content": "{\"bucketArn\":\"arn:aws:s3:::customer-analytics-data\"}"
    }
]'
```

#### Sample Response
<a name="API_CreateAssetRevision_Example_1_Response"></a>

```
{
    "createdAt": 1752601021.227,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1752554243.917,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [{
        "content": "{\"bucketArn\":\"arn:aws:s3:::customer-analytics-data\"}",
        "formName": "S3ObjectCollectionForm",
        "typeName": "amazon.datazone.S3ObjectCollectionFormType",
        "typeRevision": "7"
    }],
    "id": "ast7k9mpq2xvn4",
    "name": "CustomerDataset-v2",
    "owningProjectId": "prj7nx82mkl",
    "readOnlyFormsOutput": [],
    "revision": "2",
    "typeIdentifier": "amazon.datazone.S3ObjectCollectionAssetType",
    "typeRevision": "13"
}
```

### Example
<a name="API_CreateAssetRevision_Example_2"></a>

Failure case - invalid revision number for form input:

#### Sample Request
<a name="API_CreateAssetRevision_Example_2_Request"></a>

```
aws datazone create-asset-revision \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "ast7k9mpq2xvn4" \
--name "SalesTransactionsMart" \
--forms-input '[{
    "formName": "GlueTableForm",
    "typeIdentifier": "amazon.datazone.GlueTableFormType",
    "typeRevision": "12",
    "content": "{\"databaseName\":\"retail_analytics\",\"tableName\":\"sales_transactions\",\"catalogId\":\"\",\"region\":\"us-east-1\",\"tableArn\":\"arn:aws:glue:us-east-1:*:table/retail_analytics/sales_transactions\",\"columns\":[{\"columnName\":\"transaction_id\",\"dataType\":\"string\"},{\"columnName\":\"transaction_date\",\"dataType\":\"timestamp\"},{\"columnName\":\"product_id\",\"dataType\":\"string\"},{\"columnName\":\"quantity\",\"dataType\":\"int\"},{\"columnName\":\"total_amount\",\"dataType\":\"decimal\"}]}"
}]‘
```

#### Sample Response
<a name="API_CreateAssetRevision_Example_2_Response"></a>

```
An error occurred (ValidationException) when calling the CreateAsset operation: Form GlueTableForm expected form amazon.datazone#GlueTableFormType@13 but was provided amazon.datazone#GlueTableFormType@12
```

### Example
<a name="API_CreateAssetRevision_Example_3"></a>

Failure case - invalid or missing `--domain-identifier`:

#### Sample Request
<a name="API_CreateAssetRevision_Example_3_Request"></a>

```
aws datazone create-asset-revision \
--domain-identifier "invalid_domain" \
--identifier "ast7k9mpq2xvn4" \
--name "CustomerDataset-v2" \
--forms-input '[]'
```

#### Sample Response
<a name="API_CreateAssetRevision_Example_3_Response"></a>

```
An error occurred (ValidationException) when calling the CreateAssetRevision operation: 1 validation error detected: Value at 'domainIdentifier' failed to satisfy constraint: Member must satisfy regular expression pattern: dzd[-_][a-zA-Z0-9_-]{1,36}
```

### Example
<a name="API_CreateAssetRevision_Example_4"></a>

Failure case - unsupported form `typeIdentifier` or `typeRevision`:

#### Sample Request
<a name="API_CreateAssetRevision_Example_4_Request"></a>

```
aws datazone create-asset-revision \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "ast7k9mpq2xvn4" \
--name "CustomerDataset-v2" \
--forms-input 'INVALID_JSON'
```

#### Sample Response
<a name="API_CreateAssetRevision_Example_4_Response"></a>

```
Error parsing parameter '—forms-input': Expected: '=', received: 'EOF' for input:
{self._error_location()}
```

### Example
<a name="API_CreateAssetRevision_Example_5"></a>

Failure case - response does not exist:

#### Sample Request
<a name="API_CreateAssetRevision_Example_5_Request"></a>

```
aws datazone create-asset-revision \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "ast7k9mpq2xvn4" \
--name "CustomerDataset-v2" \
--forms-input '[
    {
        "formName": "InvalidForm",
        "typeIdentifier": "invalid.type.identifier",
        "typeRevision": "99",
        "content": "{}"
    }
]'
```

#### Sample Response
<a name="API_CreateAssetRevision_Example_5_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the CreateAssetRevision operation: The given Asset doesn't exist. Try creating Asset before accessing it.
```

### Example
<a name="API_CreateAssetRevision_Example_6"></a>

Failure case - missing required `content` field:

#### Sample Request
<a name="API_CreateAssetRevision_Example_6_Request"></a>

```
aws datazone create-asset-revision \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "ast7k9mpq2xvn4" \
--name "CustomerDataset-v2" \
--forms-input '[
    {
        "formName": "S3ObjectCollectionForm",
        "typeIdentifier": "amazon.datazone.S3ObjectCollectionFormType",
        "typeRevision": "7"
    }
]'
```

#### Sample Response
<a name="API_CreateAssetRevision_Example_6_Response"></a>

```
An error occurred (ValidationException) when calling the CreateAssetRevision operation: $.S3ObjectCollectionForm.bucketArn: is missing but it is required
```

## See Also
<a name="API_CreateAssetRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateAssetRevision)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateAssetRevision)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateAssetRevision)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateAssetRevision)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateAssetRevision)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateAssetRevision)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateAssetRevision)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateAssetRevision)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateAssetRevision)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateAssetRevision)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
