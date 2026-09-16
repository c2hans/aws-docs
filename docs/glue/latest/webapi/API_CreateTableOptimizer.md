---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateTableOptimizer.html
---

# CreateTableOptimizer
<a name="API_CreateTableOptimizer"></a>

Creates a new table optimizer for a specific function.

## Request Syntax
<a name="API_CreateTableOptimizer_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "TableName": "{{string}}",
   "TableOptimizerConfiguration": {
      "compactionConfiguration": {
         "icebergConfiguration": {
            "deleteFileThreshold": {{number}},
            "minInputFiles": {{number}},
            "strategy": "{{string}}"
         }
      },
      "enabled": {{boolean}},
      "orphanFileDeletionConfiguration": {
         "icebergConfiguration": {
            "location": "{{string}}",
            "orphanFileRetentionPeriodInDays": {{number}},
            "runRateInHours": {{number}}
         }
      },
      "retentionConfiguration": {
         "icebergConfiguration": {
            "cleanExpiredFiles": {{boolean}},
            "numberOfSnapshotsToRetain": {{number}},
            "runRateInHours": {{number}},
            "snapshotRetentionPeriodInDays": {{number}}
         }
      },
      "roleArn": "{{string}}",
      "vpcConfiguration": { ... }
   },
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateTableOptimizer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_CreateTableOptimizer_RequestSyntax) **   <a name="Glue-CreateTableOptimizer-request-CatalogId"></a>
The Catalog ID of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [DatabaseName](#API_CreateTableOptimizer_RequestSyntax) **   <a name="Glue-CreateTableOptimizer-request-DatabaseName"></a>
The name of the database in the catalog in which the table resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [TableName](#API_CreateTableOptimizer_RequestSyntax) **   <a name="Glue-CreateTableOptimizer-request-TableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [TableOptimizerConfiguration](#API_CreateTableOptimizer_RequestSyntax) **   <a name="Glue-CreateTableOptimizer-request-TableOptimizerConfiguration"></a>
A `TableOptimizerConfiguration` object representing the configuration of a table optimizer.
Type: [TableOptimizerConfiguration](API_TableOptimizerConfiguration.md) object
Required: Yes

 ** [Type](#API_CreateTableOptimizer_RequestSyntax) **   <a name="Glue-CreateTableOptimizer-request-Type"></a>
The type of table optimizer.
Type: String
Valid Values: `compaction | retention | orphan_file_deletion`
Required: Yes

## Response Elements
<a name="API_CreateTableOptimizer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateTableOptimizer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ThrottlingException **
The throttling threshhold was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ValidationException **
A value could not be validated.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_CreateTableOptimizer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateTableOptimizer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateTableOptimizer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateTableOptimizer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateTableOptimizer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateTableOptimizer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateTableOptimizer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateTableOptimizer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateTableOptimizer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateTableOptimizer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateTableOptimizer)
