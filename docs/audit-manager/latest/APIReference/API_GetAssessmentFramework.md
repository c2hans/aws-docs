---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAssessmentFramework.html
---

# GetAssessmentFramework
<a name="API_GetAssessmentFramework"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

Gets information about a specified framework.

## Request Syntax
<a name="API_GetAssessmentFramework_RequestSyntax"></a>

```
GET /assessmentFrameworks/{{frameworkId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAssessmentFramework_RequestParameters"></a>

The request uses the following URI parameters.

 ** [frameworkId](#API_GetAssessmentFramework_RequestSyntax) **   <a name="auditmanager-GetAssessmentFramework-request-uri-frameworkId"></a>
 The identifier for the framework.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_GetAssessmentFramework_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAssessmentFramework_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "framework": {
      "arn": "string",
      "complianceType": "string",
      "controlSets": [
         {
            "controls": [
               {
                  "actionPlanInstructions": "string",
                  "actionPlanTitle": "string",
                  "arn": "string",
                  "controlMappingSources": [
                     {
                        "sourceDescription": "string",
                        "sourceFrequency": "string",
                        "sourceId": "string",
                        "sourceKeyword": {
                           "keywordInputType": "string",
                           "keywordValue": "string"
                        },
                        "sourceName": "string",
                        "sourceSetUpOption": "string",
                        "sourceType": "string",
                        "troubleshootingText": "string"
                     }
                  ],
                  "controlSources": "string",
                  "createdAt": number,
                  "createdBy": "string",
                  "description": "string",
                  "id": "string",
                  "lastUpdatedAt": number,
                  "lastUpdatedBy": "string",
                  "name": "string",
                  "state": "string",
                  "tags": {
                     "string" : "string"
                  },
                  "testingInformation": "string",
                  "type": "string"
               }
            ],
            "id": "string",
            "name": "string"
         }
      ],
      "controlSources": "string",
      "createdAt": number,
      "createdBy": "string",
      "description": "string",
      "id": "string",
      "lastUpdatedAt": number,
      "lastUpdatedBy": "string",
      "logo": "string",
      "name": "string",
      "tags": {
         "string" : "string"
      },
      "type": "string"
   }
}
```

## Response Elements
<a name="API_GetAssessmentFramework_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [framework](#API_GetAssessmentFramework_ResponseSyntax) **   <a name="auditmanager-GetAssessmentFramework-response-framework"></a>
 The framework that the `GetAssessmentFramework` API returned.
The `Controls` object returns a partial response when called through Framework APIs. For a complete `Controls` object, use `GetControl`.
Type: [Framework](API_Framework.md) object

## Errors
<a name="API_GetAssessmentFramework_Errors"></a>

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
<a name="API_GetAssessmentFramework_Examples"></a>

### Getting information about a framework
<a name="API_GetAssessmentFramework_Example_1"></a>

This example shows a sample response for the `GetAssessmentFramework` API operation. This example shows details for a custom framework with two control sets and three controls.

#### Sample Response
<a name="API_GetAssessmentFramework_Example_1_Response"></a>

```
{
    "framework": {
        "arn": "arn:aws:auditmanager:us-east-1:111122223333:assessmentFramework/a1b2c3d4-5678-90ab-cdef-example11111",
        "id": "a1b2c3d4-5678-90ab-cdef-example11111",
        "name": "My example custom framework",
        "type": "Custom",
        "description": "Checks CloudTrail and AWS API calls.",
        "controlSources": "AWS API calls, AWS CloudTrail",
        "controlSets": [
            {
                "id": "AWS API Calls",
                "name": "Control set 1 - AWS API Calls",
                "controls": [
                    {
                        "arn": "arn:aws:auditmanager:us-east-1::control/control1-5678-90ab-cdef-example11111",
                        "id": "control1-5678-90ab-cdef-example11111",
                        "type": "Standard",
                        "name": "Control 1 - List Principals and Policies",
                        "state": "ACTIVE",
                        "description": "List all AWS IAM Principals and Policies",
                        "testingInformation": "IAM:\nListRoles\nListRolePolicies\nListUsers\nListGroups\n\n",
                        "controlSources": "AWS API calls",
                        "controlMappingSources": [
                            {
                                "sourceId": "sourceid-5678-90ab-cdef-example11111",
                                "sourceSetUpOption": "System_Controls_Mapping",
                                "sourceType": "AWS_API_Call",
                                "sourceKeyword": {
                                    "keywordInputType": "SELECT_FROM_LIST",
                                    "keywordValue": "iam_ListGroups"
                                },
                                "sourceFrequency": "DAILY"
                            },
                            {
                                "sourceId": "sourceid-5678-90ab-cdef-example22222",
                                "sourceSetUpOption": "System_Controls_Mapping",
                                "sourceType": "AWS_API_Call",
                                "sourceKeyword": {
                                    "keywordInputType": "SELECT_FROM_LIST",
                                    "keywordValue": "iam_ListRoles"
                                },
                                "sourceFrequency": "DAILY"
                            },
                            {
                                "sourceId": "sourceid-5678-90ab-cdef-example33333",
                                "sourceSetUpOption": "System_Controls_Mapping",
                                "sourceType": "AWS_API_Call",
                                "sourceKeyword": {
                                    "keywordInputType": "SELECT_FROM_LIST",
                                    "keywordValue": "iam_ListUsers"
                                },
                                "sourceFrequency": "DAILY"
                            },
                            {
                                "sourceId": "sourceid-5678-90ab-cdef-example44444",
                                "sourceSetUpOption": "System_Controls_Mapping",
                                "sourceType": "AWS_API_Call",
                                "sourceKeyword": {
                                    "keywordInputType": "SELECT_FROM_LIST",
                                    "keywordValue": "iam_ListPolicies"
                                },
                                "sourceFrequency": "DAILY"
                            }
                        ],
                        "createdAt": "2020-12-07T15:18:29.217000-08:00",
                        "lastUpdatedAt": "2022-03-24T12:06:55.083000-07:00",
                        "createdBy": "john-doe",
                        "tags": {}
                    },
                    {
                        "arn": "arn:aws:auditmanager:us-east-1::control/control2-5678-90ab-cdef-example22222",
                        "id": "control2-5678-90ab-cdef-example22222",
                        "type": "Standard",
                        "name": "Control 2 - Describe Networks",
                        "state": "ACTIVE",
                        "description": "Describe all VPC(s), Security Groups, Network ACL, and Routes",
                        "testingInformation": "List all VPC IDs in region.  Get a list of all Security Groups and NACLs describes for each of those VPC IDs.  Display all routes.",
                        "controlSources": "AWS API calls",
                        "controlMappingSources": [
                            {
                                "sourceId": "sourceid-5678-90ab-cdef-example55555",
                                "sourceSetUpOption": "System_Controls_Mapping",
                                "sourceType": "AWS_API_Call",
                                "sourceKeyword": {
                                    "keywordInputType": "SELECT_FROM_LIST",
                                    "keywordValue": "ec2_DescribeVpcs"
                                },
                                "sourceFrequency": "DAILY"
                            },
                            {
                                "sourceId": "sourceid-5678-90ab-cdef-example66666",
                                "sourceSetUpOption": "System_Controls_Mapping",
                                "sourceType": "AWS_API_Call",
                                "sourceKeyword": {
                                    "keywordInputType": "SELECT_FROM_LIST",
                                    "keywordValue": "ec2_DescribeSecurityGroups"
                                },
                                "sourceFrequency": "DAILY"
                            },
                            {
                                "sourceId": "sourceid-5678-90ab-cdef-example77777",
                                "sourceSetUpOption": "System_Controls_Mapping",
                                "sourceType": "AWS_API_Call",
                                "sourceKeyword": {
                                    "keywordInputType": "SELECT_FROM_LIST",
                                    "keywordValue": "ec2_DescribeNetworkAcls"
                                },
                                "sourceFrequency": "DAILY"
                            },
                            {
                                "sourceId": "sourceid-5678-90ab-cdef-example88888",
                                "sourceSetUpOption": "System_Controls_Mapping",
                                "sourceType": "AWS_API_Call",
                                "sourceKeyword": {
                                    "keywordInputType": "SELECT_FROM_LIST",
                                    "keywordValue": "ec2_DescribeRouteTables"
                                },
                                "sourceFrequency": "DAILY"
                            }
                        ],
                        "createdAt": "2020-12-07T15:18:29.217000-08:00",
                        "lastUpdatedAt": "2022-03-24T12:06:55.323000-07:00",
                        "createdBy": "john-doe",
                        "tags": {}
                    }
                ]
            },
            {
                "id": "CloudTrail Checks",
                "name": "Control set 2 - CloudTrail Checks",
                "controls": [
                    {
                        "arn": "arn:aws:auditmanager:us-east-1::control/control3-5678-90ab-cdef-example33333",
                        "id": "control3-5678-90ab-cdef-example33333",
                        "type": "Standard",
                        "name": "Control 3 - CloudTrail Volume Events",
                        "state": "END_OF_SUPPORT",
                        "description": "CloudTrail eventName for volumes",
                        "testingInformation": "CloudTrail eventName: CreateVolume\DetachVolume ",
                        "controlSources": "AWS CloudTrail",
                        "controlMappingSources": [
                            {
                                "sourceId": "sourceid-72e6-44da-8486-example99999",
                                "sourceSetUpOption": "System_Controls_Mapping",
                                "sourceType": "AWS_Cloudtrail",
                                "sourceKeyword": {
                                    "keywordInputType": "SELECT_FROM_LIST",
                                    "keywordValue": "ec2_CreateVolume"
                                }
                            },
                            {
                                "sourceId": "sourceid-7389-47ca-887b-example00000",
                                "sourceSetUpOption": "System_Controls_Mapping",
                                "sourceType": "AWS_Cloudtrail",
                                "sourceKeyword": {
                                    "keywordInputType": "SELECT_FROM_LIST",
                                    "keywordValue": "ec2_DetachVolume"
                                }
                            }
                        ],
                        "createdAt": "2020-12-07T15:18:29.217000-08:00",
                        "lastUpdatedAt": "2022-03-24T12:06:55.193000-07:00",
                        "createdBy": "john-doe",
                        "tags": {}
                    }
                ]
            }
        ],
        "createdAt": "2021-03-02T16:35:24.177000-08:00",
        "lastUpdatedAt": "2022-01-10T14:32:18.855000-08:00",
        "createdBy": "john-doe",
        "lastUpdatedBy": "jane-doe",
        "tags": {}
    }
}
```

## See Also
<a name="API_GetAssessmentFramework_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/GetAssessmentFramework)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/GetAssessmentFramework)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/GetAssessmentFramework)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/GetAssessmentFramework)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/GetAssessmentFramework)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/GetAssessmentFramework)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/GetAssessmentFramework)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/GetAssessmentFramework)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/GetAssessmentFramework)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/GetAssessmentFramework)
