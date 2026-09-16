---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetFilter.html
---

# GetFilter
<a name="API_GetFilter"></a>

Returns the details of the filter specified by the filter name.

## Request Syntax
<a name="API_GetFilter_RequestSyntax"></a>

```
GET /detector/{{DetectorId}}/filter/{{FilterName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFilter_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_GetFilter_RequestSyntax) **   <a name="guardduty-GetFilter-request-uri-DetectorId"></a>
The unique ID of the detector that is associated with this filter.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [FilterName](#API_GetFilter_RequestSyntax) **   <a name="guardduty-GetFilter-request-uri-FilterName"></a>
The name of the filter you want to get.
Required: Yes

## Request Body
<a name="API_GetFilter_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFilter_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "action": "string",
   "createdAt": number,
   "description": "string",
   "findingCriteria": {
      "criterion": {
         "string" : {
            "eq": [ "string" ],
            "equals": [ "string" ],
            "greaterThan": number,
            "greaterThanOrEqual": number,
            "gt": number,
            "gte": number,
            "lessThan": number,
            "lessThanOrEqual": number,
            "lt": number,
            "lte": number,
            "matches": [ "string" ],
            "neq": [ "string" ],
            "notEquals": [ "string" ],
            "notMatches": [ "string" ]
         }
      }
   },
   "name": "string",
   "rank": number,
   "tags": {
      "string" : "string"
   },
   "updatedAt": number,
   "version": number
}
```

## Response Elements
<a name="API_GetFilter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [action](#API_GetFilter_ResponseSyntax) **   <a name="guardduty-GetFilter-response-action"></a>
Specifies the action that is to be applied to the findings that match the filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `NOOP | ARCHIVE`

 ** [createdAt](#API_GetFilter_ResponseSyntax) **   <a name="guardduty-GetFilter-response-createdAt"></a>
The timestamp when the filter was created. This field is not available for filters that were created before the lifecycle metadata feature was enabled (legacy filters).
Type: Timestamp

 ** [description](#API_GetFilter_ResponseSyntax) **   <a name="guardduty-GetFilter-response-description"></a>
The description of the filter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.

 ** [findingCriteria](#API_GetFilter_ResponseSyntax) **   <a name="guardduty-GetFilter-response-findingCriteria"></a>
Represents the criteria to be used in the filter for querying findings.
Type: [FindingCriteria](API_FindingCriteria.md) object

 ** [name](#API_GetFilter_ResponseSyntax) **   <a name="guardduty-GetFilter-response-name"></a>
The name of the filter.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.

 ** [rank](#API_GetFilter_ResponseSyntax) **   <a name="guardduty-GetFilter-response-rank"></a>
Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [tags](#API_GetFilter_ResponseSyntax) **   <a name="guardduty-GetFilter-response-tags"></a>
The tags of the filter resource.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [updatedAt](#API_GetFilter_ResponseSyntax) **   <a name="guardduty-GetFilter-response-updatedAt"></a>
The timestamp when the filter was last updated. For legacy filters, this field is present only after the filter has been updated at least once since the lifecycle metadata feature was enabled.
Type: Timestamp

 ** [version](#API_GetFilter_ResponseSyntax) **   <a name="guardduty-GetFilter-response-version"></a>
The version of the filter. Every time the filter is updated, the version increments by 1. This field is not available for legacy filters that were created before the lifecycle metadata feature was enabled.
Type: Long
Valid Range: Minimum value of 1.

## Errors
<a name="API_GetFilter_Errors"></a>

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
<a name="API_GetFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/GetFilter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/GetFilter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/GetFilter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/GetFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/GetFilter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/GetFilter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/GetFilter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/GetFilter)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/GetFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/GetFilter)
