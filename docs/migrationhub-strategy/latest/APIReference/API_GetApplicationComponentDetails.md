---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetApplicationComponentDetails.html
---

# GetApplicationComponentDetails
<a name="API_GetApplicationComponentDetails"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

 Retrieves details about an application component.

## Request Syntax
<a name="API_GetApplicationComponentDetails_RequestSyntax"></a>

```
GET /get-applicationcomponent-details/{{applicationComponentId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetApplicationComponentDetails_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationComponentId](#API_GetApplicationComponentDetails_RequestSyntax) **   <a name="migrationhubstrategy-GetApplicationComponentDetails-request-uri-applicationComponentId"></a>
 The ID of the application component. The ID is unique within an AWS account.
Length Constraints: Minimum length of 0. Maximum length of 44.
Pattern: `.*[0-9a-zA-Z-]+.*`
Required: Yes

## Request Body
<a name="API_GetApplicationComponentDetails_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetApplicationComponentDetails_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationComponentDetail": {
      "analysisStatus": "string",
      "antipatternReportS3Object": {
         "s3Bucket": "string",
         "s3key": "string"
      },
      "antipatternReportStatus": "string",
      "antipatternReportStatusMessage": "string",
      "appType": "string",
      "appUnitError": {
         "appUnitErrorCategory": "string"
      },
      "associatedServerId": "string",
      "databaseConfigDetail": {
         "secretName": "string"
      },
      "id": "string",
      "inclusionStatus": "string",
      "lastAnalyzedTimestamp": number,
      "listAntipatternSeveritySummary": [
         {
            "count": number,
            "severity": "string"
         }
      ],
      "moreServerAssociationExists": boolean,
      "name": "string",
      "osDriver": "string",
      "osVersion": "string",
      "recommendationSet": {
         "strategy": "string",
         "targetDestination": "string",
         "transformationTool": {
            "description": "string",
            "name": "string",
            "tranformationToolInstallationLink": "string"
         }
      },
      "resourceSubType": "string",
      "resultList": [
         {
            "analysisStatus": { ... },
            "analysisType": "string",
            "antipatternReportResultList": [
               {
                  "analyzerName": { ... },
                  "antiPatternReportS3Object": {
                     "s3Bucket": "string",
                     "s3key": "string"
                  },
                  "antipatternReportStatus": "string",
                  "antipatternReportStatusMessage": "string"
               }
            ],
            "statusMessage": "string"
         }
      ],
      "runtimeStatus": "string",
      "runtimeStatusMessage": "string",
      "sourceCodeRepositories": [
         {
            "branch": "string",
            "projectName": "string",
            "repository": "string",
            "versionControlType": "string"
         }
      ],
      "statusMessage": "string"
   },
   "associatedApplications": [
      {
         "id": "string",
         "name": "string"
      }
   ],
   "associatedServerIds": [ "string" ],
   "moreApplicationResource": boolean
}
```

## Response Elements
<a name="API_GetApplicationComponentDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationComponentDetail](#API_GetApplicationComponentDetails_ResponseSyntax) **   <a name="migrationhubstrategy-GetApplicationComponentDetails-response-applicationComponentDetail"></a>
 Detailed information about an application component.
Type: [ApplicationComponentDetail](API_ApplicationComponentDetail.md) object

 ** [associatedApplications](#API_GetApplicationComponentDetails_ResponseSyntax) **   <a name="migrationhubstrategy-GetApplicationComponentDetails-response-associatedApplications"></a>
 The associated application group as defined in AWS Application Discovery Service.
Type: Array of [AssociatedApplication](API_AssociatedApplication.md) objects

 ** [associatedServerIds](#API_GetApplicationComponentDetails_ResponseSyntax) **   <a name="migrationhubstrategy-GetApplicationComponentDetails-response-associatedServerIds"></a>
 A list of the IDs of the servers on which the application component is running.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [moreApplicationResource](#API_GetApplicationComponentDetails_ResponseSyntax) **   <a name="migrationhubstrategy-GetApplicationComponentDetails-response-moreApplicationResource"></a>
 Set to true if the application component belongs to more than one application group.
Type: Boolean

## Errors
<a name="API_GetApplicationComponentDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
 The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The specified ID in the request is not found.
HTTP Status Code: 404

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_GetApplicationComponentDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhubstrategy-2020-02-19/GetApplicationComponentDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhubstrategy-2020-02-19/GetApplicationComponentDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/GetApplicationComponentDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhubstrategy-2020-02-19/GetApplicationComponentDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/GetApplicationComponentDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhubstrategy-2020-02-19/GetApplicationComponentDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhubstrategy-2020-02-19/GetApplicationComponentDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhubstrategy-2020-02-19/GetApplicationComponentDetails)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhubstrategy-2020-02-19/GetApplicationComponentDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/GetApplicationComponentDetails)
