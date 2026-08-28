---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_BatchDeleteDevicePositionHistoryError.html
---

# BatchDeleteDevicePositionHistoryError
<a name="API_BatchDeleteDevicePositionHistoryError"></a>

Contains the tracker resource details.

## Contents
<a name="API_BatchDeleteDevicePositionHistoryError_Contents"></a>

 ** DeviceId **   <a name="location-Type-BatchDeleteDevicePositionHistoryError-DeviceId"></a>
The ID of the device for this position.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

 ** Error **   <a name="location-Type-BatchDeleteDevicePositionHistoryError-Error"></a>
Contains the batch request error details associated with the request.
Type: [BatchItemError](API_BatchItemError.md) object
Required: Yes

## See Also
<a name="API_BatchDeleteDevicePositionHistoryError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/BatchDeleteDevicePositionHistoryError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/BatchDeleteDevicePositionHistoryError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/BatchDeleteDevicePositionHistoryError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
