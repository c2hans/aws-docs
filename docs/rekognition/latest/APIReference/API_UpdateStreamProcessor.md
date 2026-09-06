---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_UpdateStreamProcessor.html
---

# UpdateStreamProcessor
<a name="API_UpdateStreamProcessor"></a>

**Important**
Service availability notice: Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see [Rekognition feature availability changes](https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-availability-changes.html).
 **This change does not impact the availability of other Amazon Rekognition features.**

 Allows you to update a stream processor. You can change some settings and regions of interest and delete certain parameters.

## Request Syntax
<a name="API_UpdateStreamProcessor_RequestSyntax"></a>

```
{
   "DataSharingPreferenceForUpdate": {
      "OptIn": {{boolean}}
   },
   "Name": "{{string}}",
   "ParametersToDelete": [ "{{string}}" ],
   "RegionsOfInterestForUpdate": [
      {
         "BoundingBox": {
            "Height": {{number}},
            "Left": {{number}},
            "Top": {{number}},
            "Width": {{number}}
         },
         "Polygon": [
            {
               "X": {{number}},
               "Y": {{number}}
            }
         ]
      }
   ],
   "SettingsForUpdate": {
      "ConnectedHomeForUpdate": {
         "Labels": [ "{{string}}" ],
         "MinConfidence": {{number}}
      }
   }
}
```

## Request Parameters
<a name="API_UpdateStreamProcessor_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataSharingPreferenceForUpdate](#API_UpdateStreamProcessor_RequestSyntax) **   <a name="rekognition-UpdateStreamProcessor-request-DataSharingPreferenceForUpdate"></a>
 Shows whether you are sharing data with Rekognition to improve model performance. You can choose this option at the account level or on a per-stream basis. Note that if you opt out at the account level this setting is ignored on individual streams.
Type: [StreamProcessorDataSharingPreference](API_StreamProcessorDataSharingPreference.md) object
Required: No

 ** [Name](#API_UpdateStreamProcessor_RequestSyntax) **   <a name="rekognition-UpdateStreamProcessor-request-Name"></a>
 Name of the stream processor that you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: Yes

 ** [ParametersToDelete](#API_UpdateStreamProcessor_RequestSyntax) **   <a name="rekognition-UpdateStreamProcessor-request-ParametersToDelete"></a>
 A list of parameters you want to delete from the stream processor.
Type: Array of strings
Valid Values: `ConnectedHomeMinConfidence | RegionsOfInterest`
Required: No

 ** [RegionsOfInterestForUpdate](#API_UpdateStreamProcessor_RequestSyntax) **   <a name="rekognition-UpdateStreamProcessor-request-RegionsOfInterestForUpdate"></a>
 Specifies locations in the frames where Amazon Rekognition checks for objects or people. This is an optional parameter for label detection stream processors.
Type: Array of [RegionOfInterest](API_RegionOfInterest.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [SettingsForUpdate](#API_UpdateStreamProcessor_RequestSyntax) **   <a name="rekognition-UpdateStreamProcessor-request-SettingsForUpdate"></a>
 The stream processor settings that you want to update. Label detection settings can be updated to detect different labels with a different minimum confidence.
Type: [StreamProcessorSettingsForUpdate](API_StreamProcessorSettingsForUpdate.md) object
Required: No

## Response Elements
<a name="API_UpdateStreamProcessor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateStreamProcessor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Rekognition experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
Input parameter violated a constraint. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.
HTTP Status Code: 400

 ** ResourceInUseException **
The specified resource is already being used.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource specified in the request cannot be found.
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_UpdateStreamProcessor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/UpdateStreamProcessor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/UpdateStreamProcessor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/UpdateStreamProcessor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/UpdateStreamProcessor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/UpdateStreamProcessor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/UpdateStreamProcessor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/UpdateStreamProcessor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/UpdateStreamProcessor)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/UpdateStreamProcessor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/UpdateStreamProcessor)
