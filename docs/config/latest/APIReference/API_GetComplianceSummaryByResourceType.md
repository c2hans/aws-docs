---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_GetComplianceSummaryByResourceType.html
---

# GetComplianceSummaryByResourceType
<a name="API_GetComplianceSummaryByResourceType"></a>

Returns the number of resources that are compliant and the number that are noncompliant. You can specify one or more resource types to get these numbers for each resource type. The maximum number returned is 100.

## Request Syntax
<a name="API_GetComplianceSummaryByResourceType_RequestSyntax"></a>

```
{
   "ResourceTypes": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetComplianceSummaryByResourceType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceTypes](#API_GetComplianceSummaryByResourceType_RequestSyntax) **   <a name="config-GetComplianceSummaryByResourceType-request-ResourceTypes"></a>
Specify one or more resource types to get the number of resources that are compliant and the number that are noncompliant for each resource type.
For this request, you can specify an AWS resource type such as `AWS::EC2::Instance`. You can specify that the resource type is an AWS account by specifying `AWS::::Account`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_GetComplianceSummaryByResourceType_ResponseSyntax"></a>

```
{
   "ComplianceSummariesByResourceType": [
      {
         "ComplianceSummary": {
            "ComplianceSummaryTimestamp": number,
            "CompliantResourceCount": {
               "CapExceeded": boolean,
               "CappedCount": number
            },
            "NonCompliantResourceCount": {
               "CapExceeded": boolean,
               "CappedCount": number
            }
         },
         "ResourceType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetComplianceSummaryByResourceType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ComplianceSummariesByResourceType](#API_GetComplianceSummaryByResourceType_ResponseSyntax) **   <a name="config-GetComplianceSummaryByResourceType-response-ComplianceSummariesByResourceType"></a>
The number of resources that are compliant and the number that are noncompliant. If one or more resource types were provided with the request, the numbers are returned for each resource type. The maximum number returned is 100.
Type: Array of [ComplianceSummaryByResourceType](API_ComplianceSummaryByResourceType.md) objects

## Errors
<a name="API_GetComplianceSummaryByResourceType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

## See Also
<a name="API_GetComplianceSummaryByResourceType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/GetComplianceSummaryByResourceType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/GetComplianceSummaryByResourceType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/GetComplianceSummaryByResourceType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/GetComplianceSummaryByResourceType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/GetComplianceSummaryByResourceType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/GetComplianceSummaryByResourceType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/GetComplianceSummaryByResourceType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/GetComplianceSummaryByResourceType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/GetComplianceSummaryByResourceType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/GetComplianceSummaryByResourceType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
