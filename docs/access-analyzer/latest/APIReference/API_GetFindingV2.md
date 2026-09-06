---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetFindingV2.html
---

# GetFindingV2
<a name="API_GetFindingV2"></a>

Retrieves information about the specified finding. GetFinding and GetFindingV2 both use `access-analyzer:GetFinding` in the `Action` element of an IAM policy statement. You must have permission to perform the `access-analyzer:GetFinding` action.

## Request Syntax
<a name="API_GetFindingV2_RequestSyntax"></a>

```
GET /findingv2/{{id}}?analyzerArn={{analyzerArn}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFindingV2_RequestParameters"></a>

The request uses the following URI parameters.

 ** [analyzerArn](#API_GetFindingV2_RequestSyntax) **   <a name="accessanalyzer-GetFindingV2-request-uri-analyzerArn"></a>
The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) that generated the finding.
Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`
Required: Yes

 ** [id](#API_GetFindingV2_RequestSyntax) **   <a name="accessanalyzer-GetFindingV2-request-uri-id"></a>
The ID of the finding to retrieve.
Required: Yes

 ** [maxResults](#API_GetFindingV2_RequestSyntax) **   <a name="accessanalyzer-GetFindingV2-request-uri-maxResults"></a>
The maximum number of results to return in the response.

 ** [nextToken](#API_GetFindingV2_RequestSyntax) **   <a name="accessanalyzer-GetFindingV2-request-uri-nextToken"></a>
A token used for pagination of results returned.

## Request Body
<a name="API_GetFindingV2_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFindingV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "analyzedAt": "string",
   "createdAt": "string",
   "error": "string",
   "findingDetails": [
      { ... }
   ],
   "findingType": "string",
   "id": "string",
   "nextToken": "string",
   "resource": "string",
   "resourceOwnerAccount": "string",
   "resourceType": "string",
   "status": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_GetFindingV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [analyzedAt](#API_GetFindingV2_ResponseSyntax) **   <a name="accessanalyzer-GetFindingV2-response-analyzedAt"></a>
The time at which the resource-based policy or IAM entity that generated the finding was analyzed.
Type: Timestamp

 ** [createdAt](#API_GetFindingV2_ResponseSyntax) **   <a name="accessanalyzer-GetFindingV2-response-createdAt"></a>
The time at which the finding was created.
Type: Timestamp

 ** [error](#API_GetFindingV2_ResponseSyntax) **   <a name="accessanalyzer-GetFindingV2-response-error"></a>
An error.
Type: String

 ** [findingDetails](#API_GetFindingV2_ResponseSyntax) **   <a name="accessanalyzer-GetFindingV2-response-findingDetails"></a>
A localized message that explains the finding and provides guidance on how to address it.
Type: Array of [FindingDetails](API_FindingDetails.md) objects

 ** [findingType](#API_GetFindingV2_ResponseSyntax) **   <a name="accessanalyzer-GetFindingV2-response-findingType"></a>
The type of the finding. For external access analyzers, the type is `ExternalAccess`. For unused access analyzers, the type can be `UnusedIAMRole`, `UnusedIAMUserAccessKey`, `UnusedIAMUserPassword`, or `UnusedPermission`. For internal access analyzers, the type is `InternalAccess`.
Type: String
Valid Values: `ExternalAccess | UnusedIAMRole | UnusedIAMUserAccessKey | UnusedIAMUserPassword | UnusedPermission | InternalAccess`

 ** [id](#API_GetFindingV2_ResponseSyntax) **   <a name="accessanalyzer-GetFindingV2-response-id"></a>
The ID of the finding to retrieve.
Type: String

 ** [nextToken](#API_GetFindingV2_ResponseSyntax) **   <a name="accessanalyzer-GetFindingV2-response-nextToken"></a>
A token used for pagination of results returned.
Type: String

 ** [resource](#API_GetFindingV2_ResponseSyntax) **   <a name="accessanalyzer-GetFindingV2-response-resource"></a>
The resource that generated the finding.
Type: String

 ** [resourceOwnerAccount](#API_GetFindingV2_ResponseSyntax) **   <a name="accessanalyzer-GetFindingV2-response-resourceOwnerAccount"></a>
Tye AWS account ID that owns the resource.
Type: String

 ** [resourceType](#API_GetFindingV2_ResponseSyntax) **   <a name="accessanalyzer-GetFindingV2-response-resourceType"></a>
The type of the resource identified in the finding.
Type: String
Valid Values: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`

 ** [status](#API_GetFindingV2_ResponseSyntax) **   <a name="accessanalyzer-GetFindingV2-response-status"></a>
The status of the finding.
Type: String
Valid Values: `ACTIVE | ARCHIVED | RESOLVED`

 ** [updatedAt](#API_GetFindingV2_ResponseSyntax) **   <a name="accessanalyzer-GetFindingV2-response-updatedAt"></a>
The time at which the finding was updated.
Type: Timestamp

## Errors
<a name="API_GetFindingV2_Errors"></a>

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
<a name="API_GetFindingV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/GetFindingV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/GetFindingV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GetFindingV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/GetFindingV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GetFindingV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/GetFindingV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/GetFindingV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/GetFindingV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/GetFindingV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GetFindingV2)
