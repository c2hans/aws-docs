---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsDmsEndpointDetails.html
---

# AwsDmsEndpointDetails
<a name="API_AwsDmsEndpointDetails"></a>

 Provides details about an AWS Database Migration Service (AWS DMS) endpoint. An endpoint provides connection, data store type, and location information about your data store.

## Contents
<a name="API_AwsDmsEndpointDetails_Contents"></a>

 ** CertificateArn **   <a name="securityhub-Type-AwsDmsEndpointDetails-CertificateArn"></a>
 The Amazon Resource Name (ARN) for the SSL certificate that encrypts connections between the DMS endpoint and the replication instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DatabaseName **   <a name="securityhub-Type-AwsDmsEndpointDetails-DatabaseName"></a>
 The name of the endpoint database.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EndpointArn **   <a name="securityhub-Type-AwsDmsEndpointDetails-EndpointArn"></a>
 The Amazon Resource Name (ARN) of the endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EndpointIdentifier **   <a name="securityhub-Type-AwsDmsEndpointDetails-EndpointIdentifier"></a>
 The database endpoint identifier.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EndpointType **   <a name="securityhub-Type-AwsDmsEndpointDetails-EndpointType"></a>
 The type of endpoint. Valid values are source and target.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EngineName **   <a name="securityhub-Type-AwsDmsEndpointDetails-EngineName"></a>
 The type of engine for the endpoint, depending on the `EndpointType` value.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ExternalId **   <a name="securityhub-Type-AwsDmsEndpointDetails-ExternalId"></a>
 A value that can be used for cross-account validation.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ExtraConnectionAttributes **   <a name="securityhub-Type-AwsDmsEndpointDetails-ExtraConnectionAttributes"></a>
 Additional attributes associated with the connection.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KmsKeyId **   <a name="securityhub-Type-AwsDmsEndpointDetails-KmsKeyId"></a>
 An AWS DMS key identifier that is used to encrypt the connection parameters for the endpoint. If you don't specify a value for the `KmsKeyId` parameter, then AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Port **   <a name="securityhub-Type-AwsDmsEndpointDetails-Port"></a>
 The port used to access the endpoint.
Type: Integer
Required: No

 ** ServerName **   <a name="securityhub-Type-AwsDmsEndpointDetails-ServerName"></a>
 The name of the server where the endpoint database resides.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SslMode **   <a name="securityhub-Type-AwsDmsEndpointDetails-SslMode"></a>
 The SSL mode used to connect to the endpoint. The default is none.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Username **   <a name="securityhub-Type-AwsDmsEndpointDetails-Username"></a>
 The user name to be used to log in to the endpoint database.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsDmsEndpointDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsDmsEndpointDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsDmsEndpointDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsDmsEndpointDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
