---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateFeatureGroup.html
---

# UpdateFeatureGroup
<a name="API_UpdateFeatureGroup"></a>

Updates the feature group by either adding features or updating the online store configuration. Use one of the following request parameters at a time while using the `UpdateFeatureGroup` API.

You can add features for your feature group using the `FeatureAdditions` request parameter. Features cannot be removed from a feature group.

You can update the online store configuration by using the `OnlineStoreConfig` request parameter. If a `TtlDuration` is specified, the default `TtlDuration` applies for all records added to the feature group *after the feature group is updated*. If a record level `TtlDuration` exists from using the `PutRecord` API, the record level `TtlDuration` applies to that record instead of the default `TtlDuration`. To remove the default `TtlDuration` from an existing feature group, use the `UpdateFeatureGroup` API and set the `TtlDuration` `Unit` and `Value` to `null`.

## Request Syntax
<a name="API_UpdateFeatureGroup_RequestSyntax"></a>

```
{
   "FeatureAdditions": [
      {
         "CollectionConfig": { ... },
         "CollectionType": "{{string}}",
         "FeatureName": "{{string}}",
         "FeatureType": "{{string}}"
      }
   ],
   "FeatureGroupName": "{{string}}",
   "OnlineStoreConfig": {
      "TtlDuration": {
         "Unit": "{{string}}",
         "Value": {{number}}
      }
   },
   "ThroughputConfig": {
      "ProvisionedReadCapacityUnits": {{number}},
      "ProvisionedWriteCapacityUnits": {{number}},
      "ThroughputMode": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateFeatureGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FeatureAdditions](#API_UpdateFeatureGroup_RequestSyntax) **   <a name="sagemaker-UpdateFeatureGroup-request-FeatureAdditions"></a>
Updates the feature group. Updating a feature group is an asynchronous operation. When you get an HTTP 200 response, you've made a valid request. It takes some time after you've made a valid request for Feature Store to update the feature group.
Type: Array of [FeatureDefinition](API_FeatureDefinition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** [FeatureGroupName](#API_UpdateFeatureGroup_RequestSyntax) **   <a name="sagemaker-UpdateFeatureGroup-request-FeatureGroupName"></a>
The name or Amazon Resource Name (ARN) of the feature group that you're updating.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group\/)?([a-zA-Z0-9]([_-]*[a-zA-Z0-9]){0,63})`
Required: Yes

 ** [OnlineStoreConfig](#API_UpdateFeatureGroup_RequestSyntax) **   <a name="sagemaker-UpdateFeatureGroup-request-OnlineStoreConfig"></a>
Updates the feature group online store configuration.
Type: [OnlineStoreConfigUpdate](API_OnlineStoreConfigUpdate.md) object
Required: No

 ** [ThroughputConfig](#API_UpdateFeatureGroup_RequestSyntax) **   <a name="sagemaker-UpdateFeatureGroup-request-ThroughputConfig"></a>
The new throughput configuration for the feature group. You can switch between on-demand and provisioned modes or update the read / write capacity of provisioned feature groups. You can switch a feature group to on-demand only once in a 24 hour period.
Type: [ThroughputConfigUpdate](API_ThroughputConfigUpdate.md) object
Required: No

## Response Syntax
<a name="API_UpdateFeatureGroup_ResponseSyntax"></a>

```
{
   "FeatureGroupArn": "string"
}
```

## Response Elements
<a name="API_UpdateFeatureGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FeatureGroupArn](#API_UpdateFeatureGroup_ResponseSyntax) **   <a name="sagemaker-UpdateFeatureGroup-response-FeatureGroupArn"></a>
The Amazon Resource Number (ARN) of the feature group that you're updating.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group/.*`

## Errors
<a name="API_UpdateFeatureGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateFeatureGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateFeatureGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateFeatureGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateFeatureGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateFeatureGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateFeatureGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateFeatureGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateFeatureGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateFeatureGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateFeatureGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateFeatureGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
