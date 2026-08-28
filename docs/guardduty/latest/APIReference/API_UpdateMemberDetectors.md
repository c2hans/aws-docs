---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateMemberDetectors.html
---

# UpdateMemberDetectors
<a name="API_UpdateMemberDetectors"></a>

Contains information on member accounts to be updated.

Specifying both EKS Runtime Monitoring (`EKS_RUNTIME_MONITORING`) and Runtime Monitoring (`RUNTIME_MONITORING`) will cause an error. You can add only one of these two features because Runtime Monitoring already includes the threat detection for Amazon EKS resources. For more information, see [Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html).

There might be regional differences because some data sources might not be available in all the AWS Regions where GuardDuty is presently supported. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html).

## Request Syntax
<a name="API_UpdateMemberDetectors_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/member/detector/update HTTP/1.1
Content-type: application/json

{
   "accountIds": [ "{{string}}" ],
   "dataSources": {
      "kubernetes": {
         "auditLogs": {
            "enable": {{boolean}}
         }
      },
      "malwareProtection": {
         "scanEc2InstanceWithFindings": {
            "ebsVolumes": {{boolean}}
         }
      },
      "s3Logs": {
         "enable": {{boolean}}
      }
   },
   "features": [
      {
         "additionalConfiguration": [
            {
               "name": "{{string}}",
               "status": "{{string}}"
            }
         ],
         "name": "{{string}}",
         "status": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateMemberDetectors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_UpdateMemberDetectors_RequestSyntax) **   <a name="guardduty-UpdateMemberDetectors-request-uri-DetectorId"></a>
The detector ID of the administrator account.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_UpdateMemberDetectors_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountIds](#API_UpdateMemberDetectors_RequestSyntax) **   <a name="guardduty-UpdateMemberDetectors-request-accountIds"></a>
A list of member account IDs to be updated.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Fixed length of 12.
Required: Yes

 ** [dataSources](#API_UpdateMemberDetectors_RequestSyntax) **   <a name="guardduty-UpdateMemberDetectors-request-dataSources"></a>
 *This parameter has been deprecated.*
Describes which data sources will be updated.
Type: [DataSourceConfigurations](API_DataSourceConfigurations.md) object
Required: No

 ** [features](#API_UpdateMemberDetectors_RequestSyntax) **   <a name="guardduty-UpdateMemberDetectors-request-features"></a>
A list of features that will be updated for the specified member accounts.
Type: Array of [MemberFeaturesConfiguration](API_MemberFeaturesConfiguration.md) objects
Required: No

## Response Syntax
<a name="API_UpdateMemberDetectors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "unprocessedAccounts": [
      {
         "accountId": "string",
         "result": "string"
      }
   ]
}
```

## Response Elements
<a name="API_UpdateMemberDetectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [unprocessedAccounts](#API_UpdateMemberDetectors_ResponseSyntax) **   <a name="guardduty-UpdateMemberDetectors-response-unprocessedAccounts"></a>
A list of member account IDs that were unable to be processed along with an explanation for why they were not processed.
Type: Array of [UnprocessedAccount](API_UnprocessedAccount.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_UpdateMemberDetectors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
A bad request exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 500

## See Also
<a name="API_UpdateMemberDetectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/UpdateMemberDetectors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/UpdateMemberDetectors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/UpdateMemberDetectors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/UpdateMemberDetectors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/UpdateMemberDetectors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/UpdateMemberDetectors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/UpdateMemberDetectors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/UpdateMemberDetectors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/UpdateMemberDetectors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/UpdateMemberDetectors)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
