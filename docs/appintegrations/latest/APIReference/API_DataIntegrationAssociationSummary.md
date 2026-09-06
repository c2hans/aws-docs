---
source_url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DataIntegrationAssociationSummary.html
---

# DataIntegrationAssociationSummary
<a name="API_connect-app-integrations_DataIntegrationAssociationSummary"></a>

Summary information about the DataIntegration association.

## Contents
<a name="API_connect-app-integrations_DataIntegrationAssociationSummary_Contents"></a>

 ** ClientId **   <a name="connect-Type-connect-app-integrations_DataIntegrationAssociationSummary-ClientId"></a>
The identifier for the client that is associated with the DataIntegration association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

 ** DataIntegrationArn **   <a name="connect-Type-connect-app-integrations_DataIntegrationAssociationSummary-DataIntegrationArn"></a>
The Amazon Resource Name (ARN) of the DataIntegration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: No

 ** DataIntegrationAssociationArn **   <a name="connect-Type-connect-app-integrations_DataIntegrationAssociationSummary-DataIntegrationAssociationArn"></a>
The Amazon Resource Name (ARN) of the DataIntegration association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: No

 ** DestinationURI **   <a name="connect-Type-connect-app-integrations_DataIntegrationAssociationSummary-DestinationURI"></a>
The URI of the data destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^(\w+\:\/\/[\w.-]+[\w/!@#+=.-]+$)|(\w+\:\/\/[\w.-]+[\w/!@#+=.-]+[\w/!@#+=.-]+[\w/!@#+=.,-]+$)`
Required: No

 ** ExecutionConfiguration **   <a name="connect-Type-connect-app-integrations_DataIntegrationAssociationSummary-ExecutionConfiguration"></a>
The configuration for how the files should be pulled from the source.
Type: [ExecutionConfiguration](API_connect-app-integrations_ExecutionConfiguration.md) object
Required: No

 ** LastExecutionStatus **   <a name="connect-Type-connect-app-integrations_DataIntegrationAssociationSummary-LastExecutionStatus"></a>
The execution status of the last job.
Type: [LastExecutionStatus](API_connect-app-integrations_LastExecutionStatus.md) object
Required: No

## See Also
<a name="API_connect-app-integrations_DataIntegrationAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/DataIntegrationAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/DataIntegrationAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/DataIntegrationAssociationSummary)
