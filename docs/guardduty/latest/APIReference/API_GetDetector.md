---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetDetector.html
---

# GetDetector
<a name="API_GetDetector"></a>

Retrieves a GuardDuty detector specified by the detectorId.

There might be regional differences because some data sources might not be available in all the AWS Regions where GuardDuty is presently supported. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html).

## Request Syntax
<a name="API_GetDetector_RequestSyntax"></a>

```
GET /detector/{{DetectorId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDetector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_GetDetector_RequestSyntax) **   <a name="guardduty-GetDetector-request-uri-DetectorId"></a>
The unique ID of the detector that you want to get.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_GetDetector_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDetector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
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
   ],
   "findingPublishingFrequency": "string",
   "serviceRole": "string",
   "status": "string",
   "tags": {
      "string" : "string"
   },
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_GetDetector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetDetector_ResponseSyntax) **   <a name="guardduty-GetDetector-response-createdAt"></a>
The timestamp of when the detector was created.
Type: String

 ** [dataSources](#API_GetDetector_ResponseSyntax) **   <a name="guardduty-GetDetector-response-dataSources"></a>
 *This parameter has been deprecated.*
Describes which data sources are enabled for the detector.
Type: [DataSourceConfigurationsResult](API_DataSourceConfigurationsResult.md) object

 ** [features](#API_GetDetector_ResponseSyntax) **   <a name="guardduty-GetDetector-response-features"></a>
Describes the features that have been enabled for the detector.
Type: Array of [DetectorFeatureConfigurationResult](API_DetectorFeatureConfigurationResult.md) objects

 ** [findingPublishingFrequency](#API_GetDetector_ResponseSyntax) **   <a name="guardduty-GetDetector-response-findingPublishingFrequency"></a>
The publishing frequency of the finding.
Type: String
Valid Values: `FIFTEEN_MINUTES | ONE_HOUR | SIX_HOURS`

 ** [serviceRole](#API_GetDetector_ResponseSyntax) **   <a name="guardduty-GetDetector-response-serviceRole"></a>
The GuardDuty service role.
Type: String

 ** [status](#API_GetDetector_ResponseSyntax) **   <a name="guardduty-GetDetector-response-status"></a>
The detector status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `ENABLED | DISABLED`

 ** [tags](#API_GetDetector_ResponseSyntax) **   <a name="guardduty-GetDetector-response-tags"></a>
The tags of the detector resource.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [updatedAt](#API_GetDetector_ResponseSyntax) **   <a name="guardduty-GetDetector-response-updatedAt"></a>
The last-updated timestamp for the detector.
Type: String

## Errors
<a name="API_GetDetector_Errors"></a>

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
<a name="API_GetDetector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/GetDetector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/GetDetector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/GetDetector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/GetDetector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/GetDetector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/GetDetector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/GetDetector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/GetDetector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/GetDetector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/GetDetector)
