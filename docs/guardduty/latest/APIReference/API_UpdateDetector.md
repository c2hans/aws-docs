---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateDetector.html
---

# UpdateDetector
<a name="API_UpdateDetector"></a>

Updates the GuardDuty detector specified by the detector ID.

Specifying both EKS Runtime Monitoring (`EKS_RUNTIME_MONITORING`) and Runtime Monitoring (`RUNTIME_MONITORING`) will cause an error. You can add only one of these two features because Runtime Monitoring already includes the threat detection for Amazon EKS resources. For more information, see [Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html).

There might be regional differences because some data sources might not be available in all the AWS Regions where GuardDuty is presently supported. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html).

## Request Syntax
<a name="API_UpdateDetector_RequestSyntax"></a>

```
POST /detector/{{DetectorId}} HTTP/1.1
Content-type: application/json

{
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
   "enable": {{boolean}},
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
   ],
   "findingPublishingFrequency": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDetector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_UpdateDetector_RequestSyntax) **   <a name="guardduty-UpdateDetector-request-uri-DetectorId"></a>
The unique ID of the detector to update.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_UpdateDetector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [dataSources](#API_UpdateDetector_RequestSyntax) **   <a name="guardduty-UpdateDetector-request-dataSources"></a>
 *This parameter has been deprecated.*
Describes which data sources will be updated.
There might be regional differences because some data sources might not be available in all the AWS Regions where GuardDuty is presently supported. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html).
Type: [DataSourceConfigurations](API_DataSourceConfigurations.md) object
Required: No

 ** [enable](#API_UpdateDetector_RequestSyntax) **   <a name="guardduty-UpdateDetector-request-enable"></a>
Specifies whether the detector is enabled or not enabled.
Type: Boolean
Required: No

 ** [features](#API_UpdateDetector_RequestSyntax) **   <a name="guardduty-UpdateDetector-request-features"></a>
Provides the features that will be updated for the detector.
Type: Array of [DetectorFeatureConfiguration](API_DetectorFeatureConfiguration.md) objects
Required: No

 ** [findingPublishingFrequency](#API_UpdateDetector_RequestSyntax) **   <a name="guardduty-UpdateDetector-request-findingPublishingFrequency"></a>
An enum value that specifies how frequently findings are exported, such as to CloudWatch Events.
Type: String
Valid Values: `FIFTEEN_MINUTES | ONE_HOUR | SIX_HOURS`
Required: No

## Response Syntax
<a name="API_UpdateDetector_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateDetector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateDetector_Errors"></a>

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
<a name="API_UpdateDetector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/UpdateDetector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/UpdateDetector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/UpdateDetector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/UpdateDetector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/UpdateDetector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/UpdateDetector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/UpdateDetector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/UpdateDetector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/UpdateDetector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/UpdateDetector)
