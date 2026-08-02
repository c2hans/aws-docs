---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListCoverage.html
---

# ListCoverage
<a name="API_ListCoverage"></a>

Lists coverage details for your GuardDuty account. If you're a GuardDuty administrator, you can retrieve all resources associated with the active member accounts in your organization.

Make sure the accounts have Runtime Monitoring enabled and GuardDuty agent running on their resources.

## Request Syntax
<a name="API_ListCoverage_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/coverage HTTP/1.1
Content-type: application/json

{
   "filterCriteria": {
      "filterCriterion": [
         {
            "criterionKey": "{{string}}",
            "filterCondition": {
               "equals": [ "{{string}}" ],
               "notEquals": [ "{{string}}" ]
            }
         }
      ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sortCriteria": {
      "attributeName": "{{string}}",
      "orderBy": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListCoverage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_ListCoverage_RequestSyntax) **   <a name="guardduty-ListCoverage-request-uri-DetectorId"></a>
The unique ID of the detector whose coverage details you want to retrieve.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_ListCoverage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filterCriteria](#API_ListCoverage_RequestSyntax) **   <a name="guardduty-ListCoverage-request-filterCriteria"></a>
Represents the criteria used to filter the coverage details.
Type: [CoverageFilterCriteria](API_CoverageFilterCriteria.md) object
Required: No

 ** [maxResults](#API_ListCoverage_RequestSyntax) **   <a name="guardduty-ListCoverage-request-maxResults"></a>
The maximum number of results to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_ListCoverage_RequestSyntax) **   <a name="guardduty-ListCoverage-request-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.
Type: String
Required: No

 ** [sortCriteria](#API_ListCoverage_RequestSyntax) **   <a name="guardduty-ListCoverage-request-sortCriteria"></a>
Represents the criteria used to sort the coverage details.
Type: [CoverageSortCriteria](API_CoverageSortCriteria.md) object
Required: No

## Response Syntax
<a name="API_ListCoverage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "resources": [
      {
         "accountId": "string",
         "coverageStatus": "string",
         "detectorId": "string",
         "issue": "string",
         "resourceDetails": {
            "ec2InstanceDetails": {
               "agentDetails": {
                  "version": "string"
               },
               "clusterArn": "string",
               "instanceId": "string",
               "instanceType": "string",
               "managementType": "string"
            },
            "ecsClusterDetails": {
               "clusterName": "string",
               "containerInstanceDetails": {
                  "compatibleContainerInstances": number,
                  "coveredContainerInstances": number
               },
               "fargateDetails": {
                  "issues": [ "string" ],
                  "managementType": "string"
               }
            },
            "eksClusterDetails": {
               "addonDetails": {
                  "addonStatus": "string",
                  "addonVersion": "string"
               },
               "clusterName": "string",
               "compatibleNodes": number,
               "coveredNodes": number,
               "managementType": "string"
            },
            "resourceType": "string"
         },
         "resourceId": "string",
         "updatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_ListCoverage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListCoverage_ResponseSyntax) **   <a name="guardduty-ListCoverage-response-nextToken"></a>
The pagination parameter to be used on the next list operation to retrieve more items.
Type: String

 ** [resources](#API_ListCoverage_ResponseSyntax) **   <a name="guardduty-ListCoverage-response-resources"></a>
A list of resources and their attributes providing cluster details.
Type: Array of [CoverageResource](API_CoverageResource.md) objects

## Errors
<a name="API_ListCoverage_Errors"></a>

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
<a name="API_ListCoverage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/ListCoverage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/ListCoverage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ListCoverage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/ListCoverage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ListCoverage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/ListCoverage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/ListCoverage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/ListCoverage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/ListCoverage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ListCoverage)
