---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAnalyzedResources.html
---

# ListAnalyzedResources
<a name="API_ListAnalyzedResources"></a>

Retrieves a list of resources of the specified type that have been analyzed by the specified analyzer.

## Request Syntax
<a name="API_ListAnalyzedResources_RequestSyntax"></a>

```
POST /analyzed-resource HTTP/1.1
Content-type: application/json

{
   "analyzerArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "resourceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListAnalyzedResources_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListAnalyzedResources_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [analyzerArn](#API_ListAnalyzedResources_RequestSyntax) **   <a name="accessanalyzer-ListAnalyzedResources-request-analyzerArn"></a>
The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) to retrieve a list of analyzed resources from.
Type: String
Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`
Required: Yes

 ** [maxResults](#API_ListAnalyzedResources_RequestSyntax) **   <a name="accessanalyzer-ListAnalyzedResources-request-maxResults"></a>
The maximum number of results to return in the response.
Type: Integer
Required: No

 ** [nextToken](#API_ListAnalyzedResources_RequestSyntax) **   <a name="accessanalyzer-ListAnalyzedResources-request-nextToken"></a>
A token used for pagination of results returned.
Type: String
Required: No

 ** [resourceType](#API_ListAnalyzedResources_RequestSyntax) **   <a name="accessanalyzer-ListAnalyzedResources-request-resourceType"></a>
The type of resource.
Type: String
Valid Values: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`
Required: No

## Response Syntax
<a name="API_ListAnalyzedResources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "analyzedResources": [
      {
         "resourceArn": "string",
         "resourceOwnerAccount": "string",
         "resourceType": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAnalyzedResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [analyzedResources](#API_ListAnalyzedResources_ResponseSyntax) **   <a name="accessanalyzer-ListAnalyzedResources-response-analyzedResources"></a>
A list of resources that were analyzed.
Type: Array of [AnalyzedResourceSummary](API_AnalyzedResourceSummary.md) objects

 ** [nextToken](#API_ListAnalyzedResources_ResponseSyntax) **   <a name="accessanalyzer-ListAnalyzedResources-response-nextToken"></a>
A token used for pagination of results returned.
Type: String

## Errors
<a name="API_ListAnalyzedResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Internal server error.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ThrottlingException **
Throttling limit exceeded error.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 429

 ** ValidationException **
Validation exception error.
 ** fieldList **
A list of fields that didn't validate.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListAnalyzedResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/ListAnalyzedResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/ListAnalyzedResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ListAnalyzedResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/ListAnalyzedResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ListAnalyzedResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/ListAnalyzedResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/ListAnalyzedResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/ListAnalyzedResources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/ListAnalyzedResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ListAnalyzedResources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
