---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_StartCostAllocationTagBackfill.html
---

# StartCostAllocationTagBackfill
<a name="API_StartCostAllocationTagBackfill"></a>

 Request a cost allocation tag backfill. This will backfill the activation status (either `active` or `inactive`) for all tag keys from `para:BackfillFrom` up to the time this request is made.

You can request a backfill once every 24 hours.

## Request Syntax
<a name="API_StartCostAllocationTagBackfill_RequestSyntax"></a>

```
{
   "BackfillFrom": "{{string}}"
}
```

## Request Parameters
<a name="API_StartCostAllocationTagBackfill_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BackfillFrom](#API_StartCostAllocationTagBackfill_RequestSyntax) **   <a name="awscostmanagement-StartCostAllocationTagBackfill-request-BackfillFrom"></a>
 The date you want the backfill to start from. The date can only be a first day of the month (a billing start date). Dates can't precede the previous twelve months, or in the future.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: Yes

## Response Syntax
<a name="API_StartCostAllocationTagBackfill_ResponseSyntax"></a>

```
{
   "BackfillRequest": {
      "BackfillFrom": "string",
      "BackfillStatus": "string",
      "CompletedAt": "string",
      "LastUpdatedAt": "string",
      "RequestedAt": "string"
   }
}
```

## Response Elements
<a name="API_StartCostAllocationTagBackfill_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BackfillRequest](#API_StartCostAllocationTagBackfill_ResponseSyntax) **   <a name="awscostmanagement-StartCostAllocationTagBackfill-response-BackfillRequest"></a>
 An object containing detailed metadata of your new backfill request.
Type: [CostAllocationTagBackfillRequest](API_CostAllocationTagBackfillRequest.md) object

## Errors
<a name="API_StartCostAllocationTagBackfill_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BackfillLimitExceededException **
 A request to backfill is already in progress. Once the previous request is complete, you can create another request.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

## Examples
<a name="API_StartCostAllocationTagBackfill_Examples"></a>

The following are sample requests and responses of the `StartCostAllocationTagBackfill` operations.

### Example 1: Successfully request a cost allocation tag backfill
<a name="API_StartCostAllocationTagBackfill_Example_1"></a>

This example illustrates one usage of StartCostAllocationTagBackfill.

#### Sample Request
<a name="API_StartCostAllocationTagBackfill_Example_1_Request"></a>

```
{
    "BackfillFrom": "2024-02-01T00:00:00Z"
}
```

#### Sample Response
<a name="API_StartCostAllocationTagBackfill_Example_1_Response"></a>

```
{
    "BackfillRequest": {
        "BackfillFrom":"2024-02-01T00:00:00Z",
        "BackfillStatus":"PROCESSING",
        "RequestedAt":"2024-03-01T09:16:23Z",
        "LastUpdatedAt":"2024-03-01T09:16:23Z"
    }
}
```

### Example 2: The backfill is skipped because there is no tag status change since the last backfill
<a name="API_StartCostAllocationTagBackfill_Example_2"></a>

The latest successful backfill request is returned instead.

#### Sample Request
<a name="API_StartCostAllocationTagBackfill_Example_2_Request"></a>

```
{
    "BackfillFrom": "2024-02-01T00:00:00Z"
}
```

#### Sample Response
<a name="API_StartCostAllocationTagBackfill_Example_2_Response"></a>

```
{
    "BackfillRequest": {
        "BackfillFrom":"2024-02-01T00:00:00Z",
        "BackfillStatus":"SUCCEEDED",
        "RequestedAt":"2024-03-01T09:16:23Z",
        "LastUpdatedAt":"2024-03-02T06:45:00Z",
        "CompletedAt":"2024-03-02T06:45:00Z"
    }
}
```

## See Also
<a name="API_StartCostAllocationTagBackfill_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/StartCostAllocationTagBackfill)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/StartCostAllocationTagBackfill)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/StartCostAllocationTagBackfill)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/StartCostAllocationTagBackfill)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/StartCostAllocationTagBackfill)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/StartCostAllocationTagBackfill)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/StartCostAllocationTagBackfill)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/StartCostAllocationTagBackfill)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/StartCostAllocationTagBackfill)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/StartCostAllocationTagBackfill)
