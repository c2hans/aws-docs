---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AddThingToBillingGroup.html
---

# AddThingToBillingGroup
<a name="API_AddThingToBillingGroup"></a>

Adds a thing to a billing group.

Requires permission to access the [AddThingToBillingGroup](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_AddThingToBillingGroup_RequestSyntax"></a>

```
PUT /billing-groups/addThingToBillingGroup HTTP/1.1
Content-type: application/json

{
   "billingGroupArn": "{{string}}",
   "billingGroupName": "{{string}}",
   "thingArn": "{{string}}",
   "thingName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AddThingToBillingGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AddThingToBillingGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [billingGroupArn](#API_AddThingToBillingGroup_RequestSyntax) **   <a name="iot-AddThingToBillingGroup-request-billingGroupArn"></a>
The ARN of the billing group.
Type: String
Required: No

 ** [billingGroupName](#API_AddThingToBillingGroup_RequestSyntax) **   <a name="iot-AddThingToBillingGroup-request-billingGroupName"></a>
The name of the billing group.
This call is asynchronous. It might take several seconds for the detachment to propagate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** [thingArn](#API_AddThingToBillingGroup_RequestSyntax) **   <a name="iot-AddThingToBillingGroup-request-thingArn"></a>
The ARN of the thing to be added to the billing group.
Type: String
Required: No

 ** [thingName](#API_AddThingToBillingGroup_RequestSyntax) **   <a name="iot-AddThingToBillingGroup-request-thingName"></a>
The name of the thing to be added to the billing group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

## Response Syntax
<a name="API_AddThingToBillingGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AddThingToBillingGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AddThingToBillingGroup_Errors"></a>

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
<a name="API_AddThingToBillingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/AddThingToBillingGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/AddThingToBillingGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AddThingToBillingGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/AddThingToBillingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AddThingToBillingGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/AddThingToBillingGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/AddThingToBillingGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/AddThingToBillingGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/AddThingToBillingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AddThingToBillingGroup)
