---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHealthCheckSource.html
---

# GetHealthCheckSource

Gets information about a specified health check source, including its status and the virtual private cloud (VPC), subnets, and security groups that it uses.

## Request Syntax
<a name="API_GetHealthCheckSource_RequestSyntax"></a>

```
GET /2013-04-01/healthchecksource/{{HealthCheckSourceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetHealthCheckSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HealthCheckSourceId](#API_GetHealthCheckSource_RequestSyntax) **   <a name="Route53-GetHealthCheckSource-request-uri-HealthCheckSourceId"></a>
The ID of the health check source that you want to get information about.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Request Body
<a name="API_GetHealthCheckSource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetHealthCheckSource_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetHealthCheckSourceResponse>
   <HealthCheckSource>
      <HealthCheckSourceConfig>
         <SubnetConfigurationList>
            <SubnetConfiguration>
               <AvailabilityZoneId>string</AvailabilityZoneId>
               <SecurityGroupIdList>
                  <SecurityGroupId>string</SecurityGroupId>
               </SecurityGroupIdList>
               <SubnetId>string</SubnetId>
            </SubnetConfiguration>
         </SubnetConfigurationList>
         <VpcId>string</VpcId>
      </HealthCheckSourceConfig>
      <HealthCheckSourceId>string</HealthCheckSourceId>
      <HealthCheckSourceStatus>string</HealthCheckSourceStatus>
      <StatusReason>string</StatusReason>
      <StatusReasonCode>string</StatusReasonCode>
   </HealthCheckSource>
</GetHealthCheckSourceResponse>
```

## Response Elements
<a name="API_GetHealthCheckSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetHealthCheckSourceResponse](#API_GetHealthCheckSource_ResponseSyntax) **   <a name="Route53-GetHealthCheckSource-response-GetHealthCheckSourceResponse"></a>
Root level tag for the GetHealthCheckSourceResponse parameters.
Required: Yes

 ** [HealthCheckSource](#API_GetHealthCheckSource_ResponseSyntax) **   <a name="Route53-GetHealthCheckSource-response-HealthCheckSource"></a>
A complex type that contains information about the specified health check source.
Type: [HealthCheckSource](API_HealthCheckSource.md) object

## Errors
<a name="API_GetHealthCheckSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchHealthCheckSource **
No health check source exists with the specified ID. Verify that the ID is correct and that the health check source hasn't been deleted.
HTTP Status Code: 404

## See Also
<a name="API_GetHealthCheckSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/GetHealthCheckSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/GetHealthCheckSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GetHealthCheckSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/GetHealthCheckSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GetHealthCheckSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/GetHealthCheckSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/GetHealthCheckSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/GetHealthCheckSource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/GetHealthCheckSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GetHealthCheckSource)
