---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeComplianceByResource.html
---

# DescribeComplianceByResource
<a name="API_DescribeComplianceByResource"></a>

Indicates whether the specified AWS resources are compliant. If a resource is noncompliant, this operation returns the number of AWS Config rules that the resource does not comply with.

A resource is compliant if it complies with all the AWS Config rules that evaluate it. It is noncompliant if it does not comply with one or more of these rules.

If AWS Config has no current evaluation results for the resource, it returns `INSUFFICIENT_DATA`. This result might indicate one of the following conditions about the rules that evaluate the resource:
+  AWS Config has never invoked an evaluation for the rule. To check whether it has, use the `DescribeConfigRuleEvaluationStatus` action to get the `LastSuccessfulInvocationTime` and `LastFailedInvocationTime`.
+ The rule's AWS Lambda function is failing to send evaluation results to AWS Config. Verify that the role that you assigned to your configuration recorder includes the `config:PutEvaluations` permission. If the rule is a custom rule, verify that the AWS Lambda execution role includes the `config:PutEvaluations` permission.
+ The rule's AWS Lambda function has returned `NOT_APPLICABLE` for all evaluation results. This can occur if the resources were deleted or removed from the rule's scope.

## Request Syntax
<a name="API_DescribeComplianceByResource_RequestSyntax"></a>

```
{
   "ComplianceTypes": [ "{{string}}" ],
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "ResourceId": "{{string}}",
   "ResourceType": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeComplianceByResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ComplianceTypes](#API_DescribeComplianceByResource_RequestSyntax) **   <a name="config-DescribeComplianceByResource-request-ComplianceTypes"></a>
Filters the results by compliance.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Valid Values: `COMPLIANT | NON_COMPLIANT | NOT_APPLICABLE | INSUFFICIENT_DATA`
Required: No

 ** [Limit](#API_DescribeComplianceByResource_RequestSyntax) **   <a name="config-DescribeComplianceByResource-request-Limit"></a>
The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeComplianceByResource_RequestSyntax) **   <a name="config-DescribeComplianceByResource-request-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

 ** [ResourceId](#API_DescribeComplianceByResource_RequestSyntax) **   <a name="config-DescribeComplianceByResource-request-ResourceId"></a>
The ID of the AWS resource for which you want compliance information. You can specify only one resource ID. If you specify a resource ID, you must also specify a type for `ResourceType`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 768.
Required: No

 ** [ResourceType](#API_DescribeComplianceByResource_RequestSyntax) **   <a name="config-DescribeComplianceByResource-request-ResourceType"></a>
The types of AWS resources for which you want compliance information (for example, `AWS::EC2::Instance`). For this operation, you can specify that the resource type is an AWS account by specifying `AWS::::Account`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_DescribeComplianceByResource_ResponseSyntax"></a>

```
{
   "ComplianceByResources": [
      {
         "Compliance": {
            "ComplianceContributorCount": {
               "CapExceeded": boolean,
               "CappedCount": number
            },
            "ComplianceType": "string"
         },
         "ResourceId": "string",
         "ResourceType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeComplianceByResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ComplianceByResources](#API_DescribeComplianceByResource_ResponseSyntax) **   <a name="config-DescribeComplianceByResource-response-ComplianceByResources"></a>
Indicates whether the specified AWS resource complies with all of the AWS Config rules that evaluate it.
Type: Array of [ComplianceByResource](API_ComplianceByResource.md) objects

 ** [NextToken](#API_DescribeComplianceByResource_ResponseSyntax) **   <a name="config-DescribeComplianceByResource-response-NextToken"></a>
The string that you use in a subsequent request to get the next page of results in a paginated response.
Type: String

## Errors
<a name="API_DescribeComplianceByResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

## See Also
<a name="API_DescribeComplianceByResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DescribeComplianceByResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DescribeComplianceByResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeComplianceByResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DescribeComplianceByResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeComplianceByResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DescribeComplianceByResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DescribeComplianceByResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DescribeComplianceByResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DescribeComplianceByResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeComplianceByResource)
