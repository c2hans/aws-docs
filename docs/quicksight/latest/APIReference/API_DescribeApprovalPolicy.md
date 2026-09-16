---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeApprovalPolicy.html
---

# DescribeApprovalPolicy
<a name="API_DescribeApprovalPolicy"></a>

Describes an approval policy in Quick Sight.

## Request Syntax
<a name="API_DescribeApprovalPolicy_RequestSyntax"></a>

```
GET /governance/approvalworkflows/policies/{{PolicyId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeApprovalPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [PolicyId](#API_DescribeApprovalPolicy_RequestSyntax) **   <a name="QS-DescribeApprovalPolicy-request-uri-PolicyId"></a>
The unique identifier of the approval policy to describe.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-_]+`
Required: Yes

## Request Body
<a name="API_DescribeApprovalPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeApprovalPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Policy": {
      "Actions": [ "string" ],
      "ApplicableTo": {
         "GroupArns": [ "string" ],
         "Type": "string"
      },
      "ApprovalGroups": [ "string" ],
      "AssetTypes": [ "string" ],
      "CreatedAt": number,
      "Description": "string",
      "Name": "string",
      "PolicyArn": "string",
      "PolicyId": "string",
      "UpdatedAt": number
   }
}
```

## Response Elements
<a name="API_DescribeApprovalPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_DescribeApprovalPolicy_ResponseSyntax) **   <a name="QS-DescribeApprovalPolicy-response-Policy"></a>
The approval policy.
Type: [ApprovalPolicy](API_ApprovalPolicy.md) object

## Errors
<a name="API_DescribeApprovalPolicy_Errors"></a>

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
<a name="API_DescribeApprovalPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeApprovalPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeApprovalPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeApprovalPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeApprovalPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeApprovalPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeApprovalPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeApprovalPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeApprovalPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeApprovalPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeApprovalPolicy)
