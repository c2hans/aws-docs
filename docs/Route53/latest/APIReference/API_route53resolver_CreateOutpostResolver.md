---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateOutpostResolver.html
---

# CreateOutpostResolver
<a name="API_route53resolver_CreateOutpostResolver"></a>

Creates a Amazon Route 53 Resolver on an Outpost.

## Request Syntax
<a name="API_route53resolver_CreateOutpostResolver_RequestSyntax"></a>

```
{
   "CreatorRequestId": "{{string}}",
   "InstanceCount": {{number}},
   "Name": "{{string}}",
   "OutpostArn": "{{string}}",
   "PreferredInstanceType": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_route53resolver_CreateOutpostResolver_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreatorRequestId](#API_route53resolver_CreateOutpostResolver_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateOutpostResolver-request-CreatorRequestId"></a>
A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice.
 `CreatorRequestId` can be any unique string, for example, a date/time stamp.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [InstanceCount](#API_route53resolver_CreateOutpostResolver_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateOutpostResolver-request-InstanceCount"></a>
Number of Amazon EC2 instances for the Resolver on Outpost. The default and minimal value is 4.
Type: Integer
Required: No

 ** [Name](#API_route53resolver_CreateOutpostResolver_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateOutpostResolver-request-Name"></a>
A friendly name that lets you easily find a configuration in the Resolver dashboard in the Route 53 console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [OutpostArn](#API_route53resolver_CreateOutpostResolver_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateOutpostResolver-request-OutpostArn"></a>
The Amazon Resource Name (ARN) of the Outpost. If you specify this, you must also specify a value for the `PreferredInstanceType`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}$`
Required: Yes

 ** [PreferredInstanceType](#API_route53resolver_CreateOutpostResolver_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateOutpostResolver-request-PreferredInstanceType"></a>
 The Amazon EC2 instance type. If you specify this, you must also specify a value for the `OutpostArn`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Tags](#API_route53resolver_CreateOutpostResolver_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateOutpostResolver-request-Tags"></a>
 A string that helps identify the Route 53 Resolvers on Outpost.
Type: Array of [Tag](API_route53resolver_Tag.md) objects
Array Members: Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_route53resolver_CreateOutpostResolver_ResponseSyntax"></a>

```
{
   "OutpostResolver": {
      "Arn": "string",
      "CreationTime": "string",
      "CreatorRequestId": "string",
      "Id": "string",
      "InstanceCount": number,
      "ModificationTime": "string",
      "Name": "string",
      "OutpostArn": "string",
      "PreferredInstanceType": "string",
      "Status": "string",
      "StatusMessage": "string"
   }
}
```

## Response Elements
<a name="API_route53resolver_CreateOutpostResolver_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OutpostResolver](#API_route53resolver_CreateOutpostResolver_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_CreateOutpostResolver-response-OutpostResolver"></a>
Information about the `CreateOutpostResolver` request, including the status of the request.
Type: [OutpostResolver](API_route53resolver_OutpostResolver.md) object

## Errors
<a name="API_route53resolver_CreateOutpostResolver_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The current account doesn't have the IAM permissions required to perform the specified Resolver operation.
This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.
HTTP Status Code: 400

 ** InternalServiceErrorException **
We encountered an unknown error. Try again in a few minutes.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource doesn't exist.
 ** ResourceType **
For a `ResourceNotFoundException` error, the type of resource that doesn't exist.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
Fulfilling the request would cause one or more quotas to be exceeded.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

 ** ValidationException **
You have provided an invalid command. If you ran the `UpdateFirewallDomains` request. supported values are `ADD`, `REMOVE`, or `REPLACE` a domain.
HTTP Status Code: 400

## Examples
<a name="API_route53resolver_CreateOutpostResolver_Examples"></a>

### CreateOutpostResolver Example
<a name="API_route53resolver_CreateOutpostResolver_Example_1"></a>

This example illustrates one usage of CreateOutpostResolver.

#### Sample Request
<a name="API_route53resolver_CreateOutpostResolver_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 214
X-Amz-Target: Route53Resolver.CreateOutpostResolver
X-Amz-Date: 20230718T192937Z
User-Agent: aws-cli/2.11.9 Python/3.11.2 Darwin/22.5.0 exe/x86_64 prompt/off command/route53resolver.create-outpost-resolver
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20230718/us-west-2/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-security-token;x-amz-target,
               Signature=[calculated-signature]

{
    "CreatorRequestId": "my-first-outpost-resolver",
    "Name": "ResolverForOp0123example456op7",
    "PreferredInstanceType": "m5.large",
    "OutpostArn": "arn:aws:outposts:us-west-2:123456789012:outpost/op-0123example456op7"
}
```

#### Sample Response
<a name="API_route53resolver_CreateOutpostResolver_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 18 Jul 2023 19:29:39 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 559
x-amzn-RequestId: 08afd081-9d67-4281-a277-b3880example
Connection: keep-alive

{
    "OutpostResolver": {
        "Arn": "arn:aws:route53resolver:us-west-2:123456789012:outpost-resolver/rslvr-op-b12345example678",
        "CreationTime": "2023-07-18T19:29:39.697440Z",
        "ModificationTime": "2023-07-18T19:29:39.697440Z",
        "CreatorRequestId": "my-first-outpost-resolver",
        "Id": "rslvr-op-b12345example678",
        "InstanceCount": 4,
        "PreferredInstanceType": "m5.large",
        "Name": "ResolverForOp0123example456op7",
        "Status": "CREATING",
        "StatusMessage": "Creating the Resolver might take up to 90 minutes.",
        "OutpostArn": "arn:aws:outposts:us-west-2:123456789012:outpost/op-0123example456op7"
    }
}
```

## See Also
<a name="API_route53resolver_CreateOutpostResolver_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/CreateOutpostResolver)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/CreateOutpostResolver)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/CreateOutpostResolver)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/CreateOutpostResolver)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/CreateOutpostResolver)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/CreateOutpostResolver)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/CreateOutpostResolver)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/CreateOutpostResolver)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/CreateOutpostResolver)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/CreateOutpostResolver)
