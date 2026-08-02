---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_DeleteProfile.html
---

# DeleteProfile
<a name="API_route53profiles_DeleteProfile"></a>

 Deletes the specified Route 53 Profile. Before you can delete a profile, you must first disassociate it from all VPCs.

## Request Syntax
<a name="API_route53profiles_DeleteProfile_RequestSyntax"></a>

```
DELETE /profile/{{ProfileId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_route53profiles_DeleteProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ProfileId](#API_route53profiles_DeleteProfile_RequestSyntax) **   <a name="Route53Profiles-route53profiles_DeleteProfile-request-uri-ProfileId"></a>
 The ID of the Profile that you want to delete.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Request Body
<a name="API_route53profiles_DeleteProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_route53profiles_DeleteProfile_ResponseSyntax"></a>

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
<a name="API_route53profiles_DeleteProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Profile](#API_route53profiles_DeleteProfile_ResponseSyntax) **   <a name="Route53Profiles-route53profiles_DeleteProfile-response-Profile"></a>
 Information about the `DeleteProfile` request, including the status of the request.
Type: [Profile](API_route53profiles_Profile.md) object

## Errors
<a name="API_route53profiles_DeleteProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The current account doesn't have the IAM permissions required to perform the specified operation.
HTTP Status Code: 400

 ** ConflictException **
 The request you submitted conflicts with an existing request.
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
<a name="API_route53profiles_DeleteProfile_Examples"></a>

### DeleteProfile Example
<a name="API_route53profiles_DeleteProfile_Example_1"></a>

This example illustrates one usage of DeleteProfile.

#### Sample Request
<a name="API_route53profiles_DeleteProfile_Example_1_Request"></a>

```
DELETE /profile/rp-6ffe47d5example HTTP/1.1
host:route53profiles.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 0
X-Amz-Date:20240319T234733Z
User-Agent: aws-cli/1.32.63 botocore/1.34.63 Python/3.8.18
Content-Type: application/json
Authorization: AWS4-HMAC-SHA256
    Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-1/route53profiles/aws4_request,
    SignedHeaders=content-type;host;x-amz-date;x-amz-security-token
    Signature=[calculated-signature]
{} # RequestBody is empty
```

#### Sample Response
<a name="API_route53profiles_DeleteProfile_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 19 Mar 2024 23:47:33 GMT
Content-Type: application/json
Content-Length: 374
Connection: keep-alive
x-amzn-RequestId: dcd9d91e-1a5a-481f-82b7-bafe7dexample
Access-Control-Allow-Origin: *
x-amz-apigw-id: U5eX0FdmIexample=
X-Amzn-Trace-Id: Root=1-65fa10fe-6e5a93a56a32afdfsd3example
{
    "Profile": {
        "Arn": "arn:aws:route53profiles:us-east-1:123456789012:profile/rp-6ffe47d5example",
        "ClientToken": "0a15fec0-05d9-4f78-bec0-EXAMPLE11111",
        "CreationTime": 1710850903.578,
        "Id": "rp-6ffe47d5example",
        "ModificationTime": 1710892012.553,
        "Name": "test",
        "OwnerId": "123456789012",
        "ShareStatus": "NOT_SHARED",
        "Status": "DELETED",
        "StatusMessage": "Deleted Profile"
    }
```

## See Also
<a name="API_route53profiles_DeleteProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53profiles-2018-05-10/DeleteProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53profiles-2018-05-10/DeleteProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53profiles-2018-05-10/DeleteProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53profiles-2018-05-10/DeleteProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53profiles-2018-05-10/DeleteProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53profiles-2018-05-10/DeleteProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53profiles-2018-05-10/DeleteProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53profiles-2018-05-10/DeleteProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53profiles-2018-05-10/DeleteProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53profiles-2018-05-10/DeleteProfile)
