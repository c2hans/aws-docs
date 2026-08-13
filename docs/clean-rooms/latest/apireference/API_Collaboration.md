---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_Collaboration.html
---

# Collaboration
<a name="API_Collaboration"></a>

The multi-party data share environment. The collaboration contains metadata about its purpose and participants.

## Contents
<a name="API_Collaboration_Contents"></a>

 ** arn **   <a name="API-Type-Collaboration-arn"></a>
The unique ARN for the collaboration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** createTime **   <a name="API-Type-Collaboration-createTime"></a>
The time when the collaboration was created.
Type: Timestamp
Required: Yes

 ** creatorAccountId **   <a name="API-Type-Collaboration-creatorAccountId"></a>
The identifier used to reference members of the collaboration. Currently only supports AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** creatorDisplayName **   <a name="API-Type-Collaboration-creatorDisplayName"></a>
A display name of the collaboration creator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** id **   <a name="API-Type-Collaboration-id"></a>
The unique ID for the collaboration.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** memberStatus **   <a name="API-Type-Collaboration-memberStatus"></a>
The status of a member in a collaboration.
Type: String
Valid Values: `INVITED | ACTIVE | LEFT | REMOVED`
Required: Yes

 ** name **   <a name="API-Type-Collaboration-name"></a>
A human-readable identifier provided by the collaboration owner. Display names are not unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** queryLogStatus **   <a name="API-Type-Collaboration-queryLogStatus"></a>
An indicator as to whether query logging has been enabled or disabled for the collaboration.
When `ENABLED`, AWS Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** updateTime **   <a name="API-Type-Collaboration-updateTime"></a>
The time the collaboration metadata was last updated.
Type: Timestamp
Required: Yes

 ** allowedResultRegions **   <a name="API-Type-Collaboration-allowedResultRegions"></a>
The AWS Regions where collaboration query results can be stored. Returns the list of Region identifiers that were specified when the collaboration was created. This list is used to enforce regional storage policies and compliance requirements.
Type: Array of strings
Valid Values: `us-west-1 | us-west-2 | us-east-1 | us-east-2 | af-south-1 | ap-east-1 | ap-east-2 | ap-south-2 | ap-southeast-1 | ap-southeast-2 | ap-southeast-3 | ap-southeast-5 | ap-southeast-4 | ap-southeast-7 | ap-south-1 | ap-northeast-3 | ap-northeast-1 | ap-northeast-2 | ca-central-1 | ca-west-1 | eu-south-1 | eu-west-3 | eu-south-2 | eu-central-2 | eu-central-1 | eu-north-1 | eu-west-1 | eu-west-2 | me-south-1 | me-central-1 | il-central-1 | sa-east-1 | mx-central-1`
Required: No

 ** analyticsEngine **   <a name="API-Type-Collaboration-analyticsEngine"></a>
 The analytics engine for the collaboration.
After July 16, 2025, the `CLEAN_ROOMS_SQL` parameter will no longer be available.
Type: String
Valid Values: `SPARK | CLEAN_ROOMS_SQL`
Required: No

 ** autoApprovedChangeTypes **   <a name="API-Type-Collaboration-autoApprovedChangeTypes"></a>
The types of change requests that are automatically approved for this collaboration.
Type: Array of strings
Valid Values: `ADD_MEMBER | GRANT_RECEIVE_RESULTS_ABILITY | REVOKE_RECEIVE_RESULTS_ABILITY | GRANT_EXPORT_QUERY_ANALYSIS_LOG_ABILITY | REVOKE_EXPORT_QUERY_ANALYSIS_LOG_ABILITY`
Required: No

 ** dataEncryptionMetadata **   <a name="API-Type-Collaboration-dataEncryptionMetadata"></a>
The settings for client-side encryption for cryptographic computing.
Type: [DataEncryptionMetadata](API_DataEncryptionMetadata.md) object
Required: No

 ** description **   <a name="API-Type-Collaboration-description"></a>
A description of the collaboration provided by the collaboration owner.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `(?!\s+$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** isMetricsEnabled **   <a name="API-Type-Collaboration-isMetricsEnabled"></a>
An indicator as to whether metrics are enabled for the collaboration.
When `true`, collaboration members can opt in to Amazon CloudWatch metrics for their membership queries.
Type: Boolean
Required: No

 ** jobLogStatus **   <a name="API-Type-Collaboration-jobLogStatus"></a>
An indicator as to whether job logging has been enabled or disabled for the collaboration.
When `ENABLED`, AWS Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** membershipArn **   <a name="API-Type-Collaboration-membershipArn"></a>
The unique ARN for your membership within the collaboration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: No

 ** membershipId **   <a name="API-Type-Collaboration-membershipId"></a>
The unique ID for your membership within the collaboration.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## See Also
<a name="API_Collaboration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/Collaboration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/Collaboration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/Collaboration)
