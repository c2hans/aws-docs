---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/findings-describe.html
---

# Findings
<a name="findings-describe"></a>

The Findings resource represents the repository of findings for your Amazon Macie account. A *finding* is a detailed report of a potential issue with the security or privacy of an Amazon Simple Storage Service (Amazon S3) general purpose bucket or sensitive data in an S3 object. Each finding provides details such as a severity rating, information about the affected resource, and when and how Macie found the issue. The severity and details of each finding vary depending on the type and nature of the finding. For information about the types of findings that Macie can generate, see [Types of findings](https://docs.aws.amazon.com/macie/latest/user/findings-types.html) in the *Amazon Macie User Guide*.

You can use the Findings resource to retrieve the details of one or more findings for your account. To refine your results, you can use the supported parameters to specify how to sort the results. When you use this resource, you have to specify the unique identifier for each finding to retrieve. To obtain this identifier, use the [Finding List](findings.md) resource.

## URI
<a name="findings-describe-url"></a>

`/findings/describe`

## HTTP methods
<a name="findings-describe-http-methods"></a>

### POST
<a name="findings-describepost"></a>

**Operation ID:** `GetFindings`

Retrieves the details of one or more findings.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetFindingsResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="findings-describe-schemas"></a>

### Request bodies
<a name="findings-describe-request-examples"></a>

#### POST schema
<a name="findings-describe-request-body-post-example"></a>

```
{
  "findingIds": [
    "string"
  ],
  "sortCriteria": {
    "attributeName": "string",
    "orderBy": enum
  }
}
```

### Response bodies
<a name="findings-describe-response-examples"></a>

#### GetFindingsResponse schema
<a name="findings-describe-response-body-getfindingsresponse-example"></a>

```
{
  "findings": [
    {
      "accountId": "string",
      "archived": boolean,
      "category": enum,
      "classificationDetails": {
        "detailedResultsLocation": "string",
        "jobArn": "string",
        "jobId": "string",
        "originType": enum,
        "result": {
          "additionalOccurrences": boolean,
          "customDataIdentifiers": {
            "detections": [
              {
                "arn": "string",
                "count": integer,
                "name": "string",
                "occurrences": {
                  "cells": [
                    {
                      "cellReference": "string",
                      "column": integer,
                      "columnName": "string",
                      "row": integer
                    }
                  ],
                  "lineRanges": [
                    {
                      "end": integer,
                      "start": integer,
                      "startColumn": integer
                    }
                  ],
                  "offsetRanges": [
                    {
                      "end": integer,
                      "start": integer,
                      "startColumn": integer
                    }
                  ],
                  "pages": [
                    {
                      "lineRange": {
                        "end": integer,
                        "start": integer,
                        "startColumn": integer
                      },
                      "offsetRange": {
                        "end": integer,
                        "start": integer,
                        "startColumn": integer
                      },
                      "pageNumber": integer
                    }
                  ],
                  "records": [
                    {
                      "jsonPath": "string",
                      "recordIndex": integer
                    }
                  ]
                }
              }
            ],
            "totalCount": integer
          },
          "mimeType": "string",
          "sensitiveData": [
            {
              "category": enum,
              "detections": [
                {
                  "count": integer,
                  "occurrences": {
                    "cells": [
                      {
                        "cellReference": "string",
                        "column": integer,
                        "columnName": "string",
                        "row": integer
                      }
                    ],
                    "lineRanges": [
                      {
                        "end": integer,
                        "start": integer,
                        "startColumn": integer
                      }
                    ],
                    "offsetRanges": [
                      {
                        "end": integer,
                        "start": integer,
                        "startColumn": integer
                      }
                    ],
                    "pages": [
                      {
                        "lineRange": {
                          "end": integer,
                          "start": integer,
                          "startColumn": integer
                        },
                        "offsetRange": {
                          "end": integer,
                          "start": integer,
                          "startColumn": integer
                        },
                        "pageNumber": integer
                      }
                    ],
                    "records": [
                      {
                        "jsonPath": "string",
                        "recordIndex": integer
                      }
                    ]
                  },
                  "type": "string"
                }
              ],
              "totalCount": integer
            }
          ],
          "sizeClassified": integer,
          "status": {
            "code": "string",
            "reason": "string"
          }
        }
      },
      "count": integer,
      "createdAt": "string",
      "description": "string",
      "id": "string",
      "partition": "string",
      "policyDetails": {
        "action": {
          "actionType": enum,
          "apiCallDetails": {
            "api": "string",
            "apiServiceName": "string",
            "firstSeen": "string",
            "lastSeen": "string"
          }
        },
        "actor": {
          "domainDetails": {
            "domainName": "string"
          },
          "ipAddressDetails": {
            "ipAddressV4": "string",
            "ipCity": {
              "name": "string"
            },
            "ipCountry": {
              "code": "string",
              "name": "string"
            },
            "ipGeoLocation": {
              "lat": number,
              "lon": number
            },
            "ipOwner": {
              "asn": "string",
              "asnOrg": "string",
              "isp": "string",
              "org": "string"
            }
          },
          "userIdentity": {
            "assumedRole": {
              "accessKeyId": "string",
              "accountId": "string",
              "arn": "string",
              "principalId": "string",
              "sessionContext": {
                "attributes": {
                  "creationDate": "string",
                  "mfaAuthenticated": boolean
                },
                "sessionIssuer": {
                  "accountId": "string",
                  "arn": "string",
                  "principalId": "string",
                  "type": "string",
                  "userName": "string"
                }
              }
            },
            "awsAccount": {
              "accountId": "string",
              "principalId": "string"
            },
            "awsService": {
              "invokedBy": "string"
            },
            "federatedUser": {
              "accessKeyId": "string",
              "accountId": "string",
              "arn": "string",
              "principalId": "string",
              "sessionContext": {
                "attributes": {
                  "creationDate": "string",
                  "mfaAuthenticated": boolean
                },
                "sessionIssuer": {
                  "accountId": "string",
                  "arn": "string",
                  "principalId": "string",
                  "type": "string",
                  "userName": "string"
                }
              }
            },
            "iamUser": {
              "accountId": "string",
              "arn": "string",
              "principalId": "string",
              "userName": "string"
            },
            "root": {
              "accountId": "string",
              "arn": "string",
              "principalId": "string"
            },
            "type": enum
          }
        }
      },
      "region": "string",
      "resourcesAffected": {
        "s3Bucket": {
          "allowsUnencryptedObjectUploads": enum,
          "arn": "string",
          "createdAt": "string",
          "defaultServerSideEncryption": {
            "encryptionType": enum,
            "kmsMasterKeyId": "string"
          },
          "name": "string",
          "owner": {
            "displayName": "string",
            "id": "string"
          },
          "publicAccess": {
            "effectivePermission": enum,
            "permissionConfiguration": {
              "accountLevelPermissions": {
                "blockPublicAccess": {
                  "blockPublicAcls": boolean,
                  "blockPublicPolicy": boolean,
                  "ignorePublicAcls": boolean,
                  "restrictPublicBuckets": boolean
                }
              },
              "bucketLevelPermissions": {
                "accessControlList": {
                  "allowsPublicReadAccess": boolean,
                  "allowsPublicWriteAccess": boolean
                },
                "blockPublicAccess": {
                  "blockPublicAcls": boolean,
                  "blockPublicPolicy": boolean,
                  "ignorePublicAcls": boolean,
                  "restrictPublicBuckets": boolean
                },
                "bucketPolicy": {
                  "allowsPublicReadAccess": boolean,
                  "allowsPublicWriteAccess": boolean
                }
              }
            }
          },
          "tags": [
            {
              "key": "string",
              "value": "string"
            }
          ]
        },
        "s3Object": {
          "bucketArn": "string",
          "eTag": "string",
          "extension": "string",
          "key": "string",
          "lastModified": "string",
          "path": "string",
          "publicAccess": boolean,
          "serverSideEncryption": {
            "encryptionType": enum,
            "kmsMasterKeyId": "string"
          },
          "size": integer,
          "storageClass": enum,
          "tags": [
            {
              "key": "string",
              "value": "string"
            }
          ],
          "versionId": "string"
        }
      },
      "sample": boolean,
      "schemaVersion": "string",
      "severity": {
        "description": enum,
        "score": integer
      },
      "title": "string",
      "type": enum,
      "updatedAt": "string"
    }
  ]
}
```

#### ValidationException schema
<a name="findings-describe-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="findings-describe-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="findings-describe-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="findings-describe-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="findings-describe-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="findings-describe-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="findings-describe-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="findings-describe-properties"></a>

### AccessControlList
<a name="findings-describe-model-accesscontrollist"></a>

Provides information about the permissions settings of the bucket-level access control list (ACL) for an S3 bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| allowsPublicReadAccess | boolean | False | Specifies whether the ACL grants the general public with read access permissions for the bucket. |
| allowsPublicWriteAccess | boolean | False | Specifies whether the ACL grants the general public with write access permissions for the bucket. |

### AccessDeniedException
<a name="findings-describe-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### AccountLevelPermissions
<a name="findings-describe-model-accountlevelpermissions"></a>

Provides information about the account-level permissions settings that apply to an S3 bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| blockPublicAccess | [BlockPublicAccess](#findings-describe-model-blockpublicaccess) | False | The block public access settings for the AWS account that owns the bucket. |

### ApiCallDetails
<a name="findings-describe-model-apicalldetails"></a>

Provides information about an API operation that an entity invoked for an affected resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| api | string | False | The name of the operation that was invoked most recently and produced the finding. |
| apiServiceName | string | False | The URL of the AWS service that provides the operation, for example: `s3.amazonaws.com`. |
| firstSeen | string<br />Format: date-time | False | The first date and time, in UTC and extended ISO 8601 format, when any operation was invoked and produced the finding. |
| lastSeen | string<br />Format: date-time | False | The most recent date and time, in UTC and extended ISO 8601 format, when the specified operation (`api`) was invoked and produced the finding. |

### AssumedRole
<a name="findings-describe-model-assumedrole"></a>

Provides information about an identity that performed an action on an affected resource by using temporary security credentials. The credentials were obtained using the `AssumeRole` operation of the AWS Security Token Service (AWS STS) API.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accessKeyId | string | False | The AWS access key ID that identifies the credentials. |
| accountId | string | False | The unique identifier for the AWS account that owns the entity that was used to get the credentials. |
| arn | string | False | The Amazon Resource Name (ARN) of the entity that was used to get the credentials. |
| principalId | string | False | The unique identifier for the entity that was used to get the credentials. |
| sessionContext | [SessionContext](#findings-describe-model-sessioncontext) | False | The details of the session that was created for the credentials, including the entity that issued the session. |

### AwsAccount
<a name="findings-describe-model-awsaccount"></a>

Provides information about an AWS account and entity that performed an action on an affected resource. The action was performed using the credentials for an AWS account other than your own account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The unique identifier for the AWS account. |
| principalId | string | False | The unique identifier for the entity that performed the action. |

### AwsService
<a name="findings-describe-model-awsservice"></a>

Provides information about an AWS service that performed an action on an affected resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invokedBy | string | False | The name of the AWS service that performed the action. |

### BlockPublicAccess
<a name="findings-describe-model-blockpublicaccess"></a>

Provides information about the block public access settings for an S3 bucket. These settings can apply to a bucket at the account or bucket level. For detailed information about each setting, see [Blocking public access to your Amazon S3 storage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) in the *Amazon Simple Storage Service User Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| blockPublicAcls | boolean | False | Specifies whether Amazon S3 blocks public access control lists (ACLs) for the bucket and objects in the bucket. |
| blockPublicPolicy | boolean | False | Specifies whether Amazon S3 blocks public bucket policies for the bucket. |
| ignorePublicAcls | boolean | False | Specifies whether Amazon S3 ignores public ACLs for the bucket and objects in the bucket. |
| restrictPublicBuckets | boolean | False | Specifies whether Amazon S3 restricts public bucket policies for the bucket. |

### BucketLevelPermissions
<a name="findings-describe-model-bucketlevelpermissions"></a>

Provides information about the bucket-level permissions settings for an S3 bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accessControlList | [AccessControlList](#findings-describe-model-accesscontrollist) | False | The permissions settings of the access control list (ACL) for the bucket. This value is null if an ACL hasn't been defined for the bucket. |
| blockPublicAccess | [BlockPublicAccess](#findings-describe-model-blockpublicaccess) | False | The block public access settings for the bucket. |
| bucketPolicy | [BucketPolicy](#findings-describe-model-bucketpolicy) | False | The permissions settings of the bucket policy for the bucket. This value is null if a bucket policy hasn't been defined for the bucket. |

### BucketPermissionConfiguration
<a name="findings-describe-model-bucketpermissionconfiguration"></a>

Provides information about the account-level and bucket-level permissions settings for an S3 bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountLevelPermissions | [AccountLevelPermissions](#findings-describe-model-accountlevelpermissions) | False | The account-level permissions settings that apply to the bucket. |
| bucketLevelPermissions | [BucketLevelPermissions](#findings-describe-model-bucketlevelpermissions) | False | The bucket-level permissions settings for the bucket. |

### BucketPolicy
<a name="findings-describe-model-bucketpolicy"></a>

Provides information about the permissions settings of the bucket policy for an S3 bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| allowsPublicReadAccess | boolean | False | Specifies whether the bucket policy allows the general public to have read access to the bucket. |
| allowsPublicWriteAccess | boolean | False | Specifies whether the bucket policy allows the general public to have write access to the bucket. |

### BucketPublicAccess
<a name="findings-describe-model-bucketpublicaccess"></a>

Provides information about the permissions settings that determine whether an S3 bucket is publicly accessible.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| effectivePermission | string<br />Values: `PUBLIC \| NOT_PUBLIC \| UNKNOWN` | False | Specifies whether the bucket is publicly accessible due to the combination of permissions settings that apply to the bucket. Possible values are:   `NOT_PUBLIC` - The bucket isn't publicly accessible.    `PUBLIC` - The bucket is publicly accessible.    `UNKNOWN` - Amazon Macie can't determine whether the bucket is publicly accessible.   |
| permissionConfiguration | [BucketPermissionConfiguration](#findings-describe-model-bucketpermissionconfiguration) | False | The account-level and bucket-level permissions settings for the bucket. |

### Cell
<a name="findings-describe-model-cell"></a>

Specifies the location of an occurrence of sensitive data in a Microsoft Excel workbook, CSV file, or TSV file.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cellReference | string | False | The location of the cell, as an absolute cell reference, that contains the sensitive data, for example `Sheet2!C5` for cell C5 on Sheet2 in a Microsoft Excel workbook. This value is null for CSV and TSV files. |
| column | integer<br />Format: int64 | False | The column number of the column that contains the sensitive data. For a Microsoft Excel workbook, this value correlates to the alphabetical character(s) for a column identifier, for example: `1` for column A, `2` for column B, and so on. |
| columnName | string | False | The name of the column that contains the sensitive data, if available. |
| row | integer<br />Format: int64 | False | The row number of the row that contains the sensitive data. |

### ClassificationDetails
<a name="findings-describe-model-classificationdetails"></a>

Provides information about a sensitive data finding and the details of the finding.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| detailedResultsLocation | string | False | The path to the folder or file in Amazon S3 that contains the corresponding sensitive data discovery result for the finding. If a finding applies to a large archive or compressed file, this value is the path to a folder. Otherwise, this value is the path to a file. |
| jobArn | string | False | The Amazon Resource Name (ARN) of the classification job that produced the finding. This value is null if the origin of the finding (`originType`) is `AUTOMATED_SENSITIVE_DATA_DISCOVERY`. |
| jobId | string | False | The unique identifier for the classification job that produced the finding. This value is null if the origin of the finding (`originType`) is `AUTOMATED_SENSITIVE_DATA_DISCOVERY`. |
| originType | [OriginType](#findings-describe-model-origintype) | False | Specifies how Amazon Macie found the sensitive data that produced the finding. Possible values are: `SENSITIVE_DATA_DISCOVERY_JOB`, for a classification job; and, `AUTOMATED_SENSITIVE_DATA_DISCOVERY`, for automated sensitive data discovery. |
| result | [ClassificationResult](#findings-describe-model-classificationresult) | False | The status and other details of the finding. |

### ClassificationResult
<a name="findings-describe-model-classificationresult"></a>

Provides the details of a sensitive data finding, including the types, number of occurrences, and locations of the sensitive data that was detected.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| additionalOccurrences | boolean | False | Specifies whether Amazon Macie detected additional occurrences of sensitive data in the S3 object. A finding includes location data for a maximum of 15 occurrences of sensitive data.<br />This value can help you determine whether to investigate additional occurrences of sensitive data in an object. You can do this by referring to the corresponding sensitive data discovery result for the finding (`classificationDetails.detailedResultsLocation`). |
| customDataIdentifiers | [CustomDataIdentifiers](#findings-describe-model-customdataidentifiers) | False | The custom data identifiers that detected the sensitive data and the number of occurrences of the data that they detected. |
| mimeType | string | False | The type of content, as a MIME type, that the finding applies to. For example, `application/gzip`, for a GNU Gzip compressed archive file, or `application/pdf`, for an Adobe Portable Document Format file. |
| sensitiveData | Array of type [SensitiveDataItem](#findings-describe-model-sensitivedataitem) | False | The category, types, and number of occurrences of the sensitive data that produced the finding. |
| sizeClassified | integer<br />Format: int64 | False | The total size, in bytes, of the data that the finding applies to. |
| status | [ClassificationResultStatus](#findings-describe-model-classificationresultstatus) | False | The status of the finding. |

### ClassificationResultStatus
<a name="findings-describe-model-classificationresultstatus"></a>

Provides information about the status of a sensitive data finding.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| code | string | False | The status of the finding. Possible values are:   `COMPLETE` - Amazon Macie successfully completed its analysis of the S3 object that the finding applies to.    `PARTIAL` - Macie analyzed only a subset of the data in the S3 object that the finding applies to. For example, the object is an archive file that contains files in an unsupported format.    `SKIPPED` - Macie wasn't able to analyze the S3 object that the finding applies to. For example, the object is a file that uses an unsupported format.   |
| reason | string | False | A brief description of the status of the finding. This value is null if the status (`code`) of the finding is `COMPLETE`.<br />Amazon Macie uses this value to notify you of any errors, warnings, or considerations that might impact your analysis of the finding and the affected S3 object. Possible values are:   `ARCHIVE_CONTAINS_UNPROCESSED_FILES` - The object is an archive file and Macie extracted and analyzed only some or none of the files in the archive. To determine which files Macie analyzed, if any, refer to the corresponding sensitive data discovery result for the finding (`classificationDetails.detailedResultsLocation`).    `ARCHIVE_EXCEEDS_SIZE_LIMIT` - The object is an archive file whose total storage size exceeds the size quota for this type of archive.    `ARCHIVE_NESTING_LEVEL_OVER_LIMIT` - The object is an archive file whose nested depth exceeds the quota for the maximum number of nested levels that Macie analyzes for this type of archive.    `ARCHIVE_TOTAL_BYTES_EXTRACTED_OVER_LIMIT` - The object is an archive file that exceeds the quota for the maximum amount of data that Macie extracts and analyzes for this type of archive.    `ARCHIVE_TOTAL_DOCUMENTS_PROCESSED_OVER_LIMIT` - The object is an archive file that contains more than the maximum number of files that Macie extracts and analyzes for this type of archive.    `FILE_EXCEEDS_SIZE_LIMIT` - The storage size of the object exceeds the size quota for this type of file.    `INVALID_ENCRYPTION` - The object is encrypted using server-side encryption but Macie isn't allowed to use the key. Macie can't decrypt and analyze the object.    `INVALID_KMS_KEY` - The object is encrypted with an AWS KMS key that was disabled or is being deleted. Macie can't decrypt and analyze the object.    `INVALID_OBJECT_STATE` - The object doesn't use a supported Amazon S3 storage class.    `JSON_NESTING_LEVEL_OVER_LIMIT` - The object contains JSON data and the nested depth of the data exceeds the quota for the number of nested levels that Macie analyzes for this type of file.    `MALFORMED_FILE` - The object is a malformed or corrupted file. An error occurred when Macie attempted to detect the file's type or extract data from the file.    `MALFORMED_OR_FILE_SIZE_EXCEEDS_LIMIT` - The object is a Microsoft Office file that is malformed or exceeds the size quota for this type of file. If the file is malformed, an error occurred when Macie attempted to extract data from the file.    `NO_SUCH_BUCKET_AVAILABLE` - The object was in a bucket that was deleted shortly before or when Macie attempted to analyze the object.    `OBJECT_VERSION_MISMATCH` - The object was changed while Macie was analyzing it.    `OOXML_UNCOMPRESSED_RATIO_EXCEEDS_LIMIT` - The object is an Office Open XML file whose compression ratio exceeds the compression quota for this type of file.    `OOXML_UNCOMPRESSED_SIZE_EXCEEDS_LIMIT` - The object is an Office Open XML file that exceeds the size quota for this type of file.    `PERMISSION_DENIED` - Macie isn't allowed to access the object. The object's permissions settings prevent Macie from analyzing the object.    `SOURCE_OBJECT_NO_LONGER_AVAILABLE` - The object was deleted shortly before or when Macie attempted to analyze it.  `TIME_CUT_OFF_REACHED` - Macie started analyzing the object but additional analysis would exceed the time quota for analyzing an object.   `UNABLE_TO_PARSE_FILE` - The object is a file that contains structured data and an error occurred when Macie attempted to parse the data.    `UNSUPPORTED_FILE_TYPE_EXCEPTION` - The object is a file that uses an unsupported file or storage format.  <br />For information about quotas, supported storage classes, and supported file and storage formats, see [Quotas](https://docs.aws.amazon.com/macie/latest/user/macie-quotas.html) and [Supported storage classes and formats](https://docs.aws.amazon.com/macie/latest/user/discovery-supported-storage.html) in the *Amazon Macie User Guide*. |

### ConflictException
<a name="findings-describe-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### CustomDataIdentifiers
<a name="findings-describe-model-customdataidentifiers"></a>

Provides information about custom data identifiers that produced a sensitive data finding, and the number of occurrences of the data that they detected for the finding.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| detections | Array of type [CustomDetection](#findings-describe-model-customdetection) | False | The custom data identifiers that detected the data, and the number of occurrences of the data that each identifier detected. |
| totalCount | integer<br />Format: int64 | False | The total number of occurrences of the data that was detected by the custom data identifiers and produced the finding. |

### CustomDetection
<a name="findings-describe-model-customdetection"></a>

Provides information about a custom data identifier that produced a sensitive data finding, and the sensitive data that it detected for the finding.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The unique identifier for the custom data identifier. |
| count | integer<br />Format: int64 | False | The total number of occurrences of the sensitive data that the custom data identifier detected. |
| name | string | False | The name of the custom data identifier. |
| occurrences | [Occurrences](#findings-describe-model-occurrences) | False | The location of 1-15 occurrences of the sensitive data that the custom data identifier detected. A finding includes location data for a maximum of 15 occurrences of sensitive data. |

### DefaultDetection
<a name="findings-describe-model-defaultdetection"></a>

Provides information about a type of sensitive data that was detected by a managed data identifier and produced a sensitive data finding.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| count | integer<br />Format: int64 | False | The total number of occurrences of the type of sensitive data that was detected. |
| occurrences | [Occurrences](#findings-describe-model-occurrences) | False | The location of 1-15 occurrences of the sensitive data that was detected. A finding includes location data for a maximum of 15 occurrences of sensitive data. |
| type | string | False | The type of sensitive data that was detected. For example, `AWS_CREDENTIALS`, `PHONE_NUMBER`, or `ADDRESS`. |

### DomainDetails
<a name="findings-describe-model-domaindetails"></a>

Provides information about the domain name of the device that an entity used to perform an action on an affected resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| domainName | string | False | The name of the domain. |

### EncryptionType
<a name="findings-describe-model-encryptiontype"></a>

The server-side encryption algorithm that was used to encrypt an S3 object or is used by default to encrypt objects that are added to an S3 bucket. Possible values are:
+ `NONE`
+ `AES256`
+ `aws:kms`
+ `UNKNOWN`
+ `aws:kms:dsse`

### FederatedUser
<a name="findings-describe-model-federateduser"></a>

Provides information about an identity that performed an action on an affected resource by using temporary security credentials. The credentials were obtained using the `GetFederationToken` operation of the AWS Security Token Service (AWS STS) API.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accessKeyId | string | False | The AWS access key ID that identifies the credentials. |
| accountId | string | False | The unique identifier for the AWS account that owns the entity that was used to get the credentials. |
| arn | string | False | The Amazon Resource Name (ARN) of the entity that was used to get the credentials. |
| principalId | string | False | The unique identifier for the entity that was used to get the credentials. |
| sessionContext | [SessionContext](#findings-describe-model-sessioncontext) | False | The details of the session that was created for the credentials, including the entity that issued the session. |

### Finding
<a name="findings-describe-model-finding"></a>

Provides the details of a finding.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The unique identifier for the AWS account that the finding applies to. This is typically the account that owns the affected resource. |
| archived | boolean | False | Specifies whether the finding is archived (suppressed). |
| category | [FindingCategory](#findings-describe-model-findingcategory) | False | The category of the finding. Possible values are: `CLASSIFICATION`, for a sensitive data finding; and, `POLICY`, for a policy finding. |
| classificationDetails | [ClassificationDetails](#findings-describe-model-classificationdetails) | False | The details of a sensitive data finding. This value is null for a policy finding. |
| count | integer<br />Format: int64 | False | The total number of occurrences of the finding. For sensitive data findings, this value is always `1`. All sensitive data findings are considered unique. |
| createdAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when Amazon Macie created the finding. |
| description | string | False | The description of the finding. |
| id | string | False | The unique identifier for the finding. This is a random string that Amazon Macie generates and assigns to a finding when it creates the finding. |
| partition | string | False | The AWS partition that Amazon Macie created the finding in. |
| policyDetails | [PolicyDetails](#findings-describe-model-policydetails) | False | The details of a policy finding. This value is null for a sensitive data finding. |
| region | string | False | The AWS Region that Amazon Macie created the finding in. |
| resourcesAffected | [ResourcesAffected](#findings-describe-model-resourcesaffected) | False | The resources that the finding applies to. |
| sample | boolean | False | Specifies whether the finding is a sample finding. A *sample finding* is a finding that uses example data to demonstrate what a finding might contain. |
| schemaVersion | string | False | The version of the schema that was used to define the data structures in the finding. |
| severity | [Severity](#findings-describe-model-severity) | False | The severity level and score for the finding. |
| title | string | False | The brief description of the finding. |
| type | [FindingType](#findings-describe-model-findingtype) | False | The type of the finding. |
| updatedAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when Amazon Macie last updated the finding. For sensitive data findings, this value is the same as the value for the `createdAt` property. All sensitive data findings are considered new. |

### FindingAction
<a name="findings-describe-model-findingaction"></a>

Provides information about an action that occurred for a resource and produced a policy finding.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| actionType | [FindingActionType](#findings-describe-model-findingactiontype) | False | The type of action that occurred for the affected resource. This value is typically `AWS_API_CALL`, which indicates that an entity invoked an API operation for the resource. |
| apiCallDetails | [ApiCallDetails](#findings-describe-model-apicalldetails) | False | The invocation details of the API operation that an entity invoked for the affected resource, if the value for the `actionType` property is `AWS_API_CALL`. |

### FindingActionType
<a name="findings-describe-model-findingactiontype"></a>

The type of action that occurred for the resource and produced the policy finding:
+ `AWS_API_CALL`

### FindingActor
<a name="findings-describe-model-findingactor"></a>

Provides information about an entity that performed an action that produced a policy finding for a resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| domainDetails | [DomainDetails](#findings-describe-model-domaindetails) | False | The domain name of the device that the entity used to perform the action on the affected resource. |
| ipAddressDetails | [IpAddressDetails](#findings-describe-model-ipaddressdetails) | False | The IP address and related details about the device that the entity used to perform the action on the affected resource. The details can include information such as the owner and geographic location of the IP address. |
| userIdentity | [UserIdentity](#findings-describe-model-useridentity) | False | The type and other characteristics of the entity that performed the action on the affected resource. This value is null if the action was performed by an anonymous (unauthenticated) entity. |

### FindingCategory
<a name="findings-describe-model-findingcategory"></a>

The category of the finding. Possible values are:
+ `CLASSIFICATION`
+ `POLICY`

### FindingType
<a name="findings-describe-model-findingtype"></a>

The type of finding. For details about each type, see [Types of findings](https://docs.aws.amazon.com/macie/latest/user/findings-types.html) in the *Amazon Macie User Guide*. Possible values are:
+ `SensitiveData:S3Object/Multiple`
+ `SensitiveData:S3Object/Financial`
+ `SensitiveData:S3Object/Personal`
+ `SensitiveData:S3Object/Credentials`
+ `SensitiveData:S3Object/CustomIdentifier`
+ `Policy:IAMUser/S3BucketPublic`
+ `Policy:IAMUser/S3BucketSharedExternally`
+ `Policy:IAMUser/S3BucketReplicatedExternally`
+ `Policy:IAMUser/S3BucketEncryptionDisabled`
+ `Policy:IAMUser/S3BlockPublicAccessDisabled`
+ `Policy:IAMUser/S3BucketSharedWithCloudFront`

### GetFindingsRequest
<a name="findings-describe-model-getfindingsrequest"></a>

Specifies one or more findings to retrieve.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| findingIds | Array of type string | True | An array of strings that lists the unique identifiers for the findings to retrieve. You can specify as many as 50 unique identifiers in this array. |
| sortCriteria | [SortCriteria](#findings-describe-model-sortcriteria) | False | The criteria for sorting the results of the request. |

### GetFindingsResponse
<a name="findings-describe-model-getfindingsresponse"></a>

Provides the results of a request for one or more findings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| findings | Array of type [Finding](#findings-describe-model-finding) | False | An array of objects, one for each finding that matches the criteria specified in the request. |

### IamUser
<a name="findings-describe-model-iamuser"></a>

Provides information about an AWS Identity and Access Management (IAM) user who performed an action on an affected resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The unique identifier for the AWS account that's associated with the IAM user who performed the action. |
| arn | string | False | The Amazon Resource Name (ARN) of the principal that performed the action. The last section of the ARN contains the name of the user who performed the action. |
| principalId | string | False | The unique identifier for the IAM user who performed the action. |
| userName | string | False | The username of the IAM user who performed the action. |

### InternalServerException
<a name="findings-describe-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### IpAddressDetails
<a name="findings-describe-model-ipaddressdetails"></a>

Provides information about the IP address of the device that an entity used to perform an action on an affected resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ipAddressV4 | string | False | The Internet Protocol version 4 (IPv4) address of the device. |
| ipCity | [IpCity](#findings-describe-model-ipcity) | False | The city that the IP address originated from. |
| ipCountry | [IpCountry](#findings-describe-model-ipcountry) | False | The country that the IP address originated from. |
| ipGeoLocation | [IpGeoLocation](#findings-describe-model-ipgeolocation) | False | The geographic coordinates of the location that the IP address originated from. |
| ipOwner | [IpOwner](#findings-describe-model-ipowner) | False | The registered owner of the IP address. |

### IpCity
<a name="findings-describe-model-ipcity"></a>

Provides information about the city that an IP address originated from.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| name | string | False | The name of the city. |

### IpCountry
<a name="findings-describe-model-ipcountry"></a>

Provides information about the country that an IP address originated from.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| code | string | False | The two-character code, in ISO 3166-1 alpha-2 format, for the country that the IP address originated from. For example, `US` for the United States. |
| name | string | False | The name of the country that the IP address originated from. |

### IpGeoLocation
<a name="findings-describe-model-ipgeolocation"></a>

Provides geographic coordinates that indicate where a specified IP address originated from.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| lat | number | False | The latitude coordinate of the location, rounded to four decimal places. |
| lon | number | False | The longitude coordinate of the location, rounded to four decimal places. |

### IpOwner
<a name="findings-describe-model-ipowner"></a>

Provides information about the registered owner of an IP address.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| asn | string | False | The autonomous system number (ASN) for the autonomous system that included the IP address. |
| asnOrg | string | False | The organization identifier that's associated with the autonomous system number (ASN) for the autonomous system that included the IP address. |
| isp | string | False | The name of the internet service provider (ISP) that owned the IP address. |
| org | string | False | The name of the organization that owned the IP address. |

### KeyValuePair
<a name="findings-describe-model-keyvaluepair"></a>

Provides information about the tags that are associated with an S3 bucket or object. Each tag consists of a required tag key and an associated tag value.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| key | string | False | One part of a key-value pair that comprises a tag. A tag key is a general label that acts as a category for more specific tag values. |
| value | string | False | One part of a key-value pair that comprises a tag. A tag value acts as a descriptor for a tag key. A tag value can be an empty string. |

### Occurrences
<a name="findings-describe-model-occurrences"></a>

Specifies the location of 1-15 occurrences of sensitive data that was detected by a managed data identifier or a custom data identifier and produced a sensitive data finding.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cells | Array of type [Cell](#findings-describe-model-cell) | False | An array of objects, one for each occurrence of sensitive data in a Microsoft Excel workbook, CSV file, or TSV file. This value is null for all other types of files.<br />Each `Cell` object specifies a cell or field that contains the sensitive data. |
| lineRanges | Array of type [Range](#findings-describe-model-range) | False | An array of objects, one for each occurrence of sensitive data in an email message or a non-binary text file such as an HTML, TXT, or XML file. Each `Range` object specifies a line or inclusive range of lines that contains the sensitive data, and the position of the data on the specified line or lines.<br />This value is often null for file types that are supported by `Cell`, `Page`, or `Record` objects. Exceptions are the location of sensitive data in: unstructured sections of an otherwise structured file, such as a comment in a file; a malformed file that Amazon Macie analyzes as plain text; and, a CSV or TSV file that has any column names that contain sensitive data. |
| offsetRanges | Array of type [Range](#findings-describe-model-range) | False | Reserved for future use. |
| pages | Array of type [Page](#findings-describe-model-page) | False | An array of objects, one for each occurrence of sensitive data in an Adobe Portable Document Format file. This value is null for all other types of files.<br />Each `Page` object specifies a page that contains the sensitive data. |
| records | Array of type [Record](#findings-describe-model-record) | False | An array of objects, one for each occurrence of sensitive data in an Apache Avro object container, Apache Parquet file, JSON file, or JSON Lines file. This value is null for all other types of files.<br />For an Avro object container or Parquet file, each `Record` object specifies a record index and the path to a field in a record that contains the sensitive data. For a JSON or JSON Lines file, each `Record` object specifies the path to a field or array that contains the sensitive data. For a JSON Lines file, it also specifies the index of the line that contains the data. |

### OriginType
<a name="findings-describe-model-origintype"></a>

Specifies how Amazon Macie found the sensitive data that produced a finding. Possible values are:
+ `SENSITIVE_DATA_DISCOVERY_JOB`
+ `AUTOMATED_SENSITIVE_DATA_DISCOVERY`

### Page
<a name="findings-describe-model-page"></a>

Specifies the location of an occurrence of sensitive data in an Adobe Portable Document Format file.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| lineRange | [Range](#findings-describe-model-range) | False | Reserved for future use. |
| offsetRange | [Range](#findings-describe-model-range) | False | Reserved for future use. |
| pageNumber | integer<br />Format: int64 | False | The page number of the page that contains the sensitive data. |

### PolicyDetails
<a name="findings-describe-model-policydetails"></a>

Provides the details of a policy finding.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| action | [FindingAction](#findings-describe-model-findingaction) | False | The action that produced the finding. |
| actor | [FindingActor](#findings-describe-model-findingactor) | False | The entity that performed the action that produced the finding. |

### Range
<a name="findings-describe-model-range"></a>

Specifies the location of an occurrence of sensitive data in an email message or a non-binary text file such as an HTML, TXT, or XML file.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| end | integer<br />Format: int64 | False | The number of lines from the beginning of the file to the end of the sensitive data. |
| start | integer<br />Format: int64 | False | The number of lines from the beginning of the file to the beginning of the sensitive data. |
| startColumn | integer<br />Format: int64 | False | The number of characters, with spaces and starting from 1, from the beginning of the first line that contains the sensitive data (`start`) to the beginning of the sensitive data. |

### Record
<a name="findings-describe-model-record"></a>

Specifies the location of an occurrence of sensitive data in an Apache Avro object container, Apache Parquet file, JSON file, or JSON Lines file.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| jsonPath | string | False | The path, as a JSONPath expression, to the sensitive data. For an Avro object container or Parquet file, this is the path to the field in the record (`recordIndex`) that contains the data. For a JSON or JSON Lines file, this is the path to the field or array that contains the data. If the data is a value in an array, the path also indicates which value contains the data.<br />If Amazon Macie detects sensitive data in the name of any element in the path, Macie omits this field. If the name of an element exceeds 240 characters, Macie truncates the name by removing characters from the beginning of the name. If the resulting full path exceeds 250 characters, Macie also truncates the path, starting with the first element in the path, until the path contains 250 or fewer characters. |
| recordIndex | integer<br />Format: int64 | False | For an Avro object container or Parquet file, the record index, starting from 0, for the record that contains the sensitive data. For a JSON Lines file, the line index, starting from 0, for the line that contains the sensitive data. This value is always `0` for JSON files. |

### ResourceNotFoundException
<a name="findings-describe-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourcesAffected
<a name="findings-describe-model-resourcesaffected"></a>

Provides information about the resources that a finding applies to.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| s3Bucket | [S3Bucket](#findings-describe-model-s3bucket) | False | The details of the S3 bucket that the finding applies to. |
| s3Object | [S3Object](#findings-describe-model-s3object) | False | The details of the S3 object that the finding applies to. |

### S3Bucket
<a name="findings-describe-model-s3bucket"></a>

Provides information about the S3 bucket that a finding applies to. If a quota prevented Amazon Macie from retrieving and processing all the bucket's information prior to generating the finding, the following values are `UNKNOWN` or null: `allowsUnencryptedObjectUploads`, `defaultServerSideEncryption`, `publicAccess`, and `tags`.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| allowsUnencryptedObjectUploads | string<br />Values: `TRUE \| FALSE \| UNKNOWN` | False | Specifies whether the bucket policy for the bucket requires server-side encryption of objects when objects are added to the bucket. Possible values are:   `FALSE` - The bucket policy requires server-side encryption of new objects. `PutObject` requests must include a valid server-side encryption header.    `TRUE` - The bucket doesn't have a bucket policy or it has a bucket policy that doesn't require server-side encryption of new objects. If a bucket policy exists, it doesn't require `PutObject` requests to include a valid server-side encryption header.    `UNKNOWN` - Amazon Macie can't determine whether the bucket policy requires server-side encryption of new objects.  <br />Valid server-side encryption headers are: `x-amz-server-side-encryption` with a value of `AES256` or `aws:kms`, and `x-amz-server-side-encryption-customer-algorithm` with a value of `AES256`. |
| arn | string | False | The Amazon Resource Name (ARN) of the bucket. |
| createdAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the bucket was created. This value can also indicate when changes such as edits to the bucket's policy were most recently made to the bucket, relative to when the finding was created or last updated. |
| defaultServerSideEncryption | [ServerSideEncryption](#findings-describe-model-serversideencryption) | False | The default server-side encryption settings for the bucket. |
| name | string | False | The name of the bucket. |
| owner | [S3BucketOwner](#findings-describe-model-s3bucketowner) | False | The display name and canonical user ID for the AWS account that owns the bucket. |
| publicAccess | [BucketPublicAccess](#findings-describe-model-bucketpublicaccess) | False | The permissions settings that determine whether the bucket is publicly accessible. |
| tags | Array of type [KeyValuePair](#findings-describe-model-keyvaluepair) | False | The tags that are associated with the bucket. |

### S3BucketOwner
<a name="findings-describe-model-s3bucketowner"></a>

Provides information about the AWS account that owns an S3 bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| displayName | string | False | The display name of the account that owns the bucket. |
| id | string | False | The canonical user ID for the account that owns the bucket. |

### S3Object
<a name="findings-describe-model-s3object"></a>

Provides information about the S3 object that a finding applies to.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketArn | string | False | The Amazon Resource Name (ARN) of the bucket that contains the object. |
| eTag | string | False | The entity tag (ETag) that identifies the affected version of the object. If the object was overwritten or changed after Amazon Macie produced the finding, this value might be different from the current ETag for the object. |
| extension | string | False | The file name extension of the object. If the object doesn't have a file name extension, this value is `""`. |
| key | string | False | The full name (*key*) of the object, including the object's prefix if applicable. |
| lastModified | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the object was last modified. |
| path | string | False | The full path to the affected object, including the name of the affected bucket and the object's name (`key`). |
| publicAccess | boolean | False | Specifies whether the object is publicly accessible due to the combination of permissions settings that apply to the object. |
| serverSideEncryption | [ServerSideEncryption](#findings-describe-model-serversideencryption) | False | The type of server-side encryption that was used to encrypt the object. |
| size | integer<br />Format: int64 | False | The total storage size, in bytes, of the object. |
| storageClass | [StorageClass](#findings-describe-model-storageclass) | False | The storage class of the object. |
| tags | Array of type [KeyValuePair](#findings-describe-model-keyvaluepair) | False | The tags that are associated with the object. |
| versionId | string | False | The identifier for the affected version of the object. |

### SensitiveDataItem
<a name="findings-describe-model-sensitivedataitem"></a>

Provides information about the category, types, and occurrences of sensitive data that produced a sensitive data finding.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| category | [SensitiveDataItemCategory](#findings-describe-model-sensitivedataitemcategory) | False | The category of sensitive data that was detected. For example: `CREDENTIALS`, for credentials data such as private keys or AWS secret access keys; `FINANCIAL_INFORMATION`, for financial data such as credit card numbers; or, `PERSONAL_INFORMATION`, for personal health information, such as health insurance identification numbers, or personally identifiable information, such as passport numbers. |
| detections | Array of type [DefaultDetection](#findings-describe-model-defaultdetection) | False | An array of objects, one for each type of sensitive data that was detected. Each object reports the number of occurrences of a specific type of sensitive data that was detected, and the location of up to 15 of those occurrences. |
| totalCount | integer<br />Format: int64 | False | The total number of occurrences of the sensitive data that was detected. |

### SensitiveDataItemCategory
<a name="findings-describe-model-sensitivedataitemcategory"></a>

For a finding, the category of sensitive data that was detected and produced the finding. For a managed data identifier, the category of sensitive data that the managed data identifier detects. Possible values are:
+ `FINANCIAL_INFORMATION`
+ `PERSONAL_INFORMATION`
+ `CREDENTIALS`
+ `CUSTOM_IDENTIFIER`

### ServerSideEncryption
<a name="findings-describe-model-serversideencryption"></a>

Provides information about the default server-side encryption settings for an S3 bucket or the encryption settings for an S3 object.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| encryptionType | [EncryptionType](#findings-describe-model-encryptiontype) | False | The server-side encryption algorithm that's used when storing data in the bucket or object. If default encryption settings aren't configured for the bucket or the object isn't encrypted using server-side encryption, this value is `NONE`. |
| kmsMasterKeyId | string | False | The Amazon Resource Name (ARN) or unique identifier (key ID) for the AWS KMS key that's used to encrypt data in the bucket or the object. This value is null if an AWS KMS key isn't used to encrypt the data. |

### ServiceQuotaExceededException
<a name="findings-describe-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### SessionContext
<a name="findings-describe-model-sessioncontext"></a>

Provides information about a session that was created for an entity that performed an action by using temporary security credentials.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| attributes | [SessionContextAttributes](#findings-describe-model-sessioncontextattributes) | False | The date and time when the credentials were issued, and whether the credentials were authenticated with a multi-factor authentication (MFA) device. |
| sessionIssuer | [SessionIssuer](#findings-describe-model-sessionissuer) | False | The source and type of credentials that were issued to the entity. |

### SessionContextAttributes
<a name="findings-describe-model-sessioncontextattributes"></a>

Provides information about the context in which temporary security credentials were issued to an entity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| creationDate | string<br />Format: date-time | False | The date and time, in UTC and ISO 8601 format, when the credentials were issued. |
| mfaAuthenticated | boolean | False | Specifies whether the credentials were authenticated with a multi-factor authentication (MFA) device. |

### SessionIssuer
<a name="findings-describe-model-sessionissuer"></a>

Provides information about the source and type of temporary security credentials that were issued to an entity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The unique identifier for the AWS account that owns the entity that was used to get the credentials. |
| arn | string | False | The Amazon Resource Name (ARN) of the source account, AWS Identity and Access Management (IAM) user, or role that was used to get the credentials. |
| principalId | string | False | The unique identifier for the entity that was used to get the credentials. |
| type | string | False | The source of the temporary security credentials, such as `Root`, `IAMUser`, or `Role`.  |
| userName | string | False | The name or alias of the user or role that issued the session. This value is null if the credentials were obtained from a root account that doesn't have an alias. |

### Severity
<a name="findings-describe-model-severity"></a>

Provides the numerical and qualitative representations of a finding's severity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | [SeverityDescription](#findings-describe-model-severitydescription) | False | The qualitative representation of the finding's severity, ranging from `Low` (least severe) to `High` (most severe). |
| score | integer<br />Format: int64 | False | The numerical representation of the finding's severity, ranging from `1` (least severe) to `3` (most severe). |

### SeverityDescription
<a name="findings-describe-model-severitydescription"></a>

The qualitative representation of the finding's severity. Possible values are:
+ `Low`
+ `Medium`
+ `High`

### SortCriteria
<a name="findings-describe-model-sortcriteria"></a>

Specifies criteria for sorting the results of a request for findings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| attributeName | string | False | The name of the property to sort the results by. Valid values are: `count`, `createdAt`, `policyDetails.action.apiCallDetails.firstSeen`, `policyDetails.action.apiCallDetails.lastSeen`, `resourcesAffected`, `severity.score`, `type`, and `updatedAt`. |
| orderBy | string<br />Values: `ASC \| DESC` | False | The sort order to apply to the results, based on the value for the property specified by the `attributeName` property. Valid values are: `ASC`, sort the results in ascending order; and, `DESC`, sort the results in descending order. |

### StorageClass
<a name="findings-describe-model-storageclass"></a>

The storage class of the S3 object. Possible values are:
+ `STANDARD`
+ `REDUCED_REDUNDANCY`
+ `STANDARD_IA`
+ `INTELLIGENT_TIERING`
+ `DEEP_ARCHIVE`
+ `ONEZONE_IA`
+ `GLACIER`
+ `GLACIER_IR`
+ `OUTPOSTS`

### ThrottlingException
<a name="findings-describe-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### UserIdentity
<a name="findings-describe-model-useridentity"></a>

Provides information about the type and other characteristics of an entity that performed an action on an affected resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| assumedRole | [AssumedRole](#findings-describe-model-assumedrole) | False | If the action was performed with temporary security credentials that were obtained using the `AssumeRole` operation of the AWS Security Token Service (AWS STS) API, the identifiers, session context, and other details about the identity. |
| awsAccount | [AwsAccount](#findings-describe-model-awsaccount) | False | If the action was performed using the credentials for another AWS account, the details of that account. |
| awsService | [AwsService](#findings-describe-model-awsservice) | False | If the action was performed by an AWS account that belongs to an AWS service, the name of the service. |
| federatedUser | [FederatedUser](#findings-describe-model-federateduser) | False | If the action was performed with temporary security credentials that were obtained using the `GetFederationToken` operation of the AWS Security Token Service (AWS STS) API, the identifiers, session context, and other details about the identity. |
| iamUser | [IamUser](#findings-describe-model-iamuser) | False | If the action was performed using the credentials for an AWS Identity and Access Management (IAM) user, the name and other details about the user. |
| root | [UserIdentityRoot](#findings-describe-model-useridentityroot) | False | If the action was performed using the credentials for your AWS account, the details of your account. |
| type | [UserIdentityType](#findings-describe-model-useridentitytype) | False | The type of entity that performed the action. |

### UserIdentityRoot
<a name="findings-describe-model-useridentityroot"></a>

Provides information about an AWS account and entity that performed an action on an affected resource. The action was performed using the credentials for your AWS account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The unique identifier for the AWS account. |
| arn | string | False | The Amazon Resource Name (ARN) of the principal that performed the action. The last section of the ARN contains the name of the user or role that performed the action. |
| principalId | string | False | The unique identifier for the entity that performed the action. |

### UserIdentityType
<a name="findings-describe-model-useridentitytype"></a>

The type of entity that performed the action on the affected resource. Possible values are:
+ `AssumedRole`
+ `IAMUser`
+ `FederatedUser`
+ `Root`
+ `AWSAccount`
+ `AWSService`

### ValidationException
<a name="findings-describe-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="findings-describe-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetFindings
<a name="GetFindings-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetFindings)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetFindings)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetFindings)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetFindings)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetFindings)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetFindings)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetFindings)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetFindings)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/GetFindings)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetFindings)
