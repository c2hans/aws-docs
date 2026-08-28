---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeDataset.html
---

# DescribeDataset
<a name="API_DescribeDataset"></a>

Retrieves information about a dataset.

## Request Syntax
<a name="API_DescribeDataset_RequestSyntax"></a>

```
GET /datasets/{{datasetId}}?datasetVersion={{datasetVersion}}&workspaceName={{workspaceName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDataset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datasetId](#API_DescribeDataset_RequestSyntax) **   <a name="iotsitewise-DescribeDataset-request-uri-datasetId"></a>
The ID of the dataset.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** [datasetVersion](#API_DescribeDataset_RequestSyntax) **   <a name="iotsitewise-DescribeDataset-request-uri-datasetVersion"></a>
The version of the dataset.
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`

 ** [workspaceName](#API_DescribeDataset_RequestSyntax) **   <a name="iotsitewise-DescribeDataset-request-uri-workspaceName"></a>
The name of the workspace that contains the dataset.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Request Body
<a name="API_DescribeDataset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDataset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datasetArn": "string",
   "datasetConfig": {
      "session": {
         "sessionEndTimestamp": {
            "offsetInNanos": number,
            "timeInSeconds": number
         },
         "sessionStartTimestamp": {
            "offsetInNanos": number,
            "timeInSeconds": number
         }
      }
   },
   "datasetCreationDate": number,
   "datasetDescription": "string",
   "datasetId": "string",
   "datasetLastUpdateDate": number,
   "datasetName": "string",
   "datasetSource": {
      "sourceDetail": {
         "kendra": {
            "knowledgeBaseArn": "string",
            "roleArn": "string"
         }
      },
      "sourceFormat": "string",
      "sourceType": "string"
   },
   "datasetStatus": {
      "error": {
         "code": "string",
         "details": [
            {
               "code": "string",
               "message": "string"
            }
         ],
         "message": "string"
      },
      "state": "string"
   },
   "datasetType": "string",
   "datasetVersion": "string",
   "enrichmentStatus": {
      "video": {
         "lastEnrichedAt": number,
         "status": "string"
      }
   },
   "metadata": {
      "string" : "string"
   },
   "workspaceName": "string"
}
```

## Response Elements
<a name="API_DescribeDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datasetArn](#API_DescribeDataset_ResponseSyntax) **   <a name="iotsitewise-DescribeDataset-response-datasetArn"></a>
The [ARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) of the dataset. The format is `arn:${Partition}:iotsitewise:${Region}:${Account}:dataset/${DatasetId}`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [datasetConfig](#API_DescribeDataset_ResponseSyntax) **   <a name="iotsitewise-DescribeDataset-response-datasetConfig"></a>
The configuration for the dataset.
Type: [DatasetConfig](API_DatasetConfig.md) object

 ** [datasetCreationDate](#API_DescribeDataset_ResponseSyntax) **   <a name="iotsitewise-DescribeDataset-response-datasetCreationDate"></a>
The dataset creation date, in Unix epoch time.
Type: Timestamp

 ** [datasetDescription](#API_DescribeDataset_ResponseSyntax) **   <a name="iotsitewise-DescribeDataset-response-datasetDescription"></a>
A description about the dataset, and its functionality.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [datasetId](#API_DescribeDataset_ResponseSyntax) **   <a name="iotsitewise-DescribeDataset-response-datasetId"></a>
The ID of the dataset.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [datasetLastUpdateDate](#API_DescribeDataset_ResponseSyntax) **   <a name="iotsitewise-DescribeDataset-response-datasetLastUpdateDate"></a>
The date the dataset was last updated, in Unix epoch time.
Type: Timestamp

 ** [datasetName](#API_DescribeDataset_ResponseSyntax) **   <a name="iotsitewise-DescribeDataset-response-datasetName"></a>
The name of the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9 _\-#$*!@.]+$`

 ** [datasetSource](#API_DescribeDataset_ResponseSyntax) **   <a name="iotsitewise-DescribeDataset-response-datasetSource"></a>
The data source for the dataset.
Type: [DatasetSource](API_DatasetSource.md) object

 ** [datasetStatus](#API_DescribeDataset_ResponseSyntax) **   <a name="iotsitewise-DescribeDataset-response-datasetStatus"></a>
The status of the dataset. This contains the state and any error messages. State is `CREATING` after a successfull call to this API, and any associated error message. The state is `ACTIVE` when ready to use.
Type: [DatasetStatus](API_DatasetStatus.md) object

 ** [datasetType](#API_DescribeDataset_ResponseSyntax) **   <a name="iotsitewise-DescribeDataset-response-datasetType"></a>
The type of dataset: a session dataset, a curated dataset, or a connection to an external datasource.
Type: String
Valid Values: `SESSION | CURATED | EXTERNAL`

 ** [datasetVersion](#API_DescribeDataset_ResponseSyntax) **   <a name="iotsitewise-DescribeDataset-response-datasetVersion"></a>
The version of the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`

 ** [enrichmentStatus](#API_DescribeDataset_ResponseSyntax) **   <a name="iotsitewise-DescribeDataset-response-enrichmentStatus"></a>
The enrichment status of the dataset.
Type: [DatasetEnrichment](API_DatasetEnrichment.md) object

 ** [metadata](#API_DescribeDataset_ResponseSyntax) **   <a name="iotsitewise-DescribeDataset-response-metadata"></a>
The metadata for the dataset.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [workspaceName](#API_DescribeDataset_ResponseSyntax) **   <a name="iotsitewise-DescribeDataset-response-workspaceName"></a>
The name of the workspace that contains the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Errors
<a name="API_DescribeDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_DescribeDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeDataset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeDataset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
