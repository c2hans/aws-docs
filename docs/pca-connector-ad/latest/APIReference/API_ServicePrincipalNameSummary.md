---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ServicePrincipalNameSummary.html
---

# ServicePrincipalNameSummary
<a name="API_ServicePrincipalNameSummary"></a>

The service principal name that the connector uses to authenticate with Active Directory.

## Contents
<a name="API_ServicePrincipalNameSummary_Contents"></a>

 ** ConnectorArn **   <a name="PcaConnectorAd-Type-ServicePrincipalNameSummary-ConnectorArn"></a>
The Amazon Resource Name (ARN) that was returned when you called [CreateConnector](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html).
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w-]+:pca-connector-ad:[\w-]+:[0-9]+:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: No

 ** CreatedAt **   <a name="PcaConnectorAd-Type-ServicePrincipalNameSummary-CreatedAt"></a>
The date and time that the service principal name was created.
Type: Timestamp
Required: No

 ** DirectoryRegistrationArn **   <a name="PcaConnectorAd-Type-ServicePrincipalNameSummary-DirectoryRegistrationArn"></a>
The Amazon Resource Name (ARN) that was returned when you called [CreateDirectoryRegistration](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html).
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w-]+:pca-connector-ad:[\w-]+:[0-9]+:directory-registration\/d-[0-9a-f]{10}`
Required: No

 ** Status **   <a name="PcaConnectorAd-Type-ServicePrincipalNameSummary-Status"></a>
The status of a service principal name.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED`
Required: No

 ** StatusReason **   <a name="PcaConnectorAd-Type-ServicePrincipalNameSummary-StatusReason"></a>
Additional information for the status of a service principal name if the status is failed.
Type: String
Valid Values: `DIRECTORY_ACCESS_DENIED | DIRECTORY_NOT_ACTIVE | DIRECTORY_NOT_REACHABLE | DIRECTORY_RESOURCE_NOT_FOUND | SPN_EXISTS_ON_DIFFERENT_AD_OBJECT | SPN_LIMIT_EXCEEDED | INTERNAL_FAILURE`
Required: No

 ** UpdatedAt **   <a name="PcaConnectorAd-Type-ServicePrincipalNameSummary-UpdatedAt"></a>
Time when the service principal name was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ServicePrincipalNameSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/ServicePrincipalNameSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/ServicePrincipalNameSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/ServicePrincipalNameSummary)
