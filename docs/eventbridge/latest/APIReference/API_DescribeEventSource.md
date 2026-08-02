---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeEventSource.html
---

# DescribeEventSource
<a name="API_DescribeEventSource"></a>

This operation lists details about a partner event source that is shared with your account.

## Request Syntax
<a name="API_DescribeEventSource_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEventSource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_DescribeEventSource_RequestSyntax) **   <a name="eventbridge-DescribeEventSource-request-Name"></a>
The name of the partner event source to display the details of.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `aws\.partner(/[\.\-_A-Za-z0-9]+){2,}`
Required: Yes

## Response Syntax
<a name="API_DescribeEventSource_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "CreatedBy": "string",
   "CreationTime": number,
   "ExpirationTime": number,
   "Name": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_DescribeEventSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DescribeEventSource_ResponseSyntax) **   <a name="eventbridge-DescribeEventSource-response-Arn"></a>
The ARN of the partner event source.
Type: String

 ** [CreatedBy](#API_DescribeEventSource_ResponseSyntax) **   <a name="eventbridge-DescribeEventSource-response-CreatedBy"></a>
The name of the SaaS partner that created the event source.
Type: String

 ** [CreationTime](#API_DescribeEventSource_ResponseSyntax) **   <a name="eventbridge-DescribeEventSource-response-CreationTime"></a>
The date and time that the event source was created.
Type: Timestamp

 ** [ExpirationTime](#API_DescribeEventSource_ResponseSyntax) **   <a name="eventbridge-DescribeEventSource-response-ExpirationTime"></a>
The date and time that the event source will expire if you do not create a matching event bus.
Type: Timestamp

 ** [Name](#API_DescribeEventSource_ResponseSyntax) **   <a name="eventbridge-DescribeEventSource-response-Name"></a>
The name of the partner event source.
Type: String

 ** [State](#API_DescribeEventSource_ResponseSyntax) **   <a name="eventbridge-DescribeEventSource-response-State"></a>
The state of the event source. If it is ACTIVE, you have already created a matching event bus for this event source, and that event bus is active. If it is PENDING, either you haven't yet created a matching event bus, or that event bus is deactivated. If it is DELETED, you have created a matching event bus, but the event source has since been deleted.
Type: String
Valid Values: `PENDING | ACTIVE | DELETED`

## Errors
<a name="API_DescribeEventSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** OperationDisabledException **
The operation you are attempting is not available in this region.
HTTP Status Code: 400

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeEventSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/DescribeEventSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/DescribeEventSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/DescribeEventSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/DescribeEventSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/DescribeEventSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/DescribeEventSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/DescribeEventSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/DescribeEventSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/DescribeEventSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/DescribeEventSource)
