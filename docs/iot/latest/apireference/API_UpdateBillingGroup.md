---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateBillingGroup.html
---

# UpdateBillingGroup
<a name="API_UpdateBillingGroup"></a>

Updates information about the billing group.

Requires permission to access the [UpdateBillingGroup](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateBillingGroup_RequestSyntax"></a>

```
PATCH /billing-groups/{{billingGroupName}} HTTP/1.1
Content-type: application/json

{
   "billingGroupProperties": {
      "billingGroupDescription": "{{string}}"
   },
   "expectedVersion": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateBillingGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [billingGroupName](#API_UpdateBillingGroup_RequestSyntax) **   <a name="iot-UpdateBillingGroup-request-uri-billingGroupName"></a>
The name of the billing group.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_UpdateBillingGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [billingGroupProperties](#API_UpdateBillingGroup_RequestSyntax) **   <a name="iot-UpdateBillingGroup-request-billingGroupProperties"></a>
The properties of the billing group.
Type: [BillingGroupProperties](API_BillingGroupProperties.md) object
Required: Yes

 ** [expectedVersion](#API_UpdateBillingGroup_RequestSyntax) **   <a name="iot-UpdateBillingGroup-request-expectedVersion"></a>
The expected version of the billing group. If the version of the billing group does not match the expected version specified in the request, the `UpdateBillingGroup` request is rejected with a `VersionConflictException`.
Type: Long
Required: No

## Response Syntax
<a name="API_UpdateBillingGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "version": number
}
```

## Response Elements
<a name="API_UpdateBillingGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [version](#API_UpdateBillingGroup_ResponseSyntax) **   <a name="iot-UpdateBillingGroup-response-version"></a>
The latest version of the billing group.
Type: Long

## Errors
<a name="API_UpdateBillingGroup_Errors"></a>

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

 ** VersionConflictException **
An exception thrown when the version of an entity specified with the `expectedVersion` parameter does not match the latest version in the system.
 ** message **
The message for the exception.
HTTP Status Code: 409

## See Also
<a name="API_UpdateBillingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateBillingGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateBillingGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateBillingGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateBillingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateBillingGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateBillingGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateBillingGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateBillingGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateBillingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateBillingGroup)
