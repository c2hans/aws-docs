---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_LimitSummary.html
---

# LimitSummary
<a name="API_LimitSummary"></a>

Provides information about a specific limit.

## Contents
<a name="API_LimitSummary_Contents"></a>

 ** amountRequirementName **   <a name="deadlinecloud-Type-LimitSummary-amountRequirementName"></a>
The value that you specify as the `name` in the `amounts` field of the `hostRequirements` in a step of a job template to declare the limit requirement.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

 ** createdAt **   <a name="deadlinecloud-Type-LimitSummary-createdAt"></a>
The Unix timestamp of the date and time that the limit was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="deadlinecloud-Type-LimitSummary-createdBy"></a>
The user identifier of the person that created the limit.
Type: String
Required: Yes

 ** currentCount **   <a name="deadlinecloud-Type-LimitSummary-currentCount"></a>
The number of resources from the limit that are being used by jobs. The result is delayed and may not be the count at the time that you called the operation.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

 ** displayName **   <a name="deadlinecloud-Type-LimitSummary-displayName"></a>
The name of the limit used in lists to identify the limit.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** farmId **   <a name="deadlinecloud-Type-LimitSummary-farmId"></a>
The unique identifier of the farm that contains the limit.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** limitId **   <a name="deadlinecloud-Type-LimitSummary-limitId"></a>
The unique identifier of the limit.
Type: String
Pattern: `limit-[0-9a-f]{32}`
Required: Yes

 ** maxCount **   <a name="deadlinecloud-Type-LimitSummary-maxCount"></a>
The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit won't be scheduled until the resource is available.
The `maxValue` must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit.
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 2147483647.
Required: Yes

 ** updatedAt **   <a name="deadlinecloud-Type-LimitSummary-updatedAt"></a>
The Unix timestamp of the date and time that the limit was last updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-LimitSummary-updatedBy"></a>
The user identifier of the person that last updated the limit.
Type: String
Required: No

## See Also
<a name="API_LimitSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/LimitSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/LimitSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/LimitSummary)
