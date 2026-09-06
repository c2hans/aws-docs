---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchGetCrawlers.html
---

# BatchGetCrawlers
<a name="API_BatchGetCrawlers"></a>

Returns a list of resource metadata for a given list of crawler names. After calling the `ListCrawlers` operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that uses tags.

## Request Syntax
<a name="API_BatchGetCrawlers_RequestSyntax"></a>

```
{
   "CrawlerNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetCrawlers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CrawlerNames](#API_BatchGetCrawlers_RequestSyntax) **   <a name="Glue-BatchGetCrawlers-request-CrawlerNames"></a>
A list of crawler names, which might be the names returned from the `ListCrawlers` operation.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_BatchGetCrawlers_ResponseSyntax"></a>

```
{
   "Crawlers": [
      {
         "Classifiers": [ "string" ],
         "Configuration": "string",
         "CrawlElapsedTime": number,
         "CrawlerSecurityConfiguration": "string",
         "CreationTime": number,
         "DatabaseName": "string",
         "Description": "string",
         "LakeFormationConfiguration": {
            "AccountId": "string",
            "UseLakeFormationCredentials": boolean
         },
         "LastCrawl": {
            "ErrorMessage": "string",
            "LogGroup": "string",
            "LogStream": "string",
            "MessagePrefix": "string",
            "StartTime": number,
            "Status": "string"
         },
         "LastUpdated": number,
         "LineageConfiguration": {
            "CrawlerLineageSettings": "string"
         },
         "Name": "string",
         "RecrawlPolicy": {
            "RecrawlBehavior": "string"
         },
         "Role": "string",
         "Schedule": {
            "ScheduleExpression": "string",
            "State": "string"
         },
         "SchemaChangePolicy": {
            "DeleteBehavior": "string",
            "UpdateBehavior": "string"
         },
         "State": "string",
         "TablePrefix": "string",
         "Targets": {
            "CatalogTargets": [
               {
                  "ConnectionName": "string",
                  "DatabaseName": "string",
                  "DlqEventQueueArn": "string",
                  "EventQueueArn": "string",
                  "Tables": [ "string" ]
               }
            ],
            "DeltaTargets": [
               {
                  "ConnectionName": "string",
                  "CreateNativeDeltaTable": boolean,
                  "DeltaTables": [ "string" ],
                  "WriteManifest": boolean
               }
            ],
            "DynamoDBTargets": [
               {
                  "Path": "string",
                  "scanAll": boolean,
                  "scanRate": number
               }
            ],
            "HudiTargets": [
               {
                  "ConnectionName": "string",
                  "Exclusions": [ "string" ],
                  "MaximumTraversalDepth": number,
                  "Paths": [ "string" ]
               }
            ],
            "IcebergTargets": [
               {
                  "ConnectionName": "string",
                  "Exclusions": [ "string" ],
                  "MaximumTraversalDepth": number,
                  "Paths": [ "string" ]
               }
            ],
            "JdbcTargets": [
               {
                  "ConnectionName": "string",
                  "EnableAdditionalMetadata": [ "string" ],
                  "Exclusions": [ "string" ],
                  "Path": "string"
               }
            ],
            "MongoDBTargets": [
               {
                  "ConnectionName": "string",
                  "Path": "string",
                  "ScanAll": boolean
               }
            ],
            "S3Targets": [
               {
                  "ConnectionName": "string",
                  "DlqEventQueueArn": "string",
                  "EventQueueArn": "string",
                  "Exclusions": [ "string" ],
                  "Path": "string",
                  "SampleSize": number
               }
            ]
         },
         "Version": number
      }
   ],
   "CrawlersNotFound": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetCrawlers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Crawlers](#API_BatchGetCrawlers_ResponseSyntax) **   <a name="Glue-BatchGetCrawlers-response-Crawlers"></a>
A list of crawler definitions.
Type: Array of [Crawler](API_Crawler.md) objects

 ** [CrawlersNotFound](#API_BatchGetCrawlers_ResponseSyntax) **   <a name="Glue-BatchGetCrawlers-response-CrawlersNotFound"></a>
A list of names of crawlers that were not found.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_BatchGetCrawlers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_BatchGetCrawlers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/BatchGetCrawlers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/BatchGetCrawlers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchGetCrawlers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/BatchGetCrawlers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchGetCrawlers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/BatchGetCrawlers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/BatchGetCrawlers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/BatchGetCrawlers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/BatchGetCrawlers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchGetCrawlers)
