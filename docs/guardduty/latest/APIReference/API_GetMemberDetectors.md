---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetMemberDetectors.html
---

# GetMemberDetectors
<a name="API_GetMemberDetectors"></a>

Describes which data sources are enabled for the member account's detector.

There might be regional differences because some data sources might not be available in all the AWS Regions where GuardDuty is presently supported. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html).

## Request Syntax
<a name="API_GetMemberDetectors_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/member/detector/get HTTP/1.1
Content-type: application/json

{
   "accountIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_GetMemberDetectors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_GetMemberDetectors_RequestSyntax) **   <a name="guardduty-GetMemberDetectors-request-uri-DetectorId"></a>
The detector ID for the administrator account.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_GetMemberDetectors_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountIds](#API_GetMemberDetectors_RequestSyntax) **   <a name="guardduty-GetMemberDetectors-request-accountIds"></a>
A list of member account IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Fixed length of 12.
Required: Yes

## Response Syntax
<a name="API_GetMemberDetectors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "members": [
      {
         "accountId": "string",
         "dataSources": {
            "cloudTrail": {
               "status": "string"
            },
            "dnsLogs": {
               "status": "string"
            },
            "flowLogs": {
               "status": "string"
            },
            "kubernetes": {
               "auditLogs": {
                  "status": "string"
               }
            },
            "malwareProtection": {
               "scanEc2InstanceWithFindings": {
                  "ebsVolumes": {
                     "reason": "string",
                     "status": "string"
                  }
               },
               "serviceRole": "string"
            },
            "s3Logs": {
               "status": "string"
            }
         },
         "features": [
            {
               "additionalConfiguration": [
                  {
                     "managedBy": "string",
                     "name": "string",
                     "status": "string",
                     "updatedAt": number
                  }
               ],
               "managedBy": "string",
               "name": "string",
               "status": "string",
               "updatedAt": number
            }
         ]
      }
   ],
   "unprocessedAccounts": [
      {
         "accountId": "string",
         "result": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetMemberDetectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [members](#API_GetMemberDetectors_ResponseSyntax) **   <a name="guardduty-GetMemberDetectors-response-members"></a>
An object that describes which data sources are enabled for a member account.
Type: Array of [MemberDataSourceConfiguration](API_MemberDataSourceConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.

 ** [unprocessedAccounts](#API_GetMemberDetectors_ResponseSyntax) **   <a name="guardduty-GetMemberDetectors-response-unprocessedAccounts"></a>
A list of member account IDs that were unable to be processed along with an explanation for why they were not processed.
Type: Array of [UnprocessedAccount](API_UnprocessedAccount.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_GetMemberDetectors_Errors"></a>

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
<a name="API_GetMemberDetectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/GetMemberDetectors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/GetMemberDetectors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/GetMemberDetectors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/GetMemberDetectors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/GetMemberDetectors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/GetMemberDetectors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/GetMemberDetectors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/GetMemberDetectors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/GetMemberDetectors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/GetMemberDetectors)
