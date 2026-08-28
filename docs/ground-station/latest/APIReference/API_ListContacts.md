---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListContacts.html
---

# ListContacts
<a name="API_ListContacts"></a>

Returns a list of contacts.

If `statusList` contains AVAILABLE, the request must include ` groundStation`, `missionprofileArn`, and `satelliteArn`.

## Request Syntax
<a name="API_ListContacts_RequestSyntax"></a>

```
POST /contacts HTTP/1.1
Content-type: application/json

{
   "endTime": {{number}},
   "ephemeris": { ... },
   "groundStation": "{{string}}",
   "maxResults": {{number}},
   "missionProfileArn": "{{string}}",
   "nextToken": "{{string}}",
   "satelliteArn": "{{string}}",
   "startTime": {{number}},
   "statusList": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_ListContacts_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListContacts_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [endTime](#API_ListContacts_RequestSyntax) **   <a name="groundstation-ListContacts-request-endTime"></a>
End time of a contact in UTC.
Type: Timestamp
Required: Yes

 ** [ephemeris](#API_ListContacts_RequestSyntax) **   <a name="groundstation-ListContacts-request-ephemeris"></a>
Filter for selecting contacts that use a specific ephemeris".
Type: [EphemerisFilter](API_EphemerisFilter.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [groundStation](#API_ListContacts_RequestSyntax) **   <a name="groundstation-ListContacts-request-groundStation"></a>
Name of a ground station.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 97.
Pattern: `[ a-zA-Z0-9-._:=]{4,97}`
Required: No

 ** [maxResults](#API_ListContacts_RequestSyntax) **   <a name="groundstation-ListContacts-request-maxResults"></a>
Maximum number of contacts returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [missionProfileArn](#API_ListContacts_RequestSyntax) **   <a name="groundstation-ListContacts-request-missionProfileArn"></a>
ARN of a mission profile.
Type: String
Length Constraints: Minimum length of 89. Maximum length of 138.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:mission-profile/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [nextToken](#API_ListContacts_RequestSyntax) **   <a name="groundstation-ListContacts-request-nextToken"></a>
Next token returned in the request of a previous `ListContacts` call. Used to get the next page of results.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 1000.
Pattern: `[A-Za-z0-9-/+_.=]+`
Required: No

 ** [satelliteArn](#API_ListContacts_RequestSyntax) **   <a name="groundstation-ListContacts-request-satelliteArn"></a>
ARN of a satellite.
Type: String
Length Constraints: Minimum length of 82. Maximum length of 132.
Pattern: `arn:aws:groundstation:([-a-z0-9]{1,50})?:[0-9]{12}:satellite/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [startTime](#API_ListContacts_RequestSyntax) **   <a name="groundstation-ListContacts-request-startTime"></a>
Start time of a contact in UTC.
Type: Timestamp
Required: Yes

 ** [statusList](#API_ListContacts_RequestSyntax) **   <a name="groundstation-ListContacts-request-statusList"></a>
Status of a contact reservation.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Valid Values: `SCHEDULING | FAILED_TO_SCHEDULE | SCHEDULED | CANCELLED | AWS_CANCELLED | PREPASS | PASS | POSTPASS | COMPLETED | FAILED | AVAILABLE | CANCELLING | AWS_FAILED`
Required: Yes

## Response Syntax
<a name="API_ListContacts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "contactList": [
      {
         "contactId": "string",
         "contactStatus": "string",
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListContacts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [contactList](#API_ListContacts_ResponseSyntax) **   <a name="groundstation-ListContacts-response-contactList"></a>
List of contacts.
Type: Array of [ContactData](API_ContactData.md) objects

 ** [nextToken](#API_ListContacts_ResponseSyntax) **   <a name="groundstation-ListContacts-response-nextToken"></a>
Next token returned in the response of a previous `ListContacts` call. Used to get the next page of results.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 1000.
Pattern: `[A-Za-z0-9-/+_.=]+`

## Errors
<a name="API_ListContacts_Errors"></a>

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
<a name="API_ListContacts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/ListContacts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/ListContacts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/ListContacts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/ListContacts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/ListContacts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/ListContacts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/ListContacts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/ListContacts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/ListContacts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/ListContacts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
