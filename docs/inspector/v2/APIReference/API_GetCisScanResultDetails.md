---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetCisScanResultDetails.html
---

# GetCisScanResultDetails
<a name="API_GetCisScanResultDetails"></a>

Retrieves CIS scan result details.

## Request Syntax
<a name="API_GetCisScanResultDetails_RequestSyntax"></a>

```
POST /cis/scan-result/details/get HTTP/1.1
Content-type: application/json

{
   "accountId": "{{string}}",
   "filterCriteria": {
      "checkIdFilters": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "findingArnFilters": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "findingStatusFilters": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "securityLevelFilters": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "titleFilters": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "scanArn": "{{string}}",
   "sortBy": "{{string}}",
   "sortOrder": "{{string}}",
   "targetResourceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetCisScanResultDetails_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetCisScanResultDetails_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountId](#API_GetCisScanResultDetails_RequestSyntax) **   <a name="inspector2-GetCisScanResultDetails-request-accountId"></a>
The account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [filterCriteria](#API_GetCisScanResultDetails_RequestSyntax) **   <a name="inspector2-GetCisScanResultDetails-request-filterCriteria"></a>
The filter criteria.
Type: [CisScanResultDetailsFilterCriteria](API_CisScanResultDetailsFilterCriteria.md) object
Required: No

 ** [maxResults](#API_GetCisScanResultDetails_RequestSyntax) **   <a name="inspector2-GetCisScanResultDetails-request-maxResults"></a>
The maximum number of CIS scan result details to be returned in a single page of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_GetCisScanResultDetails_RequestSyntax) **   <a name="inspector2-GetCisScanResultDetails-request-nextToken"></a>
The pagination token from a previous request that's used to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.
Required: No

 ** [scanArn](#API_GetCisScanResultDetails_RequestSyntax) **   <a name="inspector2-GetCisScanResultDetails-request-scanArn"></a>
The scan ARN.
Type: String
Pattern: `arn:aws(-us-gov|-cn)?:inspector2:[-.a-z0-9]{0,20}:\d{12}:owner/(\d{12}|o-[a-z0-9]{10,32})/cis-scan/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** [sortBy](#API_GetCisScanResultDetails_RequestSyntax) **   <a name="inspector2-GetCisScanResultDetails-request-sortBy"></a>
The sort by order.
Type: String
Valid Values: `CHECK_ID | STATUS`
Required: No

 ** [sortOrder](#API_GetCisScanResultDetails_RequestSyntax) **   <a name="inspector2-GetCisScanResultDetails-request-sortOrder"></a>
The sort order.
Type: String
Valid Values: `ASC | DESC`
Required: No

 ** [targetResourceId](#API_GetCisScanResultDetails_RequestSyntax) **   <a name="inspector2-GetCisScanResultDetails-request-targetResourceId"></a>
The target resource ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1024.
Pattern: `.*(^arn:.*:ecr:.*:\d{12}:repository\/[a-zA-Z0-9._\/-]+(\/sha256:[a-z0-9]{64})?$)|(^i-([a-z0-9]{8}|[a-z0-9]{17}|\\*)$|(^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$)|(^arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:codesecurity-integration\/[a-f0-9-]{36}\/project-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$))|(^\/subscriptions\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\/resourcegroups\/[a-z0-9_\-\.()]+\/providers\/(microsoft\.compute\/virtualmachines\/[a-z0-9_\-]+|microsoft\.web\/sites\/[a-z0-9_\-]+|microsoft\.containerregistry\/registries\/[a-z0-9_\-]+(\/repositories\/[a-z0-9_\-\/]+\/images?\/sha256:[a-f0-9]{64})?)$).*`
Required: Yes

## Response Syntax
<a name="API_GetCisScanResultDetails_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "scanResultDetails": [
      {
         "accountId": "string",
         "checkDescription": "string",
         "checkId": "string",
         "findingArn": "string",
         "level": "string",
         "platform": "string",
         "remediation": "string",
         "scanArn": "string",
         "status": "string",
         "statusReason": "string",
         "targetResourceId": "string",
         "title": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetCisScanResultDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_GetCisScanResultDetails_ResponseSyntax) **   <a name="inspector2-GetCisScanResultDetails-response-nextToken"></a>
The pagination token from a previous request that's used to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.

 ** [scanResultDetails](#API_GetCisScanResultDetails_ResponseSyntax) **   <a name="inspector2-GetCisScanResultDetails-response-scanResultDetails"></a>
The scan result details.
Type: Array of [CisScanResultDetails](API_CisScanResultDetails.md) objects
Array Members: Minimum number of 1 item. Maximum number of 1000 items.

## Errors
<a name="API_GetCisScanResultDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

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
<a name="API_GetCisScanResultDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/GetCisScanResultDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/GetCisScanResultDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/GetCisScanResultDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/GetCisScanResultDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/GetCisScanResultDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/GetCisScanResultDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/GetCisScanResultDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/GetCisScanResultDetails)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/GetCisScanResultDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/GetCisScanResultDetails)
