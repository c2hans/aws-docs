---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_CreateProfile.html
---

# CreateProfile
<a name="API_route53profiles_CreateProfile"></a>

 Creates an empty Route 53 Profile.

## Request Syntax
<a name="API_route53profiles_CreateProfile_RequestSyntax"></a>

```
POST /profile HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Name": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_route53profiles_CreateProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_route53profiles_CreateProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_route53profiles_CreateProfile_RequestSyntax) **   <a name="Route53Profiles-route53profiles_CreateProfile-request-ClientToken"></a>
 `ClientToken` is an idempotency token that ensures a call to `CreateProfile` completes only once. You choose the value to pass. For example, an issue might prevent you from getting a response from `CreateProfile`. In this case, safely retry your call to `CreateProfile` by using the same `CreateProfile` parameter value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Name](#API_route53profiles_CreateProfile_RequestSyntax) **   <a name="Route53Profiles-route53profiles_CreateProfile-request-Name"></a>
 A name for the Profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: Yes

 ** [Tags](#API_route53profiles_CreateProfile_RequestSyntax) **   <a name="Route53Profiles-route53profiles_CreateProfile-request-Tags"></a>
 A list of the tag keys and values that you want to associate with the Route 53 Profile.
Type: Array of [Tag](API_route53profiles_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_route53profiles_CreateProfile_ResponseSyntax"></a>

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
<a name="API_route53profiles_CreateProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Profile](#API_route53profiles_CreateProfile_ResponseSyntax) **   <a name="Route53Profiles-route53profiles_CreateProfile-response-Profile"></a>
 The Profile that you just created.
Type: [Profile](API_route53profiles_Profile.md) object

## Errors
<a name="API_route53profiles_CreateProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The current account doesn't have the IAM permissions required to perform the specified operation.
HTTP Status Code: 400

 ** InvalidParameterException **
 One or more parameters in this request are not valid.
 ** FieldName **
 The parameter field name for the invalid parameter exception.
HTTP Status Code: 400

 ** LimitExceededException **
 The request caused one or more limits to be exceeded.
 ** ResourceType **
 The resource type that caused the limits to be exceeded.
HTTP Status Code: 400

 ** ThrottlingException **
 The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

 ** ValidationException **
 You have provided an invalid command.
HTTP Status Code: 400

## Examples
<a name="API_route53profiles_CreateProfile_Examples"></a>

### CreateProfile Example
<a name="API_route53profiles_CreateProfile_Example_1"></a>

This example illustrates one usage of CreateProfile.

#### Sample Request
<a name="API_route53profiles_CreateProfile_Example_1_Request"></a>

```
POST /profile HTTP/1.1
host:route53profiles.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 71
X-Amz-Date:20240319T214228Z
User-Agent: aws-cli/1.32.63 botocore/1.34.63 Python/3.8.18
Content-Type: application/json
Authorization: AWS4-HMAC-SHA256
    Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-1/route53profiles/aws4_request,
    SignedHeaders=content-type;host;x-amz-date;x-amz-security-token
    Signature=[calculated-signature]
{
    "Name": "test",
    "ClientToken": "c60a235a-e786-40bc-a5a4-f12EXAMPLE"
}
```

#### Sample Response
<a name="API_route53profiles_CreateProfile_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 19 Mar 2024 21:53:14 GMT
Content-Type: application/json
Content-Length: 371
Connection: keep-alive
x-amzn-RequestId: dcd9d91e-1a5a-481f-82b7-bafe7dexample
Access-Control-Allow-Origin: *
x-amz-apigw-id: U5eX0FdmIexample=
X-Amzn-Trace-Id: Root=1-65fa10fe-6e5a93a56a32afdfsd3example
{
    "Profile": {
        "Arn": "arn:aws:route53profiles:us-east-1:123456789012:profile/rp-6ffe47d5example",
        "ClientToken": "c60a235a-e786-40bc-a5a4-f12EXAMPLE",
        "CreationTime": 1710885194.55,
        "Id": "rp-6ffe47d5example",
        "ModificationTime": 1710885194.55,
        "Name": "test",
        "OwnerId": "123456789012",
        "ShareStatus": "NOT_SHARED",
        "Status": "COMPLETE",
        "StatusMessage": "Created Profile"
    }
}
```

## See Also
<a name="API_route53profiles_CreateProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53profiles-2018-05-10/CreateProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53profiles-2018-05-10/CreateProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53profiles-2018-05-10/CreateProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53profiles-2018-05-10/CreateProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53profiles-2018-05-10/CreateProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53profiles-2018-05-10/CreateProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53profiles-2018-05-10/CreateProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53profiles-2018-05-10/CreateProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53profiles-2018-05-10/CreateProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53profiles-2018-05-10/CreateProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
