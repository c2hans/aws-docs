---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_AssociateResourceShare.html
---

# AssociateResourceShare
<a name="API_AssociateResourceShare"></a>

Adds the specified list of principals, resources, and source constraints to a resource share. Principals that already have access to this resource share immediately receive access to the added resources. Newly added principals immediately receive access to the resources shared in this resource share.

## Request Syntax
<a name="API_AssociateResourceShare_RequestSyntax"></a>

```
POST /associateresourceshare HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "principals": [ "{{string}}" ],
   "resourceArns": [ "{{string}}" ],
   "resourceShareArn": "{{string}}",
   "sources": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_AssociateResourceShare_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AssociateResourceShare_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourceShareArn](#API_AssociateResourceShare_RequestSyntax) **   <a name="ram-AssociateResourceShare-request-resourceShareArn"></a>
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource share that you want to add principals or resources to.
Type: String
Required: Yes

 ** [clientToken](#API_AssociateResourceShare_RequestSyntax) **   <a name="ram-AssociateResourceShare-request-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Required: No

 ** [principals](#API_AssociateResourceShare_RequestSyntax) **   <a name="ram-AssociateResourceShare-request-principals"></a>
Specifies a list of principals to whom you want to the resource share. This can be `null` if you want to add only resources.
What the principals can do with the resources in the share is determined by the AWS RAM permissions that you associate with the resource share. See [AssociateResourceSharePermission](API_AssociateResourceSharePermission.md).
You can include the following values:
+ An AWS account ID, for example: `123456789012`
+ An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of an organization in AWS Organizations, for example: `arn:aws:organizations::123456789012:organization/o-exampleorgid`
+ An ARN of an organizational unit (OU) in AWS Organizations, for example: `arn:aws:organizations::123456789012:ou/o-exampleorgid/ou-examplerootid-exampleouid123`
+ An ARN of an IAM role, for example: `arn:aws:iam::123456789012:role/rolename`
+ An ARN of an IAM user, for example: `arn:aws:iam::123456789012user/username`
+ A service principal name, for example: `service-id.amazonaws.com`
Not all resource types can be shared with IAM roles and users. For more information, see [Sharing with IAM roles and users](https://docs.aws.amazon.com/ram/latest/userguide/permissions.html#permissions-rbp-supported-resource-types) in the * AWS Resource Access Manager User Guide*.
Type: Array of strings
Required: No

 ** [resourceArns](#API_AssociateResourceShare_RequestSyntax) **   <a name="ram-AssociateResourceShare-request-resourceArns"></a>
Specifies a list of [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resources that you want to share. This can be `null` if you want to add only principals.
Type: Array of strings
Required: No

 ** [sources](#API_AssociateResourceShare_RequestSyntax) **   <a name="ram-AssociateResourceShare-request-sources"></a>
Specifies source constraints (accounts, ARNs, organization IDs, or organization paths) that limit when service principals can access resources in this resource share. When a service principal attempts to access a shared resource, validation is performed to ensure the request originates from one of the specified sources. This helps prevent confused deputy attacks by applying constraints on where service principals can access resources from.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_AssociateResourceShare_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "resourceShareAssociations": [
      {
         "associatedEntity": "string",
         "associationType": "string",
         "creationTime": number,
         "external": boolean,
         "lastUpdatedTime": number,
         "resourceShareArn": "string",
         "resourceShareName": "string",
         "status": "string",
         "statusMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_AssociateResourceShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_AssociateResourceShare_ResponseSyntax) **   <a name="ram-AssociateResourceShare-response-clientToken"></a>
The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the `clientToken` request parameter of that later call. All other parameters must also have the same values that you used in the first call.
Type: String

 ** [resourceShareAssociations](#API_AssociateResourceShare_ResponseSyntax) **   <a name="ram-AssociateResourceShare-response-resourceShareAssociations"></a>
An array of objects that contain information about the associations.
Type: Array of [ResourceShareAssociation](API_ResourceShareAssociation.md) objects

## Errors
<a name="API_AssociateResourceShare_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IdempotentParameterMismatchException **
The operation failed because the client token input parameter matched one that was used with a previous call to the operation, but at least one of the other input parameters is different from the previous call.
HTTP Status Code: 400

 ** InvalidClientTokenException **
The operation failed because the specified client token isn't valid.
HTTP Status Code: 400

 ** InvalidParameterException **
The operation failed because a parameter you specified isn't valid.
HTTP Status Code: 400

 ** InvalidStateTransitionException **
The operation failed because the requested operation isn't valid for the resource share in its current state.
HTTP Status Code: 400

 ** InvalidStateTransitionException **
The operation failed because the requested operation isn't valid for the resource share in its current state.
HTTP Status Code: 400

 ** MalformedArnException **
The operation failed because the specified [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) has a format that isn't valid.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The operation failed because the requested operation isn't permitted.
HTTP Status Code: 400

 ** ResourceShareLimitExceededException **
The operation failed because it would exceed the limit for resource shares for your account. You can associate up to 100 resources per call. To view the limits for your AWS account, see the [AWS RAM page in the Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/ram/quotas).
HTTP Status Code: 400

 ** ServerInternalException **
The operation failed because the service could not respond to the request due to an internal problem. Try again later.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The operation failed because the service isn't available. Try again later.
HTTP Status Code: 503

 ** ThrottlingException **
The operation failed because it exceeded the rate at which you are allowed to perform this operation. Please try again later.
HTTP Status Code: 429

 ** UnknownResourceException **
The operation failed because a specified resource couldn't be found.
HTTP Status Code: 400

 ** UnknownResourceException **
The operation failed because a specified resource couldn't be found.
HTTP Status Code: 400

## Examples
<a name="API_AssociateResourceShare_Examples"></a>

**Note**
The examples show the JSON payloads of the request and response pretty printed with white spaces and line breaks for ease for ease of reading.

### Example 1: add a principal to a resource share
<a name="API_AssociateResourceShare_Example_1"></a>

The following example illustrates adding an organizational unit (OU) as a principal to a resource share that exists in the AWS Region `us-east-1`. After running this command, all AWS accounts in the specified OU can access the resources in the resource share.

#### Sample Request
<a name="API_AssociateResourceShare_Example_1_Request"></a>

```
POST /associateresourceshare HTTP/1.1
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>>
X-Amz-Date: 20210923T200946Z

{
    "principals": [
        "arn:aws:organizations::999999999999:ou/o-12345abcde/ou-12ab-1234abcd"
    ],
    "resourceShareArn": "arn:aws:ram:us-east-1:999999999999:resource-share/27d09b4b-5e12-41d1-a4f2-19ded10982e2"
}
```

#### Sample Response
<a name="API_AssociateResourceShare_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 23 Sep 2021 20:09:46 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "resourceShareAssociations": [
        {
            "associatedEntity": "arn:aws:organizations::999999999999:ou/o-12345abcde/ou-12ab-1234abcd",
            "associationType": "PRINCIPAL",
            "external": false,
            "resourceShareArn": "arn:aws:ram:us-east-1:999999999999:resource-share/27d09b4b-5e12-41d1-a4f2-19ded10982e2",
            "status": "ASSOCIATING"
        }
    ]
}
```

### Example 2: Add a new resource to a resource share
<a name="API_AssociateResourceShare_Example_2"></a>

The following example illustrates adding an additional AWS License Manager configuration to a resource share. After running this command, all AWS accounts that can access the resource share can use the new resource.

#### Sample Request
<a name="API_AssociateResourceShare_Example_2_Request"></a>

```
POST /associateresourceshare HTTP/1.1
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>>
X-Amz-Date: 20210924T190541Z
{
    "resourceShareArn": "arn:aws:ram:us-east-1:999999999999:resource-share/27d09b4b-5e12-41d1-a4f2-19ded10982e2",
    "resourceArns": [
        "arn:aws:license-manager:us-east-1:999999999999:license-configuration:lic-36be0485f5ae379cc74cf8e9242ab143"
    ]
}
```

#### Sample Response
<a name="API_AssociateResourceShare_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Fri, 24 Sep 2021 19:05:42 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "resourceShareAssociations": [
        {
            "associatedEntity": "arn:aws:license-manager:us-east-1:999999999999:license-configuration:lic-36be0485f5ae379cc74cf8e9242ab143",
            "associationType": "RESOURCE",
            "external": false,
            "resourceShareArn": "arn:aws:ram:us-east-1:999999999999:resource-share/27d09b4b-5e12-41d1-a4f2-19ded10982e2",
            "status": "ASSOCIATING"
        }
    ]
}
```

## See Also
<a name="API_AssociateResourceShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/AssociateResourceShare)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/AssociateResourceShare)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/AssociateResourceShare)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/AssociateResourceShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/AssociateResourceShare)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/AssociateResourceShare)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/AssociateResourceShare)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/AssociateResourceShare)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/AssociateResourceShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/AssociateResourceShare)
