---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_SearchVulnerabilities.html
---

# SearchVulnerabilities
<a name="API_SearchVulnerabilities"></a>

Lists Amazon Inspector coverage details for a specific vulnerability.

## Request Syntax
<a name="API_SearchVulnerabilities_RequestSyntax"></a>

```
POST /vulnerabilities/search HTTP/1.1
Content-type: application/json

{
   "filterCriteria": {
      "vulnerabilityIds": [ "{{string}}" ]
   },
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchVulnerabilities_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchVulnerabilities_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filterCriteria](#API_SearchVulnerabilities_RequestSyntax) **   <a name="inspector2-SearchVulnerabilities-request-filterCriteria"></a>
The criteria used to filter the results of a vulnerability search.
Type: [SearchVulnerabilitiesFilterCriteria](API_SearchVulnerabilitiesFilterCriteria.md) object
Required: Yes

 ** [nextToken](#API_SearchVulnerabilities_RequestSyntax) **   <a name="inspector2-SearchVulnerabilities-request-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the `NextToken` value returned from the previous request to continue listing results after the first page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.
Required: No

## Response Syntax
<a name="API_SearchVulnerabilities_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "vulnerabilities": [
      {
         "atigData": {
            "firstSeen": number,
            "lastSeen": number,
            "targets": [ "string" ],
            "ttps": [ "string" ]
         },
         "cisaData": {
            "action": "string",
            "dateAdded": number,
            "dateDue": number
         },
         "cvss2": {
            "baseScore": number,
            "scoringVector": "string"
         },
         "cvss3": {
            "baseScore": number,
            "scoringVector": "string"
         },
         "cvss4": {
            "baseScore": number,
            "scoringVector": "string"
         },
         "cwes": [ "string" ],
         "description": "string",
         "detectionPlatforms": [ "string" ],
         "epss": {
            "score": number
         },
         "exploitObserved": {
            "firstSeen": number,
            "lastSeen": number
         },
         "id": "string",
         "referenceUrls": [ "string" ],
         "relatedVulnerabilities": [ "string" ],
         "source": "string",
         "sourceUrl": "string",
         "vendorCreatedAt": number,
         "vendorSeverity": "string",
         "vendorUpdatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_SearchVulnerabilities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_SearchVulnerabilities_ResponseSyntax) **   <a name="inspector2-SearchVulnerabilities-response-nextToken"></a>
The pagination parameter to be used on the next list operation to retrieve more items.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.

 ** [vulnerabilities](#API_SearchVulnerabilities_ResponseSyntax) **   <a name="inspector2-SearchVulnerabilities-response-vulnerabilities"></a>
Details about the listed vulnerability.
Type: Array of [Vulnerability](API_Vulnerability.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

## Errors
<a name="API_SearchVulnerabilities_Errors"></a>

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
<a name="API_SearchVulnerabilities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/SearchVulnerabilities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/SearchVulnerabilities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/SearchVulnerabilities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/SearchVulnerabilities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/SearchVulnerabilities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/SearchVulnerabilities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/SearchVulnerabilities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/SearchVulnerabilities)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/SearchVulnerabilities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/SearchVulnerabilities)
