---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_UpdateProfileAssociation.html
---

# UpdateProfileAssociation
<a name="API_route53profiles_UpdateProfileAssociation"></a>

 Updates the name or priority of the specified Route 53 Profile association with a VPC. Route 53 VPC Resolver evaluates the Profile associations for a VPC in priority order, starting with the lowest value. Only the account that created the association can update it.

 When you change the priority, the association status is `UPDATING` until the change propagates, and then `COMPLETE`. While the status is `UPDATING`, Route 53 VPC Resolver might still use the previous priority for some queries. When the status is `COMPLETE`, the new priority applies to all queries from the VPC.

 The request fails with a `ValidationException` if another Profile association for the VPC already uses the priority that you specify, or if the priority is outside the range 100–9900.

 You can update an association whose status is `CREATING`, `UPDATING`, or `COMPLETE`. The request fails with a `ConflictException` if the association status is `DELETING`, `DELETED`, or `FAILED`, or if the account that owns the association is inactive.

## Request Syntax
<a name="API_route53profiles_UpdateProfileAssociation_RequestSyntax"></a>

```
PATCH /profileassociation/{{ProfileAssociationId}} HTTP/1.1
Content-type: application/json

{
   "Name": "{{string}}",
   "Priority": {{number}}
}
```

## URI Request Parameters
<a name="API_route53profiles_UpdateProfileAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ProfileAssociationId](#API_route53profiles_UpdateProfileAssociation_RequestSyntax) **   <a name="Route53Profiles-route53profiles_UpdateProfileAssociation-request-uri-ProfileAssociationId"></a>
 The ID of the Profile association to update.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Request Body
<a name="API_route53profiles_UpdateProfileAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_route53profiles_UpdateProfileAssociation_RequestSyntax) **   <a name="Route53Profiles-route53profiles_UpdateProfileAssociation-request-Name"></a>
 The name of the Profile association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: No

 ** [Priority](#API_route53profiles_UpdateProfileAssociation_RequestSyntax) **   <a name="Route53Profiles-route53profiles_UpdateProfileAssociation-request-Priority"></a>
 The new priority of the Profile association. Route 53 VPC Resolver evaluates the Profile associations for a VPC in priority order, starting with the lowest value.
The priority must be unique among the Profile associations for the VPC.
Type: Integer
Valid Range: Minimum value of 100. Maximum value of 9900.
Required: No

## Response Syntax
<a name="API_route53profiles_UpdateProfileAssociation_ResponseSyntax"></a>

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
      "Priority": number,
      "ProfileId": "string",
      "ResourceId": "string",
      "Status": "string",
      "StatusMessage": "string"
   }
}
```

## Response Elements
<a name="API_route53profiles_UpdateProfileAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProfileAssociation](#API_route53profiles_UpdateProfileAssociation_ResponseSyntax) **   <a name="Route53Profiles-route53profiles_UpdateProfileAssociation-response-ProfileAssociation"></a>
 Information about the `UpdateProfileAssociation` request, including a status message.
Type: [ProfileAssociation](API_route53profiles_ProfileAssociation.md) object

## Errors
<a name="API_route53profiles_UpdateProfileAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The current account doesn't have the IAM permissions required to perform the specified operation.
HTTP Status Code: 400

 ** ConflictException **
 The request you submitted conflicts with an existing request.
HTTP Status Code: 400

 ** InternalServiceErrorException **
 An internal server error occured. Retry your request.
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
<a name="API_route53profiles_UpdateProfileAssociation_Examples"></a>

### UpdateProfileAssociation Example
<a name="API_route53profiles_UpdateProfileAssociation_Example_1"></a>

This example illustrates one usage of UpdateProfileAssociation.

#### Sample Request
<a name="API_route53profiles_UpdateProfileAssociation_Example_1_Request"></a>

```
PATCH /profileassociation/rpassoc-489ce212fexample HTTP/1.1
host:route53profiles.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 23
X-Amz-Date:20240319T231512Z
User-Agent: aws-cli/1.32.63 botocore/1.34.63 Python/3.8.18
Content-Type: application/json
Authorization: AWS4-HMAC-SHA256
    Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-1/route53profiles/aws4_request,
    SignedHeaders=content-type;host;x-amz-date;x-amz-security-token
    Signature=[calculated-signature]
{
    "Priority": 150
}
```

#### Sample Response
<a name="API_route53profiles_UpdateProfileAssociation_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 19 Mar 2024 23:15:12 GMT
Content-Type: application/json
Content-Length: 324
Connection: keep-alive
x-amzn-RequestId: dcd9d91e-1a5a-481f-82b7-bafe7dexample
Access-Control-Allow-Origin: *
x-amz-apigw-id: U5eX0FdmIexample=
X-Amzn-Trace-Id: Root=1-65fa10fe-6e5a93a56a325ab8example
{
    "ProfileAssociation": {
        "CreationTime": 1710886843.849,
        "Id": "rpassoc-489ce212fexample",
        "ModificationTime": 1710890112.402,
        "Name": "test-association",
        "OwnerId": "123456789012",
        "ProfileId": "rp-4987774726example",
        "ResourceId": "vpc-0af3b96b3example",
        "Priority": 150,
        "Status": "UPDATING",
        "StatusMessage": "Updating Profile Association"
    }
}
```

## See Also
<a name="API_route53profiles_UpdateProfileAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53profiles-2018-05-10/UpdateProfileAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53profiles-2018-05-10/UpdateProfileAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53profiles-2018-05-10/UpdateProfileAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53profiles-2018-05-10/UpdateProfileAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53profiles-2018-05-10/UpdateProfileAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53profiles-2018-05-10/UpdateProfileAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53profiles-2018-05-10/UpdateProfileAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53profiles-2018-05-10/UpdateProfileAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53profiles-2018-05-10/UpdateProfileAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53profiles-2018-05-10/UpdateProfileAssociation)
