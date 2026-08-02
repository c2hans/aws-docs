---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetProtectionStatus.html
---

# GetProtectionStatus
<a name="API_GetProtectionStatus"></a>

If you created a Shield Advanced policy, returns policy-level attack summary information in the event of a potential DDoS attack. Other policy types are currently unsupported.

## Request Syntax
<a name="API_GetProtectionStatus_RequestSyntax"></a>

```
{
   "EndTime": {{number}},
   "MaxResults": {{number}},
   "MemberAccountId": "{{string}}",
   "NextToken": "{{string}}",
   "PolicyId": "{{string}}",
   "StartTime": {{number}}
}
```

## Request Parameters
<a name="API_GetProtectionStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndTime](#API_GetProtectionStatus_RequestSyntax) **   <a name="fms-GetProtectionStatus-request-EndTime"></a>
The end of the time period to query for the attacks. This is a `timestamp` type. The request syntax listing indicates a `number` type because the default used by AWS Firewall Manager is Unix time in seconds. However, any valid `timestamp` format is allowed.
Type: Timestamp
Required: No

 ** [MaxResults](#API_GetProtectionStatus_RequestSyntax) **   <a name="fms-GetProtectionStatus-request-MaxResults"></a>
Specifies the number of objects that you want AWS Firewall Manager to return for this request. If you have more objects than the number that you specify for `MaxResults`, the response includes a `NextToken` value that you can use to get another batch of objects.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [MemberAccountId](#API_GetProtectionStatus_RequestSyntax) **   <a name="fms-GetProtectionStatus-request-MemberAccountId"></a>
The AWS account that is in scope of the policy that you want to get the details for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`
Required: No

 ** [NextToken](#API_GetProtectionStatus_RequestSyntax) **   <a name="fms-GetProtectionStatus-request-NextToken"></a>
If you specify a value for `MaxResults` and you have more objects than the number that you specify for `MaxResults`, AWS Firewall Manager returns a `NextToken` value in the response, which you can use to retrieve another group of objects. For the second and subsequent `GetProtectionStatus` requests, specify the value of `NextToken` from the previous response to get information about another batch of objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** [PolicyId](#API_GetProtectionStatus_RequestSyntax) **   <a name="fms-GetProtectionStatus-request-PolicyId"></a>
The ID of the policy for which you want to get the attack information.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-z0-9A-Z-]{36}$`
Required: Yes

 ** [StartTime](#API_GetProtectionStatus_RequestSyntax) **   <a name="fms-GetProtectionStatus-request-StartTime"></a>
The start of the time period to query for the attacks. This is a `timestamp` type. The request syntax listing indicates a `number` type because the default used by AWS Firewall Manager is Unix time in seconds. However, any valid `timestamp` format is allowed.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_GetProtectionStatus_ResponseSyntax"></a>

```
{
   "AdminAccountId": "string",
   "Data": "string",
   "NextToken": "string",
   "ServiceType": "string"
}
```

## Response Elements
<a name="API_GetProtectionStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdminAccountId](#API_GetProtectionStatus_ResponseSyntax) **   <a name="fms-GetProtectionStatus-response-AdminAccountId"></a>
The ID of the AWS Firewall Manager administrator account for this policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`

 ** [Data](#API_GetProtectionStatus_ResponseSyntax) **   <a name="fms-GetProtectionStatus-response-Data"></a>
Details about the attack, including the following:
+ Attack type
+ Account ID
+ ARN of the resource attacked
+ Start time of the attack
+ End time of the attack (ongoing attacks will not have an end time)
The details are in JSON format.
Type: String

 ** [NextToken](#API_GetProtectionStatus_ResponseSyntax) **   <a name="fms-GetProtectionStatus-response-NextToken"></a>
If you have more objects than the number that you specified for `MaxResults` in the request, the response includes a `NextToken` value. To list more objects, submit another `GetProtectionStatus` request, and specify the `NextToken` value from the response in the `NextToken` value in the next request.
 AWS SDKs provide auto-pagination that identify `NextToken` in a response and make subsequent request calls automatically on your behalf. However, this feature is not supported by `GetProtectionStatus`. You must submit subsequent requests with `NextToken` using your own processes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

 ** [ServiceType](#API_GetProtectionStatus_ResponseSyntax) **   <a name="fms-GetProtectionStatus-response-ServiceType"></a>
The service type that is protected by the policy. Currently, this is always `SHIELD_ADVANCED`.
Type: String
Valid Values: `WAF | WAFV2 | SHIELD_ADVANCED | SECURITY_GROUPS_COMMON | SECURITY_GROUPS_CONTENT_AUDIT | SECURITY_GROUPS_USAGE_AUDIT | NETWORK_FIREWALL | DNS_FIREWALL | THIRD_PARTY_FIREWALL | IMPORT_NETWORK_FIREWALL | NETWORK_ACL_COMMON`

## Errors
<a name="API_GetProtectionStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 400

 ** InvalidInputException **
The parameters of the request were invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## Examples
<a name="API_GetProtectionStatus_Examples"></a>

### Example response
<a name="API_GetProtectionStatus_Example_1"></a>

This example illustrates one usage of GetProtectionStatus.

```
[
            {
            accountId: account1
            attackSummaries:[
            {
            attackId: attackId1
            resourceARN: resource1
            attackVector: [SYC_FLOOD, UDP_REFLECTION]
            startTime: 1234567890123
            endTime: 1234567890123
             },
             {
            attackId: attackId2
            resourceARN: resource2
            attackVector: [SYC_FLOOD]
            startTime: 1234567890123
            endTime: 1234567890123
            }
            ]
            },

            {
            accountId: account2
            attackSummaries:[
            {
            attackId: attackId3
            resourceARN: resource3
            attackVector: [SYC_FLOOD, UDP_REFLECTION]
            startTime: 1234567890123
            endTime: 1234567890123
            },
            {
            attackId: attackId4
            resourceARN: resource4
            attackVector: [SYC_FLOOD]
            startTime: 1234567890123
            endTime: 1234567890123
            }
            ]
            },
]
```

## See Also
<a name="API_GetProtectionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/GetProtectionStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/GetProtectionStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/GetProtectionStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/GetProtectionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/GetProtectionStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/GetProtectionStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/GetProtectionStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/GetProtectionStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/GetProtectionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/GetProtectionStatus)
