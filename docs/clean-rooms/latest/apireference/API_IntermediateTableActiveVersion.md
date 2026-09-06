---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_IntermediateTableActiveVersion.html
---

# IntermediateTableActiveVersion
<a name="API_IntermediateTableActiveVersion"></a>

Contains the details of the currently active version of an intermediate table.

## Contents
<a name="API_IntermediateTableActiveVersion_Contents"></a>

 ** analysisId **   <a name="API-Type-IntermediateTableActiveVersion-analysisId"></a>
The identifier of the protected query that created this version.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** analysisType **   <a name="API-Type-IntermediateTableActiveVersion-analysisType"></a>
The type of analysis that created this version.
Type: String
Valid Values: `QUERY`
Required: Yes

 ** inheritedConstraints **   <a name="API-Type-IntermediateTableActiveVersion-inheritedConstraints"></a>
The privacy constraints inherited from parent tables at the time this version was populated.
Type: [IntermediateTableInheritedConstraints](API_IntermediateTableInheritedConstraints.md) object
Required: Yes

 ** versionId **   <a name="API-Type-IntermediateTableActiveVersion-versionId"></a>
The unique identifier of the active version.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** expirationTime **   <a name="API-Type-IntermediateTableActiveVersion-expirationTime"></a>
The time when this version expires based on the retention period.
Type: Timestamp
Required: No

 ** kmsKeyArn **   <a name="API-Type-IntermediateTableActiveVersion-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt this version's data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:kms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:key/[a-zA-Z0-9-]+`
Required: No

 ** parameters **   <a name="API-Type-IntermediateTableActiveVersion-parameters"></a>
The runtime parameters that were used when populating this version.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `[0-9a-zA-Z_]+`
Value Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## See Also
<a name="API_IntermediateTableActiveVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/IntermediateTableActiveVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/IntermediateTableActiveVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/IntermediateTableActiveVersion)
