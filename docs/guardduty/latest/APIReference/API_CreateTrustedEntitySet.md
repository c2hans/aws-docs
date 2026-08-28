---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateTrustedEntitySet.html
---

# CreateTrustedEntitySet
<a name="API_CreateTrustedEntitySet"></a>

Creates a new trusted entity set. In the trusted entity set, you can provide IP addresses and domains that you believe are secure for communication in your AWS environment. GuardDuty will not generate findings for the entries that are specified in a trusted entity set. At any given time, you can have only one trusted entity set.

Only users of the administrator account can manage the entity sets, which automatically apply to member accounts.

## Request Syntax
<a name="API_CreateTrustedEntitySet_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/trustedentityset HTTP/1.1
Content-type: application/json

{
   "activate": {{boolean}},
   "clientToken": "{{string}}",
   "expectedBucketOwner": "{{string}}",
   "format": "{{string}}",
   "location": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateTrustedEntitySet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_CreateTrustedEntitySet_RequestSyntax) **   <a name="guardduty-CreateTrustedEntitySet-request-uri-DetectorId"></a>
The unique ID of the detector of the GuardDuty account for which you want to create a trusted entity set.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_CreateTrustedEntitySet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [activate](#API_CreateTrustedEntitySet_RequestSyntax) **   <a name="guardduty-CreateTrustedEntitySet-request-activate"></a>
A boolean value that indicates whether GuardDuty is to start using the uploaded trusted entity set.
Type: Boolean
Required: Yes

 ** [clientToken](#API_CreateTrustedEntitySet_RequestSyntax) **   <a name="guardduty-CreateTrustedEntitySet-request-clientToken"></a>
The idempotency token for the create request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [expectedBucketOwner](#API_CreateTrustedEntitySet_RequestSyntax) **   <a name="guardduty-CreateTrustedEntitySet-request-expectedBucketOwner"></a>
The AWS account ID that owns the Amazon S3 bucket specified in the **location** parameter.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: No

 ** [format](#API_CreateTrustedEntitySet_RequestSyntax) **   <a name="guardduty-CreateTrustedEntitySet-request-format"></a>
The format of the file that contains the trusted entity set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `TXT | STIX | OTX_CSV | ALIEN_VAULT | PROOF_POINT | FIRE_EYE`
Required: Yes

 ** [location](#API_CreateTrustedEntitySet_RequestSyntax) **   <a name="guardduty-CreateTrustedEntitySet-request-location"></a>
The URI of the file that contains the threat entity set. The format of the `Location` URL must be a valid Amazon S3 URL format. Invalid URL formats will result in an error, regardless of whether you activate the entity set or not. For more information about format of the location URLs, see [Format of location URL under Step 2: Adding trusted or threat intelligence data](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-lists-create-activate.html) in the *Amazon GuardDuty User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [name](#API_CreateTrustedEntitySet_RequestSyntax) **   <a name="guardduty-CreateTrustedEntitySet-request-name"></a>
A user-friendly name to identify the trusted entity set.
The name of your list can include lowercase letters, uppercase letters, numbers, dash (-), and underscore (\_).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [tags](#API_CreateTrustedEntitySet_RequestSyntax) **   <a name="guardduty-CreateTrustedEntitySet-request-tags"></a>
The tags to be added to a new trusted entity set resource.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateTrustedEntitySet_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "trustedEntitySetId": "string"
}
```

## Response Elements
<a name="API_CreateTrustedEntitySet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [trustedEntitySetId](#API_CreateTrustedEntitySet_ResponseSyntax) **   <a name="guardduty-CreateTrustedEntitySet-response-trustedEntitySetId"></a>
The ID returned by GuardDuty after creation of the trusted entity set resource.
Type: String

## Errors
<a name="API_CreateTrustedEntitySet_Errors"></a>

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
<a name="API_CreateTrustedEntitySet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/CreateTrustedEntitySet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/CreateTrustedEntitySet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CreateTrustedEntitySet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/CreateTrustedEntitySet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CreateTrustedEntitySet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/CreateTrustedEntitySet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/CreateTrustedEntitySet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/CreateTrustedEntitySet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/CreateTrustedEntitySet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CreateTrustedEntitySet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
