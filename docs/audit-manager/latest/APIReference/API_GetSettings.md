---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetSettings.html
---

# GetSettings
<a name="API_GetSettings"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Gets the settings for a specified AWS account.

## Request Syntax
<a name="API_GetSettings_RequestSyntax"></a>

```
GET /settings/{{attribute}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSettings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [attribute](#API_GetSettings_RequestSyntax) **   <a name="auditmanager-GetSettings-request-uri-attribute"></a>
 The list of setting attribute enum values.
Valid Values: `ALL | IS_AWS_ORG_ENABLED | SNS_TOPIC | DEFAULT_ASSESSMENT_REPORTS_DESTINATION | DEFAULT_PROCESS_OWNERS | EVIDENCE_FINDER_ENABLEMENT | DEREGISTRATION_POLICY | DEFAULT_EXPORT_DESTINATION`
Required: Yes

## Request Body
<a name="API_GetSettings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSettings_ResponseSyntax"></a>

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
<a name="API_GetSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [settings](#API_GetSettings_ResponseSyntax) **   <a name="auditmanager-GetSettings-response-settings"></a>
 The settings object that holds all supported Audit Manager settings.
Type: [Settings](API_Settings.md) object

## Errors
<a name="API_GetSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 Your account isn't registered with AWS Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again.
HTTP Status Code: 403

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

## Examples
<a name="API_GetSettings_Examples"></a>

### Confirming the status of evidence finder
<a name="API_GetSettings_Example_1"></a>

This is an example response for the `GetSettings` API operation, where the `attribute` parameter is set to `EVIDENCE_FINDER_ENABLEMENT`.

This response returns the following evidence finder settings:
+  `eventDataStoreArn` shows the ARN of the event data store that was created when evidence finder was enabled.
+  `enablementStatus` shows the current status of evidence finder. In this case, `ENABLED` indicates that evidence finder was successfully enabled.
+  `backfillStatus` shows the current status of the evidence data backfill. In this case, `IN_PROGRESS` indicates that the backfill is not yet complete.

#### Sample Response
<a name="API_GetSettings_Example_1_Response"></a>

```
{
    "settings": {
        "evidenceFinderEnablement": {
            "eventDataStoreArn": "arn:aws:cloudtrail:us-east-1:111122223333:eventdatastore/1q2w3e4r-2w3e-4r5t-6y7u-1q2w3e4r5t6y",
            "enablementStatus": "ENABLED",
            "backfillStatus": "IN_PROGRESS"
        }
    }
}
```

### Reviewing your data retention settings
<a name="API_GetSettings_Example_2"></a>

This is an example response for the `GetSettings` API operation, where the `attribute` parameter is set to `DEREGISTRATION_POLICY`.

This response returns your current data retention preferences. In this case, `deleteResources` has a value of `DEFAULT`. This indicates that your Audit Manager data is subject to default data retention policies. For more information about data retention, see [Data Protection](https://docs.aws.amazon.com/audit-manager/latest/userguide/data-protection.html) in the * AWS Audit Manager User Guide.*

#### Sample Response
<a name="API_GetSettings_Example_2_Response"></a>

```
{
    "settings": {
        "deregistrationPolicy": {
            "deleteResources": "DEFAULT"
        }
    }
}
```

### Reviewing your Audit Manager notification settings
<a name="API_GetSettings_Example_3"></a>

This is an example response for the `GetSettings` API operation, where the `attribute` parameter is set to `SNS_TOPIC`.

If an SNS topic is in use, the response returns the ARN for that topic.

#### Sample Response
<a name="API_GetSettings_Example_3_Response"></a>

```
{
    "settings": {
        "snsTopic": "arn:aws:sns:us-east-1:111122223333:my-assessment-topic"
    }
}
```

### Reviewing the default audit owners for your Audit Manager assessments
<a name="API_GetSettings_Example_4"></a>

This is an example response for the `GetSettings` API operation, where the `attribute` parameter is set to `DEFAULT_PROCESS_OWNERS`.

If one or more default audit owners were specified, the response returns the ARN for each audit owner's role.

#### Sample Response
<a name="API_GetSettings_Example_4_Response"></a>

```
{
    "settings": {
        "defaultProcessOwners": [
            {
                "roleType": "PROCESS_OWNER",
                "roleArn": "arn:aws:iam::111122223333:role/Administrator"
            }
        ]
    }
}
```

## See Also
<a name="API_GetSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/GetSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/GetSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/GetSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/GetSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/GetSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/GetSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/GetSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/GetSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/GetSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/GetSettings)
