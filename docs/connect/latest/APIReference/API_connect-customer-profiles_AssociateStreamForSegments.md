---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_AssociateStreamForSegments.html
---

# AssociateStreamForSegments
<a name="API_connect-customer-profiles_AssociateStreamForSegments"></a>

Associates an Amazon Kinesis data stream to receive segment membership events for a given domain. This is a domain-level configuration that applies to all segment subscriptions within the domain. A domain can have only one associated stream at a time.

## Request Syntax
<a name="API_connect-customer-profiles_AssociateStreamForSegments_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/segment-streams HTTP/1.1
Content-type: application/json

{
   "DestinationArn": "{{string}}",
   "DestinationRoleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_AssociateStreamForSegments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_AssociateStreamForSegments_RequestSyntax) **   <a name="connect-connect-customer-profiles_AssociateStreamForSegments-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_AssociateStreamForSegments_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DestinationArn](#API_connect-customer-profiles_AssociateStreamForSegments_RequestSyntax) **   <a name="connect-connect-customer-profiles_AssociateStreamForSegments-request-DestinationArn"></a>
The Amazon Resource Name (ARN) of the Amazon Kinesis data stream to deliver segment membership events to. For example, `arn:aws:kinesis:region:account-id:stream/stream-name`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [DestinationRoleArn](#API_connect-customer-profiles_AssociateStreamForSegments_RequestSyntax) **   <a name="connect-connect-customer-profiles_AssociateStreamForSegments-request-DestinationRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that allows Customer Profiles service principal to assume the role for conducting AWS Key Management Service (KMS) and Amazon Kinesis operations. The role must grant the following Amazon Kinesis permissions to deliver segment membership events to the stream:
+  `kinesis:PutRecord`
+  `kinesis:PutRecords`
+  `kinesis:DescribeStream`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*arn:aws:iam:.*:[0-9]+:.*`
Required: Yes

## Response Syntax
<a name="API_connect-customer-profiles_AssociateStreamForSegments_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-customer-profiles_AssociateStreamForSegments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-customer-profiles_AssociateStreamForSegments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## See Also
<a name="API_connect-customer-profiles_AssociateStreamForSegments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/AssociateStreamForSegments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/AssociateStreamForSegments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/AssociateStreamForSegments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/AssociateStreamForSegments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/AssociateStreamForSegments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/AssociateStreamForSegments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/AssociateStreamForSegments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/AssociateStreamForSegments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/AssociateStreamForSegments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/AssociateStreamForSegments)
