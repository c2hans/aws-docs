---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_CreateControl.html
---

# CreateControl
<a name="API_CreateControl"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Creates a new custom control in AWS Audit Manager.

## Request Syntax
<a name="API_CreateControl_RequestSyntax"></a>

```
POST /controls HTTP/1.1
Content-type: application/json

{
   "actionPlanInstructions": "{{string}}",
   "actionPlanTitle": "{{string}}",
   "controlMappingSources": [
      {
         "sourceDescription": "{{string}}",
         "sourceFrequency": "{{string}}",
         "sourceKeyword": {
            "keywordInputType": "{{string}}",
            "keywordValue": "{{string}}"
         },
         "sourceName": "{{string}}",
         "sourceSetUpOption": "{{string}}",
         "sourceType": "{{string}}",
         "troubleshootingText": "{{string}}"
      }
   ],
   "description": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "testingInformation": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateControl_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateControl_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actionPlanInstructions](#API_CreateControl_RequestSyntax) **   <a name="auditmanager-CreateControl-request-actionPlanInstructions"></a>
 The recommended actions to carry out if the control isn't fulfilled.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** [actionPlanTitle](#API_CreateControl_RequestSyntax) **   <a name="auditmanager-CreateControl-request-actionPlanTitle"></a>
 The title of the action plan for remediating the control.
Type: String
Length Constraints: Maximum length of 300.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** [controlMappingSources](#API_CreateControl_RequestSyntax) **   <a name="auditmanager-CreateControl-request-controlMappingSources"></a>
 The data mapping sources for the control.
Type: Array of [CreateControlMappingSource](API_CreateControlMappingSource.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [description](#API_CreateControl_RequestSyntax) **   <a name="auditmanager-CreateControl-request-description"></a>
 The description of the control.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** [name](#API_CreateControl_RequestSyntax) **   <a name="auditmanager-CreateControl-request-name"></a>
 The name of the control.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\]*$`
Required: Yes

 ** [tags](#API_CreateControl_RequestSyntax) **   <a name="auditmanager-CreateControl-request-tags"></a>
 The tags that are associated with the control.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.{0,255}`
Required: No

 ** [testingInformation](#API_CreateControl_RequestSyntax) **   <a name="auditmanager-CreateControl-request-testingInformation"></a>
 The steps to follow to determine if the control is satisfied.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^[\w\W\s\S]*$`
Required: No

## Response Syntax
<a name="API_CreateControl_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "control": {
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
}
```

## Response Elements
<a name="API_CreateControl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [control](#API_CreateControl_ResponseSyntax) **   <a name="auditmanager-CreateControl-response-control"></a>
 The new control that the `CreateControl` API returned.
Type: [Control](API_Control.md) object

## Errors
<a name="API_CreateControl_Errors"></a>

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
<a name="API_CreateControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/CreateControl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/CreateControl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/CreateControl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/CreateControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/CreateControl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/CreateControl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/CreateControl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/CreateControl)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/CreateControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/CreateControl)
