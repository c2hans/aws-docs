---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateCrawler.html
---

# CreateCrawler
<a name="API_CreateCrawler"></a>

Creates a new crawler with specified targets, role, configuration, and optional schedule. At least one crawl target must be specified, in the `s3Targets` field, the `jdbcTargets` field, or the `DynamoDBTargets` field.

## Request Syntax
<a name="API_CreateCrawler_RequestSyntax"></a>

```
{
   "Classifiers": [ "{{string}}" ],
   "Configuration": "{{string}}",
   "CrawlerSecurityConfiguration": "{{string}}",
   "DatabaseName": "{{string}}",
   "Description": "{{string}}",
   "LakeFormationConfiguration": {
      "AccountId": "{{string}}",
      "UseLakeFormationCredentials": {{boolean}}
   },
   "LineageConfiguration": {
      "CrawlerLineageSettings": "{{string}}"
   },
   "Name": "{{string}}",
   "RecrawlPolicy": {
      "RecrawlBehavior": "{{string}}"
   },
   "Role": "{{string}}",
   "Schedule": "{{string}}",
   "SchemaChangePolicy": {
      "DeleteBehavior": "{{string}}",
      "UpdateBehavior": "{{string}}"
   },
   "TablePrefix": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "Targets": {
      "CatalogTargets": [
         {
            "ConnectionName": "{{string}}",
            "DatabaseName": "{{string}}",
            "DlqEventQueueArn": "{{string}}",
            "EventQueueArn": "{{string}}",
            "Tables": [ "{{string}}" ]
         }
      ],
      "DeltaTargets": [
         {
            "ConnectionName": "{{string}}",
            "CreateNativeDeltaTable": {{boolean}},
            "DeltaTables": [ "{{string}}" ],
            "WriteManifest": {{boolean}}
         }
      ],
      "DynamoDBTargets": [
         {
            "Path": "{{string}}",
            "scanAll": {{boolean}},
            "scanRate": {{number}}
         }
      ],
      "HudiTargets": [
         {
            "ConnectionName": "{{string}}",
            "Exclusions": [ "{{string}}" ],
            "MaximumTraversalDepth": {{number}},
            "Paths": [ "{{string}}" ]
         }
      ],
      "IcebergTargets": [
         {
            "ConnectionName": "{{string}}",
            "Exclusions": [ "{{string}}" ],
            "MaximumTraversalDepth": {{number}},
            "Paths": [ "{{string}}" ]
         }
      ],
      "JdbcTargets": [
         {
            "ConnectionName": "{{string}}",
            "EnableAdditionalMetadata": [ "{{string}}" ],
            "Exclusions": [ "{{string}}" ],
            "Path": "{{string}}"
         }
      ],
      "MongoDBTargets": [
         {
            "ConnectionName": "{{string}}",
            "Path": "{{string}}",
            "ScanAll": {{boolean}}
         }
      ],
      "S3Targets": [
         {
            "ConnectionName": "{{string}}",
            "DlqEventQueueArn": "{{string}}",
            "EventQueueArn": "{{string}}",
            "Exclusions": [ "{{string}}" ],
            "Path": "{{string}}",
            "SampleSize": {{number}}
         }
      ]
   }
}
```

## Request Parameters
<a name="API_CreateCrawler_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Classifiers](#API_CreateCrawler_RequestSyntax) **   <a name="Glue-CreateCrawler-request-Classifiers"></a>
A list of custom classifiers that the user has registered. By default, all built-in classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Configuration](#API_CreateCrawler_RequestSyntax) **   <a name="Glue-CreateCrawler-request-Configuration"></a>
Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler's behavior. For more information, see [Setting crawler configuration options](https://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html).
Type: String
Required: No

 ** [CrawlerSecurityConfiguration](#API_CreateCrawler_RequestSyntax) **   <a name="Glue-CreateCrawler-request-CrawlerSecurityConfiguration"></a>
The name of the `SecurityConfiguration` structure to be used by this crawler.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [DatabaseName](#API_CreateCrawler_RequestSyntax) **   <a name="Glue-CreateCrawler-request-DatabaseName"></a>
The AWS Glue database where results are written, such as: `arn:aws:daylight:us-east-1::database/sometable/*`.
Type: String
Required: No

 ** [Description](#API_CreateCrawler_RequestSyntax) **   <a name="Glue-CreateCrawler-request-Description"></a>
A description of the new crawler.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [LakeFormationConfiguration](#API_CreateCrawler_RequestSyntax) **   <a name="Glue-CreateCrawler-request-LakeFormationConfiguration"></a>
Specifies AWS Lake Formation configuration settings for the crawler.
Type: [LakeFormationConfiguration](API_LakeFormationConfiguration.md) object
Required: No

 ** [LineageConfiguration](#API_CreateCrawler_RequestSyntax) **   <a name="Glue-CreateCrawler-request-LineageConfiguration"></a>
Specifies data lineage configuration settings for the crawler.
Type: [LineageConfiguration](API_LineageConfiguration.md) object
Required: No

 ** [Name](#API_CreateCrawler_RequestSyntax) **   <a name="Glue-CreateCrawler-request-Name"></a>
Name of the new crawler.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [RecrawlPolicy](#API_CreateCrawler_RequestSyntax) **   <a name="Glue-CreateCrawler-request-RecrawlPolicy"></a>
A policy that specifies whether to crawl the entire dataset again, or to crawl only folders that were added since the last crawler run.
Type: [RecrawlPolicy](API_RecrawlPolicy.md) object
Required: No

 ** [Role](#API_CreateCrawler_RequestSyntax) **   <a name="Glue-CreateCrawler-request-Role"></a>
The IAM role or Amazon Resource Name (ARN) of an IAM role used by the new crawler to access customer resources.
Type: String
Required: Yes

 ** [Schedule](#API_CreateCrawler_RequestSyntax) **   <a name="Glue-CreateCrawler-request-Schedule"></a>
A `cron` expression used to specify the schedule (see [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html). For example, to run something every day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
Type: String
Required: No

 ** [SchemaChangePolicy](#API_CreateCrawler_RequestSyntax) **   <a name="Glue-CreateCrawler-request-SchemaChangePolicy"></a>
The policy for the crawler's update and deletion behavior.
Type: [SchemaChangePolicy](API_SchemaChangePolicy.md) object
Required: No

 ** [TablePrefix](#API_CreateCrawler_RequestSyntax) **   <a name="Glue-CreateCrawler-request-TablePrefix"></a>
The table prefix used for catalog tables that are created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [Tags](#API_CreateCrawler_RequestSyntax) **   <a name="Glue-CreateCrawler-request-Tags"></a>
The tags to use with this crawler request. You may use tags to limit access to the crawler. For more information about tags in AWS Glue, see [AWS Tags in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html) in the developer guide.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [Targets](#API_CreateCrawler_RequestSyntax) **   <a name="Glue-CreateCrawler-request-Targets"></a>
A list of collection of targets to crawl.
Type: [CrawlerTargets](API_CrawlerTargets.md) object
Required: Yes

## Response Elements
<a name="API_CreateCrawler_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateCrawler_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

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

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_CreateCrawler_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateCrawler)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateCrawler)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateCrawler)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateCrawler)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateCrawler)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateCrawler)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateCrawler)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateCrawler)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateCrawler)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateCrawler)
