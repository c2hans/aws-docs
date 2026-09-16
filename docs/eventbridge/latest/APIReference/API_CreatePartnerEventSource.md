---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreatePartnerEventSource.html
---

# CreatePartnerEventSource
<a name="API_CreatePartnerEventSource"></a>

Called by an SaaS partner to create a partner event source. This operation is not used by AWS customers.

Each partner event source can be used by one AWS account to create a matching partner event bus in that AWS account. A SaaS partner must create one partner event source for each AWS account that wants to receive those event types.

A partner event source creates events based on resources within the SaaS partner's service or application.

An AWS account that creates a partner event bus that matches the partner event source can use that event bus to receive events from the partner, and then process them using AWS Events rules and targets.

Partner event source names follow this format:

 ` partner_name/event_namespace/event_name `
+  *partner\_name* is determined during partner registration, and identifies the partner to AWS customers.
+  *event\_namespace* is determined by the partner, and is a way for the partner to categorize their events.
+  *event\_name* is determined by the partner, and should uniquely identify an event-generating resource within the partner system.

  The *event\_name* must be unique across all AWS customers. This is because the event source is a shared resource between the partner and customer accounts, and each partner event source unique in the partner account.

The combination of *event\_namespace* and *event\_name* should help AWS customers decide whether to create an event bus to receive these events.

## Request Syntax
<a name="API_CreatePartnerEventSource_RequestSyntax"></a>

```
{
   "Account": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_CreatePartnerEventSource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Account](#API_CreatePartnerEventSource_RequestSyntax) **   <a name="eventbridge-CreatePartnerEventSource-request-Account"></a>
The AWS account ID that is permitted to create a matching partner event bus for this partner event source.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [Name](#API_CreatePartnerEventSource_RequestSyntax) **   <a name="eventbridge-CreatePartnerEventSource-request-Name"></a>
The name of the partner event source. This name must be unique and must be in the format ` partner_name/event_namespace/event_name `. The AWS account that wants to use this partner event source must create a partner event bus with a name that matches the name of the partner event source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `aws\.partner(/[\.\-_A-Za-z0-9]+){2,}`
Required: Yes

## Response Syntax
<a name="API_CreatePartnerEventSource_ResponseSyntax"></a>

```
{
   "EventSourceArn": "string"
}
```

## Response Elements
<a name="API_CreatePartnerEventSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventSourceArn](#API_CreatePartnerEventSource_ResponseSyntax) **   <a name="eventbridge-CreatePartnerEventSource-response-EventSourceArn"></a>
The ARN of the partner event source.
Type: String

## Errors
<a name="API_CreatePartnerEventSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
There is concurrent modification on a rule, target, archive, or replay.
HTTP Status Code: 400

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** LimitExceededException **
The request failed because it attempted to create resource beyond the allowed service quota.
HTTP Status Code: 400

 ** OperationDisabledException **
The operation you are attempting is not available in this region.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The resource you are trying to create already exists.
HTTP Status Code: 400

## See Also
<a name="API_CreatePartnerEventSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/CreatePartnerEventSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/CreatePartnerEventSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/CreatePartnerEventSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/CreatePartnerEventSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/CreatePartnerEventSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/CreatePartnerEventSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/CreatePartnerEventSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/CreatePartnerEventSource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/CreatePartnerEventSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/CreatePartnerEventSource)
