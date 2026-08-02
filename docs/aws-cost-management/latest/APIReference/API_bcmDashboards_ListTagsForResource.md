---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_bcmDashboards_ListTagsForResource"></a>

Returns a list of all tags associated with a specified dashboard resource.

## Request Syntax
<a name="API_bcmDashboards_ListTagsForResource_RequestSyntax"></a>

```
{
   "resourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_bcmDashboards_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceArn](#API_bcmDashboards_ListTagsForResource_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_ListTagsForResource-request-resourceArn"></a>
The unique identifier for the resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:bcm-dashboards::[0-9]{12}:(dashboard|scheduled-report)/(\*|[-a-z0-9]+)`
Required: Yes

## Response Syntax
<a name="API_bcmDashboards_ListTagsForResource_ResponseSyntax"></a>

```
{
   "resourceTags": [
      {
         "key": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_bcmDashboards_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resourceTags](#API_bcmDashboards_ListTagsForResource_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_ListTagsForResource-response-resourceTags"></a>
The list of tags associated with the specified dashboard resource.
Type: Array of [ResourceTag](API_bcmDashboards_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_bcmDashboards_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error occurred while processing the request. Retry your request. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource (dashboard, policy, or widget) was not found. Verify the ARN and try again.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling. Reduce the frequency of requests and use exponential backoff.
HTTP Status Code: 400

 ** ValidationException **
The input parameters do not satisfy the requirements. Check the error message for specific validation details.
HTTP Status Code: 400

## See Also
<a name="API_bcmDashboards_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-dashboards-2025-08-18/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-dashboards-2025-08-18/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-dashboards-2025-08-18/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-dashboards-2025-08-18/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-dashboards-2025-08-18/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-dashboards-2025-08-18/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-dashboards-2025-08-18/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/ListTagsForResource)
