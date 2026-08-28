---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateSettings.html
---

# UpdateSettings
<a name="API_UpdateSettings"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Updates Audit Manager settings for the current account.

## Request Syntax
<a name="API_UpdateSettings_RequestSyntax"></a>

```
PUT /settings HTTP/1.1
Content-type: application/json

{
   "defaultAssessmentReportsDestination": {
      "destination": "{{string}}",
      "destinationType": "{{string}}"
   },
   "defaultExportDestination": {
      "destination": "{{string}}",
      "destinationType": "{{string}}"
   },
   "defaultProcessOwners": [
      {
         "roleArn": "{{string}}",
         "roleType": "{{string}}"
      }
   ],
   "deregistrationPolicy": {
      "deleteResources": "{{string}}"
   },
   "evidenceFinderEnabled": {{boolean}},
   "kmsKey": "{{string}}",
   "snsTopic": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateSettings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateSettings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [defaultAssessmentReportsDestination](#API_UpdateSettings_RequestSyntax) **   <a name="auditmanager-UpdateSettings-request-defaultAssessmentReportsDestination"></a>
 The default S3 destination bucket for storing assessment reports.
Type: [AssessmentReportsDestination](API_AssessmentReportsDestination.md) object
Required: No

 ** [defaultExportDestination](#API_UpdateSettings_RequestSyntax) **   <a name="auditmanager-UpdateSettings-request-defaultExportDestination"></a>
 The default S3 destination bucket for storing evidence finder exports.
Type: [DefaultExportDestination](API_DefaultExportDestination.md) object
Required: No

 ** [defaultProcessOwners](#API_UpdateSettings_RequestSyntax) **   <a name="auditmanager-UpdateSettings-request-defaultProcessOwners"></a>
 A list of the default audit owners.
Type: Array of [Role](API_Role.md) objects
Required: No

 ** [deregistrationPolicy](#API_UpdateSettings_RequestSyntax) **   <a name="auditmanager-UpdateSettings-request-deregistrationPolicy"></a>
The deregistration policy for your Audit Manager data. You can use this attribute to determine how your data is handled when you deregister Audit Manager.
Type: [DeregistrationPolicy](API_DeregistrationPolicy.md) object
Required: No

 ** [evidenceFinderEnabled](#API_UpdateSettings_RequestSyntax) **   <a name="auditmanager-UpdateSettings-request-evidenceFinderEnabled"></a>
Specifies whether the evidence finder feature is enabled. Change this attribute to enable or disable evidence finder.
When you use this attribute to disable evidence finder, Audit Manager deletes the event data store that’s used to query your evidence data. As a result, you can’t re-enable evidence finder and use the feature again. Your only alternative is to [deregister](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeregisterAccount.html) and then [re-register](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_RegisterAccount.html) Audit Manager.
Type: Boolean
Required: No

 ** [kmsKey](#API_UpdateSettings_RequestSyntax) **   <a name="auditmanager-UpdateSettings-request-kmsKey"></a>
 The AWS KMS key details.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 2048.
Pattern: `^arn:.*:kms:.*|DEFAULT`
Required: No

 ** [snsTopic](#API_UpdateSettings_RequestSyntax) **   <a name="auditmanager-UpdateSettings-request-snsTopic"></a>
 The Amazon Simple Notification Service (Amazon SNS) topic that AWS Audit Manager sends notifications to.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 2048.
Pattern: `^arn:.*:sns:.*|NONE`
Required: No

## Response Syntax
<a name="API_UpdateSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "settings": {
      "defaultAssessmentReportsDestination": {
         "destination": "string",
         "destinationType": "string"
      },
      "defaultExportDestination": {
         "destination": "string",
         "destinationType": "string"
      },
      "defaultProcessOwners": [
         {
            "roleArn": "string",
            "roleType": "string"
         }
      ],
      "deregistrationPolicy": {
         "deleteResources": "string"
      },
      "evidenceFinderEnablement": {
         "backfillStatus": "string",
         "enablementStatus": "string",
         "error": "string",
         "eventDataStoreArn": "string"
      },
      "isAwsOrgEnabled": boolean,
      "kmsKey": "string",
      "snsTopic": "string"
   }
}
```

## Response Elements
<a name="API_UpdateSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [settings](#API_UpdateSettings_ResponseSyntax) **   <a name="auditmanager-UpdateSettings-response-settings"></a>
 The current list of settings.
Type: [Settings](API_Settings.md) object

## Errors
<a name="API_UpdateSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 Your account isn't registered with AWS Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again.
HTTP Status Code: 403

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ValidationException **
 The request has invalid or missing parameters.
 ** fields **
 The fields that caused the error, if applicable.
 ** reason **
 The reason the request failed validation.
HTTP Status Code: 400

## Examples
<a name="API_UpdateSettings_Examples"></a>

### Enabling evidence finder
<a name="API_UpdateSettings_Example_1"></a>

This is an example response for the `GetSettings` API operation, where the `evidenceFinderEnabled` parameter was used to enable evidence finder.

This response returns the following `evidenceFinderEnablement` data:
+  `enablementStatus` shows the current status of evidence finder. In this case, `ENABLE_IN_PROGRESS` indicates that you requested to enable evidence finder, and an event data store is being created to support evidence finder queries.
+  `backfillStatus` shows the current status of the evidence data backfill. In this case, `NOT_STARTED` indicates that the backfill hasn’t started yet.

#### Sample Response
<a name="API_UpdateSettings_Example_1_Response"></a>

```
{
    "settings": {
        "isAwsOrgEnabled": false,
        "snsTopic": "arn:aws:sns:us-east-1:111122223333:my-assessment-topic",
        "defaultAssessmentReportsDestination": {
            "destinationType": "S3",
            "destination": "s3://my-assessment-report-destination"
        },
        "defaultProcessOwners": [
            {
                "roleType": "PROCESS_OWNER",
                "roleArn": "arn:aws:iam::111122223333:role/Administrator"
            }
        ],
        "kmsKey": "DEFAULT",
        "evidenceFinderEnablement": {
            "enablementStatus": "ENABLE_IN_PROGRESS",
            "backfillStatus": "NOT_STARTED"
        }
    }
}
```

## See Also
<a name="API_UpdateSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/UpdateSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/UpdateSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/UpdateSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/UpdateSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/UpdateSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/UpdateSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/UpdateSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/UpdateSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/UpdateSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/UpdateSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
