---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_FarmSummary.html
---

# FarmSummary
<a name="API_FarmSummary"></a>

The summary of details for a farm.

## Contents
<a name="API_FarmSummary_Contents"></a>

 ** createdAt **   <a name="deadlinecloud-Type-FarmSummary-createdAt"></a>
The date and time the resource was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="deadlinecloud-Type-FarmSummary-createdBy"></a>
The user or system that created this resource.
Type: String
Required: Yes

 ** displayName **   <a name="deadlinecloud-Type-FarmSummary-displayName"></a>
The display name of the farm.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** farmId **   <a name="deadlinecloud-Type-FarmSummary-farmId"></a>
The farm ID.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** kmsKeyArn **   <a name="deadlinecloud-Type-FarmSummary-kmsKeyArn"></a>
The ARN for the KMS key.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):kms:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:key/[\w-]{1,120}`
Required: No

 ** updatedAt **   <a name="deadlinecloud-Type-FarmSummary-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-FarmSummary-updatedBy"></a>
The user or system that updated this resource.
Type: String
Required: No

## See Also
<a name="API_FarmSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/FarmSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/FarmSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/FarmSummary)
