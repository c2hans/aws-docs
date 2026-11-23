---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHealthCheckSource.html
---

# CreateHealthCheckSource

Creates a health check source, which defines the virtual private cloud (VPC), subnets, and security groups from which Route 53 sends private endpoint health check requests. To use this operation, you must have the `route53:CreateHealthCheckSource` permission. You must also have permission to create a service-linked role.

Specify a VPC, one subnet in each Availability Zone that Route 53 uses for private endpoint health checks in the AWS Region, and one or more security groups for each subnet. The security groups must allow outbound traffic to the endpoints that you want to check.

Route 53 creates a health check source asynchronously, and the initial `HealthCheckSourceStatus` is `CREATE_PENDING`. Call `GetHealthCheckSource` until the status is `CREATE_COMPLETED` before you create health checks that use the source. You can't change the configuration of a health check source after you create it.

If AWS Identity and Access Management (IAM) is still deleting the Route 53 service-linked role for your account, the request fails with `InvalidInput`. Retry after the deletion completes.

## Request Syntax
<a name="API_CreateHealthCheckSource_RequestSyntax"></a>

```
POST /2013-04-01/healthchecksource HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateHealthCheckSourceRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <CallerReference>{{string}}</CallerReference>
   <HealthCheckSourceConfig>
      <SubnetConfigurationList>
         <SubnetConfiguration>
            <AvailabilityZoneId>{{string}}</AvailabilityZoneId>
            <SecurityGroupIdList>
               <SecurityGroupId>{{string}}</SecurityGroupId>
            </SecurityGroupIdList>
            <SubnetId>{{string}}</SubnetId>
         </SubnetConfiguration>
      </SubnetConfigurationList>
      <VpcId>{{string}}</VpcId>
   </HealthCheckSourceConfig>
   <Tags>
      <Tag>
         <Key>{{string}}</Key>
         <Value>{{string}}</Value>
      </Tag>
   </Tags>
</CreateHealthCheckSourceRequest>
```

## URI Request Parameters
<a name="API_CreateHealthCheckSource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateHealthCheckSource_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateHealthCheckSourceRequest](#API_CreateHealthCheckSource_RequestSyntax) **   <a name="Route53-CreateHealthCheckSource-request-CreateHealthCheckSourceRequest"></a>
Root level tag for the CreateHealthCheckSourceRequest parameters.
Required: Yes

 ** [CallerReference](#API_CreateHealthCheckSource_RequestSyntax) **   <a name="Route53-CreateHealthCheckSource-request-CallerReference"></a>
A unique, case-sensitive identifier that ensures that the operation completes no more than one time. If you retry a `CreateHealthCheckSource` request with the same `CallerReference` and the same settings as a previous request, Route 53 returns the existing health check source without creating a duplicate. If that health check source has a status of `CREATE_FAILED`, Route 53 tries to create it again. To create a new health check source after a failure, specify a new value for `CallerReference`. If a health check source with the same `CallerReference` already exists and the settings differ, Route 53 returns a `HealthCheckSourceAlreadyExists` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [HealthCheckSourceConfig](#API_CreateHealthCheckSource_RequestSyntax) **   <a name="Route53-CreateHealthCheckSource-request-HealthCheckSourceConfig"></a>
A complex type that contains the virtual private cloud (VPC), subnets, and security groups for the health check source.
Type: [HealthCheckSourceConfig](API_HealthCheckSourceConfig.md) object
Required: Yes

 ** [Tags](#API_CreateHealthCheckSource_RequestSyntax) **   <a name="Route53-CreateHealthCheckSource-request-Tags"></a>
A complex type that contains a list of the tags that you want to apply to the health check source when you create it.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## Response Syntax
<a name="API_CreateHealthCheckSource_ResponseSyntax"></a>

```
HTTP/1.1 201
Location: {{Location}}
<?xml version="1.0" encoding="UTF-8"?>
<CreateHealthCheckSourceResponse>
   <HealthCheckSourceId>string</HealthCheckSourceId>
   <HealthCheckSourceStatus>string</HealthCheckSourceStatus>
</CreateHealthCheckSourceResponse>
```

## Response Elements
<a name="API_CreateHealthCheckSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The response returns the following HTTP headers.

 ** [Location](#API_CreateHealthCheckSource_ResponseSyntax) **   <a name="Route53-CreateHealthCheckSource-response-Location"></a>
The unique URL representing the new health check source.
Length Constraints: Maximum length of 1024.

The following data is returned in XML format by the service.

 ** [CreateHealthCheckSourceResponse](#API_CreateHealthCheckSource_ResponseSyntax) **   <a name="Route53-CreateHealthCheckSource-response-CreateHealthCheckSourceResponse"></a>
Root level tag for the CreateHealthCheckSourceResponse parameters.
Required: Yes

 ** [HealthCheckSourceId](#API_CreateHealthCheckSource_ResponseSyntax) **   <a name="Route53-CreateHealthCheckSource-response-HealthCheckSourceId"></a>
The ID of the new health check source. Route 53 assigns this ID when it creates the source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [HealthCheckSourceStatus](#API_CreateHealthCheckSource_ResponseSyntax) **   <a name="Route53-CreateHealthCheckSource-response-HealthCheckSourceStatus"></a>
The current status of the health check source. Immediately after you create a health check source, the status is `CREATE_PENDING`. If the request is a retry with the same `CallerReference`, the status is the current status of the existing health check source.
Type: String
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_COMPLETED | CREATE_FAILED | DELETE_PENDING | DELETE_IN_PROGRESS | DELETE_COMPLETED | DELETE_FAILED`

## Errors
<a name="API_CreateHealthCheckSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** HealthCheckSourceAlreadyExists **
The health check source that you're attempting to create already exists. Route 53 returns this error when you submit a request that has the same value for `CallerReference` as an existing health check source and one or more values that differ from the existing health check source. To create another health check source, specify a new value for `CallerReference`. To find the existing health check source, call `ListHealthCheckSources`.
HTTP Status Code: 409

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** InvalidVPCId **
The VPC ID that you specified either isn't a valid ID or the current account is not authorized to access this VPC.
 ** message **

HTTP Status Code: 400

 ** TooManyHealthCheckSources **
You can't create this health check source because the current account has reached its maximum number of health check sources. The maximum includes every health check source that hasn't reached `DELETE_COMPLETED` status, including a health check source with a status of `CREATE_FAILED`.
For information about default limits, see [Limits](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html) in the *Amazon Route 53 Developer Guide*.
For information about how to get the current limit for an account, see [GetAccountLimit](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetAccountLimit.html). To request a higher limit, [create a case](http://aws.amazon.com/route53-request) with the AWS Support Center.
HTTP Status Code: 400

## See Also
<a name="API_CreateHealthCheckSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/CreateHealthCheckSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/CreateHealthCheckSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/CreateHealthCheckSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/CreateHealthCheckSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/CreateHealthCheckSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/CreateHealthCheckSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/CreateHealthCheckSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/CreateHealthCheckSource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/CreateHealthCheckSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/CreateHealthCheckSource)
