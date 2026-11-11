---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DesignationSummary.html
---

# DesignationSummary
<a name="API_DesignationSummary"></a>

The summary representation of a designation returned by `ListDesignations`. The summary omits the Cedar permit policy. Call `GetDesignation` to retrieve the full designation record including the policy.

## Contents
<a name="API_DesignationSummary_Contents"></a>

 ** createdBy **   <a name="datazone-Type-DesignationSummary-createdBy"></a>
The identifier of the Amazon DataZone user who created the designation.
Type: String
Required: Yes

 ** deletionProtection **   <a name="datazone-Type-DesignationSummary-deletionProtection"></a>
Specifies whether deletion protection is enabled for this designation. When `true`, `DeleteDesignation` is rejected until protection is disabled through `UpdateDesignation`.
Type: Boolean
Required: Yes

 ** domainId **   <a name="datazone-Type-DesignationSummary-domainId"></a>
The identifier of the Amazon DataZone domain that contains the designation.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** id **   <a name="datazone-Type-DesignationSummary-id"></a>
The unique ID of the designation.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** name **   <a name="datazone-Type-DesignationSummary-name"></a>
The name of the designation. The name is unique within the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: Yes

 ** createdAt **   <a name="datazone-Type-DesignationSummary-createdAt"></a>
The date and time when the designation was created.
Type: Timestamp
Required: No

 ** description **   <a name="datazone-Type-DesignationSummary-description"></a>
A human-readable description of the designation and its intended use.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** designationType **   <a name="datazone-Type-DesignationSummary-designationType"></a>
The classification of this designation. Valid values:
+  `MANAGED` — System-defined designation.
+  `USER_CREATED` — User-created designation.
Type: String
Valid Values: `MANAGED | USER_CREATED`
Required: No

 ** updatedAt **   <a name="datazone-Type-DesignationSummary-updatedAt"></a>
The date and time when the designation was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_DesignationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DesignationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DesignationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DesignationSummary)
