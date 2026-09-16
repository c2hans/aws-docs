---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_ListInvestigations.html
---

# ListInvestigations
<a name="API_ListInvestigations"></a>

Detective investigations lets you investigate IAM users and IAM roles using indicators of compromise. An indicator of compromise (IOC) is an artifact observed in or on a network, system, or environment that can (with a high level of confidence) identify malicious activity or a security incident. `ListInvestigations` lists all active Detective investigations.

## Request Syntax
<a name="API_ListInvestigations_RequestSyntax"></a>

```
POST /investigations/listInvestigations HTTP/1.1
Content-type: application/json

{
   "FilterCriteria": {
      "CreatedTime": {
         "EndInclusive": "{{string}}",
         "StartInclusive": "{{string}}"
      },
      "EntityArn": {
         "Value": "{{string}}"
      },
      "Severity": {
         "Value": "{{string}}"
      },
      "State": {
         "Value": "{{string}}"
      },
      "Status": {
         "Value": "{{string}}"
      }
   },
   "GraphArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortCriteria": {
      "Field": "{{string}}",
      "SortOrder": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListInvestigations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListInvestigations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [FilterCriteria](#API_ListInvestigations_RequestSyntax) **   <a name="detective-ListInvestigations-request-FilterCriteria"></a>
Filters the investigation results based on a criteria.
Type: [FilterCriteria](API_FilterCriteria.md) object
Required: No

 ** [GraphArn](#API_ListInvestigations_RequestSyntax) **   <a name="detective-ListInvestigations-request-GraphArn"></a>
The Amazon Resource Name (ARN) of the behavior graph.
Type: String
Pattern: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`
Required: Yes

 ** [MaxResults](#API_ListInvestigations_RequestSyntax) **   <a name="detective-ListInvestigations-request-MaxResults"></a>
Lists the maximum number of investigations in a page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListInvestigations_RequestSyntax) **   <a name="detective-ListInvestigations-request-NextToken"></a>
Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.
Each pagination token expires after 24 hours. Using an expired pagination token will return a Validation Exception error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [SortCriteria](#API_ListInvestigations_RequestSyntax) **   <a name="detective-ListInvestigations-request-SortCriteria"></a>
Sorts the investigation results based on a criteria.
Type: [SortCriteria](API_SortCriteria.md) object
Required: No

## Response Syntax
<a name="API_ListInvestigations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "InvestigationDetails": [
      {
         "CreatedTime": "string",
         "EntityArn": "string",
         "EntityType": "string",
         "InvestigationId": "string",
         "Severity": "string",
         "State": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListInvestigations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InvestigationDetails](#API_ListInvestigations_ResponseSyntax) **   <a name="detective-ListInvestigations-response-InvestigationDetails"></a>
Lists the summary of uncommon behavior or malicious activity which indicates a compromise.
Type: Array of [InvestigationDetail](API_InvestigationDetail.md) objects

 ** [NextToken](#API_ListInvestigations_ResponseSyntax) **   <a name="detective-ListInvestigations-response-NextToken"></a>
Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.
Each pagination token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListInvestigations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request issuer does not have permission to access this resource or perform this operation.
 ** ErrorCode **
The SDK default error code associated with the access denied exception.
 ** ErrorCodeReason **
The SDK default explanation of why access was denied.
 ** SubErrorCode **
The error code associated with the access denied exception.
 ** SubErrorCodeReason **
 An explanation of why access was denied.
HTTP Status Code: 403

 ** InternalServerException **
The request was valid but failed because of a problem with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request refers to a nonexistent resource.
HTTP Status Code: 404

 ** TooManyRequestsException **
The request cannot be completed because too many other requests are occurring at the same time.
HTTP Status Code: 429

 ** ValidationException **
The request parameters are invalid.
 ** ErrorCode **
The error code associated with the validation failure.
 ** ErrorCodeReason **
 An explanation of why validation failed.
HTTP Status Code: 400

## See Also
<a name="API_ListInvestigations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/detective-2018-10-26/ListInvestigations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/detective-2018-10-26/ListInvestigations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/ListInvestigations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/detective-2018-10-26/ListInvestigations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/ListInvestigations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/detective-2018-10-26/ListInvestigations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/detective-2018-10-26/ListInvestigations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/detective-2018-10-26/ListInvestigations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/detective-2018-10-26/ListInvestigations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/ListInvestigations)
