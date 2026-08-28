---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImageScanFindings.html
---

# ListImageScanFindings
<a name="API_ListImageScanFindings"></a>

Returns a list of image scan findings for your account.

## Request Syntax
<a name="API_ListImageScanFindings_RequestSyntax"></a>

```
POST /ListImageScanFindings HTTP/1.1
Content-type: application/json

{
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListImageScanFindings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListImageScanFindings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListImageScanFindings_RequestSyntax) **   <a name="imagebuilder-ListImageScanFindings-request-filters"></a>
An array of name value pairs that you can use to filter your results. You can use the following filters to streamline results:
+  `imageBuildVersionArn`
+  `imagePipelineArn`
+  `vulnerabilityId`
+  `severity`
If you don't request a filter, then all findings in your account are listed.
Type: Array of [ImageScanFindingsFilter](API_ImageScanFindingsFilter.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [maxResults](#API_ListImageScanFindings_RequestSyntax) **   <a name="imagebuilder-ListImageScanFindings-request-maxResults"></a>
Specify the maximum number of items to return in a request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListImageScanFindings_RequestSyntax) **   <a name="imagebuilder-ListImageScanFindings-request-nextToken"></a>
A token to specify where to start paginating. This is the nextToken from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

## Response Syntax
<a name="API_ListImageScanFindings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "findings": [
      {
         "awsAccountId": "string",
         "description": "string",
         "firstObservedAt": number,
         "fixAvailable": "string",
         "imageBuildVersionArn": "string",
         "imagePipelineArn": "string",
         "inspectorScore": number,
         "inspectorScoreDetails": {
            "adjustedCvss": {
               "adjustments": [
                  {
                     "metric": "string",
                     "reason": "string"
                  }
               ],
               "cvssSource": "string",
               "score": number,
               "scoreSource": "string",
               "scoringVector": "string",
               "version": "string"
            }
         },
         "packageVulnerabilityDetails": {
            "cvss": [
               {
                  "baseScore": number,
                  "scoringVector": "string",
                  "source": "string",
                  "version": "string"
               }
            ],
            "referenceUrls": [ "string" ],
            "relatedVulnerabilities": [ "string" ],
            "source": "string",
            "sourceUrl": "string",
            "vendorCreatedAt": number,
            "vendorSeverity": "string",
            "vendorUpdatedAt": number,
            "vulnerabilityId": "string",
            "vulnerablePackages": [
               {
                  "arch": "string",
                  "epoch": number,
                  "filePath": "string",
                  "fixedInVersion": "string",
                  "name": "string",
                  "packageManager": "string",
                  "release": "string",
                  "remediation": "string",
                  "sourceLayerHash": "string",
                  "version": "string"
               }
            ]
         },
         "remediation": {
            "recommendation": {
               "text": "string",
               "url": "string"
            }
         },
         "severity": "string",
         "title": "string",
         "type": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_ListImageScanFindings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [findings](#API_ListImageScanFindings_ResponseSyntax) **   <a name="imagebuilder-ListImageScanFindings-response-findings"></a>
The image scan findings for your account that meet your request filter criteria.
Type: Array of [ImageScanFinding](API_ImageScanFinding.md) objects
Array Members: Maximum number of 25 items.

 ** [nextToken](#API_ListImageScanFindings_ResponseSyntax) **   <a name="imagebuilder-ListImageScanFindings-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [requestId](#API_ListImageScanFindings_ResponseSyntax) **   <a name="imagebuilder-ListImageScanFindings-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListImageScanFindings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the specific operation.
HTTP Status Code: 429

 ** ClientException **
These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidPaginationTokenException **
You have provided an invalid pagination token in your request.
HTTP Status Code: 400

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_ListImageScanFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListImageScanFindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListImageScanFindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListImageScanFindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListImageScanFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListImageScanFindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListImageScanFindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListImageScanFindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListImageScanFindings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListImageScanFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListImageScanFindings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
