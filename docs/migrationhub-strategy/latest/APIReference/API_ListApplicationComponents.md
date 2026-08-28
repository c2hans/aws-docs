---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListApplicationComponents.html
---

# ListApplicationComponents
<a name="API_ListApplicationComponents"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

 Retrieves a list of all the application components (processes).

## Request Syntax
<a name="API_ListApplicationComponents_RequestSyntax"></a>

```
POST /list-applicationcomponents HTTP/1.1
Content-type: application/json

{
   "applicationComponentCriteria": "{{string}}",
   "filterValue": "{{string}}",
   "groupIdFilter": [
      {
         "name": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sort": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListApplicationComponents_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListApplicationComponents_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applicationComponentCriteria](#API_ListApplicationComponents_RequestSyntax) **   <a name="migrationhubstrategy-ListApplicationComponents-request-applicationComponentCriteria"></a>
 Criteria for filtering the list of application components.
Type: String
Valid Values: `NOT_DEFINED | APP_NAME | SERVER_ID | APP_TYPE | STRATEGY | DESTINATION | ANALYSIS_STATUS | ERROR_CATEGORY`
Required: No

 ** [filterValue](#API_ListApplicationComponents_RequestSyntax) **   <a name="migrationhubstrategy-ListApplicationComponents-request-filterValue"></a>
 Specify the value based on the application component criteria type. For example, if `applicationComponentCriteria` is set to `SERVER_ID` and `filterValue` is set to `server1`, then [ListApplicationComponents](#API_ListApplicationComponents) returns all the application components running on server1.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** [groupIdFilter](#API_ListApplicationComponents_RequestSyntax) **   <a name="migrationhubstrategy-ListApplicationComponents-request-groupIdFilter"></a>
 The group ID specified in to filter on.
Type: Array of [Group](API_Group.md) objects
Required: No

 ** [maxResults](#API_ListApplicationComponents_RequestSyntax) **   <a name="migrationhubstrategy-ListApplicationComponents-request-maxResults"></a>
 The maximum number of items to include in the response. The maximum value is 100.
Type: Integer
Required: No

 ** [nextToken](#API_ListApplicationComponents_RequestSyntax) **   <a name="migrationhubstrategy-ListApplicationComponents-request-nextToken"></a>
 The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set `maxResults` to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** [sort](#API_ListApplicationComponents_RequestSyntax) **   <a name="migrationhubstrategy-ListApplicationComponents-request-sort"></a>
 Specifies whether to sort by ascending (`ASC`) or descending (`DESC`) order.
Type: String
Valid Values: `ASC | DESC`
Required: No

## Response Syntax
<a name="API_ListApplicationComponents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationComponentInfos": [
      {
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
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListApplicationComponents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationComponentInfos](#API_ListApplicationComponents_ResponseSyntax) **   <a name="migrationhubstrategy-ListApplicationComponents-response-applicationComponentInfos"></a>
 The list of application components with detailed information about each component.
Type: Array of [ApplicationComponentDetail](API_ApplicationComponentDetail.md) objects

 ** [nextToken](#API_ListApplicationComponents_ResponseSyntax) **   <a name="migrationhubstrategy-ListApplicationComponents-response-nextToken"></a>
 The token you use to retrieve the next set of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*\S.*`

## Errors
<a name="API_ListApplicationComponents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.
HTTP Status Code: 403

 ** InternalServerException **
 The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ServiceLinkedRoleLockClientException **
 Exception to indicate that the service-linked role (SLR) is locked.
HTTP Status Code: 400

 ** ValidationException **
 The request body isn't valid.
HTTP Status Code: 400

## See Also
<a name="API_ListApplicationComponents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhubstrategy-2020-02-19/ListApplicationComponents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhubstrategy-2020-02-19/ListApplicationComponents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/ListApplicationComponents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhubstrategy-2020-02-19/ListApplicationComponents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/ListApplicationComponents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhubstrategy-2020-02-19/ListApplicationComponents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhubstrategy-2020-02-19/ListApplicationComponents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhubstrategy-2020-02-19/ListApplicationComponents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhubstrategy-2020-02-19/ListApplicationComponents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/ListApplicationComponents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
