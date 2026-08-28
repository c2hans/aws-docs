---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateFirewallRuleGroup.html
---

# AssociateFirewallRuleGroup
<a name="API_route53resolver_AssociateFirewallRuleGroup"></a>

Associates a [FirewallRuleGroup](API_route53resolver_FirewallRuleGroup.md) with a VPC, to provide DNS filtering for the VPC.

If the rule group contains any rule configured with the `PartnerThreatProtection` rule type, the calling account must hold an active AWS Marketplace subscription to the named partner. If the subscription is missing, the association request is rejected.

## Request Syntax
<a name="API_route53resolver_AssociateFirewallRuleGroup_RequestSyntax"></a>

```
{
   "CreatorRequestId": "{{string}}",
   "FirewallRuleGroupId": "{{string}}",
   "MutationProtection": "{{string}}",
   "Name": "{{string}}",
   "Priority": {{number}},
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VpcId": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_AssociateFirewallRuleGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreatorRequestId](#API_route53resolver_AssociateFirewallRuleGroup_RequestSyntax) **   <a name="Route53Resolver-route53resolver_AssociateFirewallRuleGroup-request-CreatorRequestId"></a>
A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. `CreatorRequestId` can be any unique string, for example, a date/time stamp.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [FirewallRuleGroupId](#API_route53resolver_AssociateFirewallRuleGroup_RequestSyntax) **   <a name="Route53Resolver-route53resolver_AssociateFirewallRuleGroup-request-FirewallRuleGroupId"></a>
The unique identifier of the firewall rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [MutationProtection](#API_route53resolver_AssociateFirewallRuleGroup_RequestSyntax) **   <a name="Route53Resolver-route53resolver_AssociateFirewallRuleGroup-request-MutationProtection"></a>
If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections. When you create the association, the default setting is `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [Name](#API_route53resolver_AssociateFirewallRuleGroup_RequestSyntax) **   <a name="Route53Resolver-route53resolver_AssociateFirewallRuleGroup-request-Name"></a>
A name that lets you identify the association, to manage and use it.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: Yes

 ** [Priority](#API_route53resolver_AssociateFirewallRuleGroup_RequestSyntax) **   <a name="Route53Resolver-route53resolver_AssociateFirewallRuleGroup-request-Priority"></a>
The setting that determines the processing order of the rule group among the rule groups that you associate with the specified VPC. DNS Firewall filters VPC traffic starting from the rule group with the lowest numeric priority setting.
You must specify a unique priority for each rule group that you associate with a single VPC. To make it easier to insert rule groups later, leave space between the numbers, for example, use 101, 200, and so on. You can change the priority setting for a rule group association after you create it.
The allowed values for `Priority` are between 100 and 9900.
Type: Integer
Required: Yes

 ** [Tags](#API_route53resolver_AssociateFirewallRuleGroup_RequestSyntax) **   <a name="Route53Resolver-route53resolver_AssociateFirewallRuleGroup-request-Tags"></a>
A list of the tag keys and values that you want to associate with the rule group association.
Type: Array of [Tag](API_route53resolver_Tag.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** [VpcId](#API_route53resolver_AssociateFirewallRuleGroup_RequestSyntax) **   <a name="Route53Resolver-route53resolver_AssociateFirewallRuleGroup-request-VpcId"></a>
The unique identifier of the VPC that you want to associate with the rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_route53resolver_AssociateFirewallRuleGroup_ResponseSyntax"></a>

```
{
   "FirewallRuleGroupAssociation": {
      "Arn": "string",
      "CreationTime": "string",
      "CreatorRequestId": "string",
      "FirewallRuleGroupId": "string",
      "Id": "string",
      "ManagedOwnerName": "string",
      "ModificationTime": "string",
      "MutationProtection": "string",
      "Name": "string",
      "Priority": number,
      "Status": "string",
      "StatusMessage": "string",
      "VpcId": "string"
   }
}
```

## Response Elements
<a name="API_route53resolver_AssociateFirewallRuleGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FirewallRuleGroupAssociation](#API_route53resolver_AssociateFirewallRuleGroup_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_AssociateFirewallRuleGroup-response-FirewallRuleGroupAssociation"></a>
The association that you just created. The association has an ID that you can use to identify it in other requests, like update and delete.
Type: [FirewallRuleGroupAssociation](API_route53resolver_FirewallRuleGroupAssociation.md) object

## Errors
<a name="API_route53resolver_AssociateFirewallRuleGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The current account doesn't have the IAM permissions required to perform the specified Resolver operation.
This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.
HTTP Status Code: 400

 ** ConflictException **
The requested state transition isn't valid. For example, you can't delete a firewall domain list if it is in the process of being deleted, or you can't import domains into a domain list that is in the process of being deleted.
HTTP Status Code: 400

 ** InternalServiceErrorException **
We encountered an unknown error. Try again in a few minutes.
HTTP Status Code: 400

 ** LimitExceededException **
The request caused one or more limits to be exceeded.
 ** ResourceType **
For a `LimitExceededException` error, the type of resource that exceeded the current limit.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource doesn't exist.
 ** ResourceType **
For a `ResourceNotFoundException` error, the type of resource that doesn't exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

 ** ValidationException **
You have provided an invalid command. If you ran the `UpdateFirewallDomains` request. supported values are `ADD`, `REMOVE`, or `REPLACE` a domain.
HTTP Status Code: 400

## Examples
<a name="API_route53resolver_AssociateFirewallRuleGroup_Examples"></a>

### AssociateFirewallRuleGroup Example
<a name="API_route53resolver_AssociateFirewallRuleGroup_Example_1"></a>

This example illustrates one usage of AssociateFirewallRuleGroup.

#### Sample Request
<a name="API_route53resolver_AssociateFirewallRuleGroup_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 220
X-Amz-Target: Route53Resolver.AssociateFirewallRuleGroup
X-Amz-Date: 20260420T120000Z
User-Agent: aws-cli/2.15.0 Python/3.11.6
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20260420/us-east-1/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "CreatorRequestId": "associate-frg-1",
    "FirewallRuleGroupId": "rslvr-frg-47f93271fexample",
    "VpcId": "vpc-0fa1b2c3d4e5f6a7b",
    "Priority": 101,
    "Name": "primary-firewall"
}
```

#### Sample Response
<a name="API_route53resolver_AssociateFirewallRuleGroup_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Sun, 20 Apr 2026 12:00:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 480
x-amzn-RequestId: 1f2e3d4c-5b6a-7980-1234-5e6f7example
Connection: keep-alive

{
    "FirewallRuleGroupAssociation": {
        "Id": "rslvr-frgassoc-9a8b7c6d5example",
        "Arn": "arn:aws:route53resolver:us-east-1:111122223333:firewall-rule-group-association/rslvr-frgassoc-9a8b7c6d5example",
        "FirewallRuleGroupId": "rslvr-frg-47f93271fexample",
        "VpcId": "vpc-0fa1b2c3d4e5f6a7b",
        "Name": "primary-firewall",
        "Priority": 101,
        "MutationProtection": "DISABLED",
        "ManagedOwnerName": "111122223333",
        "Status": "UPDATING",
        "StatusMessage": "Creating Firewall Rule Group Association",
        "CreatorRequestId": "associate-frg-1",
        "CreationTime": "2026-04-20T12:00:00.000Z",
        "ModificationTime": "2026-04-20T12:00:00.000Z"
    }
}
```

## See Also
<a name="API_route53resolver_AssociateFirewallRuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/AssociateFirewallRuleGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/AssociateFirewallRuleGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/AssociateFirewallRuleGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/AssociateFirewallRuleGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/AssociateFirewallRuleGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/AssociateFirewallRuleGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/AssociateFirewallRuleGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/AssociateFirewallRuleGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/AssociateFirewallRuleGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/AssociateFirewallRuleGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
