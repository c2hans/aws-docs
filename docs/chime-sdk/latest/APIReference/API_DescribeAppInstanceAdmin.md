---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_DescribeAppInstanceAdmin.html
---

# DescribeAppInstanceAdmin
<a name="API_DescribeAppInstanceAdmin"></a>

Returns the full details of an `AppInstanceAdmin`.

## Request Syntax
<a name="API_DescribeAppInstanceAdmin_RequestSyntax"></a>

```
GET /app-instances/{{appInstanceArn}}/admins/{{appInstanceAdminArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAppInstanceAdmin_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appInstanceAdminArn](#API_DescribeAppInstanceAdmin_RequestSyntax) **   <a name="chimesdk-DescribeAppInstanceAdmin-request-uri-AppInstanceAdminArn"></a>
The ARN of the `AppInstanceAdmin`.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [appInstanceArn](#API_DescribeAppInstanceAdmin_RequestSyntax) **   <a name="chimesdk-DescribeAppInstanceAdmin-request-uri-AppInstanceArn"></a>
The ARN of the `AppInstance`.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## Request Body
<a name="API_DescribeAppInstanceAdmin_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAppInstanceAdmin_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AppInstanceAdmin": {
      "Admin": {
         "Arn": "string",
         "Name": "string"
      },
      "AppInstanceArn": "string",
      "CreatedTimestamp": number
   }
}
```

## Response Elements
<a name="API_DescribeAppInstanceAdmin_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppInstanceAdmin](#API_DescribeAppInstanceAdmin_ResponseSyntax) **   <a name="chimesdk-DescribeAppInstanceAdmin-response-AppInstanceAdmin"></a>
The ARN and name of the `AppInstanceUser`, the ARN of the `AppInstance`, and the created and last-updated timestamps. All timestamps use epoch milliseconds.
Type: [AppInstanceAdmin](API_AppInstanceAdmin.md) object

## Errors
<a name="API_DescribeAppInstanceAdmin_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The client exceeded its request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
HTTP Status Code: 401

## See Also
<a name="API_DescribeAppInstanceAdmin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-identity-2021-04-20/DescribeAppInstanceAdmin)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-identity-2021-04-20/DescribeAppInstanceAdmin)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/DescribeAppInstanceAdmin)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-identity-2021-04-20/DescribeAppInstanceAdmin)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/DescribeAppInstanceAdmin)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-identity-2021-04-20/DescribeAppInstanceAdmin)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-identity-2021-04-20/DescribeAppInstanceAdmin)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-identity-2021-04-20/DescribeAppInstanceAdmin)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-identity-2021-04-20/DescribeAppInstanceAdmin)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/DescribeAppInstanceAdmin)
