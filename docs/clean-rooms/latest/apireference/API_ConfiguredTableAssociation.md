---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ConfiguredTableAssociation.html
---

# ConfiguredTableAssociation
<a name="API_ConfiguredTableAssociation"></a>

A configured table association links a configured table to a collaboration.

## Contents
<a name="API_ConfiguredTableAssociation_Contents"></a>

 ** arn **   <a name="API-Type-ConfiguredTableAssociation-arn"></a>
The unique ARN for the configured table association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:configuredtableassociation/[\d\w-]+/[\d\w-]+`
Required: Yes

 ** configuredTableArn **   <a name="API-Type-ConfiguredTableAssociation-configuredTableArn"></a>
The unique ARN for the configured table that the association refers to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:configuredtable/[\d\w-]+`
Required: Yes

 ** configuredTableId **   <a name="API-Type-ConfiguredTableAssociation-configuredTableId"></a>
The unique ID for the configured table that the association refers to.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-ConfiguredTableAssociation-createTime"></a>
The time the configured table association was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-ConfiguredTableAssociation-id"></a>
The unique ID for the configured table association.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** membershipArn **   <a name="API-Type-ConfiguredTableAssociation-membershipArn"></a>
The unique ARN for the membership this configured table association belongs to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: Yes

 ** membershipId **   <a name="API-Type-ConfiguredTableAssociation-membershipId"></a>
The unique ID for the membership this configured table association belongs to.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-ConfiguredTableAssociation-name"></a>
The name of the configured table association, in lowercase. The table is identified by this name when running protected queries against the underlying data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
Required: Yes

 ** roleArn **   <a name="API-Type-ConfiguredTableAssociation-roleArn"></a>
The service will assume this role to access catalog metadata and query the table.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 512.
Pattern: `arn:aws:iam::[\w]+:role/[\w+=./@-]+`
Required: Yes

 ** updateTime **   <a name="API-Type-ConfiguredTableAssociation-updateTime"></a>
The time the configured table association was last updated.
Type: Timestamp
Required: Yes

 ** analysisRuleTypes **   <a name="API-Type-ConfiguredTableAssociation-analysisRuleTypes"></a>
 The analysis rule types for the configured table association.
Type: Array of strings
Valid Values: `AGGREGATION | LIST | CUSTOM`
Required: No

 ** childResources **   <a name="API-Type-ConfiguredTableAssociation-childResources"></a>
The child resources that depend on this configured table association.
Type: Array of [ChildResource](API_ChildResource.md) objects
Required: No

 ** description **   <a name="API-Type-ConfiguredTableAssociation-description"></a>
A description of the configured table association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

## See Also
<a name="API_ConfiguredTableAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ConfiguredTableAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ConfiguredTableAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ConfiguredTableAssociation)
