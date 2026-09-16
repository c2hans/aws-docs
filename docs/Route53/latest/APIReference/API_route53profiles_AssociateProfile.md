---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_AssociateProfile.html
---

# AssociateProfile
<a name="API_route53profiles_AssociateProfile"></a>

 Associates a Route 53 Profiles profile with a VPC. A VPC can have only one Profile associated with it, but a Profile can be associated with 1000 of VPCs (and you can request a higher quota). For more information, see [https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-api-entities](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-api-entities).

## Request Syntax
<a name="API_route53profiles_AssociateProfile_RequestSyntax"></a>

```
POST /profileassociation HTTP/1.1
Content-type: application/json

{
   "Name": "{{string}}",
   "ProfileId": "{{string}}",
   "ResourceId": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_route53profiles_AssociateProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_route53profiles_AssociateProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_route53profiles_AssociateProfile_RequestSyntax) **   <a name="Route53Profiles-route53profiles_AssociateProfile-request-Name"></a>
 A name for the association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: Yes

 ** [ProfileId](#API_route53profiles_AssociateProfile_RequestSyntax) **   <a name="Route53Profiles-route53profiles_AssociateProfile-request-ProfileId"></a>
 ID of the Profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [ResourceId](#API_route53profiles_AssociateProfile_RequestSyntax) **   <a name="Route53Profiles-route53profiles_AssociateProfile-request-ResourceId"></a>
 The ID of the VPC.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [Tags](#API_route53profiles_AssociateProfile_RequestSyntax) **   <a name="Route53Profiles-route53profiles_AssociateProfile-request-Tags"></a>
 A list of the tag keys and values that you want to identify the Profile association.
Type: Array of [Tag](API_route53profiles_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_route53profiles_AssociateProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ProfileAssociation": {
      "CreationTime": number,
      "Id": "string",
      "ModificationTime": number,
      "Name": "string",
      "OwnerId": "string",
      "ProfileId": "string",
      "ResourceId": "string",
      "Status": "string",
      "StatusMessage": "string"
   }
}
```

## Response Elements
<a name="API_route53profiles_AssociateProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProfileAssociation](#API_route53profiles_AssociateProfile_ResponseSyntax) **   <a name="Route53Profiles-route53profiles_AssociateProfile-response-ProfileAssociation"></a>
 The association that you just created. The association has an ID that you can use to identify it in other requests, such as update and delete.
Type: [ProfileAssociation](API_route53profiles_ProfileAssociation.md) object

## Errors
<a name="API_route53profiles_AssociateProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The current account doesn't have the IAM permissions required to perform the specified operation.
HTTP Status Code: 400

 ** ConflictException **
 The request you submitted conflicts with an existing request.
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

 ** ResourceExistsException **
 The resource you are trying to associate, has already been associated.
 ** ResourceType **
 The resource type that caused the resource exists exception.
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
<a name="API_route53profiles_AssociateProfile_Examples"></a>

### AssociateProfile Example
<a name="API_route53profiles_AssociateProfile_Example_1"></a>

This example illustrates one usage of AssociateProfile.

#### Sample Request
<a name="API_route53profiles_AssociateProfile_Example_1_Request"></a>

```
POST /profileassociation HTTP/1.1
host:route53profiles.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 103
X-Amz-Date:20240319T222051Z
User-Agent: aws-cli/1.32.63 botocore/1.34.63 Python/3.8.18
Content-Type: application/json
Authorization: AWS4-HMAC-SHA256
    Credential=AKIAJJ2SONIPEXAMPLE/20191101/us-east-1/route53profiles/aws4_request,
    SignedHeaders=content-type;host;x-amz-date;x-amz-security-token
    Signature=[calculated-signature]
{
    "Name": "test-association",
    "ProfileId": "rp-4987774726example",
    "ResourceId": "vpc-0af3b96b3example"
}
```

#### Sample Response
<a name="API_route53profiles_AssociateProfile_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 19 Mar 2024 22:20:51 GMT
Content-Type: application/json
Content-Length: 322
Connection: keep-alive
x-amzn-RequestId: dcd9d91e-1a5a-sdds-82b7-bafe7dexample
Access-Control-Allow-Origin: *
x-amz-apigw-id: U5eX0FdmIexample=
X-Amzn-Trace-Id: Root=1-65fa10fe-6e5a93a56a32afsdfd3example
{
    "ProfileAssociation": {
        "CreationTime": 1710886843.849,
        "Id": "rpassoc-489ce212fexample",
        "ModificationTime": 1710886843.849,
        "Name": "test-association",
        "OwnerId": "123456789012",
        "ProfileId": "rp-4987774726example",
        "ResourceId": "vpc-0af3b96b3example",
        "Status": "CREATING",
        "StatusMessage": "Creating Profile Association"
    }
}
```

## See Also
<a name="API_route53profiles_AssociateProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53profiles-2018-05-10/AssociateProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53profiles-2018-05-10/AssociateProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53profiles-2018-05-10/AssociateProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53profiles-2018-05-10/AssociateProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53profiles-2018-05-10/AssociateProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53profiles-2018-05-10/AssociateProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53profiles-2018-05-10/AssociateProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53profiles-2018-05-10/AssociateProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53profiles-2018-05-10/AssociateProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53profiles-2018-05-10/AssociateProfile)
