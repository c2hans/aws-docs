---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImageScanFindings.html
---

# ListImageScanFindings
<a name="API_ListImageScanFindings"></a>

Returns a list of image scan findings for your account. Amazon Inspector generates the findings when it scans images that have scanning enabled.

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
+  `imageBuildVersionArn` – Filters findings by the image build version that was scanned.
+  `imagePipelineArn` – Filters findings by the pipeline that created the scanned image.
+  `vulnerabilityId` – Filters findings by vulnerability ID, for example a CVE ID.
+  `severity` – Filters findings by severity level.
If you don't request a filter, then all findings in your account are listed.
Type: Array of [ImageScanFindingsFilter](API_ImageScanFindingsFilter.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [maxResults](#API_ListImageScanFindings_RequestSyntax) **   <a name="imagebuilder-ListImageScanFindings-request-maxResults"></a>
The maximum number of items to return in a single request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListImageScanFindings_RequestSyntax) **   <a name="imagebuilder-ListImageScanFindings-request-nextToken"></a>
A token to specify where to start paginating. Use the `nextToken` value from a previously truncated response.
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
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidPaginationTokenException **
You have provided an invalid pagination token in your request.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_ListImageScanFindings_Examples"></a>

### List vulnerability findings for an image build
<a name="API_ListImageScanFindings_Example_1"></a>

The following example lists the vulnerability findings that Amazon Inspector detected for the specified image build version.

#### Sample Request
<a name="API_ListImageScanFindings_Example_1_Request"></a>

```
POST /ListImageScanFindings HTTP/1.1
Content-type: application/json

{
    "filters": [
        {
            "name": "imageBuildVersionArn",
            "values": [
                "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1"
            ]
        }
    ]
}
```

#### Sample Response
<a name="API_ListImageScanFindings_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "233de8e7-3b58-4319-a6af-f6774cf7d371",
    "findings": [
        {
            "awsAccountId": "111122223333",
            "imageBuildVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1",
            "imagePipelineArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-pipeline/my-example-pipeline",
            "type": "PACKAGE_VULNERABILITY",
            "description": "In the Linux kernel, the following vulnerability has been resolved:\n\nvirtio: break and reset virtio devices on device_shutdown()",
            "title": "CVE-2025-38064 - kernel",
            "remediation": {
                "recommendation": {
                    "text": "None Provided"
                }
            },
            "severity": "HIGH",
            "firstObservedAt": 1767730377.0,
            "updatedAt": 1767730377.0,
            "inspectorScore": 7.0,
            "inspectorScoreDetails": {
                "adjustedCvss": {
                    "scoreSource": "AMAZON_CVE",
                    "cvssSource": "AMAZON_CVE",
                    "version": "3.1",
                    "score": 7.0,
                    "scoringVector": "CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H",
                    "adjustments": []
                }
            },
            "packageVulnerabilityDetails": {
                "vulnerabilityId": "CVE-2025-38064",
                "vulnerablePackages": [
                    {
                        "name": "kernel",
                        "version": "4.14.355",
                        "epoch": 0,
                        "release": "280.652.amzn2",
                        "arch": "X86_64",
                        "packageManager": "OS",
                        "fixedInVersion": "0:5.15.189-131.202.amzn2",
                        "remediation": "yum update kernel"
                    }
                ],
                "source": "AMAZON_CVE",
                "cvss": [
                    {
                        "baseScore": 7.0,
                        "scoringVector": "CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H",
                        "version": "3.1",
                        "source": "AMAZON_CVE"
                    }
                ],
                "relatedVulnerabilities": [
                    "ALAS2-2025-2955",
                    "ALAS2023-2025-1130"
                ],
                "sourceUrl": "https://alas.aws.amazon.com/cve/json/v1/CVE-2025-38064.json",
                "vendorSeverity": "Important",
                "vendorCreatedAt": 1750204800.0,
                "vendorUpdatedAt": 1750809600.0,
                "referenceUrls": [
                    "https://alas.aws.amazon.com/AL2/ALAS2-2025-2955.html",
                    "https://alas.aws.amazon.com/AL2023/ALAS2023-2025-1130.html"
                ]
            },
            "fixAvailable": "YES"
        }
    ]
}
```

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
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListImageScanFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListImageScanFindings)
