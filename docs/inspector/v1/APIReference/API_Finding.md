---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_Finding.html
---

# Finding
<a name="API_Finding"></a>

Contains information about an Amazon Inspector Classic finding. This data type is used as the response element in the [DescribeFindings](API_DescribeFindings.md) action.

## Contents
<a name="API_Finding_Contents"></a>

 ** arn **   <a name="Inspector-Type-Finding-arn"></a>
The ARN that specifies the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** attributes **   <a name="Inspector-Type-Finding-attributes"></a>
The system-defined attributes for the finding.
Type: Array of [Attribute](API_Attribute.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: Yes

 ** createdAt **   <a name="Inspector-Type-Finding-createdAt"></a>
The time when the finding was generated.
Type: Timestamp
Required: Yes

 ** updatedAt **   <a name="Inspector-Type-Finding-updatedAt"></a>
The time when [AddAttributesToFindings](API_AddAttributesToFindings.md) is called.
Type: Timestamp
Required: Yes

 ** userAttributes **   <a name="Inspector-Type-Finding-userAttributes"></a>
The user-defined attributes that are assigned to the finding.
Type: Array of [Attribute](API_Attribute.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 ** assetAttributes **   <a name="Inspector-Type-Finding-assetAttributes"></a>
A collection of attributes of the host from which the finding is generated.
Type: [AssetAttributes](API_AssetAttributes.md) object
Required: No

 ** assetType **   <a name="Inspector-Type-Finding-assetType"></a>
The type of the host from which the finding is generated.
Type: String
Valid Values: `ec2-instance`
Required: No

 ** confidence **   <a name="Inspector-Type-Finding-confidence"></a>
This data element is currently not used.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10.
Required: No

 ** description **   <a name="Inspector-Type-Finding-description"></a>
The description of the finding.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: No

 ** id **   <a name="Inspector-Type-Finding-id"></a>
The ID of the finding.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** indicatorOfCompromise **   <a name="Inspector-Type-Finding-indicatorOfCompromise"></a>
This data element is currently not used.
Type: Boolean
Required: No

 ** numericSeverity **   <a name="Inspector-Type-Finding-numericSeverity"></a>
The numeric value of the finding severity.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 10.0.
Required: No

 ** recommendation **   <a name="Inspector-Type-Finding-recommendation"></a>
The recommendation for the finding.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: No

 ** schemaVersion **   <a name="Inspector-Type-Finding-schemaVersion"></a>
The schema version of this data type.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** service **   <a name="Inspector-Type-Finding-service"></a>
The data element is set to "Inspector".
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** serviceAttributes **   <a name="Inspector-Type-Finding-serviceAttributes"></a>
This data type is used in the [Finding](#API_Finding) data type.
Type: [InspectorServiceAttributes](API_InspectorServiceAttributes.md) object
Required: No

 ** severity **   <a name="Inspector-Type-Finding-severity"></a>
The finding severity. Values can be set to High, Medium, Low, and Informational.
Type: String
Valid Values: `Low | Medium | High | Informational | Undefined`
Required: No

 ** title **   <a name="Inspector-Type-Finding-title"></a>
The name of the finding.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: No

## See Also
<a name="API_Finding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/Finding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/Finding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/Finding)
