---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchDisableStandards.html
---

# BatchDisableStandards
<a name="API_BatchDisableStandards"></a>

Disables the standards specified by the provided `StandardsSubscriptionArns`.

For more information, see [Security Standards](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html) section of the * AWS Security Hub CSPM User Guide*.

## Request Syntax
<a name="API_BatchDisableStandards_RequestSyntax"></a>

```
POST /standards/deregister HTTP/1.1
Content-type: application/json

{
   "StandardsSubscriptionArns": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchDisableStandards_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchDisableStandards_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [StandardsSubscriptionArns](#API_BatchDisableStandards_RequestSyntax) **   <a name="securityhub-BatchDisableStandards-request-StandardsSubscriptionArns"></a>
The ARNs of the standards subscriptions to disable.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_BatchDisableStandards_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "StandardsSubscriptions": [
      {
         "Provider": "string",
         "StandardsArn": "string",
         "StandardsControlsUpdatable": "string",
         "StandardsInput": {
            "string" : "string"
         },
         "StandardsStatus": "string",
         "StandardsStatusReason": {
            "StatusReasonCode": "string"
         },
         "StandardsSubscriptionArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDisableStandards_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StandardsSubscriptions](#API_BatchDisableStandards_ResponseSyntax) **   <a name="securityhub-BatchDisableStandards-response-StandardsSubscriptions"></a>
The details of the standards subscriptions that were disabled.
Type: Array of [StandardsSubscription](API_StandardsSubscription.md) objects

## Errors
<a name="API_BatchDisableStandards_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

## See Also
<a name="API_BatchDisableStandards_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/BatchDisableStandards)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/BatchDisableStandards)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/BatchDisableStandards)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/BatchDisableStandards)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/BatchDisableStandards)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/BatchDisableStandards)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/BatchDisableStandards)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/BatchDisableStandards)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/BatchDisableStandards)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/BatchDisableStandards)
