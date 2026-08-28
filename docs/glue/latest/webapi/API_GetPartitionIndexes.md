---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetPartitionIndexes.html
---

# GetPartitionIndexes
<a name="API_GetPartitionIndexes"></a>

Retrieves the partition indexes associated with a table.

## Request Syntax
<a name="API_GetPartitionIndexes_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "NextToken": "{{string}}",
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPartitionIndexes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_GetPartitionIndexes_RequestSyntax) **   <a name="Glue-GetPartitionIndexes-request-CatalogId"></a>
The catalog ID where the table resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_GetPartitionIndexes_RequestSyntax) **   <a name="Glue-GetPartitionIndexes-request-DatabaseName"></a>
Specifies the name of a database from which you want to retrieve partition indexes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [NextToken](#API_GetPartitionIndexes_RequestSyntax) **   <a name="Glue-GetPartitionIndexes-request-NextToken"></a>
A continuation token, included if this is a continuation call.
Type: String
Required: No

 ** [TableName](#API_GetPartitionIndexes_RequestSyntax) **   <a name="Glue-GetPartitionIndexes-request-TableName"></a>
Specifies the name of a table for which you want to retrieve the partition indexes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetPartitionIndexes_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "PartitionIndexDescriptorList": [
      {
         "BackfillErrors": [
            {
               "Code": "string",
               "Partitions": [
                  {
                     "Values": [ "string" ]
                  }
               ]
            }
         ],
         "IndexName": "string",
         "IndexStatus": "string",
         "Keys": [
            {
               "Name": "string",
               "Type": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GetPartitionIndexes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetPartitionIndexes_ResponseSyntax) **   <a name="Glue-GetPartitionIndexes-response-NextToken"></a>
A continuation token, present if the current list segment is not the last.
Type: String

 ** [PartitionIndexDescriptorList](#API_GetPartitionIndexes_ResponseSyntax) **   <a name="Glue-GetPartitionIndexes-response-PartitionIndexDescriptorList"></a>
A list of index descriptors.
Type: Array of [PartitionIndexDescriptor](API_PartitionIndexDescriptor.md) objects

## Errors
<a name="API_GetPartitionIndexes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The `CreatePartitions` API was called on a table that has indexes enabled.
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

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetPartitionIndexes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetPartitionIndexes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetPartitionIndexes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetPartitionIndexes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetPartitionIndexes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetPartitionIndexes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetPartitionIndexes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetPartitionIndexes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetPartitionIndexes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetPartitionIndexes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetPartitionIndexes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
