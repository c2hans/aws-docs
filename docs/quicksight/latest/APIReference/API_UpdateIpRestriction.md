---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateIpRestriction.html
---

# UpdateIpRestriction
<a name="API_UpdateIpRestriction"></a>

Updates the content and status of IP rules. Traffic from a source is allowed when the source satisfies either the `IpRestrictionRule`, `VpcIdRestrictionRule`, or `VpcEndpointIdRestrictionRule`. To use this operation, you must provide the entire map of rules. You can use the `DescribeIpRestriction` operation to get the current rule map.

## Request Syntax
<a name="API_UpdateIpRestriction_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/ip-restriction HTTP/1.1
Content-type: application/json

{
   "Enabled": {{boolean}},
   "IpRestrictionRuleMap": {
      "{{string}}" : "{{string}}"
   },
   "VpcEndpointIdRestrictionRuleMap": {
      "{{string}}" : "{{string}}"
   },
   "VpcIdRestrictionRuleMap": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateIpRestriction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateIpRestriction_RequestSyntax) **   <a name="QS-UpdateIpRestriction-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the IP rules.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_UpdateIpRestriction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Enabled](#API_UpdateIpRestriction_RequestSyntax) **   <a name="QS-UpdateIpRestriction-request-Enabled"></a>
A value that specifies whether IP rules are turned on.
Type: Boolean
Required: No

 ** [IpRestrictionRuleMap](#API_UpdateIpRestriction_RequestSyntax) **   <a name="QS-UpdateIpRestriction-request-IpRestrictionRuleMap"></a>
A map that describes the updated IP rules with CIDR ranges and descriptions.
Type: String to string map
Key Pattern: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[1-9]))$`
Value Length Constraints: Minimum length of 0. Maximum length of 150.
Required: No

 ** [VpcEndpointIdRestrictionRuleMap](#API_UpdateIpRestriction_RequestSyntax) **   <a name="QS-UpdateIpRestriction-request-VpcEndpointIdRestrictionRuleMap"></a>
A map of allowed VPC endpoint IDs and their corresponding rule descriptions.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `^vpce-[0-9a-z]*$`
Value Length Constraints: Minimum length of 0. Maximum length of 150.
Required: No

 ** [VpcIdRestrictionRuleMap](#API_UpdateIpRestriction_RequestSyntax) **   <a name="QS-UpdateIpRestriction-request-VpcIdRestrictionRuleMap"></a>
A map of VPC IDs and their corresponding rules. When you configure this parameter, traffic from all VPC endpoints that are present in the specified VPC is allowed.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `^vpc-[0-9a-z]*$`
Value Length Constraints: Minimum length of 0. Maximum length of 150.
Required: No

## Response Syntax
<a name="API_UpdateIpRestriction_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AwsAccountId": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateIpRestriction_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateIpRestriction_ResponseSyntax) **   <a name="QS-UpdateIpRestriction-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AwsAccountId](#API_UpdateIpRestriction_ResponseSyntax) **   <a name="QS-UpdateIpRestriction-response-AwsAccountId"></a>
The ID of the AWS account that contains the IP rules.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`

 ** [RequestId](#API_UpdateIpRestriction_ResponseSyntax) **   <a name="QS-UpdateIpRestriction-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateIpRestriction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateIpRestriction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateIpRestriction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateIpRestriction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateIpRestriction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateIpRestriction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateIpRestriction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateIpRestriction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateIpRestriction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateIpRestriction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateIpRestriction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateIpRestriction)
