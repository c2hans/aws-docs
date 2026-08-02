---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeContact.html
---

# DescribeContact
<a name="API_DescribeContact"></a>

Describes an existing contact.

## Request Syntax
<a name="API_DescribeContact_RequestSyntax"></a>

```
GET /contact/{{contactId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeContact_RequestParameters"></a>

The request uses the following URI parameters.

 ** [contactId](#API_DescribeContact_RequestSyntax) **   <a name="groundstation-DescribeContact-request-uri-contactId"></a>
UUID of a contact.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_DescribeContact_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeContact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "contactId": "string",
   "contactStatus": "string",
   "dataflowList": [
      {
         "destination": {
            "configDetails": { ... },
            "configId": "string",
            "configType": "string",
            "dataflowDestinationRegion": "string"
         },
         "errorMessage": "string",
         "source": {
            "configDetails": { ... },
            "configId": "string",
            "configType": "string",
            "dataflowSourceRegion": "string"
         }
      }
   ],
   "endTime": number,
   "ephemeris": {
      "ephemerisId": "string",
      "ephemerisType": "string"
   },
   "errorMessage": "string",
   "groundStation": "string",
   "maximumElevation": {
      "unit": "string",
      "value": number
   },
   "missionProfileArn": "string",
   "postPassEndTime": number,
   "prePassStartTime": number,
   "region": "string",
   "satelliteArn": "string",
   "startTime": number,
   "tags": {
      "string" : "string"
   },
   "trackingOverrides": {
      "programTrackSettings": { ... }
   },
   "version": {
      "activated": number,
      "created": number,
      "failureCodes": [ "string" ],
      "failureMessage": "string",
      "lastUpdated": number,
      "status": "string",
      "superseded": number,
      "versionId": number
   },
   "visibilityEndTime": number,
   "visibilityStartTime": number
}
```

## Response Elements
<a name="API_DescribeContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [contactId](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-contactId"></a>
UUID of a contact.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [contactStatus](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-contactStatus"></a>
Status of a contact.
Type: String
Valid Values: `SCHEDULING | FAILED_TO_SCHEDULE | SCHEDULED | CANCELLED | AWS_CANCELLED | PREPASS | PASS | POSTPASS | COMPLETED | FAILED | AVAILABLE | CANCELLING | AWS_FAILED`

 ** [dataflowList](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-dataflowList"></a>
List describing source and destination details for each dataflow edge.
Type: Array of [DataflowDetail](API_DataflowDetail.md) objects

 ** [endTime](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-endTime"></a>
End time of a contact in UTC.
Type: Timestamp

 ** [ephemeris](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-ephemeris"></a>
The ephemeris that determines antenna pointing directions for the contact.
Type: [EphemerisResponseData](API_EphemerisResponseData.md) object

 ** [errorMessage](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-errorMessage"></a>
Error message for a contact.
Type: String

 ** [groundStation](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-groundStation"></a>
Ground station for a contact.
Type: String

 ** [maximumElevation](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-maximumElevation"></a>
Maximum elevation angle of a contact.
Type: [Elevation](API_Elevation.md) object

 ** [missionProfileArn](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-missionProfileArn"></a>
ARN of a mission profile.
Type: String
Length Constraints: Minimum length of 89. Maximum length of 138.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:mission-profile/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [postPassEndTime](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-postPassEndTime"></a>
End time in UTC of the post-pass period, at which you receive a CloudWatch event indicating the pass has finished.
Type: Timestamp

 ** [prePassStartTime](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-prePassStartTime"></a>
Start time in UTC of the pre-pass period, at which you receive a CloudWatch event indicating an upcoming pass.
Type: Timestamp

 ** [region](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-region"></a>
Region where the `ReserveContact` API was called to schedule this contact.
Type: String

 ** [satelliteArn](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-satelliteArn"></a>
ARN of a satellite.
Type: String
Length Constraints: Minimum length of 82. Maximum length of 132.
Pattern: `arn:aws:groundstation:([-a-z0-9]{1,50})?:[0-9]{12}:satellite/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [startTime](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-startTime"></a>
Start time of a contact in UTC.
Type: Timestamp

 ** [tags](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-tags"></a>
Tags assigned to a contact.
Type: String to string map

 ** [trackingOverrides](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-trackingOverrides"></a>
Tracking configuration overrides specified when the contact was reserved.
Type: [TrackingOverrides](API_TrackingOverrides.md) object

 ** [version](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-version"></a>
Version information for a contact.
Type: [ContactVersion](API_ContactVersion.md) object

 ** [visibilityEndTime](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-visibilityEndTime"></a>
 Projected time in UTC your satellite will set below the [receive mask](https://docs.aws.amazon.com/ground-station/latest/ug/site-masks.html). This time is based on the satellite's current active ephemeris for future contacts and the ephemeris that was active during contact execution for completed contacts.
Type: Timestamp

 ** [visibilityStartTime](#API_DescribeContact_ResponseSyntax) **   <a name="groundstation-DescribeContact-response-visibilityStartTime"></a>
 Projected time in UTC your satellite will rise above the [receive mask](https://docs.aws.amazon.com/ground-station/latest/ug/site-masks.html). This time is based on the satellite's current active ephemeris for future contacts and the ephemeris that was active during contact execution for completed contacts.
Type: Timestamp

## Errors
<a name="API_DescribeContact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyException **
Dependency encountered an error.
 ** parameterName **
Name of the parameter that caused the exception.
HTTP Status Code: 531

 ** InvalidParameterException **
One or more parameters are not valid.
 ** parameterName **
Name of the invalid parameter.
HTTP Status Code: 431

 ** ResourceNotFoundException **
Resource was not found.
HTTP Status Code: 434

## See Also
<a name="API_DescribeContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/DescribeContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/DescribeContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/DescribeContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/DescribeContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/DescribeContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/DescribeContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/DescribeContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/DescribeContact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/DescribeContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/DescribeContact)
