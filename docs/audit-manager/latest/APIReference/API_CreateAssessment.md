---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_CreateAssessment.html
---

# CreateAssessment
<a name="API_CreateAssessment"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Creates an assessment in AWS Audit Manager.

## Request Syntax
<a name="API_CreateAssessment_RequestSyntax"></a>

```
POST /assessments HTTP/1.1
Content-type: application/json

{
   "assessmentReportsDestination": {
      "destination": "{{string}}",
      "destinationType": "{{string}}"
   },
   "description": "{{string}}",
   "frameworkId": "{{string}}",
   "name": "{{string}}",
   "roles": [
      {
         "roleArn": "{{string}}",
         "roleType": "{{string}}"
      }
   ],
   "scope": {
      "awsAccounts": [
         {
            "emailAddress": "{{string}}",
            "id": "{{string}}",
            "name": "{{string}}"
         }
      ],
      "awsServices": [
         {
            "serviceName": "{{string}}"
         }
      ]
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateAssessment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAssessment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [assessmentReportsDestination](#API_CreateAssessment_RequestSyntax) **   <a name="auditmanager-CreateAssessment-request-assessmentReportsDestination"></a>
 The assessment report storage destination for the assessment that's being created.
Type: [AssessmentReportsDestination](API_AssessmentReportsDestination.md) object
Required: Yes

 ** [description](#API_CreateAssessment_RequestSyntax) **   <a name="auditmanager-CreateAssessment-request-description"></a>
 The optional description of the assessment to be created.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** [frameworkId](#API_CreateAssessment_RequestSyntax) **   <a name="auditmanager-CreateAssessment-request-frameworkId"></a>
 The identifier for the framework that the assessment will be created from.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [name](#API_CreateAssessment_RequestSyntax) **   <a name="auditmanager-CreateAssessment-request-name"></a>
 The name of the assessment to be created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\]*$`
Required: Yes

 ** [roles](#API_CreateAssessment_RequestSyntax) **   <a name="auditmanager-CreateAssessment-request-roles"></a>
 The list of roles for the assessment.
Type: Array of [Role](API_Role.md) objects
Required: Yes

 ** [scope](#API_CreateAssessment_RequestSyntax) **   <a name="auditmanager-CreateAssessment-request-scope"></a>
 The wrapper that contains the AWS accounts that are in scope for the assessment.
You no longer need to specify which AWS services are in scope when you create or update an assessment. Audit Manager infers the services in scope by examining your assessment controls and their data sources, and then mapping this information to the relevant AWS services.
If an underlying data source changes for your assessment, we automatically update the services scope as needed to reflect the correct AWS services. This ensures that your assessment collects accurate and comprehensive evidence about all of the relevant services in your AWS environment.
Type: [Scope](API_Scope.md) object
Required: Yes

 ** [tags](#API_CreateAssessment_RequestSyntax) **   <a name="auditmanager-CreateAssessment-request-tags"></a>
 The tags that are associated with the assessment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.{0,255}`
Required: No

## Response Syntax
<a name="API_CreateAssessment_ResponseSyntax"></a>

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
   }
}
```

## Response Elements
<a name="API_CreateAssessment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assessment](#API_CreateAssessment_ResponseSyntax) **   <a name="auditmanager-CreateAssessment-response-assessment"></a>
 An entity that defines the scope of audit evidence collected by AWS Audit Manager. An Audit Manager assessment is an implementation of an Audit Manager framework.
Type: [Assessment](API_Assessment.md) object

## Errors
<a name="API_CreateAssessment_Errors"></a>

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

 ** ServiceQuotaExceededException **
You've reached your account quota for this resource type. To perform the requested action, delete some existing resources or [request a quota increase](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) from the Service Quotas console. For a list of Audit Manager service quotas, see [Quotas and restrictions for AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html).
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
 The request has invalid or missing parameters.
 ** fields **
 The fields that caused the error, if applicable.
 ** reason **
 The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_CreateAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/CreateAssessment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/CreateAssessment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/CreateAssessment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/CreateAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/CreateAssessment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/CreateAssessment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/CreateAssessment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/CreateAssessment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/CreateAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/CreateAssessment)
