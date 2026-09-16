---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeletePartnerEventSource.html
---

# DeletePartnerEventSource
<a name="API_DeletePartnerEventSource"></a>

This operation is used by SaaS partners to delete a partner event source. This operation is not used by AWS customers.

When you delete an event source, the status of the corresponding partner event bus in the AWS customer account becomes DELETED.

## Request Syntax
<a name="API_DeletePartnerEventSource_RequestSyntax"></a>

```
{
   "Account": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DeletePartnerEventSource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Account](#API_DeletePartnerEventSource_RequestSyntax) **   <a name="eventbridge-DeletePartnerEventSource-request-Account"></a>
The AWS account ID of the AWS customer that the event source was created for.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [Name](#API_DeletePartnerEventSource_RequestSyntax) **   <a name="eventbridge-DeletePartnerEventSource-request-Name"></a>
The name of the event source to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `aws\.partner(/[\.\-_A-Za-z0-9]+){2,}`
Required: Yes

## Response Elements
<a name="API_DeletePartnerEventSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeletePartnerEventSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
There is concurrent modification on a rule, target, archive, or replay.
HTTP Status Code: 400

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** OperationDisabledException **
The operation you are attempting is not available in this region.
HTTP Status Code: 400

## See Also
<a name="API_DeletePartnerEventSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/DeletePartnerEventSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/DeletePartnerEventSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/DeletePartnerEventSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/DeletePartnerEventSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/DeletePartnerEventSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/DeletePartnerEventSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/DeletePartnerEventSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/DeletePartnerEventSource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/DeletePartnerEventSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/DeletePartnerEventSource)
