---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetComplianceDetail.html
---

# GetComplianceDetail
<a name="API_GetComplianceDetail"></a>

Returns detailed compliance information about the specified member account. Details include resources that are in and out of compliance with the specified policy.

The reasons for resources being considered compliant depend on the Firewall Manager policy type.

## Request Syntax
<a name="API_GetComplianceDetail_RequestSyntax"></a>

```
{
   "MemberAccount": "{{string}}",
   "PolicyId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetComplianceDetail_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MemberAccount](#API_GetComplianceDetail_RequestSyntax) **   <a name="fms-GetComplianceDetail-request-MemberAccount"></a>
The AWS account that owns the resources that you want to get the details for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`
Required: Yes

 ** [PolicyId](#API_GetComplianceDetail_RequestSyntax) **   <a name="fms-GetComplianceDetail-request-PolicyId"></a>
The ID of the policy that you want to get the details for. `PolicyId` is returned by `PutPolicy` and by `ListPolicies`.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-z0-9A-Z-]{36}$`
Required: Yes

## Response Syntax
<a name="API_GetComplianceDetail_ResponseSyntax"></a>

```
{
   "PolicyComplianceDetail": {
      "EvaluationLimitExceeded": boolean,
      "ExpiredAt": number,
      "IssueInfoMap": {
         "string" : "string"
      },
      "MemberAccount": "string",
      "PolicyId": "string",
      "PolicyOwner": "string",
      "Violators": [
         {
            "Metadata": {
               "string" : "string"
            },
            "ResourceId": "string",
            "ResourceType": "string",
            "ViolationReason": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_GetComplianceDetail_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PolicyComplianceDetail](#API_GetComplianceDetail_ResponseSyntax) **   <a name="fms-GetComplianceDetail-response-PolicyComplianceDetail"></a>
Information about the resources and the policy that you specified in the `GetComplianceDetail` request.
Type: [PolicyComplianceDetail](API_PolicyComplianceDetail.md) object

## Errors
<a name="API_GetComplianceDetail_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 400

 ** InvalidInputException **
The parameters of the request were invalid.
HTTP Status Code: 400

 ** InvalidOperationException **
The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an `AssociateAdminAccount` request for an account ID that was already set as the AWS Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for AWS Organizations before you can access it.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_GetComplianceDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/GetComplianceDetail)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/GetComplianceDetail)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/GetComplianceDetail)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/GetComplianceDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/GetComplianceDetail)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/GetComplianceDetail)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/GetComplianceDetail)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/GetComplianceDetail)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/GetComplianceDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/GetComplianceDetail)
