---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListTargetsForSecurityProfile.html
---

# ListTargetsForSecurityProfile
<a name="API_ListTargetsForSecurityProfile"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

Lists the targets (thing groups) associated with a given Device Defender security profile.

Requires permission to access the [ListTargetsForSecurityProfile](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListTargetsForSecurityProfile_RequestSyntax"></a>

```
GET /security-profiles/{{securityProfileName}}/targets?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTargetsForSecurityProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListTargetsForSecurityProfile_RequestSyntax) **   <a name="iot-ListTargetsForSecurityProfile-request-uri-maxResults"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListTargetsForSecurityProfile_RequestSyntax) **   <a name="iot-ListTargetsForSecurityProfile-request-uri-nextToken"></a>
The token for the next set of results.

 ** [securityProfileName](#API_ListTargetsForSecurityProfile_RequestSyntax) **   <a name="iot-ListTargetsForSecurityProfile-request-uri-securityProfileName"></a>
The security profile.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_ListTargetsForSecurityProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTargetsForSecurityProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "securityProfileTargets": [
      {
         "arn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTargetsForSecurityProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTargetsForSecurityProfile_ResponseSyntax) **   <a name="iot-ListTargetsForSecurityProfile-response-nextToken"></a>
A token that can be used to retrieve the next set of results, or `null` if there are no additional results.
Type: String

 ** [securityProfileTargets](#API_ListTargetsForSecurityProfile_ResponseSyntax) **   <a name="iot-ListTargetsForSecurityProfile-response-securityProfileTargets"></a>
The thing groups to which the security profile is attached.
Type: Array of [SecurityProfileTarget](API_SecurityProfileTarget.md) objects

## Errors
<a name="API_ListTargetsForSecurityProfile_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListTargetsForSecurityProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListTargetsForSecurityProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListTargetsForSecurityProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListTargetsForSecurityProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListTargetsForSecurityProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListTargetsForSecurityProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListTargetsForSecurityProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListTargetsForSecurityProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListTargetsForSecurityProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListTargetsForSecurityProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListTargetsForSecurityProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
