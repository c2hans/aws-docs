---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ReserveContact.html
---

# ReserveContact
<a name="API_ReserveContact"></a>

Reserves a contact using specified parameters.

## Request Syntax
<a name="API_ReserveContact_RequestSyntax"></a>

```
POST /contact HTTP/1.1
Content-type: application/json

{
   "endTime": {{number}},
   "groundStation": "{{string}}",
   "missionProfileArn": "{{string}}",
   "satelliteArn": "{{string}}",
   "startTime": {{number}},
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "trackingOverrides": {
      "programTrackSettings": { ... }
   }
}
```

## URI Request Parameters
<a name="API_ReserveContact_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ReserveContact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [endTime](#API_ReserveContact_RequestSyntax) **   <a name="groundstation-ReserveContact-request-endTime"></a>
End time of a contact in UTC.
Type: Timestamp
Required: Yes

 ** [groundStation](#API_ReserveContact_RequestSyntax) **   <a name="groundstation-ReserveContact-request-groundStation"></a>
Name of a ground station.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 97.
Pattern: `[ a-zA-Z0-9-._:=]{4,97}`
Required: Yes

 ** [missionProfileArn](#API_ReserveContact_RequestSyntax) **   <a name="groundstation-ReserveContact-request-missionProfileArn"></a>
ARN of a mission profile.
Type: String
Length Constraints: Minimum length of 89. Maximum length of 138.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:mission-profile/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [satelliteArn](#API_ReserveContact_RequestSyntax) **   <a name="groundstation-ReserveContact-request-satelliteArn"></a>
ARN of a satellite
Type: String
Length Constraints: Minimum length of 82. Maximum length of 132.
Pattern: `arn:aws:groundstation:([-a-z0-9]{1,50})?:[0-9]{12}:satellite/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [startTime](#API_ReserveContact_RequestSyntax) **   <a name="groundstation-ReserveContact-request-startTime"></a>
Start time of a contact in UTC.
Type: Timestamp
Required: Yes

 ** [tags](#API_ReserveContact_RequestSyntax) **   <a name="groundstation-ReserveContact-request-tags"></a>
Tags assigned to a contact.
Type: String to string map
Required: No

 ** [trackingOverrides](#API_ReserveContact_RequestSyntax) **   <a name="groundstation-ReserveContact-request-trackingOverrides"></a>
Tracking configuration overrides for the contact.
Type: [TrackingOverrides](API_TrackingOverrides.md) object
Required: No

## Response Syntax
<a name="API_ReserveContact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "contactId": "string",
   "versionId": number
}
```

## Response Elements
<a name="API_ReserveContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [contactId](#API_ReserveContact_ResponseSyntax) **   <a name="groundstation-ReserveContact-response-contactId"></a>
UUID of a contact.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [versionId](#API_ReserveContact_ResponseSyntax) **   <a name="groundstation-ReserveContact-response-versionId"></a>
Version ID of a contact.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 128.

## Errors
<a name="API_ReserveContact_Errors"></a>

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

 ** ResourceLimitExceededException **
Account limits for this resource have been exceeded.
 ** parameterName **
Name of the parameter that exceeded the resource limit.
HTTP Status Code: 429

 ** ResourceNotFoundException **
Resource was not found.
HTTP Status Code: 434

## See Also
<a name="API_ReserveContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/ReserveContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/ReserveContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/ReserveContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/ReserveContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/ReserveContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/ReserveContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/ReserveContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/ReserveContact)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/ReserveContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/ReserveContact)
