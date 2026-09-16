---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateDetector.html
---

# CreateDetector
<a name="API_CreateDetector"></a>

Creates a single GuardDuty detector. A detector is a resource that represents the GuardDuty service. To start using GuardDuty, you must create a detector in each Region where you enable the service. You can have only one detector per account per Region. All data sources are enabled in a new detector by default.
+ When you don't specify any `features`, with an exception to `RUNTIME_MONITORING`, all the optional features are enabled by default.
+ When you specify some of the `features`, any feature that is not specified in the API call gets enabled by default, with an exception to `RUNTIME_MONITORING`.

Specifying both EKS Runtime Monitoring (`EKS_RUNTIME_MONITORING`) and Runtime Monitoring (`RUNTIME_MONITORING`) will cause an error. You can add only one of these two features because Runtime Monitoring already includes the threat detection for Amazon EKS resources. For more information, see [Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html).

There might be regional differences because some data sources might not be available in all the AWS Regions where GuardDuty is presently supported. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html).

## Request Syntax
<a name="API_CreateDetector_RequestSyntax"></a>

```
POST /detector HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
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
   "findingPublishingFrequency": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDetector_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDetector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateDetector_RequestSyntax) **   <a name="guardduty-CreateDetector-request-clientToken"></a>
The idempotency token for the create request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [dataSources](#API_CreateDetector_RequestSyntax) **   <a name="guardduty-CreateDetector-request-dataSources"></a>
 *This parameter has been deprecated.*
Describes which data sources will be enabled for the detector.
There might be regional differences because some data sources might not be available in all the AWS Regions where GuardDuty is presently supported. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html).
Type: [DataSourceConfigurations](API_DataSourceConfigurations.md) object
Required: No

 ** [enable](#API_CreateDetector_RequestSyntax) **   <a name="guardduty-CreateDetector-request-enable"></a>
A Boolean value that specifies whether the detector is to be enabled.
Type: Boolean
Required: Yes

 ** [features](#API_CreateDetector_RequestSyntax) **   <a name="guardduty-CreateDetector-request-features"></a>
A list of features that will be configured for the detector.
Type: Array of [DetectorFeatureConfiguration](API_DetectorFeatureConfiguration.md) objects
Required: No

 ** [findingPublishingFrequency](#API_CreateDetector_RequestSyntax) **   <a name="guardduty-CreateDetector-request-findingPublishingFrequency"></a>
A value that specifies how frequently updated findings are exported.
Type: String
Valid Values: `FIFTEEN_MINUTES | ONE_HOUR | SIX_HOURS`
Required: No

 ** [tags](#API_CreateDetector_RequestSyntax) **   <a name="guardduty-CreateDetector-request-tags"></a>
The tags to be added to a new detector resource.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateDetector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "detectorId": "string",
   "unprocessedDataSources": {
      "malwareProtection": {
         "scanEc2InstanceWithFindings": {
            "ebsVolumes": {
               "reason": "string",
               "status": "string"
            }
         },
         "serviceRole": "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateDetector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [detectorId](#API_CreateDetector_ResponseSyntax) **   <a name="guardduty-CreateDetector-response-detectorId"></a>
The unique ID of the created detector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [unprocessedDataSources](#API_CreateDetector_ResponseSyntax) **   <a name="guardduty-CreateDetector-response-unprocessedDataSources"></a>
Specifies the data sources that couldn't be enabled when GuardDuty was enabled for the first time.
Type: [UnprocessedDataSourcesResult](API_UnprocessedDataSourcesResult.md) object

## Errors
<a name="API_CreateDetector_Errors"></a>

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
<a name="API_CreateDetector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/CreateDetector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/CreateDetector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CreateDetector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/CreateDetector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CreateDetector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/CreateDetector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/CreateDetector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/CreateDetector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/CreateDetector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CreateDetector)
