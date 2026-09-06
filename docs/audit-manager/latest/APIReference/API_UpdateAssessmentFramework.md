---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentFramework.html
---

# UpdateAssessmentFramework
<a name="API_UpdateAssessmentFramework"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Updates a custom framework in AWS Audit Manager.

## Request Syntax
<a name="API_UpdateAssessmentFramework_RequestSyntax"></a>

```
PUT /assessmentFrameworks/{{frameworkId}} HTTP/1.1
Content-type: application/json

{
   "complianceType": "{{string}}",
   "controlSets": [
      {
         "controls": [
            {
               "id": "{{string}}"
            }
         ],
         "id": "{{string}}",
         "name": "{{string}}"
      }
   ],
   "description": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAssessmentFramework_RequestParameters"></a>

The request uses the following URI parameters.

 ** [frameworkId](#API_UpdateAssessmentFramework_RequestSyntax) **   <a name="auditmanager-UpdateAssessmentFramework-request-uri-frameworkId"></a>
 The unique identifier for the framework.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_UpdateAssessmentFramework_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [complianceType](#API_UpdateAssessmentFramework_RequestSyntax) **   <a name="auditmanager-UpdateAssessmentFramework-request-complianceType"></a>
 The compliance type that the new custom framework supports, such as CIS or HIPAA.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** [controlSets](#API_UpdateAssessmentFramework_RequestSyntax) **   <a name="auditmanager-UpdateAssessmentFramework-request-controlSets"></a>
 The control sets that are associated with the framework.
The `Controls` object returns a partial response when called through Framework APIs. For a complete `Controls` object, use `GetControl`.
Type: Array of [UpdateAssessmentFrameworkControlSet](API_UpdateAssessmentFrameworkControlSet.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [description](#API_UpdateAssessmentFramework_RequestSyntax) **   <a name="auditmanager-UpdateAssessmentFramework-request-description"></a>
 The description of the updated framework.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** [name](#API_UpdateAssessmentFramework_RequestSyntax) **   <a name="auditmanager-UpdateAssessmentFramework-request-name"></a>
 The name of the framework to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\]*$`
Required: Yes

## Response Syntax
<a name="API_UpdateAssessmentFramework_ResponseSyntax"></a>

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
<a name="API_UpdateAssessmentFramework_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [framework](#API_UpdateAssessmentFramework_ResponseSyntax) **   <a name="auditmanager-UpdateAssessmentFramework-response-framework"></a>
 The framework object.
Type: [Framework](API_Framework.md) object

## Errors
<a name="API_UpdateAssessmentFramework_Errors"></a>

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

 ** ValidationException **
 The request has invalid or missing parameters.
 ** fields **
 The fields that caused the error, if applicable.
 ** reason **
 The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAssessmentFramework_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/UpdateAssessmentFramework)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/UpdateAssessmentFramework)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/UpdateAssessmentFramework)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/UpdateAssessmentFramework)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/UpdateAssessmentFramework)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/UpdateAssessmentFramework)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/UpdateAssessmentFramework)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/UpdateAssessmentFramework)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/UpdateAssessmentFramework)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/UpdateAssessmentFramework)
