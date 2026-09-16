---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeAcmeEndpoint.html
---

# DescribeAcmeEndpoint
<a name="API_DescribeAcmeEndpoint"></a>

Returns detailed metadata about the specified ACME endpoint, including its status, URL, authorization behavior, and certificate authority configuration.

## Request Syntax
<a name="API_DescribeAcmeEndpoint_RequestSyntax"></a>

```
{
   "AcmeEndpointArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAcmeEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AcmeEndpointArn](#API_DescribeAcmeEndpoint_RequestSyntax) **   <a name="ACM-DescribeAcmeEndpoint-request-AcmeEndpointArn"></a>
The Amazon Resource Name (ARN) of the ACME endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:aws[a-z-]*:acm:[a-z0-9-]+:[0-9]{12}:acme-endpoint/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_DescribeAcmeEndpoint_ResponseSyntax"></a>

```
{
   "AcmeEndpoint": {
      "AcmeEndpointArn": "string",
      "AuthorizationBehavior": "string",
      "CertificateAuthority": { ... },
      "CertificateTags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "Contact": "string",
      "CreatedAt": number,
      "EndpointUrl": "string",
      "FailureReason": "string",
      "Status": "string",
      "UpdatedAt": number
   }
}
```

## Response Elements
<a name="API_DescribeAcmeEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AcmeEndpoint](#API_DescribeAcmeEndpoint_ResponseSyntax) **   <a name="ACM-DescribeAcmeEndpoint-response-AcmeEndpoint"></a>
The ACME endpoint details.
Type: [AcmeEndpoint](API_AcmeEndpoint.md) object

## Errors
<a name="API_DescribeAcmeEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have access required to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified certificate cannot be found in the caller's account or the caller's account cannot be found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied because it exceeded a quota.
 ** throttlingReasons **
One or more reasons why the request was throttled.
HTTP Status Code: 400

 ** ValidationException **
The supplied input failed to satisfy constraints of an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAcmeEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/DescribeAcmeEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/DescribeAcmeEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/DescribeAcmeEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/DescribeAcmeEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/DescribeAcmeEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/DescribeAcmeEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/DescribeAcmeEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/DescribeAcmeEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/DescribeAcmeEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/DescribeAcmeEndpoint)
