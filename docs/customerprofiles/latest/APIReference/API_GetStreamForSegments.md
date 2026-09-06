---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetStreamForSegments.html
---

# GetStreamForSegments
<a name="API_connect-customer-profiles_GetStreamForSegments"></a>

Returns information about the segment membership event stream configured for a specific domain, including the stream state and associated segments.

## Request Syntax
<a name="API_connect-customer-profiles_GetStreamForSegments_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/segment-streams HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetStreamForSegments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetStreamForSegments_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetStreamForSegments-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetStreamForSegments_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetStreamForSegments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AssociatedAt": number,
   "AssociatedSegments": [
      {
         "Message": "string",
         "SegmentName": "string",
         "Status": "string"
      }
   ],
   "DestinationArn": "string",
   "DestinationRoleArn": "string",
   "DisassociatedAt": number,
   "DomainName": "string",
   "FailureReason": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetStreamForSegments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssociatedAt](#API_connect-customer-profiles_GetStreamForSegments_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetStreamForSegments-response-AssociatedAt"></a>
The timestamp of when the stream was associated.
Type: Timestamp

 ** [AssociatedSegments](#API_connect-customer-profiles_GetStreamForSegments_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetStreamForSegments-response-AssociatedSegments"></a>
A list of segments currently associated with the stream and their subscription status.
Type: Array of [AssociatedSegment](API_connect-customer-profiles_AssociatedSegment.md) objects

 ** [DestinationArn](#API_connect-customer-profiles_GetStreamForSegments_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetStreamForSegments-response-DestinationArn"></a>
The Amazon Resource Name (ARN) of the Amazon Kinesis data stream receiving segment membership events.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [DestinationRoleArn](#API_connect-customer-profiles_GetStreamForSegments_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetStreamForSegments-response-DestinationRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role used for Amazon Kinesis and AWS Key Management Service (KMS) operations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*arn:aws:iam:.*:[0-9]+:.*`

 ** [DisassociatedAt](#API_connect-customer-profiles_GetStreamForSegments_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetStreamForSegments-response-DisassociatedAt"></a>
The timestamp of when the stream was disassociated.
Type: Timestamp

 ** [DomainName](#API_connect-customer-profiles_GetStreamForSegments_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetStreamForSegments-response-DomainName"></a>
The unique name of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [FailureReason](#API_connect-customer-profiles_GetStreamForSegments_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetStreamForSegments-response-FailureReason"></a>
The reason why the stream is in an unhealthy state, if applicable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [State](#API_connect-customer-profiles_GetStreamForSegments_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetStreamForSegments-response-State"></a>
The operational state of the destination stream. The following are valid values:
+  **RUNNING**: The stream is associated and healthy. Segment membership events are being published.
+  **UNHEALTHY**: The stream is associated but events cannot currently be published. See `FailureReason` for details.
+  **STOPPED**: The stream is no longer publishing segment membership events.
Type: String
Valid Values: `RUNNING | UNHEALTHY | STOPPED`

## Errors
<a name="API_connect-customer-profiles_GetStreamForSegments_Errors"></a>

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
<a name="API_connect-customer-profiles_GetStreamForSegments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetStreamForSegments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetStreamForSegments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetStreamForSegments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetStreamForSegments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetStreamForSegments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetStreamForSegments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetStreamForSegments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetStreamForSegments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetStreamForSegments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetStreamForSegments)
