---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteEventBus.html
---

# DeleteEventBus
<a name="API_DeleteEventBus"></a>

Deletes the specified custom event bus or partner event bus. All rules associated with this event bus need to be deleted. You can't delete your account's default event bus.

## Request Syntax
<a name="API_DeleteEventBus_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteEventBus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_DeleteEventBus_RequestSyntax) **   <a name="eventbridge-DeleteEventBus-request-Name"></a>
The name of the event bus to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[/\.\-_A-Za-z0-9]+`
Required: Yes

## Response Elements
<a name="API_DeleteEventBus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteEventBus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
There is concurrent modification on a rule, target, archive, or replay.
HTTP Status Code: 400

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

## See Also
<a name="API_DeleteEventBus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/DeleteEventBus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/DeleteEventBus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/DeleteEventBus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/DeleteEventBus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/DeleteEventBus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/DeleteEventBus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/DeleteEventBus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/DeleteEventBus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/DeleteEventBus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/DeleteEventBus)
