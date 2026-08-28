---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchDeletePartition.html
---

# BatchDeletePartition
<a name="API_BatchDeletePartition"></a>

Deletes one or more partitions in a batch operation.

## Request Syntax
<a name="API_BatchDeletePartition_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "PartitionsToDelete": [
      {
         "Values": [ "{{string}}" ]
      }
   ],
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_BatchDeletePartition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_BatchDeletePartition_RequestSyntax) **   <a name="Glue-BatchDeletePartition-request-CatalogId"></a>
The ID of the Data Catalog where the partition to be deleted resides. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_BatchDeletePartition_RequestSyntax) **   <a name="Glue-BatchDeletePartition-request-DatabaseName"></a>
The name of the catalog database in which the table in question resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [PartitionsToDelete](#API_BatchDeletePartition_RequestSyntax) **   <a name="Glue-BatchDeletePartition-request-PartitionsToDelete"></a>
A list of `PartitionInput` structures that define the partitions to be deleted.
Type: Array of [PartitionValueList](API_PartitionValueList.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: Yes

 ** [TableName](#API_BatchDeletePartition_RequestSyntax) **   <a name="Glue-BatchDeletePartition-request-TableName"></a>
The name of the table that contains the partitions to be deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_BatchDeletePartition_ResponseSyntax"></a>

```
{
   "Errors": [
      {
         "ErrorDetail": {
            "ErrorCode": "string",
            "ErrorMessage": "string"
         },
         "PartitionValues": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_BatchDeletePartition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_BatchDeletePartition_ResponseSyntax) **   <a name="Glue-BatchDeletePartition-response-Errors"></a>
The errors encountered when trying to delete the requested partitions.
Type: Array of [PartitionError](API_PartitionError.md) objects

## Errors
<a name="API_BatchDeletePartition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_BatchDeletePartition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/BatchDeletePartition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/BatchDeletePartition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchDeletePartition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/BatchDeletePartition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchDeletePartition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/BatchDeletePartition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/BatchDeletePartition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/BatchDeletePartition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/BatchDeletePartition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchDeletePartition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
