---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetCrawlers.html
---

# GetCrawlers
<a name="API_GetCrawlers"></a>

Retrieves metadata for all crawlers defined in the customer account.

## Request Syntax
<a name="API_GetCrawlers_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCrawlers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_GetCrawlers_RequestSyntax) **   <a name="Glue-GetCrawlers-request-MaxResults"></a>
The number of crawlers to return on each call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_GetCrawlers_RequestSyntax) **   <a name="Glue-GetCrawlers-request-NextToken"></a>
A continuation token, if this is a continuation request.
Type: String
Required: No

## Response Syntax
<a name="API_GetCrawlers_ResponseSyntax"></a>

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
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetCrawlers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Crawlers](#API_GetCrawlers_ResponseSyntax) **   <a name="Glue-GetCrawlers-response-Crawlers"></a>
A list of crawler metadata.
Type: Array of [Crawler](API_Crawler.md) objects

 ** [NextToken](#API_GetCrawlers_ResponseSyntax) **   <a name="Glue-GetCrawlers-response-NextToken"></a>
A continuation token, if the returned list has not reached the end of those defined in this customer account.
Type: String

## Errors
<a name="API_GetCrawlers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetCrawlers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetCrawlers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetCrawlers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetCrawlers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetCrawlers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetCrawlers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetCrawlers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetCrawlers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetCrawlers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetCrawlers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetCrawlers)
