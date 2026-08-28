---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetServerDetails.html
---

# GetServerDetails
<a name="API_GetServerDetails"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

 Retrieves detailed information about a specified server.

## Request Syntax
<a name="API_GetServerDetails_RequestSyntax"></a>

```
GET /get-server-details/{{serverId}}?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetServerDetails_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_GetServerDetails_RequestSyntax) **   <a name="migrationhubstrategy-GetServerDetails-request-uri-maxResults"></a>
 The maximum number of items to include in the response. The maximum value is 100.

 ** [nextToken](#API_GetServerDetails_RequestSyntax) **   <a name="migrationhubstrategy-GetServerDetails-request-uri-nextToken"></a>
 The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set `maxResults` to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*\S.*`

 ** [serverId](#API_GetServerDetails_RequestSyntax) **   <a name="migrationhubstrategy-GetServerDetails-request-uri-serverId"></a>
 The ID of the server.
Length Constraints: Minimum length of 1. Maximum length of 27.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_GetServerDetails_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetServerDetails_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "associatedApplications": [
      {
         "id": "string",
         "name": "string"
      }
   ],
   "nextToken": "string",
   "serverDetail": {
      "antipatternReportS3Object": {
         "s3Bucket": "string",
         "s3key": "string"
      },
      "antipatternReportStatus": "string",
      "antipatternReportStatusMessage": "string",
      "applicationComponentStrategySummary": [
         {
            "count": number,
            "strategy": "string"
         }
      ],
      "dataCollectionStatus": "string",
      "id": "string",
      "lastAnalyzedTimestamp": number,
      "listAntipatternSeveritySummary": [
         {
            "count": number,
            "severity": "string"
         }
      ],
      "name": "string",
      "recommendationSet": {
         "strategy": "string",
         "targetDestination": "string",
         "transformationTool": {
            "description": "string",
            "name": "string",
            "tranformationToolInstallationLink": "string"
         }
      },
      "serverError": {
         "serverErrorCategory": "string"
      },
      "serverType": "string",
      "statusMessage": "string",
      "systemInfo": {
         "cpuArchitecture": "string",
         "fileSystemType": "string",
         "networkInfoList": [
            {
               "interfaceName": "string",
               "ipAddress": "string",
               "macAddress": "string",
               "netMask": "string"
            }
         ],
         "osInfo": {
            "type": "string",
            "version": "string"
         }
      }
   }
}
```

## Response Elements
<a name="API_GetServerDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associatedApplications](#API_GetServerDetails_ResponseSyntax) **   <a name="migrationhubstrategy-GetServerDetails-response-associatedApplications"></a>
 The associated application group the server belongs to, as defined in AWS Application Discovery Service.
Type: Array of [AssociatedApplication](API_AssociatedApplication.md) objects

 ** [nextToken](#API_GetServerDetails_ResponseSyntax) **   <a name="migrationhubstrategy-GetServerDetails-response-nextToken"></a>
 The token you use to retrieve the next set of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [serverDetail](#API_GetServerDetails_ResponseSyntax) **   <a name="migrationhubstrategy-GetServerDetails-response-serverDetail"></a>
 Detailed information about the server.
Type: [ServerDetail](API_ServerDetail.md) object

## Errors
<a name="API_GetServerDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.
HTTP Status Code: 403

 ** InternalServerException **
 The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The specified ID in the request is not found.
HTTP Status Code: 404

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
 The request body isn't valid.
HTTP Status Code: 400

## See Also
<a name="API_GetServerDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhubstrategy-2020-02-19/GetServerDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhubstrategy-2020-02-19/GetServerDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/GetServerDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhubstrategy-2020-02-19/GetServerDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/GetServerDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhubstrategy-2020-02-19/GetServerDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhubstrategy-2020-02-19/GetServerDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhubstrategy-2020-02-19/GetServerDetails)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhubstrategy-2020-02-19/GetServerDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/GetServerDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
