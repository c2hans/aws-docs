---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateAsset.html
---

# CreateAsset
<a name="API_CreateAsset"></a>

Creates an asset in Amazon DataZone catalog.

Before creating assets, make sure that the following requirements are met:
+  `--domain-identifier` must refer to an existing domain.
+  `--owning-project-identifier` must be a valid project within the domain.
+ Asset type must be created beforehand using `create-asset-type`, or be a supported system-defined type. For more information, see [create-asset-type](https://docs.aws.amazon.com/cli/latest/reference/datazone/create-asset-type.html).
+  `--type-revision` (if used) must match a valid revision of the asset type.
+  `formsInput` is required when it is associated as required in the `asset-type`. For more information, see [create-form-type](https://docs.aws.amazon.com/cli/latest/reference/datazone/create-form-type.html).
+ Form content must include all required fields as per the form schema (e.g., `bucketArn`).

You must invoke the following pre-requisite commands before invoking this API:
+  [CreateFormType](https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateFormType.html)
+  [CreateAssetType](https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateAssetType.html)

## Request Syntax
<a name="API_CreateAsset_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/assets HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "externalIdentifier": "{{string}}",
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
   "owningProjectIdentifier": "{{string}}",
   "predictionConfiguration": {
      "businessNameGeneration": {
         "enabled": {{boolean}}
      }
   },
   "typeIdentifier": "{{string}}",
   "typeRevision": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateAsset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateAsset_RequestSyntax) **   <a name="datazone-CreateAsset-request-uri-domainIdentifier"></a>
Amazon DataZone domain where the asset is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateAsset_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateAsset_RequestSyntax) **   <a name="datazone-CreateAsset-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [description](#API_CreateAsset_RequestSyntax) **   <a name="datazone-CreateAsset-request-description"></a>
Asset description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [externalIdentifier](#API_CreateAsset_RequestSyntax) **   <a name="datazone-CreateAsset-request-externalIdentifier"></a>
The external identifier of the asset.
If the value for the `externalIdentifier` parameter is specified, it must be a unique value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 600.
Required: No

 ** [formsInput](#API_CreateAsset_RequestSyntax) **   <a name="datazone-CreateAsset-request-formsInput"></a>
Metadata forms attached to the asset.
Type: Array of [FormInput](API_FormInput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [glossaryTerms](#API_CreateAsset_RequestSyntax) **   <a name="datazone-CreateAsset-request-glossaryTerms"></a>
Glossary terms attached to the asset.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** [name](#API_CreateAsset_RequestSyntax) **   <a name="datazone-CreateAsset-request-name"></a>
Asset name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [owningProjectIdentifier](#API_CreateAsset_RequestSyntax) **   <a name="datazone-CreateAsset-request-owningProjectIdentifier"></a>
The unique identifier of the project that owns this asset.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [predictionConfiguration](#API_CreateAsset_RequestSyntax) **   <a name="datazone-CreateAsset-request-predictionConfiguration"></a>
The configuration of the automatically generated business-friendly metadata for the asset.
Type: [PredictionConfiguration](API_PredictionConfiguration.md) object
Required: No

 ** [typeIdentifier](#API_CreateAsset_RequestSyntax) **   <a name="datazone-CreateAsset-request-typeIdentifier"></a>
The unique identifier of this asset's type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 513.
Pattern: `(?!\.)[\w\.]*\w`
Required: Yes

 ** [typeRevision](#API_CreateAsset_RequestSyntax) **   <a name="datazone-CreateAsset-request-typeRevision"></a>
The revision of this asset's type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## Response Syntax
<a name="API_CreateAsset_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateAsset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-createdAt"></a>
The timestamp of when the asset was created.
Type: Timestamp

 ** [createdBy](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-createdBy"></a>
The Amazon DataZone user that created this asset in the catalog.
Type: String

 ** [description](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-description"></a>
The description of the created asset.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-domainId"></a>
The ID of the Amazon DataZone domain in which the asset was created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [externalIdentifier](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-externalIdentifier"></a>
The external identifier of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 600.

 ** [firstRevisionCreatedAt](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-firstRevisionCreatedAt"></a>
The timestamp of when the first revision of the asset took place.
Type: Timestamp

 ** [firstRevisionCreatedBy](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-firstRevisionCreatedBy"></a>
The Amazon DataZone user that made the first revision of the asset.
Type: String

 ** [formsOutput](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-formsOutput"></a>
The metadata forms that are attached to the created asset.
Type: Array of [FormOutput](API_FormOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [glossaryTerms](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-glossaryTerms"></a>
The glossary terms that are attached to the created asset.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [governedGlossaryTerms](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-governedGlossaryTerms"></a>
The glossary terms in a restricted glossary.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-id"></a>
The unique identifier of the created asset.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [latestTimeSeriesDataPointFormsOutput](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-latestTimeSeriesDataPointFormsOutput"></a>
The latest data point that was imported into the time series form for the asset.
Type: Array of [TimeSeriesDataPointSummaryFormOutput](API_TimeSeriesDataPointSummaryFormOutput.md) objects

 ** [listing](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-listing"></a>
The details of an asset published in an Amazon DataZone catalog.
Type: [AssetListingDetails](API_AssetListingDetails.md) object

 ** [name](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-name"></a>
The name of the created asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [owningProjectId](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-owningProjectId"></a>
The ID of the Amazon DataZone project that owns the created asset.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [predictionConfiguration](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-predictionConfiguration"></a>
The configuration of the automatically generated business-friendly metadata for the asset.
Type: [PredictionConfiguration](API_PredictionConfiguration.md) object

 ** [readOnlyFormsOutput](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-readOnlyFormsOutput"></a>
The read-only metadata forms that are attached to the created asset.
Type: Array of [FormOutput](API_FormOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [revision](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-revision"></a>
The revision of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [typeIdentifier](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-typeIdentifier"></a>
The identifier of the created asset type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 513.
Pattern: `(?!\.)[\w\.]*\w`

 ** [typeRevision](#API_CreateAsset_ResponseSyntax) **   <a name="datazone-CreateAsset-response-typeRevision"></a>
The revision type of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_CreateAsset_Errors"></a>

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
<a name="API_CreateAsset_Examples"></a>

### Example
<a name="API_CreateAsset_Example_1"></a>

Basic asset creation:

#### Sample Request
<a name="API_CreateAsset_Example_1_Request"></a>

```
  aws datazone create-asset \
  --domain-identifier "dzd_53ielnpxktdilj" \
  --name "customeranalytics2023" \
  --owning-project-identifier "prj9vn4wxyz8k2m" \
  --type-identifier "amazon.datazone.S3ObjectCollectionAssetType" \
  --forms-input '[{
    "formName": "S3ObjectCollectionForm",
    "typeIdentifier": "amazon.datazone.S3ObjectCollectionFormType",
    "content": "{\"bucketArn\":\"arn:aws:s3:::analytics-data-bucket\"}"
}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_1_Response"></a>

```
{
    "createdAt": 1752566607.769,
    "createdBy": "usr26dad7d796cc",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1752566607.769,
    "firstRevisionCreatedBy": "usr26dad7d796cc",
    "formsOutput": [{
        "content": "{\"bucketArn\":\"arn:aws:s3:::analytics-data-bucket\"}",
        "formName": "S3ObjectCollectionForm",
        "typeName": "amazon.datazone.S3ObjectCollectionFormType"
    }],
    "id": "ast7k9mpq2xvn4w",
    "name": "customeranalytics2023",
    "owningProjectId": "prj9vn4wxyz8k2m",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "amazon.datazone.S3ObjectCollectionAssetType",
    "typeRevision": "13"
}
```

### Example
<a name="API_CreateAsset_Example_2"></a>

Missing required parameter – `--domain-identifier`

#### Sample Request
<a name="API_CreateAsset_Example_2_Request"></a>

```
  aws datazone create-asset \
  --name "analytics-missing-domain" \
  --owning-project-identifier "prj9vn4wxyz8k2m" \
  --type-identifier "amazon.datazone.S3ObjectCollectionAssetType" \
  --forms-input '[{...}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_2_Response"></a>

```
   aws: error: the following arguments are required: —domain-identifier
```

### Example
<a name="API_CreateAsset_Example_3"></a>

Invalid parameter:

#### Sample Request
<a name="API_CreateAsset_Example_3_Request"></a>

```
  aws datazone create-asset \
  --domain-identifier "invalid-domain" \
  --owning-project-identifier "prjabc123" \
  --name "Asset2" \
  --type-identifier "my.type"
```

#### Sample Response
<a name="API_CreateAsset_Example_3_Response"></a>

```
An error occurred (ValidationException) when calling the CreateAsset operation: 1 validation error detected: Value at 'domainIdentifier' failed to satisfy constraint: Member must satisfy regular expression pattern: dzd[-_][a-zA-Z0-9_-]{1,36}
```

### Example
<a name="API_CreateAsset_Example_4"></a>

Non-existent asset type:

#### Sample Request
<a name="API_CreateAsset_Example_4_Request"></a>

```
  aws datazone create-asset \
  --domain-identifier "dzd_53ielnpxktdilj" \
  --name "analytics-invalid-type" \
  --owning-project-identifier "prj9vn4wxyz8k2m" \
  --type-identifier "non.existent.assetType" \
  --forms-input '[{
    "formName": "S3ObjectCollectionForm",
    "typeIdentifier": "amazon.datazone.S3ObjectCollectionFormType",
    "content": "{\"bucketArn\":\"arn:aws:s3:::analytics-data-bucket\"}"
}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_4_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the CreateAsset operation: The given Asset's input resource doesn't exist. Try creating Asset's input resource before accessing it.
```

### Example
<a name="API_CreateAsset_Example_5"></a>

Invalid Form JSON (`--forms-input`)

#### Sample Request
<a name="API_CreateAsset_Example_5_Request"></a>

```
  aws datazone create-asset \
  --domain-identifier "dzd_53ielnpxktdilj" \
  --name "analytics-invalid-json" \
  --owning-project-identifier "prj9vn4wxyz8k2m" \
  --type-identifier "amazon.datazone.S3ObjectCollectionAssetType" \
  --forms-input '[{formName: "S3ObjectCollectionForm", typeIdentifier: "amazon.datazone.S3ObjectCollectionFormType", content: {"bucketArn": "arn:aws:s3:::bucket"}}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_5_Response"></a>

```
Error parsing parameter '--forms-input': Invalid JSON: Expecting property name enclosed in double quotes: line 1 column 3 (char 2)

JSON received: [{formName: "S3ObjectCollectionForm", typeIdentifier: "amazon.datazone.S3ObjectCollectionFormType", content: {"bucketArn": "arn:aws:s3:::bucket"}}]
```

### Example
<a name="API_CreateAsset_Example_6"></a>

Create an asset - Amazon Bedrock chat app

#### Sample Request
<a name="API_CreateAsset_Example_6_Request"></a>

```
  aws datazone create-asset \
  --domain-identifier "dzd_53ielnpxktdilj" \
  --owning-project-identifier "prj7nx82mkl" \
  --name "CustomerSupportAIAssistant" \
  --type-identifier "dzd_53ielnpxktdilj.BedrockChatApp" \
  --type-revision "1" \
  --forms-input '[{
    "formName": "BedrockChatAppForm",
    "content": "{\"modelId\": \"anthropic.claude-v2\", \"temperature\": 0.7, \"maxTokens\": 500}",
    "typeIdentifier": "dzd_53ielnpxktdilj.BedrockChatAppForm",
    "typeRevision": "2"
}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_6_Response"></a>

```
{
    "createdAt": 1753270675.429,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1753270675.429,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [
        {
            "content": "{\"modelId\": \"anthropic.claude-v2\", \"temperature\": 0.7, \"maxTokens\": 500}",
            "formName": "BedrockChatAppForm",
            "typeName": "BedrockChatAppForm",
            "typeRevision": "2"
        }
    ],
    "id": "ast4gxn2ffpxdm",
    "name": "CustomerSupportAIAssistant",
    "owningProjectId": "prj7nx82mkl",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "BedrockChatApp",
    "typeRevision": "1"
}
```

### Example
<a name="API_CreateAsset_Example_7"></a>

Create an asset - Amazon Bedrock flow app:

#### Sample Request
<a name="API_CreateAsset_Example_7_Request"></a>

```
aws datazone create-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "InvoiceProcessingWorkflow" \
--type-identifier "dzd_53ielnpxktdilj.BedrockWorkflow" \
--type-revision "1" \
--forms-input '[{
    "formName": "BedrockWorkflowForm",
    "content": "{\"steps\": [\"extract_text\", \"classify_document\", \"extract_entities\", \"validate_data\"]}",
    "typeIdentifier": "dzd_53ielnpxktdilj.BedrockWorkflowForm",
    "typeRevision": "2"
}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_7_Response"></a>

```
{
    "createdAt": 1753270689.776,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1753270689.776,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [
        {
            "content": "{\"steps\": [\"extract_text\", \"classify_document\", \"extract_entities\", \"validate_data\"]}",
            "formName": "BedrockWorkflowForm",
            "typeName": "BedrockWorkflowForm",
            "typeRevision": "2"
        }
    ],
    "id": "ast44yf27731ur",
    "name": "InvoiceProcessingWorkflow",
    "owningProjectId": "prj7nx82mkl",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "BedrockWorkflow",
    "typeRevision": "1"
}
```

### Example
<a name="API_CreateAsset_Example_8"></a>

Create an asset - Amazon Bedrock inference only

#### Sample Request
<a name="API_CreateAsset_Example_8_Request"></a>

```
aws datazone create-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "TechnicalSupportKnowledgeBase" \
--type-identifier "dzd_53ielnpxktdilj.BedrockKnowledgeBase" \
--type-revision "1" \
--forms-input '[{
    "formName": "BedrockKnowledgeBaseForm",
    "content": "{\"dataSource\": \"s3://tech-support-docs/\", \"indexName\": \"tech_support_index\"}",
    "typeIdentifier": "dzd_53ielnpxktdilj.BedrockKnowledgeBaseForm",
    "typeRevision": "2"
}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_8_Response"></a>

```
{
    "createdAt": 1753270842.041,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1753270842.041,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [
        {
            "content": "{\"dataSource\": \"s3://tech-support-docs/\", \"indexName\": \"tech_support_index\"}",
            "formName": "BedrockKnowledgeBaseForm",
            "typeName": "BedrockKnowledgeBaseForm",
            "typeRevision": "2"
        }
    ],
    "id": "ast5w2trvqopfk",
    "name": "TechnicalSupportKnowledgeBase",
    "owningProjectId": "prj7nx82mkl",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "BedrockKnowledgeBase",
    "typeRevision": "1"
}
```

### Example
<a name="API_CreateAsset_Example_9"></a>

Create an asset - Amazon Bedrock model

#### Sample Request
<a name="API_CreateAsset_Example_9_Request"></a>

```
aws datazone create-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "SentimentAnalysisModel" \
--type-identifier "dzd_53ielnpxktdilj.BedrockModel" \
--type-revision "1" \
--forms-input '[{
    "formName": "BedrockModelForm",
    "content": "{\"modelId\": \"amazon.titan-text-express-v1\", \"customizationType\": \"finetuning\"}",
    "typeIdentifier": "dzd_53ielnpxktdilj.BedrockModelForm",
    "typeRevision": "2"
}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_9_Response"></a>

```
{
    "createdAt": 1753270853.652,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1753270853.652,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [
        {
            "content": "{\"modelId\": \"amazon.titan-text-express-v1\", \"customizationType\": \"finetuning\"}",
            "formName": "BedrockModelForm",
            "typeName": "BedrockModelForm",
            "typeRevision": "2"
        }
    ],
    "id": "astdk05pzppwhv",
    "name": "SentimentAnalysisModel",
    "owningProjectId": "prj7nx82mkl",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "BedrockModel",
    "typeRevision": "1"
}
```

### Example
<a name="API_CreateAsset_Example_10"></a>

Create an asset - Amazon Bedrock prompt

#### Sample Request
<a name="API_CreateAsset_Example_10_Request"></a>

```
aws datazone create-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "ProductDescriptionGenerator" \
--type-identifier "dzd_53ielnpxktdilj.BedrockPromptTemplate" \
--type-revision "1" \
--forms-input '[{
    "formName": "BedrockPromptTemplateForm",
    "content": "{\"template\": \"Generate a compelling product description for {product_name} with the following features: {features}\"}",
    "typeIdentifier": "dzd_53ielnpxktdilj.BedrockPromptTemplateForm",
    "typeRevision": "2"
}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_10_Response"></a>

```
{
    "createdAt": 1753270863.161,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1753270863.161,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [
        {
            "content": "{\"template\": \"Generate a compelling product description for {product_name} with the following features: {features}\"}",
            "formName": "BedrockPromptTemplateForm",
            "typeName": "BedrockPromptTemplateForm",
            "typeRevision": "2"
        }
    ],
    "id": "astcry10k3efgf",
    "name": "ProductDescriptionGenerator",
    "owningProjectId": "prj7nx82mkl",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "BedrockPromptTemplate",
    "typeRevision": "1"
}
```

### Example
<a name="API_CreateAsset_Example_11"></a>

Create an asset - Databricks table

#### Sample Request
<a name="API_CreateAsset_Example_11_Request"></a>

```
aws datazone create-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "CustomerBehaviorAnalytics" \
--type-identifier "DatabricksTableAssetTypeV2" \
--type-revision "1" \
--forms-input '[{
    "formName": "DatabricksTableForm",
    "content": "{\"name\": \"customer_behavior_analysis\", \"test\": true, \"database\": \"retail_analytics\", \"schema\": \"customer_insights\"}",
    "typeIdentifier": "dzd_53ielnpxktdilj.DatabricksTableForm",
    "typeRevision": "4"
}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_11_Response"></a>

```
{
    "createdAt": 1753271593.735,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1753271593.735,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [
        {
            "content": "{\"name\":\"customer_behavior_analysis\",\"test\":true,\"database\":\"retail_analytics\",\"schema\":\"customer_insights\"}",
            "formName": "DatabricksTableForm",
            "typeName": "DatabricksTableForm",
            "typeRevision": "4"
        }
    ],
    "id": "ast412igce0pf5",
    "name": "CustomerBehaviorAnalytics",
    "owningProjectId": "prj7nx82mkl",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "DatabricksTableAssetTypeV2",
    "typeRevision": "1"
}
```

### Example
<a name="API_CreateAsset_Example_12"></a>

Create an asset - Databricks view

#### Sample Request
<a name="API_CreateAsset_Example_12_Request"></a>

```
aws datazone create-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "CustomerEngagementMetrics" \
--type-identifier "DatabricksViewAssetType" \
--type-revision "1" \
--forms-input '[{
    "formName": "DatabricksViewForm",
    "content": "{\"viewName\": \"customer_engagement_metrics\", \"isMaterialized\": true, \"database\": \"retail_analytics\", \"refreshSchedule\": \"DAILY\"}",
    "typeIdentifier": "dzd_53ielnpxktdilj.DatabricksViewForm",
    "typeRevision": "2"
}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_12_Response"></a>

```
{
    "createdAt": 1753270961.273,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1753270961.273,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [
        {
            "content": "{\"viewName\":\"customer_engagement_metrics\",\"isMaterialized\":true,\"database\":\"retail_analytics\",\"refreshSchedule\":\"DAILY\"}",
            "formName": "DatabricksViewForm",
            "typeName": "DatabricksViewForm",
            "typeRevision": "2"
        }
    ],
    "id": "astbtcn00ocng5",
    "name": "CustomerEngagementMetrics",
    "owningProjectId": "prj7nx82mkl",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "DatabricksViewAssetType",
    "typeRevision": "1"
}
```

### Example
<a name="API_CreateAsset_Example_13"></a>

Create an asset - AWS Glue table

#### Sample Request
<a name="API_CreateAsset_Example_13_Request"></a>

```
aws datazone create-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "RetailSalesTransactions" \
--type-identifier "amazon.datazone.GlueTableAssetType" \
--forms-input '[{
    "formName": "GlueTableForm",
    "typeIdentifier": "amazon.datazone.GlueTableFormType",
    "typeRevision": "13",
    "content": "{\"databaseName\":\"retail_analytics\",\"tableName\":\"sales_transactions\",\"catalogId\":\"123456789012\",\"region\":\"us-east-1\",\"tableArn\":\"arn:aws:glue:us-east-1:123456789012:table/retail_analytics/sales_transactions\",\"columns\":[{\"columnName\":\"transaction_date\",\"dataType\":\"timestamp\",\"description\":\"Date and time of sale\"},{\"columnName\":\"store_id\",\"dataType\":\"string\",\"description\":\"Unique store identifier\"},{\"columnName\":\"product_id\",\"dataType\":\"string\",\"description\":\"Product SKU\"},{\"columnName\":\"quantity_sold\",\"dataType\":\"int\",\"description\":\"Units sold\"},{\"columnName\":\"sale_amount\",\"dataType\":\"decimal\",\"description\":\"Total sale amount\"},{\"columnName\":\"payment_method\",\"dataType\":\"string\",\"description\":\"Payment type used\"}]}"
}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_13_Response"></a>

```
{
    "createdAt": 1753271465.56,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1753271465.56,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [
        {
            "content": "{\"databaseName\":\"retail_analytics\",\"tableName\":\"sales_transactions\",\"catalogId\":\"123456789012\",\"region\":\"us-east-1\",\"tableArn\":\"arn:aws:glue:us-east-1:123456789012:table/retail_analytics/sales_transactions\",\"columns\":[{\"columnName\":\"transaction_date\",\"dataType\":\"timestamp\",\"description\":\"Date and time of sale\"},{\"columnName\":\"store_id\",\"dataType\":\"string\",\"description\":\"Unique store identifier\"},{\"columnName\":\"product_id\",\"dataType\":\"string\",\"description\":\"Product SKU\"},{\"columnName\":\"quantity_sold\",\"dataType\":\"int\",\"description\":\"Units sold\"},{\"columnName\":\"sale_amount\",\"dataType\":\"decimal\",\"description\":\"Total sale amount\"},{\"columnName\":\"payment_method\",\"dataType\":\"string\",\"description\":\"Payment type used\"}]}",
            "formName": "GlueTableForm",
            "typeName": "amazon.datazone.GlueTableFormType",
            "typeRevision": "13"
        }
    ],
    "id": "ast5lm7ud5m6km",
    "name": "RetailSalesTransactions",
    "owningProjectId": "prj7nx82mkl",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "amazon.datazone.GlueTableAssetType",
    "typeRevision": "19"
}
```

### Example
<a name="API_CreateAsset_Example_14"></a>

Create an asset - Amazon Redshift table

#### Sample Request
<a name="API_CreateAsset_Example_14_Request"></a>

```
aws datazone create-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "CustomerTransactionHistory" \
--type-identifier "RedshiftTableAssetType" \
--type-revision "1" \
--forms-input '[{
    "formName": "RedshiftTableForm",
    "content": "{\"tableName\": \"customer_transactions\", \"isPartitioned\": true, \"partitionKey\": \"transaction_date\", \"schema\": \"retail\", \"database\": \"analytics_db\"}",
    "typeIdentifier": "dzd_53ielnpxktdilj.RedshiftTableForm",
    "typeRevision": "2"
}]'
```

```
{
    "createdAt": 1753271106.79,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1753271106.79,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [
        {
            "content": "{\"tableName\":\"customer_transactions\",\"isPartitioned\":true,\"partitionKey\":\"transaction_date\",\"schema\":\"retail\",\"database\":\"analytics_db\"}",
            "formName": "RedshiftTableForm",
            "typeName": "RedshiftTableForm",
            "typeRevision": "2"
        }
    ],
    "id": "ast3iwa3n9kwd6",
    "name": "CustomerTransactionHistory",
    "owningProjectId": "prj7nx82mkl",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "RedshiftTableAssetType",
    "typeRevision": "1"
}
```

### Example
<a name="API_CreateAsset_Example_15"></a>

Create an asset - Amazon Redshift view

#### Sample Request
<a name="API_CreateAsset_Example_15_Request"></a>

```
aws datazone create-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "MonthlyCustomerMetricsView" \
--type-identifier "RedshiftViewAssetType" \
--type-revision "1" \
--forms-input '[{
    "formName": "RedshiftViewForm",
    "content": "{\"viewName\": \"monthly_customer_metrics\", \"isMaterialized\": true, \"schema\": \"analytics\", \"database\": \"retail_db\", \"refreshSchedule\": \"WEEKLY\"}",
    "typeIdentifier": "dzd_53ielnpxktdilj.RedshiftViewForm",
    "typeRevision": "2"
}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_15_Response"></a>

```
{
    "createdAt": 1753271116.838,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1753271116.838,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [
        {
            "content": "{\"viewName\":\"monthly_customer_metrics\",\"isMaterialized\":true,\"schema\":\"analytics\",\"database\":\"retail_db\",\"refreshSchedule\":\"WEEKLY\"}",
            "formName": "RedshiftViewForm",
            "typeName": "RedshiftViewForm",
            "typeRevision": "2"
        }
    ],
    "id": "ast6e7i1ieksu2",
    "name": "MonthlyCustomerMetricsView",
    "owningProjectId": "prj7nx82mkl",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "RedshiftViewAssetType",
    "typeRevision": "1"
}
```

### Example
<a name="API_CreateAsset_Example_16"></a>

Create an asset - Amazon S3 object collection

#### Sample Request
<a name="API_CreateAsset_Example_16_Request"></a>

```
aws datazone create-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--name "MarketingCampaignData" \
--owning-project-identifier "prj7nx82mkl" \
--type-identifier "amazon.datazone.S3ObjectCollectionAssetType" \
--forms-input '[{
    "formName": "S3ObjectCollectionForm",
    "typeIdentifier": "amazon.datazone.S3ObjectCollectionFormType",
    "content": "{\"bucketArn\":\"arn:aws:s3:::marketing-analytics-data\"}"
}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_16_Response"></a>

```
{
    "createdAt": 1752566607.769,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1752566607.769,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [{
        "content": "{\"bucketArn\":\"arn:aws:s3:::marketing-analytics-data\"}",
        "formName": "S3ObjectCollectionForm",
        "typeName": "amazon.datazone.S3ObjectCollectionFormType"
    }],
    "id": "ast6js4t0dhjj",
    "name": "MarketingCampaignData",
    "owningProjectId": "prj7nx82mkl",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "amazon.datazone.S3ObjectCollectionAssetType",
    "typeRevision": "13"
}
```

### Example
<a name="API_CreateAsset_Example_17"></a>

Create an asset - Snowflake table

#### Sample Request
<a name="API_CreateAsset_Example_17_Request"></a>

```
aws datazone create-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "ProductCatalogTable" \
--type-identifier "SnowflakeTableAssetType" \
--type-revision "1" \
--forms-input '[{
    "formName": "SnowflakeTableForm",
    "content": "{\"tableName\": \"product_catalog\", \"isPartitioned\": false, \"schema\": \"inventory\", \"warehouse\": \"analytics_wh\", \"database\": \"retail_ops\"}",
    "typeIdentifier": "dzd_53ielnpxktdilj.SnowflakeTableForm",
    "typeRevision": "2"
}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_17_Response"></a>

```
{
    "createdAt": 1753271227.293,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1753271227.293,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [
        {
            "content": "{\"tableName\":\"product_catalog\",\"isPartitioned\":false,\"schema\":\"inventory\",\"warehouse\":\"analytics_wh\",\"database\":\"retail_ops\"}",
            "formName": "SnowflakeTableForm",
            "typeName": "SnowflakeTableForm",
            "typeRevision": "2"
        }
    ],
    "id": "astaq1726wu6o4",
    "name": "ProductCatalogTable",
    "owningProjectId": "prj7nx82mkl",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "SnowflakeTableAssetType",
    "typeRevision": "1"
}
```

### Example
<a name="API_CreateAsset_Example_18"></a>

Create an asset - Snowflake view

#### Sample Request
<a name="API_CreateAsset_Example_18_Request"></a>

```
aws datazone create-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "OrderSummaryView" \
--type-identifier "SnowflakeViewAssetType" \
--type-revision "1" \
--forms-input '[{
    "formName": "SnowflakeViewForm",
    "content": "{\"viewName\": \"order_summary\", \"isMaterialized\": true, \"schema\": \"sales\", \"warehouse\": \"reporting_wh\", \"database\": \"retail_ops\", \"refreshSchedule\": \"DAILY\"}",
    "typeIdentifier": "dzd_53ielnpxktdilj.SnowflakeViewForm",
    "typeRevision": "2"
}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_18_Response"></a>

```
{
    "createdAt": 1753271243.513,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1753271243.513,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [
        {
            "content": "{\"viewName\":\"order_summary\",\"isMaterialized\":true,\"schema\":\"sales\",\"warehouse\":\"reporting_wh\",\"database\":\"retail_ops\",\"refreshSchedule\":\"DAILY\"}",
            "formName": "SnowflakeViewForm",
            "typeName": "SnowflakeViewForm",
            "typeRevision": "2"
        }
    ],
    "id": "ast6ip7bou5vkj",
    "name": "OrderSummaryView",
    "owningProjectId": "prj7nx82mkl",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "SnowflakeViewAssetType",
    "typeRevision": "1"
}
```

### Example
<a name="API_CreateAsset_Example_19"></a>

Create an asset Amazon SageMaker feature group

#### Sample Request
<a name="API_CreateAsset_Example_19_Request"></a>

```
aws datazone create-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "CustomerChurnPredictionFeatures" \
--type-identifier "SageMakerFeatureGroupAssetType" \
--type-revision "1" \
--forms-input '[{
    "formName": "SageMakerFeatureGroupForm",
    "content": "{\"name\": \"customer_churn_features\", \"description\": \"Features for predicting customer churn\", \"recordIdentifierFeatureName\": \"customer_id\", \"eventTimeFeatureName\": \"last_interaction_date\", \"onlineStoreConfig\": {\"enableOnlineStore\": true}, \"offlineStoreConfig\": {\"s3StorageConfig\": {\"s3Uri\": \"s3://sagemaker-featurestore-123456789012/customer-churn/\"}, \"disableGlueTableCreation\": false}, \"tags\": [{\"Key\": \"Project\", \"Value\": \"ChurnPrediction\"}]}",
    "typeIdentifier": "dzd_53ielnpxktdilj.SageMakerFeatureGroupForm",
    "typeRevision": "2"
}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_19_Response"></a>

```
{
    "createdAt": 1753271260.976,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1753271260.976,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [
        {
            "content": "{\"name\":\"customer_churn_features\",\"description\":\"Features for predicting customer churn\",\"recordIdentifierFeatureName\":\"customer_id\",\"eventTimeFeatureName\":\"last_interaction_date\",\"onlineStoreConfig\":{\"enableOnlineStore\":true},\"offlineStoreConfig\":{\"s3StorageConfig\":{\"s3Uri\":\"s3://sagemaker-featurestore-123456789012/customer-churn/\"},\"disableGlueTableCreation\":false},\"tags\":[{\"Key\":\"Project\",\"Value\":\"ChurnPrediction\"}]}",
            "formName": "SageMakerFeatureGroupForm",
            "typeName": "SageMakerFeatureGroupForm",
            "typeRevision": "2"
        }
    ],
    "id": "astb4lyqqkwuto",
    "name": "CustomerChurnPredictionFeatures",
    "owningProjectId": "prj7nx82mkl",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "SageMakerFeatureGroupAssetType",
    "typeRevision": "1"
}
```

### Example
<a name="API_CreateAsset_Example_20"></a>

Create an asset - Amazon SageMaker model package group

#### Sample Request
<a name="API_CreateAsset_Example_20_Request"></a>

```
aws datazone create-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "ChurnPredictionModelPackages" \
--type-identifier "SageMakerModelPackageGroupAssetType" \
--type-revision "1" \
--forms-input '[{
    "formName": "SageMakerModelPackageGroupForm",
    "content": "{\"modelPackageGroupName\": \"churn-prediction-models\", \"modelPackageGroupDescription\": \"Model packages for customer churn prediction\", \"tags\": [{\"Key\": \"Department\", \"Value\": \"CustomerRetention\"}]}",
    "typeIdentifier": "dzd_53ielnpxktdilj.SageMakerModelPackageGroupForm",
    "typeRevision": "2"
}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_20_Response"></a>

```
{
    "createdAt": 1753271283.422,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1753271283.422,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [
        {
            "content": "{\"modelPackageGroupName\":\"churn-prediction-models\",\"modelPackageGroupDescription\":\"Model packages for customer churn prediction\",\"tags\":[{\"Key\":\"Department\",\"Value\":\"CustomerRetention\"}]}",
            "formName": "SageMakerModelPackageGroupForm",
            "typeName": "SageMakerModelPackageGroupForm",
            "typeRevision": "2"
        }
    ],
    "id": "astcrohevshltl",
    "name": "ChurnPredictionModelPackages",
    "owningProjectId": "prj7nx82mkl",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "SageMakerModelPackageGroupAssetType",
    "typeRevision": "1"
}
```

### Example
<a name="API_CreateAsset_Example_21"></a>

Create an asset - data product

#### Sample Request
<a name="API_CreateAsset_Example_21_Request"></a>

```
aws datazone create-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "Customer360DataProduct" \
--description "Comprehensive 360-degree view of customer data for analytics and personalization" \
--type-identifier "DataProductAssetType" \
--type-revision "1" \
--forms-input '[{
    "formName": "DataProductMetadataForm",
    "content": "{\"name\": \"customer_360_view\", \"description\": \"Unified customer data across all touchpoints\", \"owner\": \"Customer Intelligence Team\", \"dataSources\": [\"CRM\", \"WebAnalytics\", \"TransactionHistory\", \"SupportTickets\"], \"updateFrequency\": \"Daily\", \"dataRetentionPeriod\": \"3 years\", \"accessControl\": \"Restricted\", \"dataQuality\": {\"completeness\": 98, \"accuracy\": 99, \"consistency\": 97}}",
    "typeIdentifier": "dzd_53ielnpxktdilj.DataProductMetadataForm",
    "typeRevision": "1"
}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_21_Response"></a>

```
{
    "createdAt": 1753271355.609,
    "createdBy": "usr7nx82mkl",
    "description": "Comprehensive 360-degree view of customer data for analytics and personalization",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1753271355.609,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [
        {
            "content": "{\"name\":\"customer_360_view\",\"description\":\"Unified customer data across all touchpoints\",\"owner\":\"Customer Intelligence Team\",\"dataSources\":[\"CRM\",\"WebAnalytics\",\"TransactionHistory\",\"SupportTickets\"],\"updateFrequency\":\"Daily\",\"dataRetentionPeriod\":\"3 years\",\"accessControl\":\"Restricted\",\"dataQuality\":{\"completeness\":98,\"accuracy\":99,\"consistency\":97}}",
            "formName": "DataProductMetadataForm",
            "typeName": "DataProductMetadataForm",
            "typeRevision": "1"
        }
    ],
    "id": "ast6ik301sa28t",
    "name": "Customer360DataProduct",
    "owningProjectId": "prj7nx82mkl",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "DataProductAssetType",
    "typeRevision": "1"
}
```

### Example
<a name="API_CreateAsset_Example_22"></a>

Create an asset - AWS Glue view

#### Sample Request
<a name="API_CreateAsset_Example_22_Request"></a>

```
aws datazone create-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "DailyStoreSalesAnalysis" \
--type-identifier "amazon.datazone.GlueViewAssetType" \
--forms-input '[{
    "formName": "GlueViewForm",
    "content": "{\"databaseName\":\"retail_analytics\",\"tableName\":\"daily_store_sales\",\"catalogId\":\"123456789012\",\"region\":\"us-east-1\",\"tableArn\":\"arn:aws:glue:us-east-1:123456789012:table/retail_analytics/daily_store_sales\",\"columns\":[{\"columnName\":\"date\",\"dataType\":\"date\",\"description\":\"Sale date\"},{\"columnName\":\"store_id\",\"dataType\":\"string\",\"description\":\"Store identifier\"},{\"columnName\":\"total_sales\",\"dataType\":\"decimal\",\"description\":\"Total daily sales\"},{\"columnName\":\"transaction_count\",\"dataType\":\"int\",\"description\":\"Number of transactions\"}]}",
    "typeIdentifier": "amazon.datazone.GlueViewFormType",
    "typeRevision": "12"
}]'
```

#### Sample Response
<a name="API_CreateAsset_Example_22_Response"></a>

```
{
    "createdAt": 1753271539.275,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1753271539.275,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [
        {
            "content": "{\"databaseName\":\"retail_analytics\",\"tableName\":\"daily_store_sales\",\"catalogId\":\"123456789012\",\"region\":\"us-east-1\",\"tableArn\":\"arn:aws:glue:us-east-1:123456789012:table/retail_analytics/daily_store_sales\",\"columns\":[{\"columnName\":\"date\",\"dataType\":\"date\",\"description\":\"Sale date\"},{\"columnName\":\"store_id\",\"dataType\":\"string\",\"description\":\"Store identifier\"},{\"columnName\":\"total_sales\",\"dataType\":\"decimal\",\"description\":\"Total daily sales\"},{\"columnName\":\"transaction_count\",\"dataType\":\"int\",\"description\":\"Number of transactions\"}]}",
            "formName": "GlueViewForm",
            "typeName": "amazon.datazone.GlueViewFormType",
            "typeRevision": "12"
        }
    ],
    "id": "astd1bi0vd0mf0",
    "name": "DailyStoreSalesAnalysis",
    "owningProjectId": "prj7nx82mkl",
    "readOnlyFormsOutput": [],
    "revision": "1",
    "typeIdentifier": "amazon.datazone.GlueViewAssetType",
    "typeRevision": "18"
}
```

## See Also
<a name="API_CreateAsset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateAsset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateAsset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateAsset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateAsset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateAsset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateAsset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateAsset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateAsset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateAsset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateAsset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
