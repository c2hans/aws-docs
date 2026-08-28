---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UpdateCostAllocationTagsStatus.html
---

# UpdateCostAllocationTagsStatus
<a name="API_UpdateCostAllocationTagsStatus"></a>

Updates status for cost allocation tags in bulk, with maximum batch size of 20. If the tag status that's updated is the same as the existing tag status, the request doesn't fail. Instead, it doesn't have any effect on the tag status (for example, activating the active tag).

## Request Syntax
<a name="API_UpdateCostAllocationTagsStatus_RequestSyntax"></a>

```
{
   "CostAllocationTagsStatus": [
      {
         "Status": "{{string}}",
         "TagKey": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateCostAllocationTagsStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CostAllocationTagsStatus](#API_UpdateCostAllocationTagsStatus_RequestSyntax) **   <a name="awscostmanagement-UpdateCostAllocationTagsStatus-request-CostAllocationTagsStatus"></a>
The list of `CostAllocationTagStatusEntry` objects that are used to update cost allocation tags status for this request.
Type: Array of [CostAllocationTagStatusEntry](API_CostAllocationTagStatusEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

## Response Syntax
<a name="API_UpdateCostAllocationTagsStatus_ResponseSyntax"></a>

```
{
   "Errors": [
      {
         "Code": "string",
         "Message": "string",
         "TagKey": "string"
      }
   ]
}
```

## Response Elements
<a name="API_UpdateCostAllocationTagsStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_UpdateCostAllocationTagsStatus_ResponseSyntax) **   <a name="awscostmanagement-UpdateCostAllocationTagsStatus-response-Errors"></a>
A list of `UpdateCostAllocationTagsStatusError` objects with error details about each cost allocation tag that can't be updated. If there's no failure, an empty array returns.
Type: Array of [UpdateCostAllocationTagsStatusError](API_UpdateCostAllocationTagsStatusError.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

## Errors
<a name="API_UpdateCostAllocationTagsStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

## Examples
<a name="API_UpdateCostAllocationTagsStatus_Examples"></a>

The following are sample requests and responses of the `UpdateCostAllocationTagsStatus` operations.

### Example 1: Successfully updated all tag status
<a name="API_UpdateCostAllocationTagsStatus_Example_1"></a>

This example illustrates one usage of UpdateCostAllocationTagsStatus.

#### Sample Request
<a name="API_UpdateCostAllocationTagsStatus_Example_1_Request"></a>

```
{
    "CostAllocationTagsStatus": [
       {
           "TagKey": "tagA",
           "Status": "Active"
       },
       {
           "TagKey": "tagB",
           "Status": "Inactive"
       }
    ]
}
```

#### Sample Response
<a name="API_UpdateCostAllocationTagsStatus_Example_1_Response"></a>

```
{
    "Errors": []
}
```

### Example 2: Failed to update one of the tag statuses
<a name="API_UpdateCostAllocationTagsStatus_Example_2"></a>

This example illustrates one usage of UpdateCostAllocationTagsStatus.

#### Sample Request
<a name="API_UpdateCostAllocationTagsStatus_Example_2_Request"></a>

```
{
    "CostAllocationTagsStatus": [
       {
           "TagKey": "tagC",
           "Status": "Active"
       },
       {
           "TagKey": "tagD",
           "Status": "Inactive"
       }
    ]
}
```

#### Sample Response
<a name="API_UpdateCostAllocationTagsStatus_Example_2_Response"></a>

```
{
    "Errors": [
        {
            "TagKey": "tagC",
            "Code": "TagKeysNotFoundException",
            "Message": "Failed to update Cost Allocation Tag: tagC"
        }
    ]
}
```

## See Also
<a name="API_UpdateCostAllocationTagsStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/UpdateCostAllocationTagsStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/UpdateCostAllocationTagsStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/UpdateCostAllocationTagsStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/UpdateCostAllocationTagsStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/UpdateCostAllocationTagsStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/UpdateCostAllocationTagsStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/UpdateCostAllocationTagsStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/UpdateCostAllocationTagsStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/UpdateCostAllocationTagsStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/UpdateCostAllocationTagsStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
