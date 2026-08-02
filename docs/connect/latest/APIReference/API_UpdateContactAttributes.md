---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateContactAttributes.html
---

# UpdateContactAttributes
<a name="API_UpdateContactAttributes"></a>

Creates or updates user-defined contact attributes associated with the specified contact.

You can create or update user-defined attributes for both ongoing and completed contacts. For example, while the call is active, you can update the customer's name or the reason the customer called. You can add notes about steps that the agent took during the call that display to the next agent that takes the call. You can also update attributes for a contact using data from your CRM application and save the data with the contact in Connect Customer. You could also flag calls for additional analysis, such as legal review or to identify abusive callers.

Contact attributes are available in Connect Customer for 24 months, and are then deleted. For information about contact record retention and the maximum size of the contact record attributes section, see [Feature specifications](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#feature-limits) in the *Connect Customer Administrator Guide*.

## Request Syntax
<a name="API_UpdateContactAttributes_RequestSyntax"></a>

```
POST /contact/attributes HTTP/1.1
Content-type: application/json

{
   "Attributes": {
      "{{string}}" : "{{string}}"
   },
   "InitialContactId": "{{string}}",
   "InstanceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateContactAttributes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateContactAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Attributes](#API_UpdateContactAttributes_RequestSyntax) **   <a name="connect-UpdateContactAttributes-request-Attributes"></a>
The Connect Customer attributes. These attributes can be accessed in flows just like any other contact attributes.
You can have up to 32,768 UTF-8 bytes across all attributes for a contact. Attribute keys can include only alphanumeric, dash, and underscore characters.
In the [Set contact attributes](https://docs.aws.amazon.com/connect/latest/adminguide/set-contact-attributes.html) block, when the attributes for a contact exceed 32 KB, the contact is routed down the Error branch of the flow. As a mitigation, consider the following options:
+ Remove unnecessary attributes by setting their values to empty.
+ If the attributes are only used in one flow and don't need to be referred to outside of that flow (for example, by a Lambda or another flow), then use flow attributes. This way you aren't needlessly persisting the 32 KB of information from one flow to another. For more information, see [Flow block: Set contact attributes](https://docs.aws.amazon.com/connect/latest/adminguide/set-contact-attributes.html) in the *Connect Customer Administrator Guide*.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 32767.
Value Length Constraints: Minimum length of 0. Maximum length of 32767.
Required: Yes

 ** [InitialContactId](#API_UpdateContactAttributes_RequestSyntax) **   <a name="connect-UpdateContactAttributes-request-InitialContactId"></a>
The identifier of the contact. This is the identifier of the contact associated with the first interaction with the contact center.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_UpdateContactAttributes_RequestSyntax) **   <a name="connect-UpdateContactAttributes-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_UpdateContactAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateContactAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateContactAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidActiveRegionException **
This exception occurs when an API request is made to a non-active region in an Amazon Connect instance configured with Amazon Connect Global Resiliency. For example, if the active region is US West (Oregon) and a request is made to US East (N. Virginia), the exception will be returned.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

## See Also
<a name="API_UpdateContactAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateContactAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateContactAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateContactAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateContactAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateContactAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateContactAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateContactAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateContactAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateContactAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateContactAttributes)
