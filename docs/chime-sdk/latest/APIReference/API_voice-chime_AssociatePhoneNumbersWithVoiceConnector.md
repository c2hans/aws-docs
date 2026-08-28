---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_AssociatePhoneNumbersWithVoiceConnector.html
---

# AssociatePhoneNumbersWithVoiceConnector
<a name="API_voice-chime_AssociatePhoneNumbersWithVoiceConnector"></a>

Associates phone numbers with the specified Amazon Chime SDK Voice Connector.

## Request Syntax
<a name="API_voice-chime_AssociatePhoneNumbersWithVoiceConnector_RequestSyntax"></a>

```
POST /voice-connectors/{voiceConnectorId}?operation=associate-phone-numbers HTTP/1.1
Content-type: application/json

{
   "E164PhoneNumbers": [ "{{string}}" ],
   "ForceAssociate": {{boolean}}
}
```

## URI Request Parameters
<a name="API_voice-chime_AssociatePhoneNumbersWithVoiceConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [voiceConnectorId](#API_voice-chime_AssociatePhoneNumbersWithVoiceConnector_RequestSyntax) **   <a name="chimesdk-voice-chime_AssociatePhoneNumbersWithVoiceConnector-request-uri-VoiceConnectorId"></a>
The Voice Connector ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_voice-chime_AssociatePhoneNumbersWithVoiceConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [E164PhoneNumbers](#API_voice-chime_AssociatePhoneNumbersWithVoiceConnector_RequestSyntax) **   <a name="chimesdk-voice-chime_AssociatePhoneNumbersWithVoiceConnector-request-E164PhoneNumbers"></a>
List of phone numbers, in E.164 format.
Type: Array of strings
Pattern: `^\+?[1-9]\d{1,14}$`
Required: Yes

 ** [ForceAssociate](#API_voice-chime_AssociatePhoneNumbersWithVoiceConnector_RequestSyntax) **   <a name="chimesdk-voice-chime_AssociatePhoneNumbersWithVoiceConnector-request-ForceAssociate"></a>
If true, associates the provided phone numbers with the provided Amazon Chime SDK Voice Connector and removes any previously existing associations. If false, does not associate any phone numbers that have previously existing associations.
Type: Boolean
Required: No

## Response Syntax
<a name="API_voice-chime_AssociatePhoneNumbersWithVoiceConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PhoneNumberErrors": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "PhoneNumberId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_voice-chime_AssociatePhoneNumbersWithVoiceConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PhoneNumberErrors](#API_voice-chime_AssociatePhoneNumbersWithVoiceConnector_ResponseSyntax) **   <a name="chimesdk-voice-chime_AssociatePhoneNumbersWithVoiceConnector-response-PhoneNumberErrors"></a>
If the action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.
Type: Array of [PhoneNumberError](API_voice-chime_PhoneNumberError.md) objects

## Errors
<a name="API_voice-chime_AssociatePhoneNumbersWithVoiceConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** AccessDeniedException **
You don't have the permissions needed to run this action.
HTTP Status Code: 403

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
The requested resource couldn't be found.
HTTP Status Code: 404

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The number of customer requests exceeds the request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client isn't authorized to request a resource.
HTTP Status Code: 401

## Examples
<a name="API_voice-chime_AssociatePhoneNumbersWithVoiceConnector_Examples"></a>

In the following example or examples, the Authorization header contents(`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_voice-chime_AssociatePhoneNumbersWithVoiceConnector_Example_1"></a>

This example associates the specified phone number with the specified Amazon Chime SDK Voice Connector.

#### Sample Request
<a name="API_voice-chime_AssociatePhoneNumbersWithVoiceConnector_Example_1_Request"></a>

```
POST /voice-connectors/abcdef1ghij2klmno3pqr4?operation=associate-phone-numbers HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.170 Python/3.6.0 Windows/10 botocore/1.12.160 X-Amz-Date: 20191028T184037Z Authorization: AUTHPARAMS Content-Length: 78 {"E164PhoneNumbers": ["+12065550100", "+12065550101"], "ForceAssociate": true}
```

#### Sample Response
<a name="API_voice-chime_AssociatePhoneNumbersWithVoiceConnector_Example_1_Response"></a>

```
HTTP/1.1 200 OK x-amzn-RequestId: ac266ffd-3732-4a4a-b8dd-4b64399dde0c Content-Type: application/json Content-Length: 24 Date: Mon, 28 Oct 2019 18:40:37 GMT Connection: keep-alive {"PhoneNumberErrors":[]}
```

## See Also
<a name="API_voice-chime_AssociatePhoneNumbersWithVoiceConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/AssociatePhoneNumbersWithVoiceConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/AssociatePhoneNumbersWithVoiceConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/AssociatePhoneNumbersWithVoiceConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/AssociatePhoneNumbersWithVoiceConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/AssociatePhoneNumbersWithVoiceConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/AssociatePhoneNumbersWithVoiceConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/AssociatePhoneNumbersWithVoiceConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/AssociatePhoneNumbersWithVoiceConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/AssociatePhoneNumbersWithVoiceConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/AssociatePhoneNumbersWithVoiceConnector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
