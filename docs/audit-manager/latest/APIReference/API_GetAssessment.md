---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAssessment.html
---

# GetAssessment
<a name="API_GetAssessment"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

Gets information about a specified assessment.

## Request Syntax
<a name="API_GetAssessment_RequestSyntax"></a>

```
GET /assessments/{{assessmentId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAssessment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assessmentId](#API_GetAssessment_RequestSyntax) **   <a name="auditmanager-GetAssessment-request-uri-assessmentId"></a>
The unique identifier for the assessment.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_GetAssessment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAssessment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assessment": {
      "arn": "string",
      "awsAccount": {
         "emailAddress": "string",
         "id": "string",
         "name": "string"
      },
      "framework": {
         "arn": "string",
         "controlSets": [
            {
               "controls": [
                  {
                     "assessmentReportEvidenceCount": number,
                     "comments": [
                        {
                           "authorName": "string",
                           "commentBody": "string",
                           "postedDate": number
                        }
                     ],
                     "description": "string",
                     "evidenceCount": number,
                     "evidenceSources": [ "string" ],
                     "id": "string",
                     "name": "string",
                     "response": "string",
                     "status": "string"
                  }
               ],
               "delegations": [
                  {
                     "assessmentId": "string",
                     "assessmentName": "string",
                     "comment": "string",
                     "controlSetId": "string",
                     "createdBy": "string",
                     "creationTime": number,
                     "id": "string",
                     "lastUpdated": number,
                     "roleArn": "string",
                     "roleType": "string",
                     "status": "string"
                  }
               ],
               "description": "string",
               "id": "string",
               "manualEvidenceCount": number,
               "roles": [
                  {
                     "roleArn": "string",
                     "roleType": "string"
                  }
               ],
               "status": "string",
               "systemEvidenceCount": number
            }
         ],
         "id": "string",
         "metadata": {
            "complianceType": "string",
            "description": "string",
            "logo": "string",
            "name": "string"
         }
      },
      "metadata": {
         "assessmentReportsDestination": {
            "destination": "string",
            "destinationType": "string"
         },
         "complianceType": "string",
         "creationTime": number,
         "delegations": [
            {
               "assessmentId": "string",
               "assessmentName": "string",
               "comment": "string",
               "controlSetId": "string",
               "createdBy": "string",
               "creationTime": number,
               "id": "string",
               "lastUpdated": number,
               "roleArn": "string",
               "roleType": "string",
               "status": "string"
            }
         ],
         "description": "string",
         "id": "string",
         "lastUpdated": number,
         "name": "string",
         "roles": [
            {
               "roleArn": "string",
               "roleType": "string"
            }
         ],
         "scope": {
            "awsAccounts": [
               {
                  "emailAddress": "string",
                  "id": "string",
                  "name": "string"
               }
            ],
            "awsServices": [
               {
                  "serviceName": "string"
               }
            ]
         },
         "status": "string"
      },
      "tags": {
         "string" : "string"
      }
   },
   "userRole": {
      "roleArn": "string",
      "roleType": "string"
   }
}
```

## Response Elements
<a name="API_GetAssessment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assessment](#API_GetAssessment_ResponseSyntax) **   <a name="auditmanager-GetAssessment-response-assessment"></a>
 An entity that defines the scope of audit evidence collected by AWS Audit Manager. An Audit Manager assessment is an implementation of an Audit Manager framework.
Type: [Assessment](API_Assessment.md) object

 ** [userRole](#API_GetAssessment_ResponseSyntax) **   <a name="auditmanager-GetAssessment-response-userRole"></a>
 The wrapper that contains the Audit Manager role information of the current user. This includes the role type and IAM Amazon Resource Name (ARN).
Type: [Role](API_Role.md) object

## Errors
<a name="API_GetAssessment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 Your account isn't registered with AWS Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again.
HTTP Status Code: 403

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource that's specified in the request can't be found.
 ** resourceId **
 The unique identifier for the resource.
 ** resourceType **
 The type of resource that's affected by the error.
HTTP Status Code: 404

 ** ValidationException **
 The request has invalid or missing parameters.
 ** fields **
 The fields that caused the error, if applicable.
 ** reason **
 The reason the request failed validation.
HTTP Status Code: 400

## Examples
<a name="API_GetAssessment_Examples"></a>

### Getting information about an assessment
<a name="API_GetAssessment_Example_1"></a>

This example shows a sample response for the `GetAssessment` API operation.

#### Sample Response
<a name="API_GetAssessment_Example_1_Response"></a>

```
{
    "assessment": {
        "arn": "arn:aws:auditmanager:us-east-1:111122223333:assessment/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "awsAccount": {
            "id": "111122223333"
        },
        "metadata": {
            "name": "My assessment",
            "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "description": "This is a description about the assessment",
            "complianceType": "AWS Audit Manager Sample Framework",
            "status": "ACTIVE",
            "assessmentReportsDestination": {
                "destinationType": "S3",
                "destination": "s3://my-assessment-report-destination"
            },
            "scope": {
                "awsAccounts": [
                    {
                        "id": "111122223333"
                    }
                ],
                "awsServices": [
                    {
                        "serviceName": "iam"
                    },
                    {
                        "serviceName": "ec2"
                    },
                    {
                        "serviceName": "cloudtrail"
                    }
                ]
            },
            "roles": [
                {
                    "roleType": "PROCESS_OWNER",
                    "roleArn": "arn:aws:iam::111122223333:role/Administrator"
                },
                {
                    "roleType": "PROCESS_OWNER",
                    "roleArn": "arn:aws:iam::222233334444:role/ReadOnly"
                }
            ],
            "delegations": [],
            "creationTime": "2023-03-13T16:05:55.180000-07:00",
            "lastUpdated": "2023-03-13T16:05:55.309000-07:00"
        },
        "framework": {
            "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "metadata": {
                "name": "AWS Audit Manager Sample Framework",
                "description": "The AWS Audit Manager sample template contains CloudTrail and AWS API calls.  \n\n4 automated controls\n1 manual controls",
                "logo": "Arch_AWS-Audit-Manager_16.svg",
                "complianceType": "AWS Audit Manager Sample Framework"
            },
            "controlSets": [
                {
                    "id": "AWS API",
                    "description": "AWS API",
                    "status": "ACTIVE",
                    "roles": [
                        {
                            "roleType": "PROCESS_OWNER",
                            "roleArn": "arn:aws:iam::111122223333:role/Administrator"
                        },
                        {
                            "roleType": "PROCESS_OWNER",
                            "roleArn": "arn:aws:iam::222233334444:role/ReadOnly"
                        }
                    ],
                    "controls": [
                        {
                            "id": "control1-5678-90ab-cdef-example11111",
                            "name": "2.2.0 - List Principals and Policies",
                            "description": "2.2.0 - List Principals and Policies",
                            "status": "UNDER_REVIEW",
                            "comments": [],
                            "evidenceSources": [
                                "AWS API calls"
                            ],
                            "evidenceCount": 0,
                            "assessmentReportEvidenceCount": 0
                        },
                        {
                            "id": "control2-5678-90ab-cdef-example22222",
                            "name": "2.2.1 - Describe Networks",
                            "description": "2.2.1 - Describe Networks",
                            "status": "UNDER_REVIEW",
                            "comments": [],
                            "evidenceSources": [
                                "AWS API calls"
                            ],
                            "evidenceCount": 0,
                            "assessmentReportEvidenceCount": 0
                        }
                    ],
                    "delegations": [],
                    "systemEvidenceCount": 0,
                    "manualEvidenceCount": 0
                },
                {
                    "id": "Account",
                    "description": "Account",
                    "status": "ACTIVE",
                    "roles": [
                        {
                            "roleType": "PROCESS_OWNER",
                            "roleArn": "arn:aws:iam::111122223333:role/Administrator"
                        },
                        {
                            "roleType": "PROCESS_OWNER",
                            "roleArn": "arn:aws:iam::222233334444:role/ReadOnly"
                        }
                    ],
                    "controls": [
                        {
                            "id": "control3-5678-90ab-cdef-example33333",
                            "name": "3.0.0 - Account Summary",
                            "description": "3.0.0 - Account Summary",
                            "status": "REVIEWED",
                            "comments": [],
                            "evidenceSources": [
                                "Manual"
                            ],
                            "evidenceCount": 1,
                            "assessmentReportEvidenceCount": 1
                        }
                    ],
                    "delegations": [],
                    "systemEvidenceCount": 0,
                    "manualEvidenceCount": 0
                },
                {
                    "id": "CloudTrail",
                    "description": "CloudTrail",
                    "status": "ACTIVE",
                    "roles": [
                        {
                            "roleType": "PROCESS_OWNER",
                            "roleArn": "arn:aws:iam::111122223333:role/Administrator"
                        },
                        {
                            "roleType": "PROCESS_OWNER",
                            "roleArn": "arn:aws:iam::222233334444:role/ReadOnly"
                        }
                    ],
                    "controls": [
                        {
                            "id": "control4-5678-90ab-cdef-example44444",
                            "name": "1.0.1 - CloudTrail Instance Events",
                            "description": "1.0.1 - CloudTrail Instance Events",
                            "status": "UNDER_REVIEW",
                            "comments": [],
                            "evidenceSources": [
                                "AWS CloudTrail"
                            ],
                            "evidenceCount": 0,
                            "assessmentReportEvidenceCount": 0
                        },
                        {
                            "id": "ab65b812-0e1d-4aa9-ad61-0a642535824d",
                            "name": "1.0.2 - CloudTrail Volume Events",
                            "description": "1.0.2 - CloudTrail Volume Events",
                            "status": "UNDER_REVIEW",
                            "comments": [],
                            "evidenceSources": [
                                "AWS CloudTrail"
                            ],
                            "evidenceCount": 0,
                            "assessmentReportEvidenceCount": 0
                        }
                    ],
                    "delegations": [],
                    "systemEvidenceCount": 0,
                    "manualEvidenceCount": 0
                }
            ]
        },
        "tags": {}
    },
    "userRole": {
        "roleType": "PROCESS_OWNER",
        "roleArn": "arn:aws:iam::111122223333:role/Administrator"
    }
}
```

## See Also
<a name="API_GetAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/GetAssessment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/GetAssessment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/GetAssessment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/GetAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/GetAssessment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/GetAssessment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/GetAssessment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/GetAssessment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/GetAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/GetAssessment)
