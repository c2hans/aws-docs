---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImageScanFindings.html
---

# DescribeImageScanFindings
<a name="API_DescribeImageScanFindings"></a>

Returns the scan findings for the specified image.

## Request Syntax
<a name="API_DescribeImageScanFindings_RequestSyntax"></a>

```
{
   "imageId": {
      "imageDigest": "{{string}}",
      "imageTag": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeImageScanFindings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [imageId](#API_DescribeImageScanFindings_RequestSyntax) **   <a name="ECR-DescribeImageScanFindings-request-imageId"></a>
An object with identifying information for an image in an Amazon ECR repository.
Type: [ImageIdentifier](API_ImageIdentifier.md) object
Required: Yes

 ** [maxResults](#API_DescribeImageScanFindings_RequestSyntax) **   <a name="ECR-DescribeImageScanFindings-request-maxResults"></a>
The maximum number of image scan results returned by `DescribeImageScanFindings` in paginated output. When this parameter is used, `DescribeImageScanFindings` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `DescribeImageScanFindings` request with the returned `nextToken` value. This value can be between 1 and 1000. If this parameter is not used, then `DescribeImageScanFindings` returns up to 100 results and a `nextToken` value, if applicable.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeImageScanFindings_RequestSyntax) **   <a name="ECR-DescribeImageScanFindings-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `DescribeImageScanFindings` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is null when there are no more results to return.
Type: String
Required: No

 ** [registryId](#API_DescribeImageScanFindings_RequestSyntax) **   <a name="ECR-DescribeImageScanFindings-request-registryId"></a>
The AWS account ID associated with the registry that contains the repository in which to describe the image scan findings for. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_DescribeImageScanFindings_RequestSyntax) **   <a name="ECR-DescribeImageScanFindings-request-repositoryName"></a>
The repository for the image for which to describe the scan findings.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

## Response Syntax
<a name="API_DescribeImageScanFindings_ResponseSyntax"></a>

```
{
   "imageId": {
      "imageDigest": "string",
      "imageTag": "string"
   },
   "imageScanFindings": {
      "enhancedFindings": [
         {
            "awsAccountId": "string",
            "description": "string",
            "exploitAvailable": "string",
            "findingArn": "string",
            "firstObservedAt": number,
            "fixAvailable": "string",
            "lastObservedAt": number,
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
            "resources": [
               {
                  "details": {
                     "awsEcrContainerImage": {
                        "architecture": "string",
                        "author": "string",
                        "imageHash": "string",
                        "imageTags": [ "string" ],
                        "inUseCount": number,
                        "lastInUseAt": number,
                        "platform": "string",
                        "pushedAt": number,
                        "registry": "string",
                        "repositoryName": "string"
                     }
                  },
                  "id": "string",
                  "tags": {
                     "string" : "string"
                  },
                  "type": "string"
               }
            ],
            "score": number,
            "scoreDetails": {
               "cvss": {
                  "adjustments": [
                     {
                        "metric": "string",
                        "reason": "string"
                     }
                  ],
                  "score": number,
                  "scoreSource": "string",
                  "scoringVector": "string",
                  "version": "string"
               }
            },
            "severity": "string",
            "status": "string",
            "title": "string",
            "type": "string",
            "updatedAt": number
         }
      ],
      "findings": [
         {
            "attributes": [
               {
                  "key": "string",
                  "value": "string"
               }
            ],
            "description": "string",
            "name": "string",
            "severity": "string",
            "uri": "string"
         }
      ],
      "findingSeverityCounts": {
         "string" : number
      },
      "imageScanCompletedAt": number,
      "vulnerabilitySourceUpdatedAt": number
   },
   "imageScanStatus": {
      "description": "string",
      "status": "string"
   },
   "nextToken": "string",
   "registryId": "string",
   "repositoryName": "string"
}
```

## Response Elements
<a name="API_DescribeImageScanFindings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageId](#API_DescribeImageScanFindings_ResponseSyntax) **   <a name="ECR-DescribeImageScanFindings-response-imageId"></a>
An object with identifying information for an image in an Amazon ECR repository.
Type: [ImageIdentifier](API_ImageIdentifier.md) object

 ** [imageScanFindings](#API_DescribeImageScanFindings_ResponseSyntax) **   <a name="ECR-DescribeImageScanFindings-response-imageScanFindings"></a>
The information contained in the image scan findings.
Type: [ImageScanFindings](API_ImageScanFindings.md) object

 ** [imageScanStatus](#API_DescribeImageScanFindings_ResponseSyntax) **   <a name="ECR-DescribeImageScanFindings-response-imageScanStatus"></a>
The current state of the scan.
Type: [ImageScanStatus](API_ImageScanStatus.md) object

 ** [nextToken](#API_DescribeImageScanFindings_ResponseSyntax) **   <a name="ECR-DescribeImageScanFindings-response-nextToken"></a>
The `nextToken` value to include in a future `DescribeImageScanFindings` request. When the results of a `DescribeImageScanFindings` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is null when there are no more results to return.
Type: String

 ** [registryId](#API_DescribeImageScanFindings_ResponseSyntax) **   <a name="ECR-DescribeImageScanFindings-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [repositoryName](#API_DescribeImageScanFindings_ResponseSyntax) **   <a name="ECR-DescribeImageScanFindings-response-repositoryName"></a>
The repository name associated with the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`

## Errors
<a name="API_DescribeImageScanFindings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ImageNotFoundException **
The image requested does not exist in the specified repository.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** RepositoryNotFoundException **
The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** ScanNotFoundException **
The specified image scan could not be found. Ensure that image scanning is enabled on the repository and try again.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** message **
The error message associated with the exception.
HTTP Status Code: 500

 ** ValidationException **
There was an exception validating this request.
HTTP Status Code: 400

## Examples
<a name="API_DescribeImageScanFindings_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example for basic image scanning
<a name="API_DescribeImageScanFindings_Example_1"></a>

This example returns the image scan findings for an image using the image digest in a repository named `sample-repo` in the default registry for an account.

#### Sample Request
<a name="API_DescribeImageScanFindings_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 141
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.DescribeImageScanFindings
X-Amz-Date: 20200124T034807Z
User-Agent: aws-cli/1.16.310 Python/3.6.1 Darwin/18.7.0 botocore/1.13.46
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "repositoryName": "sample-repo",
    "imageId": {
        "imageDigest": "sha256:74b2c688c700ec95a93e478cdb959737c148df3fbf5ea706abe0318726e885e6"
    }
}
```

#### Sample Response
<a name="API_DescribeImageScanFindings_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Fri, 24 Jan 2020 03:48:07 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 33967
Connection: keep-alive
x-amzn-RequestId: 3081a92b-2066-41f8-8a47-0580288ada9e

{
    "imageScanFindings": {
        "findings": [
            {
                "name": "CVE-2019-5188",
                "description": "A code execution vulnerability exists in the directory rehashing functionality of E2fsprogs e2fsck 1.45.4. A specially crafted ext4 directory can cause an out-of-bounds write on the stack, resulting in code execution. An attacker can corrupt a partition to trigger this vulnerability.",
                "uri": "http://people.ubuntu.com/~ubuntu-security/cve/CVE-2019-5188",
                "severity": "MEDIUM",
                "attributes": [
                    {
                        "key": "package_version",
                        "value": "1.44.1-1ubuntu1.1"
                    },
                    {
                        "key": "package_name",
                        "value": "e2fsprogs"
                    },
                    {
                        "key": "CVSS2_VECTOR",
                        "value": "AV:L/AC:L/Au:N/C:P/I:P/A:P"
                    },
                    {
                        "key": "CVSS2_SCORE",
                        "value": "4.6"
                    }
                ]
            }
        ],
        "imageScanCompletedAt": 1579839105.0,
        "vulnerabilitySourceUpdatedAt": 1579811117.0,
        "findingSeverityCounts": {
            "MEDIUM": 1
        }
    },
    "registryId": "012345678910",
    "repositoryName": "sample-repo",
    "imageId": {
        "imageDigest": "sha256:74b2c688c700ec95a93e478cdb959737c148df3fbf5ea706abe0318726e885e6"
    },
    "imageScanStatus": {
        "status": "COMPLETE",
        "description": "The scan was completed successfully."
    }
}
```

### Example for enhanced image scanning
<a name="API_DescribeImageScanFindings_Example_2"></a>

This example illustrates one usage of DescribeImageScanFindings.

#### Sample Request
<a name="API_DescribeImageScanFindings_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 141
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.DescribeImageScanFindings
X-Amz-Date: 20250610T201255Z
User-Agent: aws-cli/1.16.310 Python/3.6.1 Darwin/18.7.0 botocore/1.13.46
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "registryId": "123456789012",
  "repositoryName": "sample-repo",
  "imageId": {
    "imageDigest": "sha256:74b2c688c700ec95a93e478cdb959737c148df3fbf5ea706abe0318726e885e6"
  }
}
```

#### Sample Response
<a name="API_DescribeImageScanFindings_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Mon, 10 Jun 2025 20:12:55 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 33967
Connection: keep-alive
x-amzn-RequestId: 3081a92b-2066-41f8-8a47-0580288ada9e
{
    "imageScanFindings": {
        "enhancedFindings": [
            {
                "awsAccountId": "123456789012",
                "description": "xmlXIncludeAddNode in xinclude.c in libxml2 before 2.11.0 has a use-after-free.",
                "findingArn": "arn:aws:inspector2:us-west-2:123456789012:finding/123456789012123456789012",
                "firstObservedAt": "2025-05-27T17:54:07.765000+00:00",
                "lastObservedAt": "2025-06-09T07:08:40.144000+00:00",
                "packageVulnerabilityDetails": {
                    "cvss": [
                        {
                            "baseScore": 8.1,
                            "scoringVector": "CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H",
                            "source": "NVD",
                            "version": "3.1"
                        }
                    ],
                    "referenceUrls": [
                        "https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1094238",
                        "https://security-tracker.debian.org/tracker/CVE-2022-49043"
                    ],
                    "relatedVulnerabilities": [],
                    "source": "DEBIAN_CVE",
                    "sourceUrl": "https://security-tracker.debian.org/tracker/CVE-2022-49043",
                    "vendorSeverity": "not yet assigned",
                    "vulnerabilityId": "CVE-2022-49043",
                    "vulnerablePackages": [
                        {
                            "arch": "AMD64",
                            "epoch": 0,
                            "name": "libxml2",
                            "packageManager": "OS",
                            "release": "1.3~deb12u1",
                            "sourceLayerHash": "sha256:deb7d8874f38d4ec281d990aac2c7badbfcd5b97d602a388056e3f918a3f8cc7",
                            "version": "2.9.14+dfsg",
                            "fixedInVersion": "NotAvailable"
                        }
                    ]
                },
                "remediation": {
                    "recommendation": {
                        "text": "None Provided"
                    }
                },
                "resources": [
                    {
                        "details": {
                            "awsEcrContainerImage": {
                                "architecture": "amd64",
                                "imageHash": "sha256:74b2c688c700ec95a93e478cdb959737c148df3fbf5ea706abe0318726e885e6",
                                "imageTags": [
                                    "latest"
                                ],
                                "platform": "DEBIAN_12",
                                "pushedAt": "2025-05-27T17:53:50.554000+00:00",
                                "lastInUseAt": "2025-06-09T04:43:20.427000+00:00",
                                "inUseCount": 1,
                                "registry": "123456789012",
                                "repositoryName": "sample-repo"
                            }
                        },
                        "id": "arn:aws:ecr:us-west-2:123456789012:repository/sample-repo/sha256:74b2c688c700ec95a93e478cdb959737c148df3fbf5ea706abe0318726e885e6",
                        "tags": {},
                        "type": "AWS_ECR_CONTAINER_IMAGE"
                    }
                ],
                "score": 8.1,
                "scoreDetails": {
                    "cvss": {
                        "adjustments": [],
                        "score": 8.1,
                        "scoreSource": "NVD",
                        "scoringVector": "CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H",
                        "version": "3.1"
                    }
                },
                "severity": "HIGH",
                "status": "ACTIVE",
                "title": "CVE-2022-49043 - libxml2",
                "type": "PACKAGE_VULNERABILITY",
                "updatedAt": "2025-06-09T07:08:40.144000+00:00",
                "fixAvailable": "NO",
                "exploitAvailable": "NO"
            },
        ],
        "imageScanCompletedAt": "2025-06-09T07:08:40.144000+00:00",
        "vulnerabilitySourceUpdatedAt": "2025-06-09T07:08:40.144000+00:00",
        "findingSeverityCounts": {
            "HIGH": 1,
        }
    },
    "registryId": "123456789012",
    "repositoryName": "sample-repo",
    "imageId": {
        "imageDigest": "sha256:74b2c688c700ec95a93e478cdb959737c148df3fbf5ea706abe0318726e885e6"
    },
    "imageScanStatus": {
        "status": "ACTIVE",
        "description": "Continuous scan is selected for image."
    }
}
```

## See Also
<a name="API_DescribeImageScanFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/DescribeImageScanFindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/DescribeImageScanFindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/DescribeImageScanFindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/DescribeImageScanFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DescribeImageScanFindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/DescribeImageScanFindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/DescribeImageScanFindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/DescribeImageScanFindings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DescribeImageScanFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/DescribeImageScanFindings)
