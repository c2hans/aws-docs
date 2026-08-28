---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_BatchGetDevicePositionError.html
---

# BatchGetDevicePositionError
<a name="API_WaypointTracking_BatchGetDevicePositionError"></a>

Contains error details for each device that didn't return a position.

## Contents
<a name="API_WaypointTracking_BatchGetDevicePositionError_Contents"></a>

 ** DeviceId **   <a name="location-Type-WaypointTracking_BatchGetDevicePositionError-DeviceId"></a>
The ID of the device that didn't return a position.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

 ** Error **   <a name="location-Type-WaypointTracking_BatchGetDevicePositionError-Error"></a>
Contains details related to the error code.
Type: [BatchItemError](API_WaypointTracking_BatchItemError.md) object
Required: Yes

## See Also
<a name="API_WaypointTracking_BatchGetDevicePositionError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointtracking-2020-11-19/BatchGetDevicePositionError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointtracking-2020-11-19/BatchGetDevicePositionError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointtracking-2020-11-19/BatchGetDevicePositionError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
