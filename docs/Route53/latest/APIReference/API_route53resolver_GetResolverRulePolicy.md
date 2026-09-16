---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverRulePolicy.html
---

# GetResolverRulePolicy
<a name="API_route53resolver_GetResolverRulePolicy"></a>

Gets information about the Resolver rule policy for a specified rule. A Resolver rule policy includes the rule that you want to share with another account, the account that you want to share the rule with, and the Resolver operations that you want to allow the account to use.

## Request Syntax
<a name="API_route53resolver_GetResolverRulePolicy_RequestSyntax"></a>

```
{
   "Arn": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_GetResolverRulePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Arn](#API_route53resolver_GetResolverRulePolicy_RequestSyntax) **   <a name="Route53Resolver-route53resolver_GetResolverRulePolicy-request-Arn"></a>
The ID of the Resolver rule that you want to get the Resolver rule policy for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_route53resolver_GetResolverRulePolicy_ResponseSyntax"></a>

```
{
   "ResolverRulePolicy": "string"
}
```

## Response Elements
<a name="API_route53resolver_GetResolverRulePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResolverRulePolicy](#API_route53resolver_GetResolverRulePolicy_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_GetResolverRulePolicy-response-ResolverRulePolicy"></a>
The Resolver rule policy for the rule that you specified in a `GetResolverRulePolicy` request.
Type: String
Length Constraints: Maximum length of 30000.

## Errors
<a name="API_route53resolver_GetResolverRulePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The current account doesn't have the IAM permissions required to perform the specified Resolver operation.
This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.
HTTP Status Code: 400

 ** InternalServiceErrorException **
We encountered an unknown error. Try again in a few minutes.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more parameters in this request are not valid.
 ** FieldName **
For an `InvalidParameterException` error, the name of the parameter that's invalid.
HTTP Status Code: 400

 ** UnknownResourceException **
The specified resource doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_route53resolver_GetResolverRulePolicy_Examples"></a>

### GetResolverRulePolicy Example
<a name="API_route53resolver_GetResolverRulePolicy_Example_1"></a>

This example illustrates one usage of GetResolverRulePolicy.

#### Sample Request
<a name="API_route53resolver_GetResolverRulePolicy_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 48
X-Amz-Target: Route53Resolver.GetResolverRulePolicy
X-Amz-Date: 20181101T192652Z
User-Agent: aws-cli/1.16.45 Python/2.7.10 Darwin/16.7.0 botocore/1.12.35
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-2/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "Arn": "arn:aws:route53resolver:us-east-2:123456789012:resolver-rule/rslvr-rr-5328a0899aexample"
}
```

#### Sample Response
<a name="API_route53resolver_GetResolverRulePolicy_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 01 Nov 2018 19:26:52 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 314
x-amzn-RequestId: 1d7c8aad-1c63-413d-88a9-bc7b0example
Connection: keep-alive

{
    "ResolverRulePolicy":{
      "Version": "2012-10-17",
      "Statement": [
         {
            "Effect" : "Allow",
            "Principal" : {"AWS" : [ "123456789012" ] },
            "Action" : [
               "route53resolver:GetResolverRule",
               "route53resolver:AssociateResolverRule",
               "route53resolver:DisassociateResolverRule",
               "route53resolver:ListResolverRules",
               "route53resolver:ListResolverRuleAssociations"
            ],
            "Resource" : [
               "arn:aws:route53resolver:us-east-2:123456789012:resolver-rule/rslvr-rr-5328a0899aexample"
            ]
         }
      ]
   }
}
```

## See Also
<a name="API_route53resolver_GetResolverRulePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/GetResolverRulePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/GetResolverRulePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/GetResolverRulePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/GetResolverRulePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/GetResolverRulePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/GetResolverRulePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/GetResolverRulePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/GetResolverRulePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/GetResolverRulePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/GetResolverRulePolicy)
