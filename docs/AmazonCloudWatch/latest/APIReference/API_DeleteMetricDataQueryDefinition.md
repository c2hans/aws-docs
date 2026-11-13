---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteMetricDataQueryDefinition.html
---

# DeleteMetricDataQueryDefinition
<a name="API_DeleteMetricDataQueryDefinition"></a>

Deletes a metric data query definition.

This operation is idempotent. If the definition doesn't exist, the operation succeeds without returning an error.

 **Permissions**

To delete a definition, you need the `cloudwatch:DeleteMetricDataQueryDefinition` permission on the metric data query definition resource. You can use the `aws:ResourceTag/${TagKey}` condition key to control access based on the tags of the definition.

## Request Syntax
<a name="API_DeleteMetricDataQueryDefinition_RequestSyntax"></a>

```
{
   "Id": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteMetricDataQueryDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Id](#API_DeleteMetricDataQueryDefinition_RequestSyntax) **   <a name="ACW-DeleteMetricDataQueryDefinition-request-Id"></a>
The ID of the metric data query definition to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]{1,64}`
Required: Yes

## Response Elements
<a name="API_DeleteMetricDataQueryDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteMetricDataQueryDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteMetricDataQueryDefinition_Examples"></a>

### Example – Delete a metric data query definition
<a name="API_DeleteMetricDataQueryDefinition_Example_1"></a>

The following AWS CLI command deletes a definition by its ID. Replace the ID with your definition ID. The command doesn't return any output when it succeeds.

#### Sample Request
<a name="API_DeleteMetricDataQueryDefinition_Example_1_Request"></a>

```
PROMPT> aws cloudwatch delete-metric-data-query-definition \
    --id a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
```

## See Also
<a name="API_DeleteMetricDataQueryDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DeleteMetricDataQueryDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DeleteMetricDataQueryDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DeleteMetricDataQueryDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DeleteMetricDataQueryDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteMetricDataQueryDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DeleteMetricDataQueryDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DeleteMetricDataQueryDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DeleteMetricDataQueryDefinition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DeleteMetricDataQueryDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteMetricDataQueryDefinition)
