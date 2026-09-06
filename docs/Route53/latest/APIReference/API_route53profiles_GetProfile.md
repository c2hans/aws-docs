---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_GetProfile.html
---

# GetProfile
<a name="API_route53profiles_GetProfile"></a>

 Returns information about a specified Route 53 Profile, such as whether whether the Profile is shared, and the current status of the Profile.

## Request Syntax
<a name="API_route53profiles_GetProfile_RequestSyntax"></a>

```
GET /profile/{{ProfileId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_route53profiles_GetProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ProfileId](#API_route53profiles_GetProfile_RequestSyntax) **   <a name="Route53Profiles-route53profiles_GetProfile-request-uri-ProfileId"></a>
 ID of the Profile.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Request Body
<a name="API_route53profiles_GetProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_route53profiles_GetProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Profile": {
      "Arn": "string",
      "ClientToken": "string",
      "CreationTime": number,
      "Id": "string",
      "ModificationTime": number,
      "Name": "string",
      "OwnerId": "string",
      "ShareStatus": "string",
      "Status": "string",
      "StatusMessage": "string"
   }
}
```

## Response Elements
<a name="API_route53profiles_GetProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Profile](#API_route53profiles_GetProfile_ResponseSyntax) **   <a name="Route53Profiles-route53profiles_GetProfile-response-Profile"></a>
 Information about the Profile, including the status of the Profile.
Type: [Profile](API_route53profiles_Profile.md) object

## Errors
<a name="API_route53profiles_GetProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The current account doesn't have the IAM permissions required to perform the specified operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 The resource you are associating is not found.
 ** ResourceType **
 The resource type that caused the resource not found exception.
HTTP Status Code: 400

 ** ThrottlingException **
 The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

 ** ValidationException **
 You have provided an invalid command.
HTTP Status Code: 400

## Examples
<a name="API_route53profiles_GetProfile_Examples"></a>

### GetProfile Example
<a name="API_route53profiles_GetProfile_Example_1"></a>

This example illustrates one usage of GetProfile.

#### Sample Request
<a name="API_route53profiles_GetProfile_Example_1_Request"></a>

```
GET /profile/rp-4987774726example HTTP/1.1
host:route53profiles.us-east-1.amazonaws.com
Accept-Encoding: identity
X-Amz-Date:20240319T224652Z
User-Agent: aws-cli/1.32.63 botocore/1.34.63 Python/3.8.18
Authorization: AWS4-HMAC-SHA256
    Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-1/route53profiles/aws4_request,
    SignedHeaders=host;x-amz-date;x-amz-security-token
    Signature=[calculated-signature]
{} # RequestBody is empty
```

#### Sample Response
<a name="API_route53profiles_GetProfile_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 19 Mar 2024 22:46:52 GMT
Content-Type: application/json
Content-Length: 373
Connection: keep-alive
x-amzn-RequestId: dcd9d91e-1a5a-481f-82b7-bafe7dexample
Access-Control-Allow-Origin: *
x-amz-apigw-id: U5eX0FdmIexample=
X-Amzn-Trace-Id: Root=1-65fa10fe-6e5a93a56a325ab8example

{
    "Profile": {
        "Arn": "arn:aws:route53profiles:us-east-1:123456789012:profile/rp-4987774726example",
        "ClientToken": "0cbc5ae7-4921-4204-bea9-EXAMPLE11111",
        "CreationTime": 1710851044.288,
        "Id": "rp-4987774726example",
        "ModificationTime": 1710851044.288,
        "Name": "test",
        "OwnerId": "123456789012",
        "ShareStatus": "NOT_SHARED",
        "Status": "COMPLETE",
        "StatusMessage": "Created Profile"
    }
}
```

## See Also
<a name="API_route53profiles_GetProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53profiles-2018-05-10/GetProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53profiles-2018-05-10/GetProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53profiles-2018-05-10/GetProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53profiles-2018-05-10/GetProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53profiles-2018-05-10/GetProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53profiles-2018-05-10/GetProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53profiles-2018-05-10/GetProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53profiles-2018-05-10/GetProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53profiles-2018-05-10/GetProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53profiles-2018-05-10/GetProfile)
