---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetFindingsStatistics.html
---

# GetFindingsStatistics
<a name="API_GetFindingsStatistics"></a>

Lists GuardDuty findings statistics for the specified detector ID.

You must provide either `findingStatisticTypes` or `groupBy` parameter, and not both. You can use the `maxResults` and `orderBy` parameters only when using `groupBy`.

There might be regional differences because some flags might not be available in all the Regions where GuardDuty is currently supported. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html).

## Request Syntax
<a name="API_GetFindingsStatistics_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/findings/statistics HTTP/1.1
Content-type: application/json

{
   "findingCriteria": {
      "criterion": {
         "{{string}}" : {
            "eq": [ "{{string}}" ],
            "equals": [ "{{string}}" ],
            "greaterThan": {{number}},
            "greaterThanOrEqual": {{number}},
            "gt": {{number}},
            "gte": {{number}},
            "lessThan": {{number}},
            "lessThanOrEqual": {{number}},
            "lt": {{number}},
            "lte": {{number}},
            "matches": [ "{{string}}" ],
            "neq": [ "{{string}}" ],
            "notEquals": [ "{{string}}" ],
            "notMatches": [ "{{string}}" ]
         }
      }
   },
   "findingStatisticTypes": [ "{{string}}" ],
   "groupBy": "{{string}}",
   "maxResults": {{number}},
   "orderBy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetFindingsStatistics_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_GetFindingsStatistics_RequestSyntax) **   <a name="guardduty-GetFindingsStatistics-request-uri-DetectorId"></a>
The ID of the detector whose findings statistics you want to retrieve.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_GetFindingsStatistics_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [findingCriteria](#API_GetFindingsStatistics_RequestSyntax) **   <a name="guardduty-GetFindingsStatistics-request-findingCriteria"></a>
Represents the criteria that is used for querying findings.
Type: [FindingCriteria](API_FindingCriteria.md) object
Required: No

 ** [findingStatisticTypes](#API_GetFindingsStatistics_RequestSyntax) **   <a name="guardduty-GetFindingsStatistics-request-findingStatisticTypes"></a>
 *This parameter has been deprecated.*
The types of finding statistics to retrieve.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Valid Values: `COUNT_BY_SEVERITY`
Required: No

 ** [groupBy](#API_GetFindingsStatistics_RequestSyntax) **   <a name="guardduty-GetFindingsStatistics-request-groupBy"></a>
Displays the findings statistics grouped by one of the listed valid values.
Type: String
Valid Values: `ACCOUNT | DATE | FINDING_TYPE | RESOURCE | SEVERITY`
Required: No

 ** [maxResults](#API_GetFindingsStatistics_RequestSyntax) **   <a name="guardduty-GetFindingsStatistics-request-maxResults"></a>
The maximum number of results to be returned in the response. The default value is 25.
You can use this parameter only with the `groupBy` parameter.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [orderBy](#API_GetFindingsStatistics_RequestSyntax) **   <a name="guardduty-GetFindingsStatistics-request-orderBy"></a>
Displays the sorted findings in the requested order. The default value of `orderBy` is `DESC`.
You can use this parameter only with the `groupBy` parameter.
Type: String
Valid Values: `ASC | DESC`
Required: No

## Response Syntax
<a name="API_GetFindingsStatistics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "findingStatistics": {
      "countBySeverity": {
         "string" : number
      },
      "groupedByAccount": [
         {
            "accountId": "string",
            "lastGeneratedAt": number,
            "totalFindings": number
         }
      ],
      "groupedByDate": [
         {
            "date": number,
            "lastGeneratedAt": number,
            "severity": number,
            "totalFindings": number
         }
      ],
      "groupedByFindingType": [
         {
            "findingType": "string",
            "lastGeneratedAt": number,
            "totalFindings": number
         }
      ],
      "groupedByResource": [
         {
            "accountId": "string",
            "lastGeneratedAt": number,
            "resourceId": "string",
            "resourceType": "string",
            "totalFindings": number
         }
      ],
      "groupedBySeverity": [
         {
            "lastGeneratedAt": number,
            "severity": number,
            "totalFindings": number
         }
      ]
   },
   "nextToken": "string"
}
```

## Response Elements
<a name="API_GetFindingsStatistics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [findingStatistics](#API_GetFindingsStatistics_ResponseSyntax) **   <a name="guardduty-GetFindingsStatistics-response-findingStatistics"></a>
The finding statistics object.
Type: [FindingStatistics](API_FindingStatistics.md) object

 ** [nextToken](#API_GetFindingsStatistics_ResponseSyntax) **   <a name="guardduty-GetFindingsStatistics-response-nextToken"></a>
The pagination parameter to be used on the next list operation to retrieve more items.
This parameter is currently not supported.
Type: String

## Errors
<a name="API_GetFindingsStatistics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
A bad request exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 500

## See Also
<a name="API_GetFindingsStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/GetFindingsStatistics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/GetFindingsStatistics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/GetFindingsStatistics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/GetFindingsStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/GetFindingsStatistics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/GetFindingsStatistics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/GetFindingsStatistics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/GetFindingsStatistics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/GetFindingsStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/GetFindingsStatistics)
