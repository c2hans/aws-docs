---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateDataset.html
---

# CreateDataset
<a name="API_CreateDataset"></a>

Creates a dataset. Session and curated datasets are created in a workspace. A session dataset contains data segments of time series data, and a curated dataset curates data segments selected from source session datasets. A dataset that connects to an external datasource is created outside of a workspace.

## Request Syntax
<a name="API_CreateDataset_RequestSyntax"></a>

```
POST /datasets HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "datasetConfig": {
      "session": {
         "sessionEndTimestamp": {
            "offsetInNanos": {{number}},
            "timeInSeconds": {{number}}
         },
         "sessionStartTimestamp": {
            "offsetInNanos": {{number}},
            "timeInSeconds": {{number}}
         }
      }
   },
   "datasetDescription": "{{string}}",
   "datasetId": "{{string}}",
   "datasetName": "{{string}}",
   "datasetSource": {
      "sourceDetail": {
         "kendra": {
            "knowledgeBaseArn": "{{string}}",
            "roleArn": "{{string}}"
         }
      },
      "sourceFormat": "{{string}}",
      "sourceType": "{{string}}"
   },
   "datasetType": "{{string}}",
   "metadata": {
      "{{string}}" : "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "workspaceName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateDataset_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDataset_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateDataset_RequestSyntax) **   <a name="iotsitewise-CreateDataset-request-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [datasetConfig](#API_CreateDataset_RequestSyntax) **   <a name="iotsitewise-CreateDataset-request-datasetConfig"></a>
The configuration for the dataset.
Type: [DatasetConfig](API_DatasetConfig.md) object
Required: No

 ** [datasetDescription](#API_CreateDataset_RequestSyntax) **   <a name="iotsitewise-CreateDataset-request-datasetDescription"></a>
A description about the dataset, and its functionality.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [datasetId](#API_CreateDataset_RequestSyntax) **   <a name="iotsitewise-CreateDataset-request-datasetId"></a>
The ID of the dataset.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** [datasetName](#API_CreateDataset_RequestSyntax) **   <a name="iotsitewise-CreateDataset-request-datasetName"></a>
The name of the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9 _\-#$*!@.]+$`
Required: Yes

 ** [datasetSource](#API_CreateDataset_RequestSyntax) **   <a name="iotsitewise-CreateDataset-request-datasetSource"></a>
The data source for the dataset.
Type: [DatasetSource](API_DatasetSource.md) object
Required: Yes

 ** [datasetType](#API_CreateDataset_RequestSyntax) **   <a name="iotsitewise-CreateDataset-request-datasetType"></a>
The type of dataset: a session dataset, a curated dataset, or a connection to an external datasource.
Type: String
Valid Values: `SESSION | CURATED | EXTERNAL`
Required: No

 ** [metadata](#API_CreateDataset_RequestSyntax) **   <a name="iotsitewise-CreateDataset-request-metadata"></a>
The metadata for the dataset, provided as key-value pairs.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [tags](#API_CreateDataset_RequestSyntax) **   <a name="iotsitewise-CreateDataset-request-tags"></a>
A list of key-value pairs that contain metadata for the access policy. For more information, see [Tagging your AWS IoT SiteWise resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html) in the * AWS IoT SiteWise User Guide*.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [workspaceName](#API_CreateDataset_RequestSyntax) **   <a name="iotsitewise-CreateDataset-request-workspaceName"></a>
The name of the workspace that contains the dataset. Required for session and curated datasets. Omit this field for datasets that connect to an external datasource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

## Response Syntax
<a name="API_CreateDataset_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "datasetArn": "string",
   "datasetId": "string",
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
   }
}
```

## Response Elements
<a name="API_CreateDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [datasetArn](#API_CreateDataset_ResponseSyntax) **   <a name="iotsitewise-CreateDataset-response-datasetArn"></a>
The [ARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) of the dataset. The format is `arn:${Partition}:iotsitewise:${Region}:${Account}:dataset/${DatasetId}`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [datasetId](#API_CreateDataset_ResponseSyntax) **   <a name="iotsitewise-CreateDataset-response-datasetId"></a>
The ID of the dataset.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [datasetStatus](#API_CreateDataset_ResponseSyntax) **   <a name="iotsitewise-CreateDataset-response-datasetStatus"></a>
The status of the dataset. This contains the state and any error messages. State is `CREATING` after a successfull call to this API, and any associated error message. The state is `ACTIVE` when ready to use.
Type: [DatasetStatus](API_DatasetStatus.md) object

## Errors
<a name="API_CreateDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictingOperationException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resourceArn **
The ARN of the resource that conflicts with this operation.
 ** resourceId **
The ID of the resource that conflicts with this operation.
HTTP Status Code: 409

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** LimitExceededException **
You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 410

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** resourceArn **
The ARN of the resource that already exists.
 ** resourceId **
The ID of the resource that already exists.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_CreateDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/CreateDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/CreateDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CreateDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/CreateDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CreateDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/CreateDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/CreateDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/CreateDataset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/CreateDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CreateDataset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
