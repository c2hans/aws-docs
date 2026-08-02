---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AutomationRulesFindingFilters.html
---

# AutomationRulesFindingFilters
<a name="API_AutomationRulesFindingFilters"></a>

 The criteria that determine which findings a rule applies to.

## Contents
<a name="API_AutomationRulesFindingFilters_Contents"></a>

 ** AwsAccountId **   <a name="securityhub-Type-AutomationRulesFindingFilters-AwsAccountId"></a>
The AWS account ID in which a finding was generated.
 Array Members: Minimum number of 1 item. Maximum number of 100 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** AwsAccountName **   <a name="securityhub-Type-AutomationRulesFindingFilters-AwsAccountName"></a>
The name of the AWS account in which a finding was generated.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** CompanyName **   <a name="securityhub-Type-AutomationRulesFindingFilters-CompanyName"></a>
 The name of the company for the product that generated the finding. For control-based findings, the company is AWS.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ComplianceAssociatedStandardsId **   <a name="securityhub-Type-AutomationRulesFindingFilters-ComplianceAssociatedStandardsId"></a>
The unique identifier of a standard in which a control is enabled. This field consists of the resource portion of the Amazon Resource Name (ARN) returned for a standard in the [DescribeStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html) API response.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ComplianceSecurityControlId **   <a name="securityhub-Type-AutomationRulesFindingFilters-ComplianceSecurityControlId"></a>
 The security control ID for which a finding was generated. Security control IDs are the same across standards.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ComplianceStatus **   <a name="securityhub-Type-AutomationRulesFindingFilters-ComplianceStatus"></a>
 The result of a security check. This field is only used for findings generated from controls.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** Confidence **   <a name="securityhub-Type-AutomationRulesFindingFilters-Confidence"></a>
The likelihood that a finding accurately identifies the behavior or issue that it was intended to identify. `Confidence` is scored on a 0–100 basis using a ratio scale. A value of `0` means 0 percent confidence, and a value of `100` means 100 percent confidence. For example, a data exfiltration detection based on a statistical deviation of network traffic has low confidence because an actual exfiltration hasn't been verified. For more information, see [Confidence](https://docs.aws.amazon.com/securityhub/latest/userguide/asff-top-level-attributes.html#asff-confidence) in the * AWS Security Hub CSPM User Guide*.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [NumberFilter](API_NumberFilter.md) objects
Required: No

 ** CreatedAt **   <a name="securityhub-Type-AutomationRulesFindingFilters-CreatedAt"></a>
 A timestamp that indicates when this finding record was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [DateFilter](API_DateFilter.md) objects
Required: No

 ** Criticality **   <a name="securityhub-Type-AutomationRulesFindingFilters-Criticality"></a>
 The level of importance that is assigned to the resources that are associated with a finding. `Criticality` is scored on a 0–100 basis, using a ratio scale that supports only full integers. A score of `0` means that the underlying resources have no criticality, and a score of `100` is reserved for the most critical resources. For more information, see [Criticality](https://docs.aws.amazon.com/securityhub/latest/userguide/asff-top-level-attributes.html#asff-criticality) in the * AWS Security Hub CSPM User Guide*.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [NumberFilter](API_NumberFilter.md) objects
Required: No

 ** Description **   <a name="securityhub-Type-AutomationRulesFindingFilters-Description"></a>
 A finding's description.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** FirstObservedAt **   <a name="securityhub-Type-AutomationRulesFindingFilters-FirstObservedAt"></a>
 A timestamp that indicates when the potential security issue captured by a finding was first observed by the security findings product.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [DateFilter](API_DateFilter.md) objects
Required: No

 ** GeneratorId **   <a name="securityhub-Type-AutomationRulesFindingFilters-GeneratorId"></a>
 The identifier for the solution-specific component that generated a finding.
 Array Members: Minimum number of 1 item. Maximum number of 100 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** Id **   <a name="securityhub-Type-AutomationRulesFindingFilters-Id"></a>
 The product-specific identifier for a finding.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** LastObservedAt **   <a name="securityhub-Type-AutomationRulesFindingFilters-LastObservedAt"></a>
 A timestamp that indicates when the security findings provider most recently observed a change in the resource that is involved in the finding.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [DateFilter](API_DateFilter.md) objects
Required: No

 ** NoteText **   <a name="securityhub-Type-AutomationRulesFindingFilters-NoteText"></a>
 The text of a user-defined note that's added to a finding.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** NoteUpdatedAt **   <a name="securityhub-Type-AutomationRulesFindingFilters-NoteUpdatedAt"></a>
 The timestamp of when the note was updated.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [DateFilter](API_DateFilter.md) objects
Required: No

 ** NoteUpdatedBy **   <a name="securityhub-Type-AutomationRulesFindingFilters-NoteUpdatedBy"></a>
 The principal that created a note.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ProductArn **   <a name="securityhub-Type-AutomationRulesFindingFilters-ProductArn"></a>
 The Amazon Resource Name (ARN) for a third-party product that generated a finding in Security Hub CSPM.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ProductName **   <a name="securityhub-Type-AutomationRulesFindingFilters-ProductName"></a>
 Provides the name of the product that generated the finding. For control-based findings, the product name is Security Hub CSPM.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** RecordState **   <a name="securityhub-Type-AutomationRulesFindingFilters-RecordState"></a>
 Provides the current state of a finding.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** RelatedFindingsId **   <a name="securityhub-Type-AutomationRulesFindingFilters-RelatedFindingsId"></a>
 The product-generated identifier for a related finding.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** RelatedFindingsProductArn **   <a name="securityhub-Type-AutomationRulesFindingFilters-RelatedFindingsProductArn"></a>
 The ARN for the product that generated a related finding.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceApplicationArn **   <a name="securityhub-Type-AutomationRulesFindingFilters-ResourceApplicationArn"></a>
 The Amazon Resource Name (ARN) of the application that is related to a finding.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceApplicationName **   <a name="securityhub-Type-AutomationRulesFindingFilters-ResourceApplicationName"></a>
 The name of the application that is related to a finding.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceDetailsOther **   <a name="securityhub-Type-AutomationRulesFindingFilters-ResourceDetailsOther"></a>
 Custom fields and values about the resource that a finding pertains to.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [MapFilter](API_MapFilter.md) objects
Required: No

 ** ResourceId **   <a name="securityhub-Type-AutomationRulesFindingFilters-ResourceId"></a>
 The identifier for the given resource type. For AWS resources that are identified by Amazon Resource Names (ARNs), this is the ARN. For AWS resources that lack ARNs, this is the identifier as defined by the AWS service that created the resource. For non-AWS resources, this is a unique identifier that is associated with the resource.
 Array Members: Minimum number of 1 item. Maximum number of 100 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceOwnerAccountId **   <a name="securityhub-Type-AutomationRulesFindingFilters-ResourceOwnerAccountId"></a>
The unique identifier of the account that owns the resource that the finding applies to, for example, Azure Subscription Id or AWS Account Id
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceOwnerOrgId **   <a name="securityhub-Type-AutomationRulesFindingFilters-ResourceOwnerOrgId"></a>
The unique identifier of the organization that owns the resource that the finding applies to, for example, Azure Tenant Id
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourcePartition **   <a name="securityhub-Type-AutomationRulesFindingFilters-ResourcePartition"></a>
 The partition in which the resource that the finding pertains to is located. A partition is a group of AWS Regions. Each AWS account is scoped to one partition.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceProvider **   <a name="securityhub-Type-AutomationRulesFindingFilters-ResourceProvider"></a>
The cloud provider that the resource belongs to. Valid values are `AWS` and `Azure`.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceRegion **   <a name="securityhub-Type-AutomationRulesFindingFilters-ResourceRegion"></a>
 The AWS Region where the resource that a finding pertains to is located.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceTags **   <a name="securityhub-Type-AutomationRulesFindingFilters-ResourceTags"></a>
 A list of AWS tags associated with a resource at the time the finding was processed.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [MapFilter](API_MapFilter.md) objects
Required: No

 ** ResourceType **   <a name="securityhub-Type-AutomationRulesFindingFilters-ResourceType"></a>
 The type of resource that the finding pertains to.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** SeverityLabel **   <a name="securityhub-Type-AutomationRulesFindingFilters-SeverityLabel"></a>
 The severity value of the finding.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** SourceUrl **   <a name="securityhub-Type-AutomationRulesFindingFilters-SourceUrl"></a>
 Provides a URL that links to a page about the current finding in the finding product.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** Title **   <a name="securityhub-Type-AutomationRulesFindingFilters-Title"></a>
 A finding's title.
 Array Members: Minimum number of 1 item. Maximum number of 100 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** Type **   <a name="securityhub-Type-AutomationRulesFindingFilters-Type"></a>
 One or more finding types in the format of namespace/category/classifier that classify a finding. For a list of namespaces, classifiers, and categories, see [Types taxonomy for ASFF](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format-type-taxonomy.html) in the * AWS Security Hub CSPM User Guide*.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** UpdatedAt **   <a name="securityhub-Type-AutomationRulesFindingFilters-UpdatedAt"></a>
 A timestamp that indicates when the finding record was most recently updated.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [DateFilter](API_DateFilter.md) objects
Required: No

 ** UserDefinedFields **   <a name="securityhub-Type-AutomationRulesFindingFilters-UserDefinedFields"></a>
 A list of user-defined name and value string pairs added to a finding.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [MapFilter](API_MapFilter.md) objects
Required: No

 ** VerificationState **   <a name="securityhub-Type-AutomationRulesFindingFilters-VerificationState"></a>
 Provides the veracity of a finding.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** WorkflowStatus **   <a name="securityhub-Type-AutomationRulesFindingFilters-WorkflowStatus"></a>
 Provides information about the status of the investigation into a finding.
 Array Members: Minimum number of 1 item. Maximum number of 20 items.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

## See Also
<a name="API_AutomationRulesFindingFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AutomationRulesFindingFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AutomationRulesFindingFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AutomationRulesFindingFilters)
