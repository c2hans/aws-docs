---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCoverageStatistics.html
---

# ListCoverageStatistics
<a name="API_ListCoverageStatistics"></a>

Lists Amazon Inspector coverage statistics for your environment.

## Request Syntax
<a name="API_ListCoverageStatistics_RequestSyntax"></a>

```
POST /coverage/statistics/list HTTP/1.1
Content-type: application/json

{
   "filterCriteria": {
      "accountId": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudContainerImageTags": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudContainerRegistryName": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudContainerRepositoryName": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudProvider": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudProviderAccountId": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudProviderOrgId": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudProviderRegion": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudServerlessFunctionName": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudServerlessFunctionRuntime": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudServerlessFunctionTags": [
         {
            "comparison": "{{string}}",
            "key": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudVmInstanceTags": [
         {
            "comparison": "{{string}}",
            "key": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "codeRepositoryProjectName": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "codeRepositoryProviderType": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "codeRepositoryProviderTypeVisibility": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "ec2InstanceTags": [
         {
            "comparison": "{{string}}",
            "key": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "ecrImageInUseCount": [
         {
            "lowerInclusive": {{number}},
            "upperInclusive": {{number}}
         }
      ],
      "ecrImageLastInUseAt": [
         {
            "endInclusive": {{number}},
            "startInclusive": {{number}}
         }
      ],
      "ecrImageTags": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "ecrRepositoryName": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "imagePulledAt": [
         {
            "endInclusive": {{number}},
            "startInclusive": {{number}}
         }
      ],
      "lambdaFunctionName": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "lambdaFunctionRuntime": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "lambdaFunctionTags": [
         {
            "comparison": "{{string}}",
            "key": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "lastScannedAt": [
         {
            "endInclusive": {{number}},
            "startInclusive": {{number}}
         }
      ],
      "lastScannedCommitId": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "resourceId": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "resourceType": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "scanMode": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "scanStatusCode": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "scanStatusReason": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "scanType": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ]
   },
   "groupBy": "{{string}}",
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListCoverageStatistics_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListCoverageStatistics_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filterCriteria](#API_ListCoverageStatistics_RequestSyntax) **   <a name="inspector2-ListCoverageStatistics-request-filterCriteria"></a>
An object that contains details on the filters to apply to the coverage data for your environment.
Type: [CoverageFilterCriteria](API_CoverageFilterCriteria.md) object
Required: No

 ** [groupBy](#API_ListCoverageStatistics_RequestSyntax) **   <a name="inspector2-ListCoverageStatistics-request-groupBy"></a>
The value to group the results by.
Type: String
Valid Values: `SCAN_STATUS_CODE | SCAN_STATUS_REASON | ACCOUNT_ID | RESOURCE_TYPE | ECR_REPOSITORY_NAME | PROVIDER | PROVIDER_ACCOUNT_ID | PROVIDER_REGION | PROVIDER_ORG_ID`
Required: No

 ** [nextToken](#API_ListCoverageStatistics_RequestSyntax) **   <a name="inspector2-ListCoverageStatistics-request-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the `NextToken` value returned from the previous request to continue listing results after the first page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.
Required: No

## Response Syntax
<a name="API_ListCoverageStatistics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "countsByGroup": [
      {
         "count": number,
         "groupKey": "string"
      }
   ],
   "nextToken": "string",
   "totalCounts": number
}
```

## Response Elements
<a name="API_ListCoverageStatistics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [countsByGroup](#API_ListCoverageStatistics_ResponseSyntax) **   <a name="inspector2-ListCoverageStatistics-response-countsByGroup"></a>
An array with the number for each group.
Type: Array of [Counts](API_Counts.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.

 ** [nextToken](#API_ListCoverageStatistics_ResponseSyntax) **   <a name="inspector2-ListCoverageStatistics-response-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the `NextToken` value returned from the previous request to continue listing results after the first page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.

 ** [totalCounts](#API_ListCoverageStatistics_ResponseSyntax) **   <a name="inspector2-ListCoverageStatistics-response-totalCounts"></a>
The total number for all groups.
Type: Long

## Errors
<a name="API_ListCoverageStatistics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListCoverageStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/ListCoverageStatistics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/ListCoverageStatistics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ListCoverageStatistics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/ListCoverageStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ListCoverageStatistics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/ListCoverageStatistics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/ListCoverageStatistics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/ListCoverageStatistics)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/ListCoverageStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ListCoverageStatistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
