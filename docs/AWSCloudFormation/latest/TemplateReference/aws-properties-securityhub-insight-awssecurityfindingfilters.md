---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-insight-awssecurityfindingfilters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::Insight AwsSecurityFindingFilters
<a name="aws-properties-securityhub-insight-awssecurityfindingfilters"></a>

A collection of filters that are applied to all active findings aggregated by AWS Security Hub CSPM.

You can filter by up to ten finding attributes. For each attribute, you can provide up to 20 filter values.

## Syntax
<a name="aws-properties-securityhub-insight-awssecurityfindingfilters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-insight-awssecurityfindingfilters-syntax.json"></a>

```
{
  "[AwsAccountId](#cfn-securityhub-insight-awssecurityfindingfilters-awsaccountid)" : {{[ StringFilter, ... ]}},
  "[AwsAccountName](#cfn-securityhub-insight-awssecurityfindingfilters-awsaccountname)" : {{[ StringFilter, ... ]}},
  "[CompanyName](#cfn-securityhub-insight-awssecurityfindingfilters-companyname)" : {{[ StringFilter, ... ]}},
  "[ComplianceAssociatedStandardsId](#cfn-securityhub-insight-awssecurityfindingfilters-complianceassociatedstandardsid)" : {{[ StringFilter, ... ]}},
  "[ComplianceSecurityControlId](#cfn-securityhub-insight-awssecurityfindingfilters-compliancesecuritycontrolid)" : {{[ StringFilter, ... ]}},
  "[ComplianceSecurityControlParametersName](#cfn-securityhub-insight-awssecurityfindingfilters-compliancesecuritycontrolparametersname)" : {{[ StringFilter, ... ]}},
  "[ComplianceSecurityControlParametersValue](#cfn-securityhub-insight-awssecurityfindingfilters-compliancesecuritycontrolparametersvalue)" : {{[ StringFilter, ... ]}},
  "[ComplianceStatus](#cfn-securityhub-insight-awssecurityfindingfilters-compliancestatus)" : {{[ StringFilter, ... ]}},
  "[Confidence](#cfn-securityhub-insight-awssecurityfindingfilters-confidence)" : {{[ NumberFilter, ... ]}},
  "[CreatedAt](#cfn-securityhub-insight-awssecurityfindingfilters-createdat)" : {{[ DateFilter, ... ]}},
  "[Criticality](#cfn-securityhub-insight-awssecurityfindingfilters-criticality)" : {{[ NumberFilter, ... ]}},
  "[Description](#cfn-securityhub-insight-awssecurityfindingfilters-description)" : {{[ StringFilter, ... ]}},
  "[FindingProviderFieldsConfidence](#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsconfidence)" : {{[ NumberFilter, ... ]}},
  "[FindingProviderFieldsCriticality](#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldscriticality)" : {{[ NumberFilter, ... ]}},
  "[FindingProviderFieldsRelatedFindingsId](#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsrelatedfindingsid)" : {{[ StringFilter, ... ]}},
  "[FindingProviderFieldsRelatedFindingsProductArn](#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsrelatedfindingsproductarn)" : {{[ StringFilter, ... ]}},
  "[FindingProviderFieldsSeverityLabel](#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsseveritylabel)" : {{[ StringFilter, ... ]}},
  "[FindingProviderFieldsSeverityOriginal](#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsseverityoriginal)" : {{[ StringFilter, ... ]}},
  "[FindingProviderFieldsTypes](#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldstypes)" : {{[ StringFilter, ... ]}},
  "[FirstObservedAt](#cfn-securityhub-insight-awssecurityfindingfilters-firstobservedat)" : {{[ DateFilter, ... ]}},
  "[GeneratorId](#cfn-securityhub-insight-awssecurityfindingfilters-generatorid)" : {{[ StringFilter, ... ]}},
  "[Id](#cfn-securityhub-insight-awssecurityfindingfilters-id)" : {{[ StringFilter, ... ]}},
  "[Keyword](#cfn-securityhub-insight-awssecurityfindingfilters-keyword)" : {{[ KeywordFilter, ... ]}},
  "[LastObservedAt](#cfn-securityhub-insight-awssecurityfindingfilters-lastobservedat)" : {{[ DateFilter, ... ]}},
  "[MalwareName](#cfn-securityhub-insight-awssecurityfindingfilters-malwarename)" : {{[ StringFilter, ... ]}},
  "[MalwarePath](#cfn-securityhub-insight-awssecurityfindingfilters-malwarepath)" : {{[ StringFilter, ... ]}},
  "[MalwareState](#cfn-securityhub-insight-awssecurityfindingfilters-malwarestate)" : {{[ StringFilter, ... ]}},
  "[MalwareType](#cfn-securityhub-insight-awssecurityfindingfilters-malwaretype)" : {{[ StringFilter, ... ]}},
  "[NetworkDestinationDomain](#cfn-securityhub-insight-awssecurityfindingfilters-networkdestinationdomain)" : {{[ StringFilter, ... ]}},
  "[NetworkDestinationIpV4](#cfn-securityhub-insight-awssecurityfindingfilters-networkdestinationipv4)" : {{[ IpFilter, ... ]}},
  "[NetworkDestinationIpV6](#cfn-securityhub-insight-awssecurityfindingfilters-networkdestinationipv6)" : {{[ IpFilter, ... ]}},
  "[NetworkDestinationPort](#cfn-securityhub-insight-awssecurityfindingfilters-networkdestinationport)" : {{[ NumberFilter, ... ]}},
  "[NetworkDirection](#cfn-securityhub-insight-awssecurityfindingfilters-networkdirection)" : {{[ StringFilter, ... ]}},
  "[NetworkProtocol](#cfn-securityhub-insight-awssecurityfindingfilters-networkprotocol)" : {{[ StringFilter, ... ]}},
  "[NetworkSourceDomain](#cfn-securityhub-insight-awssecurityfindingfilters-networksourcedomain)" : {{[ StringFilter, ... ]}},
  "[NetworkSourceIpV4](#cfn-securityhub-insight-awssecurityfindingfilters-networksourceipv4)" : {{[ IpFilter, ... ]}},
  "[NetworkSourceIpV6](#cfn-securityhub-insight-awssecurityfindingfilters-networksourceipv6)" : {{[ IpFilter, ... ]}},
  "[NetworkSourceMac](#cfn-securityhub-insight-awssecurityfindingfilters-networksourcemac)" : {{[ StringFilter, ... ]}},
  "[NetworkSourcePort](#cfn-securityhub-insight-awssecurityfindingfilters-networksourceport)" : {{[ NumberFilter, ... ]}},
  "[NoteText](#cfn-securityhub-insight-awssecurityfindingfilters-notetext)" : {{[ StringFilter, ... ]}},
  "[NoteUpdatedAt](#cfn-securityhub-insight-awssecurityfindingfilters-noteupdatedat)" : {{[ DateFilter, ... ]}},
  "[NoteUpdatedBy](#cfn-securityhub-insight-awssecurityfindingfilters-noteupdatedby)" : {{[ StringFilter, ... ]}},
  "[ProcessLaunchedAt](#cfn-securityhub-insight-awssecurityfindingfilters-processlaunchedat)" : {{[ DateFilter, ... ]}},
  "[ProcessName](#cfn-securityhub-insight-awssecurityfindingfilters-processname)" : {{[ StringFilter, ... ]}},
  "[ProcessParentPid](#cfn-securityhub-insight-awssecurityfindingfilters-processparentpid)" : {{[ NumberFilter, ... ]}},
  "[ProcessPath](#cfn-securityhub-insight-awssecurityfindingfilters-processpath)" : {{[ StringFilter, ... ]}},
  "[ProcessPid](#cfn-securityhub-insight-awssecurityfindingfilters-processpid)" : {{[ NumberFilter, ... ]}},
  "[ProcessTerminatedAt](#cfn-securityhub-insight-awssecurityfindingfilters-processterminatedat)" : {{[ DateFilter, ... ]}},
  "[ProductArn](#cfn-securityhub-insight-awssecurityfindingfilters-productarn)" : {{[ StringFilter, ... ]}},
  "[ProductFields](#cfn-securityhub-insight-awssecurityfindingfilters-productfields)" : {{[ MapFilter, ... ]}},
  "[ProductName](#cfn-securityhub-insight-awssecurityfindingfilters-productname)" : {{[ StringFilter, ... ]}},
  "[RecommendationText](#cfn-securityhub-insight-awssecurityfindingfilters-recommendationtext)" : {{[ StringFilter, ... ]}},
  "[RecordState](#cfn-securityhub-insight-awssecurityfindingfilters-recordstate)" : {{[ StringFilter, ... ]}},
  "[Region](#cfn-securityhub-insight-awssecurityfindingfilters-region)" : {{[ StringFilter, ... ]}},
  "[RelatedFindingsId](#cfn-securityhub-insight-awssecurityfindingfilters-relatedfindingsid)" : {{[ StringFilter, ... ]}},
  "[RelatedFindingsProductArn](#cfn-securityhub-insight-awssecurityfindingfilters-relatedfindingsproductarn)" : {{[ StringFilter, ... ]}},
  "[ResourceApplicationArn](#cfn-securityhub-insight-awssecurityfindingfilters-resourceapplicationarn)" : {{[ StringFilter, ... ]}},
  "[ResourceApplicationName](#cfn-securityhub-insight-awssecurityfindingfilters-resourceapplicationname)" : {{[ StringFilter, ... ]}},
  "[ResourceAwsEc2InstanceIamInstanceProfileArn](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instanceiaminstanceprofilearn)" : {{[ StringFilter, ... ]}},
  "[ResourceAwsEc2InstanceImageId](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instanceimageid)" : {{[ StringFilter, ... ]}},
  "[ResourceAwsEc2InstanceIpV4Addresses](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instanceipv4addresses)" : {{[ IpFilter, ... ]}},
  "[ResourceAwsEc2InstanceIpV6Addresses](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instanceipv6addresses)" : {{[ IpFilter, ... ]}},
  "[ResourceAwsEc2InstanceKeyName](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancekeyname)" : {{[ StringFilter, ... ]}},
  "[ResourceAwsEc2InstanceLaunchedAt](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancelaunchedat)" : {{[ DateFilter, ... ]}},
  "[ResourceAwsEc2InstanceSubnetId](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancesubnetid)" : {{[ StringFilter, ... ]}},
  "[ResourceAwsEc2InstanceType](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancetype)" : {{[ StringFilter, ... ]}},
  "[ResourceAwsEc2InstanceVpcId](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancevpcid)" : {{[ StringFilter, ... ]}},
  "[ResourceAwsIamAccessKeyCreatedAt](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamaccesskeycreatedat)" : {{[ DateFilter, ... ]}},
  "[ResourceAwsIamAccessKeyPrincipalName](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamaccesskeyprincipalname)" : {{[ StringFilter, ... ]}},
  "[ResourceAwsIamAccessKeyStatus](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamaccesskeystatus)" : {{[ StringFilter, ... ]}},
  "[ResourceAwsIamAccessKeyUserName](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamaccesskeyusername)" : {{[ StringFilter, ... ]}},
  "[ResourceAwsIamUserUserName](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamuserusername)" : {{[ StringFilter, ... ]}},
  "[ResourceAwsS3BucketOwnerId](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawss3bucketownerid)" : {{[ StringFilter, ... ]}},
  "[ResourceAwsS3BucketOwnerName](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawss3bucketownername)" : {{[ StringFilter, ... ]}},
  "[ResourceContainerImageId](#cfn-securityhub-insight-awssecurityfindingfilters-resourcecontainerimageid)" : {{[ StringFilter, ... ]}},
  "[ResourceContainerImageName](#cfn-securityhub-insight-awssecurityfindingfilters-resourcecontainerimagename)" : {{[ StringFilter, ... ]}},
  "[ResourceContainerLaunchedAt](#cfn-securityhub-insight-awssecurityfindingfilters-resourcecontainerlaunchedat)" : {{[ DateFilter, ... ]}},
  "[ResourceContainerName](#cfn-securityhub-insight-awssecurityfindingfilters-resourcecontainername)" : {{[ StringFilter, ... ]}},
  "[ResourceDetailsOther](#cfn-securityhub-insight-awssecurityfindingfilters-resourcedetailsother)" : {{[ MapFilter, ... ]}},
  "[ResourceId](#cfn-securityhub-insight-awssecurityfindingfilters-resourceid)" : {{[ StringFilter, ... ]}},
  "[ResourcePartition](#cfn-securityhub-insight-awssecurityfindingfilters-resourcepartition)" : {{[ StringFilter, ... ]}},
  "[ResourceRegion](#cfn-securityhub-insight-awssecurityfindingfilters-resourceregion)" : {{[ StringFilter, ... ]}},
  "[ResourceTags](#cfn-securityhub-insight-awssecurityfindingfilters-resourcetags)" : {{[ MapFilter, ... ]}},
  "[ResourceType](#cfn-securityhub-insight-awssecurityfindingfilters-resourcetype)" : {{[ StringFilter, ... ]}},
  "[Sample](#cfn-securityhub-insight-awssecurityfindingfilters-sample)" : {{[ BooleanFilter, ... ]}},
  "[SeverityLabel](#cfn-securityhub-insight-awssecurityfindingfilters-severitylabel)" : {{[ StringFilter, ... ]}},
  "[SeverityNormalized](#cfn-securityhub-insight-awssecurityfindingfilters-severitynormalized)" : {{[ NumberFilter, ... ]}},
  "[SeverityProduct](#cfn-securityhub-insight-awssecurityfindingfilters-severityproduct)" : {{[ NumberFilter, ... ]}},
  "[SourceUrl](#cfn-securityhub-insight-awssecurityfindingfilters-sourceurl)" : {{[ StringFilter, ... ]}},
  "[ThreatIntelIndicatorCategory](#cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorcategory)" : {{[ StringFilter, ... ]}},
  "[ThreatIntelIndicatorLastObservedAt](#cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorlastobservedat)" : {{[ DateFilter, ... ]}},
  "[ThreatIntelIndicatorSource](#cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorsource)" : {{[ StringFilter, ... ]}},
  "[ThreatIntelIndicatorSourceUrl](#cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorsourceurl)" : {{[ StringFilter, ... ]}},
  "[ThreatIntelIndicatorType](#cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatortype)" : {{[ StringFilter, ... ]}},
  "[ThreatIntelIndicatorValue](#cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorvalue)" : {{[ StringFilter, ... ]}},
  "[Title](#cfn-securityhub-insight-awssecurityfindingfilters-title)" : {{[ StringFilter, ... ]}},
  "[Type](#cfn-securityhub-insight-awssecurityfindingfilters-type)" : {{[ StringFilter, ... ]}},
  "[UpdatedAt](#cfn-securityhub-insight-awssecurityfindingfilters-updatedat)" : {{[ DateFilter, ... ]}},
  "[UserDefinedFields](#cfn-securityhub-insight-awssecurityfindingfilters-userdefinedfields)" : {{[ MapFilter, ... ]}},
  "[VerificationState](#cfn-securityhub-insight-awssecurityfindingfilters-verificationstate)" : {{[ StringFilter, ... ]}},
  "[VulnerabilitiesExploitAvailable](#cfn-securityhub-insight-awssecurityfindingfilters-vulnerabilitiesexploitavailable)" : {{[ StringFilter, ... ]}},
  "[VulnerabilitiesFixAvailable](#cfn-securityhub-insight-awssecurityfindingfilters-vulnerabilitiesfixavailable)" : {{[ StringFilter, ... ]}},
  "[WorkflowState](#cfn-securityhub-insight-awssecurityfindingfilters-workflowstate)" : {{[ StringFilter, ... ]}},
  "[WorkflowStatus](#cfn-securityhub-insight-awssecurityfindingfilters-workflowstatus)" : {{[ StringFilter, ... ]}}
}
```

### YAML
<a name="aws-properties-securityhub-insight-awssecurityfindingfilters-syntax.yaml"></a>

```
  [AwsAccountId](#cfn-securityhub-insight-awssecurityfindingfilters-awsaccountid): {{
    - StringFilter}}
  [AwsAccountName](#cfn-securityhub-insight-awssecurityfindingfilters-awsaccountname): {{
    - StringFilter}}
  [CompanyName](#cfn-securityhub-insight-awssecurityfindingfilters-companyname): {{
    - StringFilter}}
  [ComplianceAssociatedStandardsId](#cfn-securityhub-insight-awssecurityfindingfilters-complianceassociatedstandardsid): {{
    - StringFilter}}
  [ComplianceSecurityControlId](#cfn-securityhub-insight-awssecurityfindingfilters-compliancesecuritycontrolid): {{
    - StringFilter}}
  [ComplianceSecurityControlParametersName](#cfn-securityhub-insight-awssecurityfindingfilters-compliancesecuritycontrolparametersname): {{
    - StringFilter}}
  [ComplianceSecurityControlParametersValue](#cfn-securityhub-insight-awssecurityfindingfilters-compliancesecuritycontrolparametersvalue): {{
    - StringFilter}}
  [ComplianceStatus](#cfn-securityhub-insight-awssecurityfindingfilters-compliancestatus): {{
    - StringFilter}}
  [Confidence](#cfn-securityhub-insight-awssecurityfindingfilters-confidence): {{
    - NumberFilter}}
  [CreatedAt](#cfn-securityhub-insight-awssecurityfindingfilters-createdat): {{
    - DateFilter}}
  [Criticality](#cfn-securityhub-insight-awssecurityfindingfilters-criticality): {{
    - NumberFilter}}
  [Description](#cfn-securityhub-insight-awssecurityfindingfilters-description): {{
    - StringFilter}}
  [FindingProviderFieldsConfidence](#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsconfidence): {{
    - NumberFilter}}
  [FindingProviderFieldsCriticality](#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldscriticality): {{
    - NumberFilter}}
  [FindingProviderFieldsRelatedFindingsId](#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsrelatedfindingsid): {{
    - StringFilter}}
  [FindingProviderFieldsRelatedFindingsProductArn](#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsrelatedfindingsproductarn): {{
    - StringFilter}}
  [FindingProviderFieldsSeverityLabel](#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsseveritylabel): {{
    - StringFilter}}
  [FindingProviderFieldsSeverityOriginal](#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsseverityoriginal): {{
    - StringFilter}}
  [FindingProviderFieldsTypes](#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldstypes): {{
    - StringFilter}}
  [FirstObservedAt](#cfn-securityhub-insight-awssecurityfindingfilters-firstobservedat): {{
    - DateFilter}}
  [GeneratorId](#cfn-securityhub-insight-awssecurityfindingfilters-generatorid): {{
    - StringFilter}}
  [Id](#cfn-securityhub-insight-awssecurityfindingfilters-id): {{
    - StringFilter}}
  [Keyword](#cfn-securityhub-insight-awssecurityfindingfilters-keyword): {{
    - KeywordFilter}}
  [LastObservedAt](#cfn-securityhub-insight-awssecurityfindingfilters-lastobservedat): {{
    - DateFilter}}
  [MalwareName](#cfn-securityhub-insight-awssecurityfindingfilters-malwarename): {{
    - StringFilter}}
  [MalwarePath](#cfn-securityhub-insight-awssecurityfindingfilters-malwarepath): {{
    - StringFilter}}
  [MalwareState](#cfn-securityhub-insight-awssecurityfindingfilters-malwarestate): {{
    - StringFilter}}
  [MalwareType](#cfn-securityhub-insight-awssecurityfindingfilters-malwaretype): {{
    - StringFilter}}
  [NetworkDestinationDomain](#cfn-securityhub-insight-awssecurityfindingfilters-networkdestinationdomain): {{
    - StringFilter}}
  [NetworkDestinationIpV4](#cfn-securityhub-insight-awssecurityfindingfilters-networkdestinationipv4): {{
    - IpFilter}}
  [NetworkDestinationIpV6](#cfn-securityhub-insight-awssecurityfindingfilters-networkdestinationipv6): {{
    - IpFilter}}
  [NetworkDestinationPort](#cfn-securityhub-insight-awssecurityfindingfilters-networkdestinationport): {{
    - NumberFilter}}
  [NetworkDirection](#cfn-securityhub-insight-awssecurityfindingfilters-networkdirection): {{
    - StringFilter}}
  [NetworkProtocol](#cfn-securityhub-insight-awssecurityfindingfilters-networkprotocol): {{
    - StringFilter}}
  [NetworkSourceDomain](#cfn-securityhub-insight-awssecurityfindingfilters-networksourcedomain): {{
    - StringFilter}}
  [NetworkSourceIpV4](#cfn-securityhub-insight-awssecurityfindingfilters-networksourceipv4): {{
    - IpFilter}}
  [NetworkSourceIpV6](#cfn-securityhub-insight-awssecurityfindingfilters-networksourceipv6): {{
    - IpFilter}}
  [NetworkSourceMac](#cfn-securityhub-insight-awssecurityfindingfilters-networksourcemac): {{
    - StringFilter}}
  [NetworkSourcePort](#cfn-securityhub-insight-awssecurityfindingfilters-networksourceport): {{
    - NumberFilter}}
  [NoteText](#cfn-securityhub-insight-awssecurityfindingfilters-notetext): {{
    - StringFilter}}
  [NoteUpdatedAt](#cfn-securityhub-insight-awssecurityfindingfilters-noteupdatedat): {{
    - DateFilter}}
  [NoteUpdatedBy](#cfn-securityhub-insight-awssecurityfindingfilters-noteupdatedby): {{
    - StringFilter}}
  [ProcessLaunchedAt](#cfn-securityhub-insight-awssecurityfindingfilters-processlaunchedat): {{
    - DateFilter}}
  [ProcessName](#cfn-securityhub-insight-awssecurityfindingfilters-processname): {{
    - StringFilter}}
  [ProcessParentPid](#cfn-securityhub-insight-awssecurityfindingfilters-processparentpid): {{
    - NumberFilter}}
  [ProcessPath](#cfn-securityhub-insight-awssecurityfindingfilters-processpath): {{
    - StringFilter}}
  [ProcessPid](#cfn-securityhub-insight-awssecurityfindingfilters-processpid): {{
    - NumberFilter}}
  [ProcessTerminatedAt](#cfn-securityhub-insight-awssecurityfindingfilters-processterminatedat): {{
    - DateFilter}}
  [ProductArn](#cfn-securityhub-insight-awssecurityfindingfilters-productarn): {{
    - StringFilter}}
  [ProductFields](#cfn-securityhub-insight-awssecurityfindingfilters-productfields): {{
    - MapFilter}}
  [ProductName](#cfn-securityhub-insight-awssecurityfindingfilters-productname): {{
    - StringFilter}}
  [RecommendationText](#cfn-securityhub-insight-awssecurityfindingfilters-recommendationtext): {{
    - StringFilter}}
  [RecordState](#cfn-securityhub-insight-awssecurityfindingfilters-recordstate): {{
    - StringFilter}}
  [Region](#cfn-securityhub-insight-awssecurityfindingfilters-region): {{
    - StringFilter}}
  [RelatedFindingsId](#cfn-securityhub-insight-awssecurityfindingfilters-relatedfindingsid): {{
    - StringFilter}}
  [RelatedFindingsProductArn](#cfn-securityhub-insight-awssecurityfindingfilters-relatedfindingsproductarn): {{
    - StringFilter}}
  [ResourceApplicationArn](#cfn-securityhub-insight-awssecurityfindingfilters-resourceapplicationarn): {{
    - StringFilter}}
  [ResourceApplicationName](#cfn-securityhub-insight-awssecurityfindingfilters-resourceapplicationname): {{
    - StringFilter}}
  [ResourceAwsEc2InstanceIamInstanceProfileArn](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instanceiaminstanceprofilearn): {{
    - StringFilter}}
  [ResourceAwsEc2InstanceImageId](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instanceimageid): {{
    - StringFilter}}
  [ResourceAwsEc2InstanceIpV4Addresses](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instanceipv4addresses): {{
    - IpFilter}}
  [ResourceAwsEc2InstanceIpV6Addresses](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instanceipv6addresses): {{
    - IpFilter}}
  [ResourceAwsEc2InstanceKeyName](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancekeyname): {{
    - StringFilter}}
  [ResourceAwsEc2InstanceLaunchedAt](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancelaunchedat): {{
    - DateFilter}}
  [ResourceAwsEc2InstanceSubnetId](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancesubnetid): {{
    - StringFilter}}
  [ResourceAwsEc2InstanceType](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancetype): {{
    - StringFilter}}
  [ResourceAwsEc2InstanceVpcId](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancevpcid): {{
    - StringFilter}}
  [ResourceAwsIamAccessKeyCreatedAt](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamaccesskeycreatedat): {{
    - DateFilter}}
  [ResourceAwsIamAccessKeyPrincipalName](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamaccesskeyprincipalname): {{
    - StringFilter}}
  [ResourceAwsIamAccessKeyStatus](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamaccesskeystatus): {{
    - StringFilter}}
  [ResourceAwsIamAccessKeyUserName](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamaccesskeyusername): {{
    - StringFilter}}
  [ResourceAwsIamUserUserName](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamuserusername): {{
    - StringFilter}}
  [ResourceAwsS3BucketOwnerId](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawss3bucketownerid): {{
    - StringFilter}}
  [ResourceAwsS3BucketOwnerName](#cfn-securityhub-insight-awssecurityfindingfilters-resourceawss3bucketownername): {{
    - StringFilter}}
  [ResourceContainerImageId](#cfn-securityhub-insight-awssecurityfindingfilters-resourcecontainerimageid): {{
    - StringFilter}}
  [ResourceContainerImageName](#cfn-securityhub-insight-awssecurityfindingfilters-resourcecontainerimagename): {{
    - StringFilter}}
  [ResourceContainerLaunchedAt](#cfn-securityhub-insight-awssecurityfindingfilters-resourcecontainerlaunchedat): {{
    - DateFilter}}
  [ResourceContainerName](#cfn-securityhub-insight-awssecurityfindingfilters-resourcecontainername): {{
    - StringFilter}}
  [ResourceDetailsOther](#cfn-securityhub-insight-awssecurityfindingfilters-resourcedetailsother): {{
    - MapFilter}}
  [ResourceId](#cfn-securityhub-insight-awssecurityfindingfilters-resourceid): {{
    - StringFilter}}
  [ResourcePartition](#cfn-securityhub-insight-awssecurityfindingfilters-resourcepartition): {{
    - StringFilter}}
  [ResourceRegion](#cfn-securityhub-insight-awssecurityfindingfilters-resourceregion): {{
    - StringFilter}}
  [ResourceTags](#cfn-securityhub-insight-awssecurityfindingfilters-resourcetags): {{
    - MapFilter}}
  [ResourceType](#cfn-securityhub-insight-awssecurityfindingfilters-resourcetype): {{
    - StringFilter}}
  [Sample](#cfn-securityhub-insight-awssecurityfindingfilters-sample): {{
    - BooleanFilter}}
  [SeverityLabel](#cfn-securityhub-insight-awssecurityfindingfilters-severitylabel): {{
    - StringFilter}}
  [SeverityNormalized](#cfn-securityhub-insight-awssecurityfindingfilters-severitynormalized): {{
    - NumberFilter}}
  [SeverityProduct](#cfn-securityhub-insight-awssecurityfindingfilters-severityproduct): {{
    - NumberFilter}}
  [SourceUrl](#cfn-securityhub-insight-awssecurityfindingfilters-sourceurl): {{
    - StringFilter}}
  [ThreatIntelIndicatorCategory](#cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorcategory): {{
    - StringFilter}}
  [ThreatIntelIndicatorLastObservedAt](#cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorlastobservedat): {{
    - DateFilter}}
  [ThreatIntelIndicatorSource](#cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorsource): {{
    - StringFilter}}
  [ThreatIntelIndicatorSourceUrl](#cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorsourceurl): {{
    - StringFilter}}
  [ThreatIntelIndicatorType](#cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatortype): {{
    - StringFilter}}
  [ThreatIntelIndicatorValue](#cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorvalue): {{
    - StringFilter}}
  [Title](#cfn-securityhub-insight-awssecurityfindingfilters-title): {{
    - StringFilter}}
  [Type](#cfn-securityhub-insight-awssecurityfindingfilters-type): {{
    - StringFilter}}
  [UpdatedAt](#cfn-securityhub-insight-awssecurityfindingfilters-updatedat): {{
    - DateFilter}}
  [UserDefinedFields](#cfn-securityhub-insight-awssecurityfindingfilters-userdefinedfields): {{
    - MapFilter}}
  [VerificationState](#cfn-securityhub-insight-awssecurityfindingfilters-verificationstate): {{
    - StringFilter}}
  [VulnerabilitiesExploitAvailable](#cfn-securityhub-insight-awssecurityfindingfilters-vulnerabilitiesexploitavailable): {{
    - StringFilter}}
  [VulnerabilitiesFixAvailable](#cfn-securityhub-insight-awssecurityfindingfilters-vulnerabilitiesfixavailable): {{
    - StringFilter}}
  [WorkflowState](#cfn-securityhub-insight-awssecurityfindingfilters-workflowstate): {{
    - StringFilter}}
  [WorkflowStatus](#cfn-securityhub-insight-awssecurityfindingfilters-workflowstatus): {{
    - StringFilter}}
```

## Properties
<a name="aws-properties-securityhub-insight-awssecurityfindingfilters-properties"></a>

`AwsAccountId`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-awsaccountid"></a>
The AWS account ID in which a finding is generated.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsAccountName`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-awsaccountname"></a>
The name of the AWS account in which a finding is generated.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CompanyName`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-companyname"></a>
The name of the findings provider (company) that owns the solution (product) that generates findings.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComplianceAssociatedStandardsId`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-complianceassociatedstandardsid"></a>
 The unique identifier of a standard in which a control is enabled. This field consists of the resource portion of the Amazon Resource Name (ARN) returned for a standard in the [DescribeStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html) API response.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComplianceSecurityControlId`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-compliancesecuritycontrolid"></a>
 The unique identifier of a control across standards. Values for this field typically consist of an AWS service and a number, such as APIGateway.5.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComplianceSecurityControlParametersName`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-compliancesecuritycontrolparametersname"></a>
 The name of a security control parameter.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComplianceSecurityControlParametersValue`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-compliancesecuritycontrolparametersvalue"></a>
 The current value of a security control parameter.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComplianceStatus`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-compliancestatus"></a>
Exclusive to findings that are generated as the result of a check run against a specific rule in a supported standard, such as CIS AWS Foundations. Contains security standard-related finding details.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Confidence`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-confidence"></a>
A finding's confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.
Confidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.
*Required*: No
*Type*: Array of [NumberFilter](aws-properties-securityhub-insight-numberfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreatedAt`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-createdat"></a>
A timestamp that indicates when the security findings provider created the potential security issue that a finding reflects.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
*Required*: No
*Type*: Array of [DateFilter](aws-properties-securityhub-insight-datefilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Criticality`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-criticality"></a>
The level of importance assigned to the resources associated with the finding.
A score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.
*Required*: No
*Type*: Array of [NumberFilter](aws-properties-securityhub-insight-numberfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-description"></a>
A finding's description.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FindingProviderFieldsConfidence`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsconfidence"></a>
The finding provider value for the finding confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.
Confidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.
*Required*: No
*Type*: Array of [NumberFilter](aws-properties-securityhub-insight-numberfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FindingProviderFieldsCriticality`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldscriticality"></a>
The finding provider value for the level of importance assigned to the resources associated with the findings.
A score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.
*Required*: No
*Type*: Array of [NumberFilter](aws-properties-securityhub-insight-numberfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FindingProviderFieldsRelatedFindingsId`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsrelatedfindingsid"></a>
The finding identifier of a related finding that is identified by the finding provider.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FindingProviderFieldsRelatedFindingsProductArn`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsrelatedfindingsproductarn"></a>
The ARN of the solution that generated a related finding that is identified by the finding provider.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FindingProviderFieldsSeverityLabel`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsseveritylabel"></a>
The finding provider value for the severity label.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FindingProviderFieldsSeverityOriginal`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsseverityoriginal"></a>
The finding provider's original value for the severity.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FindingProviderFieldsTypes`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldstypes"></a>
One or more finding types that the finding provider assigned to the finding. Uses the format of `namespace/category/classifier` that classify a finding.
Valid namespace values are: Software and Configuration Checks \| TTPs \| Effects \| Unusual Behaviors \| Sensitive Data Identifications
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirstObservedAt`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-firstobservedat"></a>
A timestamp that indicates when the security findings provider first observed the potential security issue that a finding captured.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
*Required*: No
*Type*: Array of [DateFilter](aws-properties-securityhub-insight-datefilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GeneratorId`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-generatorid"></a>
The identifier for the solution-specific component (a discrete unit of logic) that generated a finding. In various security findings providers' solutions, this generator can be called a rule, a check, a detector, a plugin, etc.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-id"></a>
The security findings provider-specific identifier for a finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Keyword`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-keyword"></a>
This field is deprecated. A keyword for a finding.
*Required*: No
*Type*: Array of [KeywordFilter](aws-properties-securityhub-insight-keywordfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastObservedAt`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-lastobservedat"></a>
A timestamp that indicates when the security findings provider most recently observed a change in the resource that is involved in the finding.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
*Required*: No
*Type*: Array of [DateFilter](aws-properties-securityhub-insight-datefilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MalwareName`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-malwarename"></a>
The name of the malware that was observed.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MalwarePath`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-malwarepath"></a>
The filesystem path of the malware that was observed.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MalwareState`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-malwarestate"></a>
The state of the malware that was observed.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MalwareType`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-malwaretype"></a>
The type of the malware that was observed.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkDestinationDomain`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-networkdestinationdomain"></a>
The destination domain of network-related information about a finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkDestinationIpV4`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-networkdestinationipv4"></a>
The destination IPv4 address of network-related information about a finding.
*Required*: No
*Type*: Array of [IpFilter](aws-properties-securityhub-insight-ipfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkDestinationIpV6`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-networkdestinationipv6"></a>
The destination IPv6 address of network-related information about a finding.
*Required*: No
*Type*: Array of [IpFilter](aws-properties-securityhub-insight-ipfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkDestinationPort`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-networkdestinationport"></a>
The destination port of network-related information about a finding.
*Required*: No
*Type*: Array of [NumberFilter](aws-properties-securityhub-insight-numberfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkDirection`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-networkdirection"></a>
Indicates the direction of network traffic associated with a finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkProtocol`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-networkprotocol"></a>
The protocol of network-related information about a finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkSourceDomain`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-networksourcedomain"></a>
The source domain of network-related information about a finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkSourceIpV4`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-networksourceipv4"></a>
The source IPv4 address of network-related information about a finding.
*Required*: No
*Type*: Array of [IpFilter](aws-properties-securityhub-insight-ipfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkSourceIpV6`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-networksourceipv6"></a>
The source IPv6 address of network-related information about a finding.
*Required*: No
*Type*: Array of [IpFilter](aws-properties-securityhub-insight-ipfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkSourceMac`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-networksourcemac"></a>
The source media access control (MAC) address of network-related information about a finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkSourcePort`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-networksourceport"></a>
The source port of network-related information about a finding.
*Required*: No
*Type*: Array of [NumberFilter](aws-properties-securityhub-insight-numberfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NoteText`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-notetext"></a>
The text of a note.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NoteUpdatedAt`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-noteupdatedat"></a>
The timestamp of when the note was updated.
*Required*: No
*Type*: Array of [DateFilter](aws-properties-securityhub-insight-datefilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NoteUpdatedBy`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-noteupdatedby"></a>
The principal that created a note.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProcessLaunchedAt`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-processlaunchedat"></a>
A timestamp that identifies when the process was launched.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
*Required*: No
*Type*: Array of [DateFilter](aws-properties-securityhub-insight-datefilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProcessName`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-processname"></a>
The name of the process.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProcessParentPid`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-processparentpid"></a>
The parent process ID. This field accepts positive integers between `O` and `2147483647`.
*Required*: No
*Type*: Array of [NumberFilter](aws-properties-securityhub-insight-numberfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProcessPath`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-processpath"></a>
The path to the process executable.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProcessPid`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-processpid"></a>
The process ID.
*Required*: No
*Type*: Array of [NumberFilter](aws-properties-securityhub-insight-numberfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProcessTerminatedAt`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-processterminatedat"></a>
A timestamp that identifies when the process was terminated.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
*Required*: No
*Type*: Array of [DateFilter](aws-properties-securityhub-insight-datefilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProductArn`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-productarn"></a>
The ARN generated by Security Hub CSPM that uniquely identifies a third-party company (security findings provider) after this provider's product (solution that generates findings) is registered with Security Hub CSPM.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProductFields`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-productfields"></a>
A data type where security findings providers can include additional solution-specific details that aren't part of the defined `AwsSecurityFinding` format.
*Required*: No
*Type*: Array of [MapFilter](aws-properties-securityhub-insight-mapfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProductName`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-productname"></a>
The name of the solution (product) that generates findings.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecommendationText`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-recommendationtext"></a>
The recommendation of what to do about the issue described in a finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordState`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-recordstate"></a>
The updated record state for the finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-region"></a>
The Region from which the finding was generated.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RelatedFindingsId`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-relatedfindingsid"></a>
The solution-generated identifier for a related finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RelatedFindingsProductArn`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-relatedfindingsproductarn"></a>
The ARN of the solution that generated a related finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceApplicationArn`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceapplicationarn"></a>
 The ARN of the application that is related to a finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceApplicationName`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceapplicationname"></a>
 The name of the application that is related to a finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceAwsEc2InstanceIamInstanceProfileArn`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instanceiaminstanceprofilearn"></a>
The IAM profile ARN of the instance.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceAwsEc2InstanceImageId`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instanceimageid"></a>
The Amazon Machine Image (AMI) ID of the instance.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceAwsEc2InstanceIpV4Addresses`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instanceipv4addresses"></a>
The IPv4 addresses associated with the instance.
*Required*: No
*Type*: Array of [IpFilter](aws-properties-securityhub-insight-ipfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceAwsEc2InstanceIpV6Addresses`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instanceipv6addresses"></a>
The IPv6 addresses associated with the instance.
*Required*: No
*Type*: Array of [IpFilter](aws-properties-securityhub-insight-ipfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceAwsEc2InstanceKeyName`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancekeyname"></a>
The key name associated with the instance.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceAwsEc2InstanceLaunchedAt`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancelaunchedat"></a>
The date and time the instance was launched.
*Required*: No
*Type*: Array of [DateFilter](aws-properties-securityhub-insight-datefilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceAwsEc2InstanceSubnetId`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancesubnetid"></a>
The identifier of the subnet that the instance was launched in.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceAwsEc2InstanceType`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancetype"></a>
The instance type of the instance.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceAwsEc2InstanceVpcId`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancevpcid"></a>
The identifier of the VPC that the instance was launched in.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceAwsIamAccessKeyCreatedAt`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamaccesskeycreatedat"></a>
The creation date/time of the IAM access key related to a finding.
*Required*: No
*Type*: Array of [DateFilter](aws-properties-securityhub-insight-datefilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceAwsIamAccessKeyPrincipalName`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamaccesskeyprincipalname"></a>
The name of the principal that is associated with an IAM access key.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceAwsIamAccessKeyStatus`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamaccesskeystatus"></a>
The status of the IAM access key related to a finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceAwsIamAccessKeyUserName`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamaccesskeyusername"></a>
This field is deprecated. The username associated with the IAM access key related to a finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceAwsIamUserUserName`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamuserusername"></a>
The name of an IAM user.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceAwsS3BucketOwnerId`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceawss3bucketownerid"></a>
The canonical user ID of the owner of the S3 bucket.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceAwsS3BucketOwnerName`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceawss3bucketownername"></a>
The display name of the owner of the S3 bucket.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceContainerImageId`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourcecontainerimageid"></a>
The identifier of the image related to a finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceContainerImageName`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourcecontainerimagename"></a>
The name of the image related to a finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceContainerLaunchedAt`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourcecontainerlaunchedat"></a>
A timestamp that identifies when the container was started.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
*Required*: No
*Type*: Array of [DateFilter](aws-properties-securityhub-insight-datefilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceContainerName`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourcecontainername"></a>
The name of the container related to a finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceDetailsOther`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourcedetailsother"></a>
The details of a resource that doesn't have a specific subfield for the resource type defined.
*Required*: No
*Type*: Array of [MapFilter](aws-properties-securityhub-insight-mapfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceId`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceid"></a>
The canonical identifier for the given resource type.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourcePartition`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourcepartition"></a>
The canonical AWS partition name that the Region is assigned to.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceRegion`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourceregion"></a>
The canonical AWS external Region name where this resource is located.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceTags`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourcetags"></a>
A list of AWS tags associated with a resource at the time the finding was processed.
*Required*: No
*Type*: Array of [MapFilter](aws-properties-securityhub-insight-mapfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceType`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-resourcetype"></a>
Specifies the type of the resource that details are provided for.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sample`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-sample"></a>
Indicates whether or not sample findings are included in the filter results.
*Required*: No
*Type*: Array of [BooleanFilter](aws-properties-securityhub-insight-booleanfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SeverityLabel`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-severitylabel"></a>
The label of a finding's severity.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SeverityNormalized`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-severitynormalized"></a>
Deprecated. The normalized severity of a finding. Instead of providing `Normalized`, provide `Label`.
The value of `Normalized` can be an integer between `0` and `100`.
If you provide `Label` and don't provide `Normalized`, then `Normalized` is set automatically as follows.
+ `INFORMATIONAL` - 0
+ `LOW` - 1
+ `MEDIUM` - 40
+ `HIGH` - 70
+ `CRITICAL` - 90
*Required*: No
*Type*: Array of [NumberFilter](aws-properties-securityhub-insight-numberfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SeverityProduct`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-severityproduct"></a>
Deprecated. This attribute isn't included in findings. Instead of providing `Product`, provide `Original`.
The native severity as defined by the AWS service or integrated partner product that generated the finding.
*Required*: No
*Type*: Array of [NumberFilter](aws-properties-securityhub-insight-numberfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceUrl`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-sourceurl"></a>
A URL that links to a page about the current finding in the security findings provider's solution.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThreatIntelIndicatorCategory`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorcategory"></a>
The category of a threat intelligence indicator.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThreatIntelIndicatorLastObservedAt`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorlastobservedat"></a>
A timestamp that identifies the last observation of a threat intelligence indicator.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
*Required*: No
*Type*: Array of [DateFilter](aws-properties-securityhub-insight-datefilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThreatIntelIndicatorSource`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorsource"></a>
The source of the threat intelligence.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThreatIntelIndicatorSourceUrl`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorsourceurl"></a>
The URL for more details from the source of the threat intelligence.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThreatIntelIndicatorType`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatortype"></a>
The type of a threat intelligence indicator.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThreatIntelIndicatorValue`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorvalue"></a>
The value of a threat intelligence indicator.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-title"></a>
A finding's title.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-type"></a>
A finding type in the format of `namespace/category/classifier` that classifies a finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdatedAt`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-updatedat"></a>
A timestamp that indicates when the security findings provider last updated the finding record.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
*Required*: No
*Type*: Array of [DateFilter](aws-properties-securityhub-insight-datefilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserDefinedFields`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-userdefinedfields"></a>
A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.
*Required*: No
*Type*: Array of [MapFilter](aws-properties-securityhub-insight-mapfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VerificationState`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-verificationstate"></a>
The veracity of a finding.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VulnerabilitiesExploitAvailable`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-vulnerabilitiesexploitavailable"></a>
 Indicates whether a software vulnerability in your environment has a known exploit. You can filter findings by this field only if you use Security Hub CSPM and Amazon Inspector.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VulnerabilitiesFixAvailable`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-vulnerabilitiesfixavailable"></a>
 Indicates whether a vulnerability is fixed in a newer version of the affected software packages. You can filter findings by this field only if you use Security Hub CSPM and Amazon Inspector.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkflowState`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-workflowstate"></a>
The workflow state of a finding.
Note that this field is deprecated. To search for a finding based on its workflow status, use `WorkflowStatus`.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkflowStatus`  <a name="cfn-securityhub-insight-awssecurityfindingfilters-workflowstatus"></a>
The status of the investigation into a finding. Allowed values are the following.
+ `NEW` - The initial state of a finding, before it is reviewed.

  Security Hub CSPM also resets the workflow status from `NOTIFIED` or `RESOLVED` to `NEW` in the following cases:
  + `RecordState` changes from `ARCHIVED` to `ACTIVE`.
  + `Compliance.Status` changes from `PASSED` to either `WARNING`, `FAILED`, or `NOT_AVAILABLE`.
+ `NOTIFIED` - Indicates that the resource owner has been notified about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner.

  If one of the following occurs, the workflow status is changed automatically from `NOTIFIED` to `NEW`:
  + `RecordState` changes from `ARCHIVED` to `ACTIVE`.
  + `Compliance.Status` changes from `PASSED` to `FAILED`, `WARNING`, or `NOT_AVAILABLE`.
+ `SUPPRESSED` - Indicates that you reviewed the finding and don't believe that any action is needed.

  The workflow status of a `SUPPRESSED` finding does not change if `RecordState` changes from `ARCHIVED` to `ACTIVE`.
+ `RESOLVED` - The finding was reviewed and remediated and is now considered resolved.

  The finding remains `RESOLVED` unless one of the following occurs:
  + `RecordState` changes from `ARCHIVED` to `ACTIVE`.
  + `Compliance.Status` changes from `PASSED` to `FAILED`, `WARNING`, or `NOT_AVAILABLE`.

  In those cases, the workflow status is automatically reset to `NEW`.

  For findings from controls, if `Compliance.Status` is `PASSED`, then Security Hub CSPM automatically sets the workflow status to `RESOLVED`.
*Required*: No
*Type*: Array of [StringFilter](aws-properties-securityhub-insight-stringfilter.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
