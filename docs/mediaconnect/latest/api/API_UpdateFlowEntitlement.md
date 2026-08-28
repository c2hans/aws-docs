---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateFlowEntitlement.html
---

# UpdateFlowEntitlement
<a name="API_UpdateFlowEntitlement"></a>

 Updates an entitlement. You can change an entitlement's description, subscribers, and encryption. If you change the subscribers, the service will remove the outputs that are are used by the subscribers that are removed.

## Request Syntax
<a name="API_UpdateFlowEntitlement_RequestSyntax"></a>

```
PUT /v1/flows/{{flowArn}}/entitlements/{{entitlementArn}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "encryption": {
      "algorithm": "{{string}}",
      "constantInitializationVector": "{{string}}",
      "deviceId": "{{string}}",
      "keyType": "{{string}}",
      "region": "{{string}}",
      "resourceId": "{{string}}",
      "roleArn": "{{string}}",
      "secretArn": "{{string}}",
      "url": "{{string}}"
   },
   "entitlementStatus": "{{string}}",
   "subscribers": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateFlowEntitlement_RequestParameters"></a>

The request uses the following URI parameters.

 ** [entitlementArn](#API_UpdateFlowEntitlement_RequestSyntax) **   <a name="mediaconnect-UpdateFlowEntitlement-request-uri-entitlementArn"></a>
 The Amazon Resource Name (ARN) of the entitlement that you want to update.
Pattern: `arn:.+:mediaconnect.+:entitlement:.+`
Required: Yes

 ** [flowArn](#API_UpdateFlowEntitlement_RequestSyntax) **   <a name="mediaconnect-UpdateFlowEntitlement-request-uri-flowArn"></a>
 The ARN of the flow that is associated with the entitlement that you want to update.
Pattern: `arn:.+:mediaconnect.+:flow:.+`
Required: Yes

## Request Body
<a name="API_UpdateFlowEntitlement_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateFlowEntitlement_RequestSyntax) **   <a name="mediaconnect-UpdateFlowEntitlement-request-description"></a>
 A description of the entitlement. This description appears only on the MediaConnect console and will not be seen by the subscriber or end user.
Type: String
Required: No

 ** [encryption](#API_UpdateFlowEntitlement_RequestSyntax) **   <a name="mediaconnect-UpdateFlowEntitlement-request-encryption"></a>
 The type of encryption that will be used on the output associated with this entitlement. Allowable encryption types: static-key, speke.
Type: [UpdateEncryption](API_UpdateEncryption.md) object
Required: No

 ** [entitlementStatus](#API_UpdateFlowEntitlement_RequestSyntax) **   <a name="mediaconnect-UpdateFlowEntitlement-request-entitlementStatus"></a>
 An indication of whether you want to enable the entitlement to allow access, or disable it to stop streaming content to the subscriber’s flow temporarily. If you don’t specify the `entitlementStatus` field in your request, MediaConnect leaves the value unchanged.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [subscribers](#API_UpdateFlowEntitlement_RequestSyntax) **   <a name="mediaconnect-UpdateFlowEntitlement-request-subscribers"></a>
 The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_UpdateFlowEntitlement_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "entitlement": {
      "dataTransferSubscriberFeePercent": number,
      "description": "string",
      "encryption": {
         "algorithm": "string",
         "constantInitializationVector": "string",
         "deviceId": "string",
         "keyType": "string",
         "region": "string",
         "resourceId": "string",
         "roleArn": "string",
         "secretArn": "string",
         "url": "string"
      },
      "entitlementArn": "string",
      "entitlementStatus": "string",
      "name": "string",
      "subscribers": [ "string" ]
   },
   "flowArn": "string"
}
```

## Response Elements
<a name="API_UpdateFlowEntitlement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [entitlement](#API_UpdateFlowEntitlement_ResponseSyntax) **   <a name="mediaconnect-UpdateFlowEntitlement-response-entitlement"></a>
 The new configuration of the entitlement that you updated.
Type: [Entitlement](API_Entitlement.md) object

 ** [flowArn](#API_UpdateFlowEntitlement_ResponseSyntax) **   <a name="mediaconnect-UpdateFlowEntitlement-response-flowArn"></a>
 The ARN of the flow that this entitlement was granted on.
Type: String

## Errors
<a name="API_UpdateFlowEntitlement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ForbiddenException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_UpdateFlowEntitlement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/UpdateFlowEntitlement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/UpdateFlowEntitlement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/UpdateFlowEntitlement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/UpdateFlowEntitlement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/UpdateFlowEntitlement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/UpdateFlowEntitlement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/UpdateFlowEntitlement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/UpdateFlowEntitlement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/UpdateFlowEntitlement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/UpdateFlowEntitlement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
